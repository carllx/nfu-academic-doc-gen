"""
gen_lessonplan_xml.py — 纯 XML 操作的教案生成器

模板结构 (Template_LessonPlan.docx — 16 行教案表):
  P: "XXXX"  — 标题段落 (如 "第1周教案")
  TABLE 0: 教案主表 (16 行)
    R0-R8:   基本信息区 (2列: 标签 | XXXX)
      R0: 授课章节
      R1: 授课内容
      R2: 授课时间
      R3: 学时数
      R4: 支撑课程目标
      R5: 教学目标与要求
      R6: 教学重点与难点
      R7: 学生课前阅读材料与其他准备
      R8: 教学方法
    R9:      教学环节表头 (3列: 主要教学环节设计 | 课堂教学进程 | 课堂教学设计)
    R10-R14: 教学环节详情 (3列: vMerge | 环节名 | XXXX)
      R10: 上次课复习
      R11: 课程导入
      R12: 新课讲授
      R13: 实践训练
      R14: 课程小结
    R15:     课后作业 (2列: 标签 | XXXX)

数据源: course.yaml 的 calendar[] 各 week
"""

import copy
import re
from pathlib import Path

from lxml import etree

try:
    from scripts.utils.semester_utils import (
        SemesterDateCalculator, HolidayManager,
        get_step_time_cap, scale_steps
    )
except ImportError:
    from utils.semester_utils import (
        SemesterDateCalculator, HolidayManager,
        get_step_time_cap, scale_steps
    )

from scripts.docx_engine import (
    qn,
    get_paragraph_text,
    get_cell_text,
    merge_runs,
    replace_xxxx,
    set_run_text,
    fill_multiline,
    render_docx,
    merge_docx_files,
)
try:
    from scripts.utils.chapter_utils import build_chapter_title as _build_chapter_title
    from scripts.utils.reading_utils import (
        extract_readings_from_week as _extract_readings,
        resolve_chapter_titles as _resolve_chapter_titles,
    )
except ImportError:
    from utils.chapter_utils import build_chapter_title as _build_chapter_title
    from utils.reading_utils import (
        extract_readings_from_week as _extract_readings,
        resolve_chapter_titles as _resolve_chapter_titles,
    )


def _remove_identifiers(element):
    """移除深拷贝时产生的重复 ID 节点，防止在使用 docxcompose 合并时导致 Word 不可读。
    主要清除 w:bookmarkStart 和 w:bookmarkEnd。
    """
    for bm in element.findall('.//w:bookmarkStart', namespaces=element.nsmap):
        bm.getparent().remove(bm)
    for bm in element.findall('.//w:bookmarkEnd', namespaces=element.nsmap):
        bm.getparent().remove(bm)



# ═══════════════════════════════════════════════════════════════════════
# 0. 工具函数
# ═══════════════════════════════════════════════════════════════════════

_CN_NUMS = '零一二三四五六七八九十'

def _to_cn_num(n: int) -> str:
    """将阿拉伯数字转为中文数字（1-99）。"""
    if n <= 0:
        return str(n)
    if n <= 10:
        return _CN_NUMS[n]
    if n < 20:
        return f'十{_CN_NUMS[n - 10]}' if n > 10 else '十'
    tens = n // 10
    ones = n % 10
    result = f'{_CN_NUMS[tens]}十'
    if ones:
        result += _CN_NUMS[ones]
    return result


def _parse_schedule_time_lp(schedule_time: str):
    """解析 schedule_time 提取星期几和默认节次。

    与 gen_schedule_xml._parse_schedule_time 同源，避免跨模块循环导入。
    支持 '周X' 和 '星期X' 两种格式。
    """
    weekday = ''
    period = ''
    wd_match = re.search(r'(周[一二三四五六日])', schedule_time)
    if wd_match:
        weekday = wd_match.group(1)
    else:
        xq_match = re.search(r'星期([一二三四五六日])', schedule_time)
        if xq_match:
            weekday = f'周{xq_match.group(1)}'
    pd_match = re.search(r'(\d+[-\u2013]\d+)', schedule_time)
    if pd_match:
        period = pd_match.group(1)
    return weekday, period


def _resolve_period_lp(cls: dict, actual_week: int, default_period: str) -> str:
    """根据 schedule_segments 查找当前周次的具体节次。

    与 gen_schedule_xml._resolve_period 同源，避免跨模块循环导入。
    支持分段排课，包括逗号枚举格式，例如：
      schedule_segments:
        - weeks: "10-13"
          period: "1-5节"
        - weeks: "7,9"
          period: "1-5节"
    """
    segments = cls.get('schedule_segments', [])
    if not segments:
        return default_period

    def _parse_weeks(ws: str) -> set:
        result = set()
        for part in str(ws).split(','):
            part = part.strip()
            m = re.match(r'(\d+)\s*[-~]\s*(\d+)', part)
            if m:
                result.update(range(int(m.group(1)), int(m.group(2)) + 1))
            elif part.isdigit():
                result.add(int(part))
        return result

    for seg in segments:
        weeks_set = _parse_weeks(seg.get('weeks', ''))
        if actual_week in weeks_set:
            pd_match = re.search(r'(\d+[-\u2013]\d+)', seg.get('period', ''))
            return pd_match.group(1) if pd_match else default_period
    return default_period


def _resolve_actual_week(cls: dict, calendar_index: int, calendar_len: int) -> int | None:
    """将 calendar 序号（从1开始）映射到班级的实际教学周次。

    映射规则（与 gen_schedule_xml._fill_schedule_table 的 content_map 逻辑一致）：
      1. 从 week_range 起始周开始，逐周递推
      2. 跳过 excluded_weeks 中的停课周
      3. calendar_index=1 对应第1个未停课的实际周

    Args:
        cls: 班级配置字典
        calendar_index: calendar 序号（week 字段值，1-based）
        calendar_len: calendar 总长度

    Returns:
        实际教学周次（int），或 None（该 calendar 条目不在此班级范围内）
    """
    week_range_str = cls.get('week_range', '')
    if not week_range_str:
        # 无 week_range 的班级，calendar 序号即为实际周次
        return calendar_index

    wr_match = re.match(r'(\d+)[\-~](\d+)', str(week_range_str))
    if not wr_match:
        return calendar_index

    start_week = int(wr_match.group(1))
    end_week = int(wr_match.group(2))
    excluded = set(int(e) for e in cls.get('excluded_weeks', []))

    # 逐周递推，跳过停课周，找到第 calendar_index 个有效教学周
    teaching_count = 0
    for wk in range(start_week, end_week + 1):
        if wk in excluded:
            continue
        teaching_count += 1
        if teaching_count == calendar_index:
            return wk

    # calendar_index 超出该班级的有效教学周数
    return None


# ═══════════════════════════════════════════════════════════════════════
# 1. 数据准备
# ═══════════════════════════════════════════════════════════════════════

def _build_steps_map(week: dict, minutes_per_period: int = 45) -> dict:
    """构建教学环节 R10-R14 的数据字典。

    数据源优先级:
      1. lessons[].steps[] (结构化步骤数据)
      2. 默认框架占位符

    有 steps 数据时的组装规则:
      R10-R13: 【教学组织】+ 【教学方法】(继承 week 级) + 【时间安排】+ 【课堂思考】
      R12 额外: 【课程思政融入点】
      R14:     【教学组织】+ 【时间安排】+ 【课程回顾与反思】

    时间输出格式（双单位消歧，Spec §3.4，MSG-017 落地）:
      【时间安排】约{minutes}分钟（{hours_equiv}理论/实践学时）
      使用 steps[].minutes / minutes_per_period 换算，保留一位小数。
      最后一个同类 step 采用末项补正（差值兜底），确保各 step 学时之和
      精确等于声明学时 hours_theory/hours_practice，消除 round 累积误差。

    Args:
        week: calendar[] 中的单个 week 对象
        minutes_per_period: 每节课标准分钟数（默认 45），用于分钟→学时换算

    Returns:
        {'上次课复习': str, '课程导入': str, '新课讲授': str,
         '实践训练': str, '课程小结': str,
         '_theory_hours': float, '_practice_hours': float}
    """
    steps_map = {
        '上次课复习': '',
        '课程导入': '',
        '新课讲授': '',
        '实践训练': '',
        '课程小结': '',
    }

    # week 级数据
    week_method = week.get('teaching_method', '')
    declared_theory = week.get('hours_theory', 0) or 0
    declared_practice = week.get('hours_practice', 0) or 0

    lessons = week.get('lessons', [])
    has_steps = False

    # ── 收集所有 steps ──────────────────────────────────
    all_steps = []
    if lessons:
        for les in lessons:
            for step in les.get('steps', []):
                has_steps = True
                all_steps.append(step)

    # ── 组装文本 ──────────────────────────────────────────
    if has_steps:
        # ── 第一遍：收集各 step 的分类和独立 round 学时 ──
        step_infos = []
        for step in all_steps:
            stage = step.get('stage', '')
            minutes = int(step.get('minutes', 0) or 0)
            is_theory = any(k in stage for k in ('复习', '导入', '讲授', '演示'))
            is_practice = any(k in stage for k in ('实践', '练习', '训练', '总结', '小结'))
            
            # 动态纠正纯实践/纯理论课程的时间分类
            if declared_theory == 0 and declared_practice > 0:
                category = '实践'
            elif declared_practice == 0 and declared_theory > 0:
                category = '理论'
            else:
                category = '理论' if is_theory else ('实践' if is_practice else '')
                
            raw_hours = round(minutes / minutes_per_period, 1) if minutes > 0 else 0.0
            step_infos.append({
                'category': category,
                'raw_hours': raw_hours,
            })

        # ── 末项补正：保证同类 step 学时之和 == 声明学时 ──
        # 找到理论/实践各自的最后一个 step 的索引
        last_theory_idx = -1
        last_practice_idx = -1
        for i, info in enumerate(step_infos):
            if info['category'] == '理论':
                last_theory_idx = i
            elif info['category'] == '实践':
                last_practice_idx = i

        # 计算前面 step 的学时之和（不含最后一个）
        theory_prefix_sum = 0.0
        practice_prefix_sum = 0.0
        for i, info in enumerate(step_infos):
            if info['category'] == '理论' and i != last_theory_idx:
                theory_prefix_sum += info['raw_hours']
            elif info['category'] == '实践' and i != last_practice_idx:
                practice_prefix_sum += info['raw_hours']

        # 补正：最后一个 step 的学时 = 声明学时 - 前面之和
        corrected_hours = [info['raw_hours'] for info in step_infos]
        if last_theory_idx >= 0 and declared_theory > 0:
            corrected_hours[last_theory_idx] = round(
                declared_theory - theory_prefix_sum, 1
            )
        if last_practice_idx >= 0 and declared_practice > 0:
            corrected_hours[last_practice_idx] = round(
                declared_practice - practice_prefix_sum, 1
            )

        # ── 第二遍：使用补正后的学时值组装文本 ──
        for idx, step in enumerate(all_steps):
            stage = step.get('stage', '')
            summary = step.get('summary', '') or step.get('content', '')
            minutes = int(step.get('minutes', 0) or 0)
            ideology = step.get('ideology', '')

            is_summary_stage = ('总结' in stage or '小结' in stage)

            # 按教案格式组装子节
            parts = []
            if summary:
                parts.append(f"【教学组织】{summary}")

            if not is_summary_stage and week_method:
                parts.append(f"【教学方法】{week_method}")

            # ── 时间安排（双单位消歧 + 末项补正，Spec §3.4，MSG-017）──
            if minutes > 0:
                category = step_infos[idx]['category']
                hours_display = corrected_hours[idx]
                cat_label = f"{category}学时" if category else "学时"
                parts.append(f"【时间安排】约{minutes}分钟（{hours_display}{cat_label}）")

            if not is_summary_stage:
                parts.append("【课堂思考】")

            if '讲授' in stage:
                if ideology:
                    parts.append(f"【课程思政融入点】{ideology}")
                else:
                    parts.append("【课程思政融入点】")

            if is_summary_stage:
                parts.append("【课程回顾与反思】")

            step_text = '\n'.join(parts)

            # 映射 stage 名称到表格行
            if '复习' in stage:
                steps_map['上次课复习'] += step_text + '\n'
            elif '导入' in stage:
                steps_map['课程导入'] += step_text + '\n'
            elif '讲授' in stage or '演示' in stage:
                steps_map['新课讲授'] += step_text + '\n'
            elif '实践' in stage or '练习' in stage or '训练' in stage:
                steps_map['实践训练'] += step_text + '\n'
            elif is_summary_stage:
                steps_map['课程小结'] += step_text + '\n'

    # 如果没有 steps 数据，生成默认占位框架
    if not has_steps:
        method = week.get('teaching_method', '')
        ideology = week.get('ideology', '')
        default_stages = {
            '上次课复习': '【教学组织】\n【教学方法】\n【时间安排】\n【课堂思考】',
            '课程导入': '【教学组织】\n【教学方法】\n【时间安排】\n【课堂思考】',
            '新课讲授': '【教学组织】\n【教学方法】\n【时间安排】\n【课堂思考】'
                + (f'\n【课程思政融入点】{ideology}' if ideology else '\n【课程思政融入点】'),
            '实践训练': '【教学组织】\n【教学方法】\n【时间安排】\n【课堂思考】',
            '课程小结': '【教学组织】\n【时间安排】\n【课程回顾与反思】',
        }
        steps_map = default_stages

    # ── 学时合计直接使用声明学时（锚定大纲，MSG-017 任务 3）──
    steps_map['_theory_hours'] = float(declared_theory)
    steps_map['_practice_hours'] = float(declared_practice)

    # 去除末尾换行
    for k in steps_map:
        if isinstance(steps_map[k], str):
            steps_map[k] = steps_map[k].strip()

    return steps_map


def prepare_week_context(week: dict, global_ctx: dict) -> dict:
    """为单周教案准备数据上下文。

    Args:
        week: calendar[] 中的单个 week 对象
        global_ctx: generate.py 传入的全局上下文

    Returns:
        教案填充所需的数据字典
    """
    course = global_ctx.get('course', {})
    objectives = global_ctx.get('objectives', {})
    classes = course.get('classes', [])
    textbooks = global_ctx.get('textbooks', [])
    # 毕业要求数据（从 graduation_requirements.yaml 加载）
    grad_reqs = global_ctx.get('_graduation_requirements', {})

    week_num = week.get('week', '')
    topic = week.get('topic', '')
    content = week.get('content', '')
    h_theory = week.get('hours_theory', 0)
    h_practice = week.get('hours_practice', 0)
    total_hours = (h_theory or 0) + (h_practice or 0)

    # --- 标题 (中文数字) ---
    title = f"第{_to_cn_num(int(week_num))}次课教案" if str(week_num).isdigit() else f"第{week_num}次课教案"

    # --- R0 授课章节 (自动合成前缀: "第1章 xxx" 或 "项目一 xxx") ---
    course = global_ctx.get('course', {})
    chapter_title = _build_chapter_title(course, week, int(week_num) if str(week_num).isdigit() else 1)

    # --- R2 授课时间 (多班级周次/节次感知) ---
    calendar_list = global_ctx.get('calendar', [])
    time_parts = []
    if classes:
        for cls in classes:
            name = cls.get('name', '')
            cal_idx = int(week_num) if str(week_num).isdigit() else 0
            # 将 calendar 序号映射为该班级的实际教学周次
            actual_week = _resolve_actual_week(cls, cal_idx, len(calendar_list))
            if actual_week is None:
                continue  # 该 calendar 条目超出此班级的教学周范围
            # 解析星期和默认节次
            schedule_time = cls.get('schedule_time', '')
            weekday, default_period = _parse_schedule_time_lp(schedule_time)
            # 查询分段排课节次
            period = _resolve_period_lp(cls, actual_week, default_period)
            period_str = f"{period}节" if period else ''
            part = f"{name}：第 {actual_week} 周，{weekday}{period_str}"
            time_parts.append(part)
    if not time_parts:
        time_parts.append(f"第 {week_num} 周")

    # --- R2 附注：节次缩减压缩说明（仅差异周出现） ---
    hours_cfg = global_ctx.get('course', {}).get('hours', {})
    mpp = hours_cfg.get('minutes_per_period', 45) if isinstance(hours_cfg, dict) else 45
    # 计算教学设计的标准节次（steps 总分钟 / 每节分钟）
    all_steps_min = 0
    for les in week.get('lessons', []):
        for step in les.get('steps', []):
            all_steps_min += int(step.get('minutes', 0) or 0)
    designed_periods = round(all_steps_min / mpp) if all_steps_min > 0 else total_hours

    if classes and designed_periods > 0:
        compress_notes = []
        for cls in classes:
            cal_idx = int(week_num) if str(week_num).isdigit() else 0
            actual_wk = _resolve_actual_week(cls, cal_idx, len(calendar_list))
            if actual_wk is None:
                continue
            schedule_time = cls.get('schedule_time', '')
            _, default_pd = _parse_schedule_time_lp(schedule_time)
            period_str = _resolve_period_lp(cls, actual_wk, default_pd)
            if period_str:
                pd_match = re.search(r'(\d+)[-–](\d+)', period_str)
                if pd_match:
                    actual_periods = int(pd_match.group(2)) - int(pd_match.group(1)) + 1
                    if actual_periods < designed_periods:
                        # 提取班级简称（去掉年级+专业前缀，如"24数字媒体艺术游戏班"→"游戏班"）
                        cls_name = cls.get('name', '')
                        short_match = re.search(r'(?:级|艺术|技术|工程|专业)([\u4e00-\u9fa5]{1,4}班)$', cls_name)
                        short_name = short_match.group(1) if short_match else cls_name
                        actual_min = actual_periods * mpp
                        compress_notes.append(
                            f"※ {short_name}本周实际{actual_periods}节（{actual_min}分钟），"
                            f"以下教学设计按{designed_periods}节编排，授课时等比压缩。"
                        )
        if compress_notes:
            time_parts.extend(compress_notes)

    # --- R3 学时数 ---
    if h_theory and h_practice:
        hours_str = f"{total_hours}学时（理论{h_theory}，实践{h_practice}）"
    elif h_theory:
        hours_str = f"{h_theory}学时（理论）"
    elif h_practice:
        hours_str = f"{h_practice}学时（实践）"
    else:
        hours_str = f"{total_hours}学时"

    # --- R4 支撑课程目标 ---
    # 优先使用 supported_objectives 引用 (如 ["知识1", "能力2"])
    # 否则展示所有 objectives
    # 根据 _schema_type 调整输出格式：
    #   detailed: 完整引用（含观测点）
    #   coarse:   引用毕业要求大类，不含观测点
    #   none:     仅描述，无毕业要求引用
    supported_refs = week.get('supported_objectives', [])
    schema_type = global_ctx.get('_schema_type', 'detailed')

    support_lines = []
    seq = 1  # 全局编号
    for cat, cat_cn in [('knowledge', '知识'), ('ability', '能力'), ('quality', '素质')]:
        for obj in objectives.get(cat, []):
            idx = obj.get('index', '')
            ref_key = f"{cat_cn}{idx}"
            # 如果指定了 supported_objectives，仅包含引用的目标
            if supported_refs and ref_key not in supported_refs:
                continue
            desc = obj.get('desc', '')
            # desc 可能已含尾部句号，去重避免 。。
            desc_clean = desc.rstrip('。.')

            if schema_type == 'none':
                # none: 仅描述，无毕业要求引用
                line = f"{seq}. {desc_clean}。"
            else:
                # detailed / coarse: 构建毕业要求引用文字
                req_parts = []
                for m in obj.get('mappings', []):
                    requirement = m.get('requirement', '')
                    point = m.get('point', '')
                    if requirement:
                        req_num = requirement.split()[0] if requirement else ''
                        part = f"毕业要求{req_num}"
                        # 仅 detailed 追加观测点
                        if schema_type == 'detailed' and point:
                            part += f"（观测点{point}）"
                        req_parts.append(part)
                req_text = ''
                if req_parts:
                    req_text = f"支撑课程{cat_cn}目标（{idx}），对应{'；'.join(req_parts)}。"
                line = f"{seq}. {desc_clean}。{req_text}"
            support_lines.append(line)
            seq += 1

    support_text = '\n'.join(support_lines) if support_lines else '见教学大纲'

    # --- R5 教学目标与要求 ---
    teaching_req_raw = week.get('teaching_requirements', '')
    # 支持结构化字典格式 {knowledge, ability, quality, method}
    if isinstance(teaching_req_raw, dict):
        req_parts = []
        if teaching_req_raw.get('knowledge'):
            req_parts.append(f"知识目标：{teaching_req_raw['knowledge']}")
        if teaching_req_raw.get('ability'):
            req_parts.append(f"能力目标：{teaching_req_raw['ability']}")
        if teaching_req_raw.get('quality'):
            req_parts.append(f"素质目标：{teaching_req_raw['quality']}")
        if teaching_req_raw.get('method'):
            req_parts.append(f"过程与方法：{teaching_req_raw['method']}")
        teaching_req = '\n'.join(req_parts)
    else:
        teaching_req = str(teaching_req_raw)

    # --- R6 教学重点与难点 ---
    focus = week.get('focus', '')
    difficulty = week.get('difficulty', '')
    emphasis_parts = []
    if focus:
        emphasis_parts.append(f"重点：{focus}")
    if difficulty:
        emphasis_parts.append(f"难点：{difficulty}")
    emphasis_text = '\n'.join(emphasis_parts) if emphasis_parts else ''

    # --- R7 课前阅读 ---
    # textbooks 可能是 Pydantic 对象列表或原始 dict 列表，统一转为 dict
    tb_dicts = []
    for b in textbooks:
        tb_dicts.append(b if isinstance(b, dict) else b.dict())

    readings = _extract_readings(week, tb_dicts)
    # Phase 2b: 使用 resolve 引擎增强 readings，将章节引用解析为带标题的全称
    if readings:
        readings = _resolve_chapter_titles(readings, tb_dicts, fmt='full')
    reading_lines = []
    if readings:
        reading_lines.append("课前指定阅读教材与章节：")
        for r in readings:
            reading_lines.append(f"  {r}")
    else:
        # 回退逻辑: 若无具体章节，放主教材列表
        main_books = [b for b in tb_dicts if b.get('type') == 'textbook']
        if main_books:
            reading_lines.append("必读书目：")
            for b in main_books:
                reading_lines.append(
                    f"  {b.get('author', '')}：{b.get('title', '')}[M]. "
                    f"{b.get('publisher', '')}, {b.get('year', '')}."
                )
    reading_text = '\n'.join(reading_lines) if reading_lines else ''

    # --- R8 教学方法 ---
    teaching_method = week.get('teaching_method', '')

    # --- R10-R14 教学环节 ---
    # 改进 D：从 hours 配置获取 minutes_per_period，传入 _build_steps_map
    hours_cfg = global_ctx.get('course', {}).get('hours', {})
    if isinstance(hours_cfg, dict):
        mpp = hours_cfg.get('minutes_per_period', 45)
    else:
        mpp = 45
    steps_map = _build_steps_map(week, minutes_per_period=mpp)

    # --- R15 课后作业 ---
    homework = week.get('task', '') or week.get('assignment', '') or ''

    return {
        'title': title,
        'chapter': chapter_title,             # R0 授课章节 (含章节编号)
        'content': content,                   # R1 授课内容
        'time': '\n'.join(time_parts),        # R2 授课时间 (无日期)
        'hours': hours_str,                   # R3 学时数
        'support_objectives': support_text,   # R4 支撑课程目标 (含毕业要求)
        'teaching_req': teaching_req,         # R5 教学目标与要求 (分类)
        'emphasis': emphasis_text,            # R6 教学重点与难点
        'reading': reading_text,              # R7 课前阅读
        'method': teaching_method,            # R8 教学方法
        'steps': steps_map,                   # R10-R14 教学环节
        'homework': homework,                 # R15 课后作业
        # MSG-017：学时合计元数据（用于 R14 末尾汇总行）
        'steps_theory_hours': steps_map.get('_theory_hours', 0.0),
        'steps_practice_hours': steps_map.get('_practice_hours', 0.0),
        'declared_theory': h_theory or 0,
        'declared_practice': h_practice or 0,
    }


# ═══════════════════════════════════════════════════════════════════════
# 2. 表格填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_lessonplan(root, context: dict):
    """教案专用填充回调函数，供 render_docx() 调用。"""
    body = root.find(qn('w:body'))
    week_ctx = context.get('_week_ctx', {})

    # --- 标题段落 ---
    for p in body.findall(qn('w:p')):
        text = get_paragraph_text(p)
        if 'XXXX' in text:
            replace_xxxx(p, week_ctx.get('title', ''))
            break

    # --- 教案表 ---
    tables = list(body.iter(qn('w:tbl')))
    if not tables:
        print("    ⚠️ 模板中未找到表格")
        return

    table = tables[0]
    rows = table.findall(qn('w:tr'))

    if len(rows) < 16:
        print(f"    ⚠️ 预期 16 行，实际 {len(rows)} 行")
        return

    # R0-R8: 基本信息区 (2列, C1 = XXXX)
    info_values = {
        0: week_ctx.get('chapter', ''),
        1: week_ctx.get('content', ''),
        2: week_ctx.get('time', ''),
        3: week_ctx.get('hours', ''),
        4: week_ctx.get('support_objectives', ''),
        5: week_ctx.get('teaching_req', ''),
        6: week_ctx.get('emphasis', ''),
        7: week_ctx.get('reading', ''),
        8: week_ctx.get('method', ''),
    }

    for ri, value in info_values.items():
        cells = rows[ri].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            p = tc.find(qn('w:p'))
            if p is not None:
                text = get_paragraph_text(p)
                if 'XXXX' in text:
                    if '\n' in str(value):
                        fill_multiline(p, str(value))
                    else:
                        replace_xxxx(p, str(value))
                else:
                    if '\n' in str(value):
                        fill_multiline(p, str(value))
                    else:
                        set_run_text(p, str(value))

    # R9: 教学环节表头 — 跳过
    # R10-R14: 教学环节详情 (C2 = XXXX)
    steps = week_ctx.get('steps', {})
    step_keys = ['上次课复习', '课程导入', '新课讲授', '实践训练', '课程小结']

    for si, key in enumerate(step_keys):
        ri = 10 + si
        if ri >= len(rows):
            break

        value = steps.get(key, '')
        cells = rows[ri].findall(qn('w:tc'))

        # 教学环节行可能是 3 列 (vMerge | 环节名 | 教学设计) 或 2 列
        target_ci = len(cells) - 1  # 最后一列是数据列
        if target_ci < 0:
            continue

        tc = cells[target_ci]
        p = tc.find(qn('w:p'))
        if p is not None:
            text = get_paragraph_text(p)
            if 'XXXX' in text:
                if '\n' in value:
                    fill_multiline(p, value)
                else:
                    replace_xxxx(p, value)
            else:
                if '\n' in value:
                    fill_multiline(p, value)
                else:
                    set_run_text(p, value)

    # R15: 课后作业 (C1 = XXXX)
    if len(rows) >= 16:
        cells = rows[15].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            p = tc.find(qn('w:p'))
            if p is not None:
                value = week_ctx.get('homework', '')
                text = get_paragraph_text(p)
                if 'XXXX' in text:
                    replace_xxxx(p, value)
                else:
                    set_run_text(p, value)


# ═══════════════════════════════════════════════════════════════════════
# 3. 教案首页（封面）
# ═══════════════════════════════════════════════════════════════════════

def _format_team(teacher: dict) -> str:
    """格式化课程团队教师字段，输出 `姓名（职称）` 格式，多人用 `；` 分隔。

    teacher.team 字段语义：协作教师，不含主讲教师本人。
    推荐使用对象列表格式以保留职称信息：[{name: 姓名, title: 职称}]。
    兼容三种格式（向下兼容旧数据）：
      - 空字符串 / None → 回退为主讲教师姓名（无），如 '林昕（无）'
      - 字符串: '张三'             → 直接输出 '张三'（无职称括号）
      - 字符串列表: ['张三','李四'] → '张三；李四'（无职称括号）
      - 对象列表: [{name,title}]   → '张三（讲师）；李四（副教授）'
    """
    team_raw = teacher.get('team', '')

    def fmt_one(name: str, title: str) -> str:
        # 有职称时显示职称，无职称时显示（无），符合教务填报规范
        return f"{name}（{title}）" if title else f"{name}（无）"

    if isinstance(team_raw, list):
        parts = []
        for item in team_raw:
            if isinstance(item, dict):
                parts.append(fmt_one(item.get('name', ''), item.get('title', '')))
            else:
                # 纯字符串列表：无职称信息，直接输出姓名
                parts.append(str(item))
        return '；'.join(parts)
    elif isinstance(team_raw, str) and team_raw:
        # 单字符串：仅有姓名，直接输出（不从主讲教师职称补全）
        return team_raw
    # team 为空：回退至主讲教师本人（无），确保字段不留空白
    instructor_name = teacher.get('name', '')
    return f"{instructor_name}（无）" if instructor_name else ''



def prepare_cover_context(global_ctx: dict) -> dict:
    """为教案首页准备数据上下文。

    数据源:
        course.yaml 的全局字段 (course, teacher, objectives, textbooks,
        student_analysis, calendar, hours, semester_config)
    """
    course = global_ctx.get('course', {})
    teacher = global_ctx.get('teacher', {})
    hours = course.get('hours', {})
    if isinstance(hours, str):
        hours = {}
    objectives = global_ctx.get('objectives', {})
    textbooks = global_ctx.get('textbooks', [])
    calendar = global_ctx.get('calendar', [])
    semester_config = global_ctx.get('semester_config', {})

    # --- 学期文本 ---
    # 支持编码格式 "2025-2026-2" → "2025～2026学年第二学期"
    semester_raw = course.get('semester', '')
    m = re.match(r'(\d{4})-(\d{4})-([12])', str(semester_raw))
    if m:
        y1, y2, term = m.groups()
        semester = f"{y1}～{y2}学年第{'一' if term == '1' else '二'}学期"
    elif semester_raw:
        semester = str(semester_raw)
    else:
        academic_year = semester_config.get('academic_year', '')
        term = semester_config.get('term', '')
        if academic_year and term:
            semester = f"{academic_year}学年第{'一' if str(term) == '1' else '二'}学期"
        else:
            semester = ''

    # --- Table 0 基本信息 ---
    classes = course.get('classes', [])
    target_parts = []
    for cls in classes:
        name = cls.get('name', '')
        if name:
            target_parts.append(name)
    target = '、'.join(target_parts) if target_parts else ''

    # --- Table 1 Row[0] 学分学时 ---
    h_theory = hours.get('theory', '')
    h_practice = hours.get('practice', '')

    # --- Table 1 Row[1] 教材参考资料 ---
    main_books = [b for b in textbooks if b.get('type') == 'textbook']
    ref_books = [b for b in textbooks if b.get('type') == 'reference']
    resources_url = course.get('resources_url', '')

    # 子项序号规则：单项无序号，多项用 (1)(2) 格式（与上层 1. 2. 3. 区分）
    def _fmt_book(k, b, total):
        entry = f"{b.get('author', '')}.{b.get('title', '')}[M].{b.get('publisher', '')},{b.get('year', '')}."
        return f"({k}){entry}" if total > 1 else entry

    tb_lines = [_fmt_book(k, b, len(main_books)) for k, b in enumerate(main_books, 1)]
    textbook_str = '\n'.join(tb_lines) if tb_lines else ''

    ref_lines = [_fmt_book(k, b, len(ref_books)) for k, b in enumerate(ref_books, 1)]
    reference_str = '\n'.join(ref_lines) if ref_lines else ''

    # 网站序号规则：单项无序号，多项用 (1)(2) 格式
    url_raw = str(resources_url or '').strip()
    def clean_prefix(s):
        """剥离行首已存在的序号"""
        return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())

    url_lines_raw = [clean_prefix(line) for line in url_raw.split('\n') if line.strip()]
    url_lines = []
    for k, line in enumerate(url_lines_raw, 1):
        url_lines.append(f"({k}){line}" if len(url_lines_raw) > 1 else line)
    resources_url_str = '\n'.join(url_lines) if url_lines else '无'

    # --- Table 1 Row[2] 学情分析 ---
    student_analysis = global_ctx.get('student_analysis', '')

    # --- Table 1 Row[3] 课程目标嵌套表 ---
    # 按维度组织：[{cat_cn, items: [{desc, req_text, point_text}]}]
    # 根据 _schema_type 调整数据结构：
    #   detailed: 完整 4 列（desc + req_text + point_text）
    #   coarse:   3 列（desc + req_text，point_text 留空）
    #   none:     无表格，obj_groups 仅含 desc（供段落渲染）
    schema_type = global_ctx.get('_schema_type', 'detailed')
    obj_groups = []
    for cat, cat_cn in [('knowledge', '知识目标'), ('ability', '能力目标'), ('quality', '素质目标')]:
        items = []
        for obj in objectives.get(cat, []):
            idx = obj.get('index', '')
            desc = obj.get('desc', '')
            desc_text = f"{idx}. {desc.rstrip('。.')}。" if desc else ''

            if schema_type == 'none':
                # none: 仅描述，无毕业要求/观测点
                items.append({
                    'desc': desc_text,
                    'req_text': '',
                    'point_text': '',
                })
            else:
                # detailed / coarse: 构建毕业要求和观测点文字
                req_parts = []
                point_parts = []
                for m in obj.get('mappings', []):
                    requirement = m.get('requirement', '')
                    point = m.get('point', '')
                    if requirement:
                        req_parts.append(f"毕业要求{requirement}")
                    if schema_type == 'detailed' and point:
                        point_parts.append(str(point))

                items.append({
                    'desc': desc_text,
                    'req_text': '；'.join(req_parts),
                    'point_text': '；'.join(point_parts),
                })
        if items:
            obj_groups.append({'cat_cn': cat_cn, 'items': items})

    # --- Table 1 Row[5-10] 内容课时分配 ---
    chapter_rows = []
    for ch_idx, week in enumerate(calendar, start=1):
        topic = week.get('topic', '')
        if not topic:
            continue
        week_num = week.get('week', '')
        content = week.get('content', '')
        h_t = week.get('hours_theory', 0) or 0
        h_p = week.get('hours_practice', 0) or 0
        total = h_t + h_p

        chapter_title = _build_chapter_title(course, week, int(week_num) if str(week_num).isdigit() else ch_idx)

        chapter_rows.append({
            'chapter': chapter_title,
            'content': content,
            'hours': str(total) if total else '',
        })

    return {
        'semester': semester,
        # Table 0
        'course_name': course.get('name', ''),
        'nature': course.get('nature', ''),
        'credits': str(course.get('credits', '')),
        'total_hours': str(hours.get('total', '')),
        'target': target,
        'department': course.get('department', ''),
        'instructor': teacher.get('name', ''),
        'instructor_title': teacher.get('title', ''),
        'team': _format_team(teacher),
        # Table 1
        'hours_theory': str(h_theory),
        'hours_practice': str(h_practice),
        'textbook': textbook_str,
        'reference': reference_str,
        'resources_url': resources_url_str,
        'student_analysis': str(student_analysis),
        'obj_groups': obj_groups,
        'chapter_rows': chapter_rows,
    }


def _fill_cover(root, context: dict):
    """教案首页填充回调函数，供 render_docx() 调用。"""
    body = root.find(qn('w:body'))
    cover_ctx = context.get('_cover_ctx', {})

    # --- P[4] 学期段落（封面区域：首个表格之前含 XXXX 的段落） ---
    all_paragraphs = body.findall(qn('w:p'))
    # 找到第一个 w:tbl 的位置，只在其之前搜索
    first_tbl = body.find(qn('w:tbl'))
    body_children = list(body)
    tbl_pos = body_children.index(first_tbl) if first_tbl is not None else len(body_children)
    for child in body_children[:tbl_pos]:
        if child.tag == qn('w:p'):
            text = get_paragraph_text(child)
            if 'XXXX' in text:
                replace_xxxx(child, cover_ctx.get('semester', ''))
                break

    # --- Table 0: 基本信息 (9行, C2 = XXXX) ---
    tables = list(body.iter(qn('w:tbl')))
    if len(tables) < 2:
        print("    ⚠️ 首页模板表格不足")
        return

    tbl0 = tables[0]
    tbl0_rows = tbl0.findall(qn('w:tr'))
    tbl0_values = [
        cover_ctx.get('course_name', ''),
        cover_ctx.get('nature', ''),
        cover_ctx.get('credits', ''),
        cover_ctx.get('total_hours', ''),
        cover_ctx.get('target', ''),
        cover_ctx.get('department', ''),
        cover_ctx.get('instructor', ''),
        cover_ctx.get('instructor_title', ''),
        cover_ctx.get('team', ''),
    ]
    for ri, value in enumerate(tbl0_values):
        if ri >= len(tbl0_rows):
            break
        cells = tbl0_rows[ri].findall(qn('w:tc'))
        # 数据在最后一列 (C2)
        tc = cells[-1] if cells else None
        if tc is not None:
            p = tc.find(qn('w:p'))
            if p is not None:
                text = get_paragraph_text(p)
                if 'XXXX' in text:
                    replace_xxxx(p, str(value))
                else:
                    set_run_text(p, str(value))

    # --- Table 1: 教学规划 ---
    tbl1 = tables[1]
    tbl1_rows = tbl1.findall(qn('w:tr'))

    # Row[0]: 课程学分 + 学时安排
    if len(tbl1_rows) > 0:
        cells = tbl1_rows[0].findall(qn('w:tc'))
        # C1 (span:2) = 学分 XXXX
        if len(cells) >= 2:
            p = cells[1].find(qn('w:p'))
            if p is not None:
                replace_xxxx(p, cover_ctx.get('credits', ''))
        # C3 (span:2) = 理论：XXXX学时\n实践：XXXX学时
        if len(cells) >= 4:
            # 这个单元格有两个 XXXX：理论和实践
            tc = cells[3]
            for p in tc.findall(qn('w:p')):
                merge_runs(p)
                for t_elem in p.iter(qn('w:t')):
                    if t_elem.text and 'XXXX' in t_elem.text:
                        # 第一次替换理论学时，第二次替换实践学时
                        if '理论' in t_elem.text:
                            t_elem.text = t_elem.text.replace('XXXX', cover_ctx.get('hours_theory', ''), 1)
                        elif '实践' in t_elem.text:
                            t_elem.text = t_elem.text.replace('XXXX', cover_ctx.get('hours_practice', ''), 1)
                        else:
                            t_elem.text = t_elem.text.replace('XXXX', '', 1)

    # Row[1]: 教材和主要参考资料
    # 模板结构: P[0]="1.选用教材：" P[1]="XXXX" P[2]="2.参考书目…" P[3]="XXXX" P[4]="课程网站…" P[5]="XXXX"
    if len(tbl1_rows) > 1:
        cells = tbl1_rows[1].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            all_paras = tc.findall(qn('w:p'))
            def clean_prefix(s):
                """剥离行首已存在的序号，如 '1.', '(1)', '1、' 等"""
                return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())

            prev_label = ''
            for p in all_paras:
                text = get_paragraph_text(p)
                if 'XXXX' in text:
                    # 根据前一段的标签确定类别
                    val = ''
                    if '教材' in prev_label:
                        val = cover_ctx.get('textbook', '')
                    elif '参考' in prev_label or '文献' in prev_label:
                        val = cover_ctx.get('reference', '')
                    elif '网站' in prev_label or '支持条件' in prev_label:
                        val = cover_ctx.get('resources_url', '')
                    
                    if val:
                        # 应用 fill_multiline 并清除首行缩进与段落间距，确保列表项紧凑对齐
                        fill_multiline(p, str(val), clear_list_indent=True, fix_spacing=True)
                else:
                    prev_label = text
            
            # 清理末尾多余空行
            all_ps = tc.findall(qn('w:p'))
            if len(all_ps) > 1:
                last_p = all_ps[-1]
                if not get_paragraph_text(last_p).strip():
                    tc.remove(last_p)

    # Row[2]: 授课对象学情分析
    if len(tbl1_rows) > 2:
        cells = tbl1_rows[2].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc = cells[1]
            p = tc.find(qn('w:p'))
            if p is not None:
                sa_text = cover_ctx.get('student_analysis', '')
                if '\n' in str(sa_text):
                    fill_multiline(p, str(sa_text))
                else:
                    text = get_paragraph_text(p)
                    if 'XXXX' in text:
                        replace_xxxx(p, str(sa_text))
                    else:
                        set_run_text(p, str(sa_text))

    # Row[3]: 课程目标嵌套表 (动态行)
    # 根据 _schema_type 路由：
    #   detailed: 填充 4 列嵌套表
    #   coarse:   删列后填充 3 列嵌套表
    #   none:     删除嵌套表，插入段落
    schema_type = context.get('_schema_type', 'detailed')
    if len(tbl1_rows) > 3:
        cells = tbl1_rows[3].findall(qn('w:tc'))
        if len(cells) >= 2:
            tc_obj = cells[1]
            nested_tables = tc_obj.findall(qn('w:tbl'))

            if schema_type == 'none':
                # 删除嵌套表，插入段落
                for nt in nested_tables:
                    tc_obj.remove(nt)
                _fill_cover_objectives_paragraphs(tc_obj, cover_ctx.get('obj_groups', []))
            elif nested_tables:
                if schema_type == 'coarse':
                    _remove_nested_table_last_column(nested_tables[0])
                _fill_objectives_table(nested_tables[0], cover_ctx.get('obj_groups', []), schema_type)

    # Row[5-10]: 内容课时分配 (动态行)
    _fill_chapter_table(tbl1, cover_ctx.get('chapter_rows', []))


def _clean_cell_paragraphs(tc):
    """清除单元格中多余段落，只保留第一个。

    模板中的 cell 可能包含多个段落（如字体设计课残留数据），
    克隆后需要先清除再设置新文本。
    """
    paras = tc.findall(qn('w:p'))
    for p in paras[1:]:
        tc.remove(p)


def _remove_nested_table_last_column(ntbl):
    """物理删除嵌套表格最后一列（观测点列），宽度归还给倒数第二列。"""
    tbl_grid = ntbl.find(qn('w:tblGrid'))
    if tbl_grid is not None:
        grid_cols = tbl_grid.findall(qn('w:gridCol'))
        if len(grid_cols) >= 2:
            last_gc = grid_cols[-1]
            prev_gc = grid_cols[-2]
            last_w = int(last_gc.get(qn('w:w'), '0'))
            prev_w = int(prev_gc.get(qn('w:w'), '0'))
            prev_gc.set(qn('w:w'), str(prev_w + last_w))
            tbl_grid.remove(last_gc)
    for row in ntbl.findall(qn('w:tr')):
        cells = row.findall(qn('w:tc'))
        if cells:
            row.remove(cells[-1])
    print("    ✂️ [coarse] 已删除教案首页嵌套表的观测点列")


def _fill_cover_objectives_paragraphs(tc_obj, obj_groups: list):
    """在单元格内插入段落式课程目标（适用于 schema_type='none'）。

    输出格式：
      （一）知识目标
      1. desc1。
      ...
    """
    cn_nums = ['一', '二', '三']
    # 取现有段落作为格式模板
    existing_p = tc_obj.find(qn('w:p'))

    for ci, group in enumerate(obj_groups):
        cat_cn = group.get('cat_cn', '')
        items = group.get('items', [])

        # 子标题段落
        if existing_p is not None:
            p_heading = copy.deepcopy(existing_p)
        else:
            p_heading = etree.SubElement(tc_obj, qn('w:p'))
        for r in p_heading.findall(qn('w:r')):
            rpr = r.find(qn('w:rPr'))
            if rpr is None:
                rpr = etree.SubElement(r, qn('w:rPr'))
                r.insert(0, rpr)
            if rpr.find(qn('w:b')) is None:
                etree.SubElement(rpr, qn('w:b'))
        set_run_text(p_heading, f"（{cn_nums[ci]}）{cat_cn}")
        tc_obj.append(p_heading)

        # 各条目
        for item in items:
            desc = item.get('desc', '')
            if not desc:
                continue
            if existing_p is not None:
                p_item = copy.deepcopy(existing_p)
            else:
                p_item = etree.SubElement(tc_obj, qn('w:p'))
            for r in p_item.findall(qn('w:r')):
                rpr = r.find(qn('w:rPr'))
                if rpr is not None:
                    b = rpr.find(qn('w:b'))
                    if b is not None:
                        rpr.remove(b)
            set_run_text(p_item, desc)
            tc_obj.append(p_item)

    # 清除原有的空白占位段落
    if existing_p is not None:
        text = get_paragraph_text(existing_p)
        if not text.strip() or 'XXXX' in text:
            tc_obj.remove(existing_p)
    print("    ✅ [none] 教案首页课程目标已替换为段落格式")


def _fill_objectives_table(ntbl, obj_groups: list, schema_type: str = 'detailed'):
    """填充课程目标嵌套表（动态行数）。

    策略：保留表头行(NRow[0])和首个数据行(NRow[1])作为格式模板，
    清空所有数据行，按 obj_groups 动态生成新行。

    根据 schema_type 决定填充列数：
      - detailed: C0(维度) + C1(描述) + C2(毕业要求) + C3(观测点)
      - coarse:   C0(维度) + C1(描述) + C2(毕业要求)（已物理删列）
    """
    nrows = ntbl.findall(qn('w:tr'))
    if len(nrows) < 2:
        return

    # 确定期望的最小列数
    min_cols = 3 if schema_type == 'coarse' else 4

    header_row = nrows[0]
    template_row = nrows[1]  # 用作格式模板

    # 删除所有数据行（保留表头）
    for nr in nrows[1:]:
        ntbl.remove(nr)

    # 按维度生成数据行
    insert_after = header_row
    for group in obj_groups:
        cat_cn = group.get('cat_cn', '')
        items = group.get('items', [])

        for i, item in enumerate(items):
            new_row = copy.deepcopy(template_row)
            _remove_identifiers(new_row)
            ncells = new_row.findall(qn('w:tc'))

            if len(ncells) < min_cols:
                continue

            # C0: 维度名 + vMerge
            tc0 = ncells[0]
            tc0_pr = tc0.find(qn('w:tcPr'))
            if tc0_pr is None:
                tc0_pr = etree.SubElement(tc0, qn('w:tcPr'))
                tc0.insert(0, tc0_pr)

            # 清除已有 vMerge
            for old_vm in tc0_pr.findall(qn('w:vMerge')):
                tc0_pr.remove(old_vm)

            if i == 0:
                # 首行：vMerge restart + 设置维度名
                vm = etree.SubElement(tc0_pr, qn('w:vMerge'))
                vm.set(qn('w:val'), 'restart')
                p = tc0.find(qn('w:p'))
                if p is not None:
                    set_run_text(p, cat_cn)
            else:
                # 后续行：vMerge continue (空文本)
                vm = etree.SubElement(tc0_pr, qn('w:vMerge'))
                # 不设 val 属性 = continue
                p = tc0.find(qn('w:p'))
                if p is not None:
                    set_run_text(p, '')

            # C1: 课程目标描述
            _clean_cell_paragraphs(ncells[1])
            p1 = ncells[1].find(qn('w:p'))
            if p1 is not None:
                set_run_text(p1, item.get('desc', ''))

            # C2: 对应毕业要求
            _clean_cell_paragraphs(ncells[2])
            p2 = ncells[2].find(qn('w:p'))
            if p2 is not None:
                req_text = item.get('req_text', '')
                if '；' in req_text:
                    fill_multiline(p2, req_text.replace('；', '\n'))
                else:
                    set_run_text(p2, req_text)

            # C3: 对应观测点（仅 detailed 模式）
            if schema_type == 'detailed' and len(ncells) > 3:
                _clean_cell_paragraphs(ncells[3])
                p3 = ncells[3].find(qn('w:p'))
                if p3 is not None:
                    point_text = item.get('point_text', '')
                    if '；' in point_text:
                        fill_multiline(p3, point_text.replace('；', '\n'))
                    else:
                        set_run_text(p3, point_text)

            insert_after.addnext(new_row)
            insert_after = new_row


def _fill_chapter_table(tbl1, chapter_rows: list):
    """填充内容课时分配行（Table 1 Row[5]-[10]）。

    策略：Row[5] 是带 XXXX 的数据行模板，
    按 chapter_rows 数量动态克隆/删减。
    """
    rows = tbl1.findall(qn('w:tr'))
    # Row[4]=表头, Row[5]=数据模板, Row[6-10]=空行
    if len(rows) < 6:
        return

    template_ri = 5
    template_row = rows[template_ri]

    # 删除 Row[6]-Row[10]（已有空行）
    for ri in range(len(rows) - 1, template_ri, -1):
        tbl1.remove(rows[ri])

    if not chapter_rows:
        # 无数据，清空模板行
        for tc in template_row.findall(qn('w:tc')):
            p = tc.find(qn('w:p'))
            if p is not None:
                text = get_paragraph_text(p)
                if 'XXXX' in text:
                    replace_xxxx(p, '')
        return

    # 填充第一行
    _fill_chapter_row(template_row, chapter_rows[0])

    # 克隆剩余行
    insert_after = template_row
    for cr in chapter_rows[1:]:
        new_row = copy.deepcopy(template_row)
        _remove_identifiers(new_row)
        _fill_chapter_row(new_row, cr)
        insert_after.addnext(new_row)
        insert_after = new_row


def _fill_chapter_row(row, data: dict):
    """填充内容课时分配行。

    自动检测段落是否含 XXXX：含则替换占位符，否则直接设置文本。
    适用于模板行（首行）和克隆行（后续行）。
    """
    cells = row.findall(qn('w:tc'))
    values = [data.get('chapter', ''), data.get('content', ''), data.get('hours', '')]
    # 跳过 C0 ("内容课时分配" vMerge)
    data_cells = cells[1:] if len(cells) > 3 else cells
    for ci, value in enumerate(values):
        if ci >= len(data_cells):
            break
        tc = data_cells[ci]
        p = tc.find(qn('w:p'))
        if p is not None:
            text = get_paragraph_text(p)
            if 'XXXX' in text:
                if '\n' in str(value):
                    fill_multiline(p, str(value))
                else:
                    replace_xxxx(p, str(value))
            else:
                if '\n' in str(value):
                    fill_multiline(p, str(value))
                else:
                    set_run_text(p, str(value))


# ═══════════════════════════════════════════════════════════════════════
# 3.5 教案生成前置硬性检测 Gate（双检测架构 L2 层）
# ═══════════════════════════════════════════════════════════════════════

# 教学环节 stage 分类定义
_THEORY_STAGE_KEYWORDS = ('复习', '导入', '讲授', '演示')
_PRACTICE_STAGE_KEYWORDS = ('实践', '练习', '训练', '总结', '小结')

def _validate_week_steps(week: dict, week_num, min_per_period: int = 45) -> list:
    """教案生成前置硬性检测。返回错误列表，非空则阻止该周教案输出。

    规则：
      Gate-1: W1 禁止 stage=复习（第一周无上次课内容可复习）
      Gate-2: 理论/实践 stage 分钟折算与 hours_theory/hours_practice 偏差 > 2h
    """
    errors = []

    # 收集所有 steps
    all_steps = []
    for les in week.get('lessons', []):
        all_steps.extend(les.get('steps', []))

    if not all_steps:
        return errors  # 无 steps 数据，不做检测（生成器使用默认占位）

    wk = int(week_num) if str(week_num).isdigit() else 0

    # Gate-1: W1 禁止复习
    if wk == 1:
        for step in all_steps:
            stage = step.get('stage', '')
            if '复习' in stage:
                errors.append(
                    f"W1 禁止 stage='{stage}'——第一周不应有「上次课复习」教学环节"
                )

    # Gate-2: stage 分钟归属与学时偏差检测
    h_t = week.get('hours_theory', 0) or 0
    h_p = week.get('hours_practice', 0) or 0

    if h_t + h_p > 0:
        theory_min, practice_min = 0, 0
        for step in all_steps:
            stage = step.get('stage', '')
            m = step.get('minutes', 0) or 0
            if any(kw in stage for kw in _THEORY_STAGE_KEYWORDS):
                theory_min += m
            elif any(kw in stage for kw in _PRACTICE_STAGE_KEYWORDS):
                practice_min += m

        if theory_min + practice_min > 0:
            t_hours = round(theory_min / min_per_period, 1)
            p_hours = round(practice_min / min_per_period, 1)
            
            # 仅当本周既有理论又有实践学时（混合周）时，才严格校验细分 stage 的归属。
            # 对于纯实践周 (h_t=0) 或纯理论周 (h_p=0)，允许灵活混用讲授与练习，
            # 只要总时长（Gate-3）匹配即可。
            if h_t > 0 and h_p > 0:
                if abs(t_hours - h_t) > 1:  # 收紧：>1h 即 BLOCK（原 >2h）
                    errors.append(
                        f"理论stage折算({t_hours}h)与hours_theory({h_t}h)"
                        f"偏差{abs(t_hours - h_t)}h(>1h)"
                    )
                if abs(p_hours - h_p) > 1:  # 收紧：>1h 即 BLOCK（原 >2h）
                    errors.append(
                        f"实践stage折算({p_hours}h)与hours_practice({h_p}h)"
                        f"偏差{abs(p_hours - h_p)}h(>1h)"
                    )

    # Gate-3: steps 总分钟与声明总学时一致性（MSG-013 建议）
    total_min = sum(s.get('minutes', 0) or 0 for s in all_steps)
    declared_min = (h_t + h_p) * min_per_period
    if declared_min > 0 and total_min > 0:
        diff_min = abs(total_min - declared_min)
        if diff_min > min_per_period:  # 偏差超过 1 课时 → BLOCKED
            errors.append(
                f"steps总分钟({total_min}min)与声明学时"
                f"({h_t + h_p}h×{min_per_period}={declared_min}min)"
                f"偏差{diff_min}min(>{min_per_period}min)"
            )

    return errors


# ═══════════════════════════════════════════════════════════════════════
# 4. 主入口
# ═══════════════════════════════════════════════════════════════════════

def gen_lessonplan(base_dir: Path, output_dir: Path, context: dict):
    """教案生成主函数 — 纯 XML 操作

    流程：先生成教案首页（封面），再为 calendar 中的每一周生成教案。
    所有教案文件统一写入 output_dir/教案/ 子目录，与实验材料/考核材料保持一致。

    Args:
        base_dir: 项目根目录 (教务材料/)
        output_dir: 输出根目录 (课程/Output/)，教案写入其下的 教案/ 子目录
        context: 全局数据上下文 (course.yaml 的完整内容)
    """
    print("  - Generating Lesson Plans (XML direct)...")

    # --- 所有教案统一写入 教案/ 子目录 ---
    lesson_dir = output_dir / "教案"
    lesson_dir.mkdir(parents=True, exist_ok=True)

    # --- 教案首页（封面）---
    cover_tpl = base_dir / "03_LessonPlan_Generator" / "Template_LessonPlan_Cover.docx"
    if cover_tpl.exists():
        cover_ctx = prepare_cover_context(context)
        ctx_cover = context.copy()
        ctx_cover['_cover_ctx'] = cover_ctx

        cover_out = lesson_dir / "教案_首页.docx"
        try:
            render_docx(
                template_path=cover_tpl,
                output_path=cover_out,
                fill_fn=_fill_cover,
                context=ctx_cover,
            )
            print(f"    ✨ Saved: 教案_首页.docx")
        except Exception as e:
            print(f"    ❌ Failed (首页): {e}")
            import traceback
            traceback.print_exc()
    else:
        print("    ⚠️ Template_LessonPlan_Cover.docx not found. Skipping cover.")

    # --- 每周教案 ---
    tpl_path = base_dir / "03_LessonPlan_Generator" / "Template_LessonPlan.docx"
    if not tpl_path.exists():
        print("    ⚠️ Template_LessonPlan.docx not found. Skipping.")
        return

    calendar = context.get('calendar', [])
    if not calendar:
        print("    ⚠️ calendar 为空，跳过教案生成")
        return

    # --- 节假日自动检测初始化 ---
    _cal_yaml = base_dir / "00_Data_Context" / "semester_calendar.yaml"
    holiday_mgr = HolidayManager.from_yaml(_cal_yaml) if _cal_yaml.exists() else HolidayManager()
    _start_date = context.get('semester_config', {}).get('start_date', '')
    calc = SemesterDateCalculator(_start_date, holiday_mgr) if _start_date else None

    # 预建周次→星期映射表（支持多班级课程 self-resolve weekday by week_range）
    def _get_weekday_for_week(wk: int) -> str:
        """根据班级 week_range 返回该自然周的上课星期；无匹配返回空字符串。"""
        import re as _re
        for cls in context.get('course', {}).get('classes', []):
            wr = cls.get('week_range', '')
            sch = cls.get('schedule_time', '')
            if wr:
                m = _re.match(r'(\d+)[\-~](\d+)', str(wr))
                if m and int(m.group(1)) <= wk <= int(m.group(2)):
                    wd = _re.search(r'(周[一二三四五六日])', sch)
                    return wd.group(1) if wd else ''
            elif sch:  # 没有 week_range 的班级，默认全学期都上
                wd = _re.search(r'(周[一二三四五六日])', sch)
                return wd.group(1) if wd else ''
        return ''

    generated = 0
    for week in calendar:
        week_num = week.get('week', '')
        topic = week.get('topic', '')

        if not topic:
            continue

        # ── 节假日自动跳过 ───────────────────────────────────
        if calc and str(week_num).isdigit():
            weekday = _get_weekday_for_week(int(week_num))
            if weekday and calc.is_class_holiday(int(week_num), weekday):
                print(f"    ⏭️  W{week_num} ({weekday}) 为节假日，自动跳过教案生成")
                continue
        # ── excluded_weeks 补充跳过（非国家节假日停课） ───────────────
        _skip_excluded = False
        for cls in context.get('course', {}).get('classes', []):
            exc = cls.get('excluded_weeks', [])
            if str(week_num).isdigit() and int(week_num) in [int(e) for e in exc]:
                print(f"    ⏭️  W{week_num} 在 excluded_weeks 中，跳过教案生成")
                _skip_excluded = True
                break
        if _skip_excluded:
            continue

        # ── 前置硬性检测 Gate（双检测架构 L2 层）───────────────
        hours_cfg = context.get('course', {}).get('hours', {})
        _mpp = hours_cfg.get('minutes_per_period', 45) if isinstance(hours_cfg, dict) else 45
        gate_errors = _validate_week_steps(week, week_num, _mpp)
        if gate_errors:
            for ge in gate_errors:
                print(f"    ❌ [BLOCKED] W{week_num}: {ge}")
            print(f"    ⛔ W{week_num} 教案因校验不通过而被阻止输出")
            continue

        # 准备该周上下文（含 steps 时长裁剪）
        week_ctx = prepare_week_context(week, context)

        # ── session_time_overrides 步骤时长裁剪 ───────────────────
        if str(week_num).isdigit():
            for cls in context.get('course', {}).get('classes', []):
                cap = get_step_time_cap(cls, int(week_num))
                if cap is not None:
                    raw_steps = week.get('lessons', [{}])[0].get('steps', []) if week.get('lessons') else []
                    if raw_steps:
                        compressed = scale_steps(raw_steps, cap)
                        if compressed is not raw_steps:
                            print(f"    ✂️  W{week_num} steps 总时长裁剪至 {cap}min (节次变化)")
                            # 写回压缩后的 steps——通过 week_ctx 下发至填充函数
                            if 'steps' in week_ctx:
                                for i, step in enumerate(compressed):
                                    stage = step.get('stage', '')
                                    stage_map = {
                                        '复习': '上次课复习',
                                        '导入': '课程导入',
                                        '講授': '新课讲授', '讲授': '新课讲授',
                                        '演示': '新课讲授',
                                        '实践': '实践训练',
                                        '小结': '课程小结',
                                    }
                                    key = stage_map.get(stage, stage)
                                    if key in week_ctx['steps']:
                                        old_text = week_ctx['steps'][key]
                                        mins = step.get('minutes', 0)
                                        week_ctx['steps'][key] = f"{old_text.rstrip()} [{mins}min]"
                    break  # 仅取第一个匹配班级的 override

        # 构建上下文 (包含全局 + 周特定数据)
        ctx = context.copy()
        ctx['_week_ctx'] = week_ctx

        # 输出文件名
        clean_topic = re.sub(r'[/\\:*?"<>|]', '_', topic)[:30]
        filename = f"教案_第{week_num}周_{clean_topic}.docx"
        out_path = lesson_dir / filename

        try:
            render_docx(
                template_path=tpl_path,
                output_path=out_path,
                fill_fn=_fill_lessonplan,
                context=ctx,
            )
            print(f"    ✨ Saved: {filename}")
            generated += 1

        except Exception as e:
            print(f"    ❌ Failed (Week {week_num}): {e}")
            import traceback
            traceback.print_exc()

    print(f"    📊 教案生成完成: {generated}/{len(calendar)} 周")

    # --- 合并输出 ---
    print("    - 合并教案...")
    merge_parts = []
    
    # 1. 封面
    cover_out = lesson_dir / "教案_首页.docx"
    if cover_out.exists():
        merge_parts.append(cover_out)
        
    # 2. 各周教案 (按周数排序)
    # 文件名格式如: 教案_第1周_xxx.docx
    week_files = []
    for f in lesson_dir.glob("教案_第*周_*.docx"):
        m = re.match(r'教案_第(\d+)周_', f.name)
        if m:
            week_files.append((int(m.group(1)), f))
        else:
            week_files.append((999, f))
    week_files.sort(key=lambda x: x[0])
    for _, f in week_files:
        merge_parts.append(f)
        
    # 3. 生成署名页 (作为一个简单渲染，无特殊上下文要求)并添加到合并列表
    footer_tpl = base_dir / "03_LessonPlan_Generator" / "Template_LessonPlan_Footer.docx"
    footer_out = lesson_dir / "教案_尾页署名.docx"
    if footer_tpl.exists():
        try:
            render_docx(
                template_path=footer_tpl,
                output_path=footer_out,
                fill_fn=lambda r, c: None, # Footer 无需填充变量
                context={},
            )
            merge_parts.append(footer_out)
        except Exception as e:
            print(f"    ⚠️ Failed to generate footer: {e}")
            
    if len(merge_parts) > 1:
        merged_out = lesson_dir / "教案_合并版.docx"
        # 归档命名版本
        from scripts.docx_engine import archive_filename
        arch_name = archive_filename(context, '教案')
        if arch_name:
            merged_out = lesson_dir / arch_name
        try:
            merge_docx_files(merge_parts, merged_out, page_break=True)
            print(f"    ✅ 已生成合并版: {merged_out.name}")
        except Exception as e:
            print(f"    ❌ 合并失败: {e}")
    elif len(merge_parts) == 1:
        print("    ⚠️ 只有一个文件，未进行合并")
    else:
        print("    ⚠️ 没有生成任何文件，无法合并")
