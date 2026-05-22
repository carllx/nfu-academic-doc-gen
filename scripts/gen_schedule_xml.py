"""
gen_schedule_xml.py — 纯 XML 操作的教学进度表生成器

模板结构 (Template_Schedule.docx — 官方教务处完整模板):
  P: "20  ～20  学年第  学期"              — 学年学期
  TABLE 0: 封面信息表 (9行×3列)
    R0~R8: 课程名称/类别/学时/学分/授课对象/开课单位/教师/职称/团队
    值列 C2 均为 XXXX
  TABLE 1: 课程基本信息表 (5行)
    R0-R1: 合并表头 (vMerge)
    R2: 数据行 (7cells: 课程名称|课程代码|学分|考核方式|理论|实践|周学时)
    R3: 课程目标 C1=XXXX (gridSpan=6)
    R4: 教材参考 C1=含XXXX (gridSpan=6)
  TABLE 2: 教学进度安排表 (23行)
    R0-R1: 表头 (vMerge)
    R2: Week1 数据行 (8cells, 全部 XXXX)
    R3~R19: Week2~18 (8cells, 周次已预填, 其余空)
    R20-R22: 签名区
"""

import copy
import re
from pathlib import Path

try:
    from scripts.utils.semester_utils import SemesterDateCalculator, HolidayManager
except ImportError:
    from utils.semester_utils import SemesterDateCalculator, HolidayManager

from scripts.docx_engine import (
    qn,
    get_paragraph_text,
    get_cell_text,
    merge_runs,
    replace_xxxx,
    set_run_text,
    fill_multiline,
    render_docx,
    clone_table_row,
)
from scripts.gen_lessonplan_xml import _format_team
from scripts.utils.reading_utils import resolve_chapter_titles as _resolve_chapter_titles


# ═══════════════════════════════════════════════════════════════════════
# 1. 学年学期段落填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_semester_paragraph(body, context: dict):
    """填充 '20  ～20  学年第  学期' 段落。"""
    course = context.get('course', {})
    semester = course.get('semester', '')

    term_map = {'1': '一', '2': '二'}
    parts = semester.split('-') if semester else []
    year1 = parts[0][2:] if len(parts) >= 1 else ''
    year2 = parts[1][2:] if len(parts) >= 2 else ''
    term = term_map.get(parts[2], parts[2]) if len(parts) >= 3 else ''

    for p in body.findall(qn('w:p')):
        text = get_paragraph_text(p)
        if '学年' in text and '学期' in text and '20' in text:
            merge_runs(p)
            for r in p.findall(qn('w:r')):
                for t in r.iter(qn('w:t')):
                    if t.text and '20' in t.text:
                        t.text = t.text.replace('20  ～20', f'20{year1}～20{year2}', 1)
                        t.text = t.text.replace('第  学期', f'第 {term} 学期', 1)
            break


# ═══════════════════════════════════════════════════════════════════════
# 2. 封面信息表 (Table 0) 填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_cover_table(table, context: dict):
    """填充封面信息表 — 9行×3列, C2 为 XXXX 占位符。"""
    course = context.get('course', {})
    teacher = context.get('teacher', {})

    current_class = context.get('_current_class', {})
    class_name = current_class.get('name', '')

    cover_values = {
        0: course.get('name', ''),              # 课程名称
        1: course.get('nature', ''),             # 课程类别
        2: str(course.get('hours', {}).get('total', '')),  # 总学时
        3: str(course.get('credits', '')),       # 总学分
        4: class_name,                           # 授课对象
        5: course.get('department', ''),          # 开课单位
        6: teacher.get('name', ''),              # 主讲教师
        7: teacher.get('title', ''),             # 职称
        8: _format_team(teacher),                # 课程团队教师（格式化为「姓名（职称）」）
    }

    rows = table.findall(qn('w:tr'))
    for row_idx, value in cover_values.items():
        if row_idx >= len(rows):
            break
        cells = rows[row_idx].findall(qn('w:tc'))
        if len(cells) >= 3:
            tc = cells[2]
            p = tc.find(qn('w:p'))
            if p is not None:
                existing = get_paragraph_text(p)
                if 'XXXX' in existing:
                    replace_xxxx(p, str(value))
                else:
                    set_run_text(p, str(value))


# ═══════════════════════════════════════════════════════════════════════
# 3. 课程基本信息表 (Table 1) 填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_info_table(table, context: dict):
    """填充课程基本信息表。"""
    course = context.get('course', {})
    hours = course.get('hours', {})
    objectives = context.get('objectives', {})
    textbooks = context.get('textbooks', [])

    nature = course.get('nature', '')
    exam_method = '考试' if '必修' in nature else '考查'

    total_hours = hours.get('total', 0)
    calendar = context.get('calendar', [])
    teaching_weeks = len(calendar) if calendar else 18
    weekly_hours = round(total_hours / teaching_weeks) if teaching_weeks > 0 else 0

    rows = table.findall(qn('w:tr'))

    # R2 数据行 (7 cells)
    if len(rows) >= 3:
        data_row = rows[2]
        cells = data_row.findall(qn('w:tc'))
        values = [
            course.get('name', ''),
            course.get('code', ''),
            str(course.get('credits', '')),
            exam_method,
            str(hours.get('theory', '')),
            str(hours.get('practice', '')),
            str(weekly_hours),
        ]
        for ci, val in enumerate(values):
            if ci < len(cells):
                p = cells[ci].find(qn('w:p'))
                if p is not None:
                    set_run_text(p, val)

    # R3 课程目标 (C1, gridSpan=6, XXXX)
    if len(rows) >= 4:
        cells = rows[3].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            obj_lines = []
            for cat, label in [('knowledge', '知识目标'), ('ability', '能力目标'), ('quality', '素质目标')]:
                items = objectives.get(cat, [])
                if items:
                    obj_lines.append(f'{label}：')
                    for item in items:
                        obj_lines.append(f'  {item.get("index", "")}. {item.get("desc", "")}')
            if obj_lines:
                p = tc.find(qn('w:p'))
                if p is not None:
                    # 始终用 fill_multiline 确保多行目标正确换行（replace_xxxx 不处理 \n）
                    fill_multiline(p, '\n'.join(obj_lines))

    # R4 教材和参考资料 (C1, gridSpan=6, 含 XXXX)
    if len(rows) >= 5:
        cells = rows[4].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            # 收集教材/参考文本
            main_books = [b for b in textbooks if b.get('type') == 'textbook']
            ref_books = [b for b in textbooks if b.get('type') == 'reference']

            def clean_prefix(s):
                """剥离行首已存在的序号，如 '1.', '(1)', '1、' 等"""
                return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())

            # 子项序号规则：单项无序号，多项用 (1)(2) 格式（与上层 1. 2. 3. 区分）
            def _fmt_book(k, b, total):
                title = clean_prefix(b.get('title', ''))
                author = clean_prefix(b.get('author', ''))
                entry = f"{author}.{title}[M].{b.get('publisher', '')},{b.get('year', '')}."
                return f"({k}){entry}" if total > 1 else entry

            main_lines = [_fmt_book(k, b, len(main_books)) for k, b in enumerate(main_books, 1)]
            main_text = '\n'.join(main_lines) if main_lines else '无'

            ref_lines = [_fmt_book(k, b, len(ref_books)) for k, b in enumerate(ref_books, 1)]
            ref_text = '\n'.join(ref_lines) if ref_lines else '无'

            url_raw = str(course.get('resources_url', '无')).strip()
            # 网站序号逻辑：如果是多行，也应用 (1)(2)
            url_lines_raw = [clean_prefix(line) for line in url_raw.split('\n') if line.strip()]
            url_lines = []
            for k, line in enumerate(url_lines_raw, 1):
                url_lines.append(f"({k}){line}" if len(url_lines_raw) > 1 else line)
            url_text = '\n'.join(url_lines)

            # R4 单元格含 14 个段落, 其中 3 个 XXXX:
            #   P[2]=选用教材, P[6]=参考文献, P[10]=课程网站
            paragraphs = tc.findall(qn('w:p'))
            xxxx_values = [main_text, ref_text, url_text]
            xxxx_idx = 0
            for p in paragraphs:
                text = get_paragraph_text(p)
                if 'XXXX' in text and xxxx_idx < len(xxxx_values):
                    val = xxxx_values[xxxx_idx]
                    # 应用 fill_multiline 并清除首行缩进与段落间距，确保列表项紧凑对齐
                    if val:
                        fill_multiline(p, str(val), clear_list_indent=True, fix_spacing=True)
                    xxxx_idx += 1
            
            # 清理末尾多余空行：如果最后一个段落没内容且不是占位符，删掉
            all_ps = tc.findall(qn('w:p'))
            if len(all_ps) > 1:
                last_p = all_ps[-1]
                if not get_paragraph_text(last_p).strip():
                    tc.remove(last_p)


# ═══════════════════════════════════════════════════════════════════════
# 4. 教学进度安排表 (Table 2) 填充
# ═══════════════════════════════════════════════════════════════════════

def _parse_schedule_time(schedule_time: str):
    """解析 schedule_time 提取星期几和默认节次。

    支持两种星期格式：
      - '周四2-5节'    -> weekday='周四'
      - '星期日(分段排课)' -> weekday='周日'
    """
    weekday = ''
    period = ''

    # 优先匹配 '周X'
    wd_match = re.search(r'(周[一二三四五六日])', schedule_time)
    if wd_match:
        weekday = wd_match.group(1)
    else:
        # 兼容 '星期X' 格式，归一化为 '周X'
        xq_match = re.search(r'星期([一二三四五六日])', schedule_time)
        if xq_match:
            weekday = f'周{xq_match.group(1)}'

    pd_match = re.search(r'(\d+[-\u2013]\d+)', schedule_time)
    if pd_match:
        period = pd_match.group(1)

    return weekday, period


def _parse_weeks_str(weeks_str: str) -> set:
    """解析 weeks 字符串为周次集合。

    支持多种格式：
      - 范围: "10-13"        -> {10,11,12,13}
      - 枚举: "7,9"          -> {7,9}
      - 混合: "7,9,11-13"    -> {7,9,11,12,13}
      - 单值: "10"           -> {10}
    """
    result = set()
    for part in str(weeks_str).split(','):
        part = part.strip()
        m = re.match(r'(\d+)\s*[-~]\s*(\d+)', part)
        if m:
            result.update(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            result.add(int(part))
    return result


def _resolve_period(current_class: dict, week_num: int, default_period: str) -> str:
    """根据 schedule_segments 查找当前周次的具体节次（返回第一个匹配）。

    支持分段排课, 例如:
      schedule_segments:
        - weeks: "10-13"
          period: "1-5节"
        - weeks: "14-18"
          period: "2-5节"
        - weeks: "7,9"          # 逗号枚举
          period: "1-5节"
    """
    segments = current_class.get('schedule_segments', [])
    if not segments:
        return default_period

    for seg in segments:
        weeks_set = _parse_weeks_str(seg.get('weeks', ''))
        if week_num in weeks_set:
            pd_match = re.search(r'(\d+[-\u2013]\d+)', seg.get('period', ''))
            return pd_match.group(1) if pd_match else default_period

    return default_period


def _resolve_all_sessions(current_class: dict, week_num: int, default_weekday: str, default_period: str) -> list:
    """查找某周次的所有上课时段（支持同一周多次上课）。

    返回列表，每个元素为 (weekday, period) 元组，按节次升序排列。
    支持：
      - 同一 segment 内逗号分隔的多个 period: "1-5节, 11-15节" -> 2个session
      - 多个 segment 匹配同一周: 各自生成 session
    若 segments 中有 day 字段则使用，否则使用 default_weekday。
    无 segments 时返回单个默认时段。
    """
    segments = current_class.get('schedule_segments', [])
    if not segments:
        return [(default_weekday, default_period)]

    sessions = []
    for seg in segments:
        weeks_set = _parse_weeks_str(seg.get('weeks', ''))
        if week_num in weeks_set:
            day = seg.get('day', default_weekday)
            period_str = seg.get('period', '')
            # 提取所有 "数字-数字" 格式的节次（支持逗号分隔的多个）
            all_periods = re.findall(r'(\d+[-\u2013]\d+)', period_str)
            if all_periods:
                for p in all_periods:
                    sessions.append((day, p))
            else:
                sessions.append((day, default_period))

    if not sessions:
        return [(default_weekday, default_period)]

    # 按节次起始值升序排列（确保 1-5 排在 7-11 前面）
    def _period_sort_key(item):
        m = re.match(r'(\d+)', item[1])
        return int(m.group(1)) if m else 0

    sessions.sort(key=_period_sort_key)
    return sessions


def _calc_needed_rows(current_class: dict, calendar: list) -> int:
    """计算该班级进度表需要的数据行数。

    规则（优先级从高到低）：
      1. 检测多日制排课（calendar 条目数 > week_range 可用周数）
         -> 行数 = calendar 条目数 + 停课周数
      2. 行数 = week_range 跨度
      3. 无 week_range 时按 calendar 条目数 fallback
    """
    wr = current_class.get('week_range', '')
    m = re.match(r'(\d+)-(\d+)', str(wr))
    if m:
        span = int(m.group(2)) - int(m.group(1)) + 1
        excluded = set(int(e) for e in current_class.get('excluded_weeks', []))
        excluded_in_range = len(excluded & set(range(int(m.group(1)), int(m.group(2)) + 1)))
        available_weeks = span - excluded_in_range
        cal_count = len(calendar) if calendar else 0
        if cal_count > available_weeks:
            # 多日制：行数 = 教学单元数 + 停课周行数
            return cal_count + excluded_in_range
        return span
    return len(calendar) if calendar else 18


def _fill_schedule_table(table, context: dict):
    """填充教学进度安排表 - 支持多日制排课（同一周多行）。

    填充模式：
      - 标准模式：week_range 跨度 >= calendar 条目数 -> 每周一行，线性映射
      - 多日制模式：calendar 条目数 > week_range 可用周数 -> 按 calendar 顺序
        逐条分配，同一周可占多行（如周四一行 + 周日一行）
    """
    course = context.get('course', {})
    teacher = context.get('teacher', {})
    calendar = context.get('calendar', [])
    hours = course.get('hours', {})

    current_class = context.get('_current_class', {})
    schedule_time = current_class.get('schedule_time', '')
    weekday, period = _parse_schedule_time(schedule_time)

    teacher_name = teacher.get('name', '')

    rows = table.findall(qn('w:tr'))

    # 识别签名区起始行
    sign_start = None
    for ri in range(len(rows)):
        text = ''
        for tc in rows[ri].findall(qn('w:tc')):
            text += get_cell_text(tc)
        if '签名' in text:
            sign_start = ri
            break
    if sign_start is None:
        sign_start = len(rows)

    # 数据行: R2 ~ sign_start-1
    data_start = 2
    data_rows = list(rows[data_start:sign_start])

    # -- 解析 week_range --
    week_range_str = current_class.get('week_range', '')
    start_week = 1
    end_week_range = 18
    if week_range_str:
        wr_match = re.match(r'(\d+)\s*[-~]\s*(\d+)', str(week_range_str))
        if wr_match:
            start_week = int(wr_match.group(1))
            end_week_range = int(wr_match.group(2))

    # -- 构建节假日/excluded 跳过集合 --
    calc = context.get('_holiday_calc')
    exc_weeks = set(int(e) for e in current_class.get('excluded_weeks', []))
    skip_weeks = set(exc_weeks)
    if calc and weekday:
        for wk in range(start_week, end_week_range + 1):
            if calc.is_class_holiday(wk, weekday):
                skip_weeks.add(wk)

    # -- 检测多日制模式 --
    available_weeks = sum(1 for wk in range(start_week, end_week_range + 1) if wk not in skip_weeks)
    multi_session_mode = len(calendar) > available_weeks

    # -- 构建行计划 (row_plan) --
    # 每个元素: dict with actual_week, weekday, period, calendar_item, is_skip
    row_plan = []

    if multi_session_mode:
        # 多日制：calendar 条目数 > 可用周数
        cal_iter = iter(calendar)
        for wk in range(start_week, end_week_range + 1):
            if wk in skip_weeks:
                row_plan.append({'actual_week': wk, 'is_skip': True,
                                 'weekday': weekday, 'period': period})
                continue
            sessions = _resolve_all_sessions(current_class, wk, weekday, period)
            for sess_weekday, sess_period in sessions:
                cal_item = next(cal_iter, None)
                if cal_item is None:
                    break
                row_plan.append({
                    'actual_week': wk,
                    'weekday': sess_weekday,
                    'period': sess_period,
                    'calendar_item': cal_item,
                    'is_skip': False,
                })
    else:
        # 标准模式：每周一行，线性映射
        cal_idx = 0
        for wk in range(start_week, end_week_range + 1):
            if wk in skip_weeks:
                row_plan.append({'actual_week': wk, 'is_skip': True,
                                 'weekday': weekday, 'period': period})
                continue
            cal_item = calendar[cal_idx] if cal_idx < len(calendar) else None
            row_plan.append({
                'actual_week': wk,
                'weekday': weekday,
                'period': _resolve_period(current_class, wk, period),
                'calendar_item': cal_item,
                'is_skip': False,
            })
            cal_idx += 1

    needed_rows = len(row_plan)
    current_count = len(data_rows)

    # -- 动态裁剪/扩展数据行 --
    if needed_rows < current_count:
        for excess_row in reversed(data_rows[needed_rows:]):
            table.remove(excess_row)
        data_rows = data_rows[:needed_rows]
    elif needed_rows > current_count:
        last_data_idx = data_start + current_count - 1
        new_rows = clone_table_row(table, last_data_idx,
                                   needed_rows - current_count)
        data_rows.extend(new_rows)

    mode_label = '多日制' if multi_session_mode else '标准'
    print(f"    info 进度表: {current_count}->{len(data_rows)} 行, "
          f"{len(calendar)} 个教学单元, 起始周={start_week}, 模式={mode_label}")

    # 格式化学时数
    def _fmt_hours(v):
        return str(int(v)) if v == int(v) else str(v)

    # -- 逐行填充 --
    for di, tr in enumerate(data_rows):
        cells = tr.findall(qn('w:tc'))
        if len(cells) < 5:
            continue

        if di >= len(row_plan):
            break

        plan = row_plan[di]
        actual_week = plan['actual_week']
        row_weekday = plan.get('weekday', weekday)
        row_period = plan.get('period', period)

        if plan.get('is_skip'):
            # 停课周
            skip_period = _resolve_period(current_class, actual_week, period)
            pd_match = re.search(r'(\d+)[-\u2013](\d+)', skip_period)
            if pd_match:
                planned_slots = int(pd_match.group(2)) - int(pd_match.group(1)) + 1
            else:
                planned_slots = 0
            total_h = hours.get('total', 1) or 1
            theory_ratio = hours.get('theory', 0) / total_h
            practice_ratio = hours.get('practice', 0) / total_h
            planned_theory = round(planned_slots * theory_ratio)
            planned_practice = round(planned_slots * practice_ratio)
            col_values = {
                0: str(actual_week), 1: row_weekday, 2: skip_period,
                3: '节假日停课', 4: teacher_name,
                5: str(int(planned_theory)), 6: str(int(planned_practice)), 7: '0'
            }
        elif plan.get('calendar_item'):
            week = plan['calendar_item']
            topic = week.get('topic', '')
            content = week.get('content', '')
            h_theory = float(week.get('hours_theory', 0) or 0)
            h_practice = float(week.get('hours_practice', 0) or 0)

            teaching_content = topic
            if content and content != topic:
                teaching_content = f'{topic}\n{content}'

            # Phase 2d: 追加教材引用摘要（短格式）
            week_readings = week.get('readings', [])
            textbooks = context.get('textbooks', [])
            if week_readings and textbooks:
                resolved = _resolve_chapter_titles(week_readings, textbooks, fmt='short')
                if resolved:
                    ref_summary = '（' + '；'.join(resolved) + '）'
                    teaching_content += '\n' + ref_summary

            # ISSUE-010: 节次 < calendar 学时时按比例缩放
            if current_class.get('schedule_segments'):
                pd_match = re.search(r'(\d+)[-\u2013](\d+)', row_period)
                if pd_match:
                    period_count = int(pd_match.group(2)) - int(pd_match.group(1)) + 1
                    h_total_orig = h_theory + h_practice
                    if period_count < h_total_orig and h_total_orig > 0:
                        ratio = period_count / h_total_orig
                        h_theory = round(h_theory * ratio, 1)
                        h_practice = round(h_practice * ratio, 1)

            col_values = {
                0: str(actual_week),
                1: row_weekday,
                2: row_period,
                3: teaching_content,
                4: teacher_name,
                5: _fmt_hours(h_theory),
                6: _fmt_hours(h_practice) if h_practice else '',
                7: str(week.get('hours_extracurricular', 0) or 0),
            }
        else:
            col_values = {
                0: str(actual_week), 1: '', 2: '', 3: '', 4: '',
                5: '', 6: '', 7: '',
            }

        for ci, val in col_values.items():
            if val is None:
                continue
            if ci >= len(cells):
                break
            tc = cells[ci]
            p = tc.find(qn('w:p'))
            if p is not None:
                existing = get_paragraph_text(p)
                if 'XXXX' in existing:
                    replace_xxxx(p, str(val))
                else:
                    set_run_text(p, str(val))


# ═══════════════════════════════════════════════════════════════════════
# 5. 主入口
# ═══════════════════════════════════════════════════════════════════════

def _fill_schedule(root, context: dict):
    """Schedule 专用的填充回调函数。"""
    body = root.find(qn('w:body'))

    _fill_semester_paragraph(body, context)

    tables = list(body.iter(qn('w:tbl')))
    if len(tables) < 3:
        print(f"    ⚠️ 预期 3 个表格，实际找到 {len(tables)} 个")

    if len(tables) >= 1:
        _fill_cover_table(tables[0], context)
    if len(tables) >= 2:
        _fill_info_table(tables[1], context)
    if len(tables) >= 3:
        _fill_schedule_table(tables[2], context)


def gen_schedule(base_dir: Path, output_dir: Path, context: dict):
    """教学进度表生成主函数 — XML 直接操作"""
    print("  - Generating Schedule (XML direct)...")

    tpl_path = base_dir / "02_Schedule_Generator" / "Template_Schedule.docx"
    if not tpl_path.exists():
        print("    ⚠️ Template_Schedule.docx not found. Skipping.")
        return

    classes = context.get('course', {}).get('classes', [])
    if not classes:
        classes = [{'name': '默认班级'}]

    for cls in classes:
        ctx = context.copy()
        ctx['_current_class'] = cls

        # ── 初始化节假日计算器并注入 context ──────────────────
        _cal_yaml = base_dir / "00_Data_Context" / "semester_calendar.yaml"
        holiday_mgr = HolidayManager.from_yaml(_cal_yaml) if _cal_yaml.exists() else HolidayManager()
        _start_date = context.get('semester_config', {}).get('start_date', '')
        ctx['_holiday_calc'] = SemesterDateCalculator(_start_date, holiday_mgr) if _start_date else None

        course_name = context.get('course', {}).get('name', '未命名')
        class_name = cls.get('name', '')

        # 归档命名（per-class 文档，必含班级）
        from scripts.docx_engine import archive_filename
        arch_name = archive_filename(context, '教学进度表', class_info=cls)
        if arch_name:
            filename = arch_name
        elif len(classes) == 1:
            filename = f"2025-2026-2_教学进度表_{course_name}.docx"
        else:
            filename = f"2025-2026-2_教学进度表_{course_name}_{class_name}.docx"

        out_path = output_dir / filename

        try:
            render_docx(
                template_path=tpl_path,
                output_path=out_path,
                fill_fn=_fill_schedule,
                context=ctx,
            )
            print(f"    ✨ Saved: {filename}")

        except Exception as e:
            print(f"    ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
