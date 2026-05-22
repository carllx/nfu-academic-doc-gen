"""
gen_experiment_xml.py — 纯 XML 操作的实验材料生成器 v2.0

生成 3 类实验文档:
  1. Template_Exp_Report.docx    → 每实验×每班 1 份（封面信息预填）
  2. Template_Exp_Recognition.docx → 仅综合性/设计性实验各 1 份
  3. Template_Exp_Guide.docx     → 每课程 1 份（全实验汇编）

数据来源: context['experiments'] — course.yaml 中的实验列表
版本: 2.0 (2026-02-24) — 修复 B1-B14，对齐 Spec_Experiment.md v2026-02-24
"""

import copy
import re
from datetime import date, timedelta
from pathlib import Path

from lxml import etree

from scripts.docx_engine import (
    qn,
    XML_SPACE,
    get_paragraph_text,
    get_cell_text,
    merge_runs,
    replace_xxxx,
    set_run_text,
    fill_multiline,
    clone_table_row,
    get_table_cell,
    find_table_by_header,
    render_docx,
)

# 触发认定表的枚举值（B1/B2 修复）
RECOGNITION_TYPES = {'综合性', '设计性'}

# 中文序数对照表（指导书实验节标题用）
_ORDINAL_CN = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八'}


def _exp_sort_key(exp):
    """混合类型 ID 安全排序键。

    字符串 ID（如 'A', 'B'）按字母序排在前面，
    整数 ID（如 1, 2, 3）按数值序排在后面。
    这与课程 YAML 中的典型声明顺序一致：
      - 交互产品开发：A, B, 2, 3, 4
      - 信息可视化：1, 2, 3, 4
    """
    eid = exp.get('id', 999)
    if isinstance(eid, str):
        return (0, 0, eid)   # 字符串 ID 优先，按字母排
    return (1, eid, '')      # 整数 ID 其次，按数值排


# ───────────────────────────────────────────────────────────────────────
# 公共辅助函数
# ───────────────────────────────────────────────────────────────────────

def _format_steps_as_text(steps: list) -> str:
    """将 exp_x.yaml 的 steps 结构转换为指导书正文文本。

    每个步骤格式：
      步骤 S1：{step.name}
      {guide_text 逐行输出}
      （空行分隔下一步骤）

    如果 steps 为空或无 guide_text，返回空字符串。
    """
    if not steps:
        return ''
    lines = []
    for step in steps:
        sid = step.get('id', '')
        name = step.get('name', '')
        guide_texts = step.get('guide_text', [])
        if not guide_texts:
            continue
        lines.append(f"步骤 {sid}：{name}")
        for gt in guide_texts:
            gt = gt.strip() if gt else ''
            if gt:
                lines.append(gt)
        lines.append('')  # 步骤间空行
    return '\n'.join(lines).strip()

def _extract_class_abbr(class_name: str) -> str:
    """从班级全名提取简称，用于文件名后缀。

    策略：去掉年份数字和常见专业名称前缀后，取末尾特征词。
    例：'24数字媒体艺术影视班' → '影视班'
         '24数字媒体艺术游戏班' → '游戏班'
         '2023数字媒体艺术'     → '术'（回退取末4字）
    """
    # 已知专业前缀：去除后剩余部分即为班级标识词
    _MAJOR_PREFIXES = [
        '数字媒体艺术', '视觉传达设计', '产品设计', '动画', '影视摄影与制作',
        '数字媒体技术', '艺术设计',
    ]
    name = re.sub(r'^\d{2,4}', '', class_name).strip()
    for prefix in _MAJOR_PREFIXES:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    # 去掉空白后取剩余（可能是「影视班」「游戏班」等）
    name = name.strip()
    return name if name else class_name[-3:]


def _get_class_experiment_dates(context: dict, cls: dict, exp_id: int) -> str:
    """推算某班级某实验的上课日期（用于报告封面「实验日期」）。

    策略：
      1. 从 calendar 中找 exp_id 匹配的条目，获取 calendar 序号（1-based）
      2. 根据班级 week_range + excluded_weeks 映射为实际教学周次
      3. 从 _calc 取该周对应星期的上课日期
    若无法推算返回空字符串（保留 XXXX 模板原样）。
    """
    try:
        calc = context.get('_calc')
        if not calc:
            return ''

        # 1. 从 schedule_time 提取星期
        schedule_time = cls.get('schedule_time', '')
        wd_match = re.search(r'(周[一二三四五六日])', schedule_time)
        if not wd_match:
            return ''
        weekday_str = wd_match.group(1)

        # 2. 从 calendar 查找 exp_id 对应的 calendar 序号
        calendar_list = context.get('calendar', [])
        cal_idx = None  # 1-based calendar 序号
        for ci, week_item in enumerate(calendar_list):
            if week_item.get('exp_id') == exp_id:
                cal_idx = ci + 1  # calendar 序号从 1 开始
                break
        if cal_idx is None:
            return ''

        # 3. 将 calendar 序号映射为班级实际教学周次
        #    （复用教案生成器 _resolve_actual_week 的核心逻辑）
        week_range_str = str(cls.get('week_range', ''))
        excluded = set(cls.get('excluded_weeks', []) or [])
        if '-' in week_range_str:
            start_w = int(week_range_str.split('-')[0])
        else:
            start_w = 1

        # 线性映射：calendar 第 N 项对应实际第 (start_w + N - 1) 周
        # 但需跳过 excluded_weeks（与教案/进度表逻辑一致）
        actual_week = start_w
        mapped = 0
        total_weeks = int(week_range_str.split('-')[1]) if '-' in week_range_str else 18
        while mapped < cal_idx and actual_week <= total_weeks:
            if actual_week not in excluded:
                mapped += 1
            if mapped < cal_idx:
                actual_week += 1
        if mapped < cal_idx:
            return ''  # calendar 序号超出班级周次范围

        result = calc.get_class_date(actual_week, weekday_str)
        date_str = result.get('date', '')
        return date_str
    except Exception:
        return ''


# TODO: 若其他生成器需要类似功能，可迁移到 docx_engine.py
def _replace_after_colon(parent_elem, keyword: str, value: str):
    """在含 keyword 的段落或单元格中，将 XXXX 替换为 value。

    防御性策略：先 merge_runs，再扫描含 keyword 的 <w:t>，
    对同一段落内的 XXXX 或尾部追加 value。
    """
    for p in parent_elem.iter(qn('w:p')):
        text = get_paragraph_text(p)
        if keyword in text:
            merge_runs(p)
            for t in p.iter(qn('w:t')):
                if t.text and keyword in t.text:
                    if 'XXXX' in t.text:
                        t.text = t.text.replace('XXXX', value)
                    elif t.text.rstrip().endswith(keyword):
                        t.text = t.text.rstrip() + value
                    break  # 只处理第一个匹配
            break


# TODO: 若其他生成器需要类似功能，可迁移到 docx_engine.py
def _fill_section_content(body, section_keyword: str, value: str):
    """找到含 section_keyword 节标题后的 XXXX 段落，用 fill_multiline 填充。

    查找策略：在 body 直接子元素中找含 section_keyword 的段落，
    然后对其后第一个含 XXXX 文本的段落调用 fill_multiline。
    """
    children = list(body)
    found_header = False
    for elem in children:
        if elem.tag != qn('w:p'):
            continue
        text = get_paragraph_text(elem)
        if not found_header:
            if section_keyword in text:
                found_header = True
        else:
            # 找到节标题后的第一个内容段落（可能是 XXXX 或空白）
            if 'XXXX' in text or text.strip() == '':
                if value:
                    fill_multiline(elem, value)
                return
            # 如果遇到下一个节标题，停止
            if re.match(r'[一二三四五六]、', text.strip()):
                return


def _date_to_chinese(date_str: str) -> str:
    """将 '2026-03-02' 或 '2026.03.02' 格式转为 '二〇二六年三月'。"""
    chinese_digits = {
        '0': '〇', '1': '一', '2': '二', '3': '三', '4': '四',
        '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'
    }
    try:
        date_str_clean = date_str.replace('.', '-')
        parts = date_str_clean.split('-')
        year_str = ''.join(chinese_digits.get(c, c) for c in parts[0])
        month = int(parts[1])
        return f"{year_str}年{month}月"
    except Exception:
        return date_str


# ═══════════════════════════════════════════════════════════════════════
# 1. 实验报告封面 (Report) — 每实验×每班 1 份
# ═══════════════════════════════════════════════════════════════════════

# TODO: 若其他生成器需要类似功能，可迁移到 docx_engine.py
def _replace_para_xxxx(body, keyword: str, value: str):
    """在段落中找含 keyword 的段落，把**该段落内**的 XXXX run 替换为 value。

    模板结构：「关键字：」是 run[0]，「XXXX」是 run[1]，两个独立 run 同一段落。
    策略：找到含 keyword 的段落 → 遍历所有 run → 找第一个 text='XXXX' 的 run → 替换。
    """
    for p in body.iter(qn('w:p')):
        full_text = get_paragraph_text(p)
        if keyword in full_text:
            for r in p.findall(qn('w:r')):
                t_el = r.find(qn('w:t'))
                if t_el is not None and t_el.text == 'XXXX':
                    t_el.text = value
                    t_el.set(XML_SPACE, 'preserve')
                    return


def _fill_table_cell_xxxx(tc, value: str):
    """在单元格内找第一个 XXXX 替换为 value（直接 run 级别）。"""
    for p in tc.findall(qn('w:p')):
        for r in p.findall(qn('w:r')):
            t_el = r.find(qn('w:t'))
            if t_el is not None and t_el.text == 'XXXX':
                t_el.text = value
                t_el.set(XML_SPACE, 'preserve')
                return
    # 如果没有独立 XXXX run，尝试「关键字+XXXX」同文本替换
    for p in tc.findall(qn('w:p')):
        merge_runs(p)
        for r in p.findall(qn('w:r')):
            t_el = r.find(qn('w:t'))
            if t_el is not None and t_el.text and 'XXXX' in t_el.text:
                t_el.text = t_el.text.replace('XXXX', value, 1)
                t_el.set(XML_SPACE, 'preserve')
                return


def _fill_report(root, context: dict):
    """填充实验报告封面的 XXXX 占位符。

    模板真实结构 (Template_Exp_Report.docx)：
      封面段落（P12-P18）：每段两个 run——「关键字：」run + 「XXXX」run
        P12: 项目名称：XXXX
        P13: 学院名称：XXXX
        P14: 专业班级：XXXX
        P15: 学生学号：XXXX  ← 学生填，跳过
        P16: 学生姓名：XXXX  ← 学生填，跳过
        P17: 授课教师：XXXX
        P18: 实验日期：XXXX
      正文大表格（1张，8行）：
        R0: 实验地点（C1-XXXX）| 指导教师（C2-标签，C3-XXXX）
        R1: 同组人员（学生填，跳过）
        R2：「一、实验目的XXXX」← 同一单元格，关键字+XXXX 合并文本
        R3：「二、实验条件（环境）XXXX」
        R4：「三、实验方法（原理）XXXX」
        R5：「四、实验内容（步骤）XXXX」← 学生填，跳过
        R6：「五、实验结果分析XXXX」← 学生填，跳过
        R7：成绩评定（教师手填，跳过）

    程序预填：项目名称/学院名称/专业班级/授课教师/实验日期/实验地点/指导教师/一~三节
    学生填写：学号/姓名/同组人员/四五节内容 → 保留 XXXX
    """
    body = root.find(qn('w:body'))

    course = context.get('course', {})
    teacher = context.get('teacher', {})
    exp = context.get('current_experiment', {})
    cls = context.get('current_class', {})

    # ——— 封面段落：每段独立 XXXX run（精确关键字匹配替换）———
    _replace_para_xxxx(body, '项目名称：', exp.get('name', ''))
    _replace_para_xxxx(body, '学院名称：', course.get('department', ''))
    _replace_para_xxxx(body, '专业班级：', cls.get('name', ''))
    _replace_para_xxxx(body, '授课教师：', teacher.get('name', ''))

    exp_date = context.get('_exp_date', '')
    if exp_date:
        _replace_para_xxxx(body, '实验日期：', exp_date)

    # ——— 正文大表格 ———
    tables = list(body.iter(qn('w:tbl')))
    if not tables:
        return
    tbl = tables[0]
    rows = tbl.findall(qn('w:tr'))

    # R0: 实验地点（C1=XXXX）/ 指导教师（C3=XXXX）
    if len(rows) > 0:
        r0_cells = rows[0].findall(qn('w:tc'))
        # R0 结构: C0=「实验地点：」C1=「XXXX」C2=「指导教师：」C3=（第4列，但可能合并）
        # 通过文本内容定位各单元格
        classroom = cls.get('classroom', '')
        teacher_name = teacher.get('name', '')
        for ci, tc in enumerate(r0_cells):
            ct = get_paragraph_text(tc.findall(qn('w:p'))[0]) if tc.findall(qn('w:p')) else ''
            if ct.strip() == '' or ct.strip() == 'XXXX':
                # XXXX 单元格：根据位置判断填什么
                prev_label = ''
                if ci > 0:
                    prev_tc = r0_cells[ci - 1]
                    prev_label = get_paragraph_text(prev_tc.findall(qn('w:p'))[0]) if prev_tc.findall(qn('w:p')) else ''
                if '实验地点' in prev_label and classroom:
                    _fill_table_cell_xxxx(tc, classroom)
                elif '指导教师' in prev_label and teacher_name:
                    _fill_table_cell_xxxx(tc, teacher_name)

    # R2-R4: 每行单元格内有多段落，P0=「一、实验目的」，P1=「XXXX」（独立段落）
    section_map = [
        ('一、实验目的', exp.get('objectives', '')),
        ('二、实验条件', exp.get('equipment', '')),
        ('三、实验方法', exp.get('methods', '')),
    ]
    for row in rows[2:5]:  # R2, R3, R4
        tcs = row.findall(qn('w:tc'))
        for tc in tcs:
            all_paras = tc.findall(qn('w:p'))
            for kw, value in section_map:
                if not value:
                    continue
                # 找含关键字的段落（P0）
                for pi, p in enumerate(all_paras):
                    text = get_paragraph_text(p)
                    if kw in text:
                        # 在其后找第一个独立 XXXX 段落（P1）
                        for p2 in all_paras[pi + 1:]:
                            t2 = get_paragraph_text(p2).strip()
                            if t2 == 'XXXX' or t2 == '':
                                # 直接用 fill_multiline 填入内容
                                if value:
                                    fill_multiline(p2, value)
                                break
                            elif t2 and not t2.startswith('XXXX'):
                                break  # 遇到其他内容段落，停止
                        break


def gen_experiment_reports(base_dir: Path, output_dir: Path, context: dict):
    """生成实验报告文档（每实验×每班 1 份）。"""
    print("  - Generating Experiment Reports...")

    tpl_path = base_dir / "04_Experiment_Generator" / "Template_Exp_Report.docx"
    if not tpl_path.exists():
        print("    ⚠️ Template_Exp_Report.docx not found. Skipping.")
        return

    experiments = context.get('experiments', [])
    if not experiments:
        print("    ⚠️ No experiments in context. Skipping.")
        return

    course = context.get('course', {})
    course_name = course.get('name', '未命名')
    classes = course.get('classes', [{}])

    # B6 多班逻辑：对每个班级生成一套报告封面
    multi_class = len(classes) > 1

    for cls in classes:
        class_abbr = _extract_class_abbr(cls.get('name', ''))
        for exp in experiments:
            exp_id = exp.get('id', '?')
            exp_name = exp.get('name', f'实验{exp_id}')

            exp_context = context.copy()
            exp_context['current_experiment'] = exp
            exp_context['current_class'] = cls

            # 推算实验日期
            exp_date = _get_class_experiment_dates(context, cls, exp_id if isinstance(exp_id, int) else 1)
            exp_context['_exp_date'] = exp_date

            # 文件名：多班加后缀
            safe_name = exp_name.replace('/', '_').replace('&', '_')
            if multi_class:
                filename = f"{course_name}_实验报告封面_实验{exp_id}_{class_abbr}.docx"
            else:
                filename = f"{course_name}_实验报告封面_实验{exp_id}.docx"
            out_path = output_dir / filename

            try:
                render_docx(
                    template_path=tpl_path,
                    output_path=out_path,
                    fill_fn=_fill_report,
                    context=exp_context,
                )
                print(f"    ✨ Saved: {filename}")
            except Exception as e:
                print(f"    ❌ Failed ({filename}): {e}")


# ═══════════════════════════════════════════════════════════════════════
# 2. 实验认定表 (Recognition) — 仅综合性/设计性实验各 1 份
# ═══════════════════════════════════════════════════════════════════════

def _fill_recognition(root, context: dict):
    """填充实验认定表。

    表格结构：合并单元格，关键字段均位于行数据单元格的段落文本中。
    R0: 「项目名称：XXXX    学时   XXXX」—— 第1个XXXX=项目名，第2个XXXX=学时
    R1: 「项目类型：综合性实验（ XXXX ）    设计性实验（ XXXX ）」—— 类型勾选
    R2: 「所属课程名称：」后紧跟 XXXX 或空白
    后续行: 含「实验内容简介」字样的行填 summary
    """
    body = root.find(qn('w:body'))

    course = context.get('course', {})
    exp = context.get('current_experiment', {})
    exp_type = exp.get('type', '')

    # ——— 封面段落：开课专业 ———
    major = course.get('major', '')
    if major:
        _replace_after_colon(body, '开课专业：', major)

    # ——— 扫描全表所有段落，按关键字直接处理 ———
    tables = list(body.iter(qn('w:tbl')))
    if not tables:
        return

    # 对所有行的所有非重复单元格段落进行一次通扫
    _seen_paragraphs = set()  # 避免合并单元格重复处理

    for table in tables:
        for row in table.findall(qn('w:tr')):
            for tc in row.findall(qn('w:tc')):
                for p in tc.findall(qn('w:p')):
                    pid = id(p)
                    if pid in _seen_paragraphs:
                        continue
                    _seen_paragraphs.add(pid)

                    merge_runs(p)
                    text = get_paragraph_text(p)

                    # —— 项目名称 + 学时（同一段落，顺序替换两个 XXXX）——
                    if '项目名称：' in text and 'XXXX' in text:
                        exp_name = exp.get('name', '')
                        hours_str = str(exp.get('hours', ''))
                        # merge_runs 之后应该只有 1 个 run，直接操作其 <w:t>
                        replacements = [exp_name, hours_str]  # 依序：名称、学时
                        ri_repl = 0
                        for t_el in p.iter(qn('w:t')):
                            if t_el.text and 'XXXX' in t_el.text and ri_repl < len(replacements):
                                # 只替换第一次出现的XXXX
                                t_el.text = t_el.text.replace('XXXX', replacements[ri_repl], 1)
                                ri_repl += 1
                                # 如果同一个 t_el 还有 XXXX（即两个XXXX在同一节点），继续
                                if 'XXXX' in t_el.text and ri_repl < len(replacements):
                                    t_el.text = t_el.text.replace('XXXX', replacements[ri_repl], 1)
                                    ri_repl += 1
                                t_el.set(XML_SPACE, 'preserve')

                    # —— 类型勾选框（B1 修复）——
                    # merge_runs 后段落文本如 '项目类型：综合性实验（ XXXX' 和 ' ）  设计性实验（ XXXX'
                    # 各 run 的 w:t 包含类型关键字+XXXX，直接用同节点判断
                    elif '项目类型：' in text or ('综合性实验' in text and '设计性实验' in text):
                        for r in p.findall(qn('w:r')):
                            t_el = r.find(qn('w:t'))
                            if t_el is None or not t_el.text:
                                continue
                            if 'XXXX' in t_el.text:
                                if '综合性实验' in t_el.text:
                                    # 这个 run 包含综合性实验 + XXXX → 打或不打
                                    t_el.text = t_el.text.replace('XXXX', '√' if exp_type == '综合性' else ' ')
                                elif '设计性实验' in t_el.text:
                                    t_el.text = t_el.text.replace('XXXX', '√' if exp_type == '设计性' else ' ')

                    # —— 所属课程名称 ——
                    elif '所属课程名称：' in text:
                        course_name = course.get('name', '')
                        if course_name and 'XXXX' in text:
                            for t_el in p.iter(qn('w:t')):
                                if t_el.text and 'XXXX' in t_el.text:
                                    t_el.text = t_el.text.replace('XXXX', course_name, 1)
                                    break
                        elif course_name and text.rstrip().endswith('所属课程名称：'):
                            # 追加到末尾
                            for t_el in p.iter(qn('w:t')):
                                if t_el.text and t_el.text.rstrip().endswith('所属课程名称：'):
                                    t_el.text = t_el.text.rstrip() + course_name
                                    break

                    # —— 实验内容简介（B4）——
                    elif '实验内容简介' in text:
                        summary_val = exp.get('summary', '')
                        if summary_val and 'XXXX' in text:
                            for t_el in p.iter(qn('w:t')):
                                if t_el.text and 'XXXX' in t_el.text:
                                    t_el.text = t_el.text.replace('XXXX', summary_val, 1)
                                    break
                        elif summary_val:
                            # summary 可能在下一段落
                            pass  # 由下方「空白段落」逻辑处理

    # 处理 summary 在独立段落的情况（找到实验内容简介行后的第一个空白/XXXX段落）
    _in_summary_section = False
    for table in tables:
        for row in table.findall(qn('w:tr')):
            for tc in row.findall(qn('w:tc')):
                for p in tc.findall(qn('w:p')):
                    text = get_paragraph_text(p)
                    if '实验内容简介' in text:
                        _in_summary_section = True
                        continue
                    if _in_summary_section:
                        summary_val = exp.get('summary', '')
                        if summary_val and ('XXXX' in text or text.strip() == ''):
                            fill_multiline(p, summary_val)
                            _in_summary_section = False
                        elif text.strip():
                            _in_summary_section = False  # 遇到有内容的行，停止



def merge_runs_in_tc(tc):
    """对单元格内所有段落执行 merge_runs。"""
    for p in tc.findall(qn('w:p')):
        merge_runs(p)


def replace_xxxx_in_tc(tc, value: str):
    """替换单元格内所有 XXXX 为 value。"""
    for p in tc.findall(qn('w:p')):
        for t in p.iter(qn('w:t')):
            if t.text and 'XXXX' in t.text:
                t.text = t.text.replace('XXXX', value)


def gen_experiment_recognition(base_dir: Path, output_dir: Path, context: dict):
    """生成实验认定表（仅综合性/设计性实验，每实验 1 份）。"""
    print("  - Generating Experiment Recognition Forms...")

    tpl_path = base_dir / "04_Experiment_Generator" / "Template_Exp_Recognition.docx"
    if not tpl_path.exists():
        print("    ⚠️ Template_Exp_Recognition.docx not found. Skipping.")
        return

    experiments = context.get('experiments', [])
    if not experiments:
        print("    ⚠️ No experiments in context. Skipping.")
        return

    course_name = context.get('course', {}).get('name', '未命名')
    generated = 0

    for exp in experiments:
        # B2：类型过滤，仅触发综合性/设计性
        exp_type = exp.get('type', '')
        if exp_type not in RECOGNITION_TYPES:
            print(f"    ⏭️  跳过实验{exp.get('id')}（{exp_type}）—不触发认定表")
            continue

        exp_context = context.copy()
        exp_context['current_experiment'] = exp

        exp_id = exp.get('id', '?')
        exp_name = exp.get('name', f'实验{exp_id}')
        safe_name = exp_name.replace('/', '_').replace('&', '_').replace(' ', '_')
        filename = f"{course_name}_实验认定表_实验{exp_id}_{safe_name}.docx"
        out_path = output_dir / filename

        try:
            render_docx(
                template_path=tpl_path,
                output_path=out_path,
                fill_fn=_fill_recognition,
                context=exp_context,
            )
            print(f"    ✨ Saved: {filename}")
            generated += 1
        except Exception as e:
            print(f"    ❌ Failed ({filename}): {e}")

    print(f"    📊 共生成认定表 {generated} 份")


# ═══════════════════════════════════════════════════════════════════════
# 3. 实验指导书 (Guide) — 每课程 1 份
# ═══════════════════════════════════════════════════════════════════════

def _fill_guide_cover(body, context: dict):
    """填充实验指导书封面。

    模板真实结构 (Template_Exp_Guide.docx)：
      P14: 课程代码：XXXX   ← 各自独立 run
      P15: 课程名称：XXXX
      P16: 适用年级：XXXX
      P17: 适用专业：XXXX
      P22: 二零二六年三月一日  ← 已硬编码，无 XXXX，跳过
      P29: 课程代码：XXXX  ...  课程名称：XXXX  ← 多 run 混合段落（一览表下方）
    """
    course = context.get('course', {})

    # 从班级名推断年级
    grade_str = ''
    classes = course.get('classes', [])
    if classes:
        class_name = classes[0].get('name', '')
        year_match = re.match(r'(\d{4}|\d{2})', class_name)
        if year_match:
            yr = year_match.group(1)
            grade_str = f"20{yr}级" if len(yr) == 2 else f"{yr}级"

    # 封面四个段落（P14-P17）：独立 XXXX run
    _replace_para_xxxx(body, '课程代码：', course.get('code', ''))
    _replace_para_xxxx(body, '课程名称：', course.get('name', ''))
    _replace_para_xxxx(body, '适用年级：', grade_str)
    _replace_para_xxxx(body, '适用专业：', course.get('major', ''))

    # P29：「课程代码：XXXX ... 课程名称：XXXX」
    # P29 有多个 run，需找含关键字的段落，然后按出现顺序替换两个 XXXX
    code_val = course.get('code', '')
    name_val = course.get('name', '')
    for p in body.iter(qn('w:p')):
        text = get_paragraph_text(p)
        if '课程代码：' in text and '课程名称' in text:
            # 遍历所有 run，顺序替换：第1个XXXX=课程代码，第2个XXXX=课程名称
            replacements = [code_val, name_val]
            ri_repl = 0
            for r in p.findall(qn('w:r')):
                t_el = r.find(qn('w:t'))
                if t_el is not None and t_el.text == 'XXXX' and ri_repl < len(replacements):
                    t_el.text = replacements[ri_repl]
                    t_el.set(XML_SPACE, 'preserve')
                    ri_repl += 1
            break


def _fill_guide_toc(body, experiments: list):
    """填充目录区域中的实验名占位符。

    模板真实目录结构（已通过 XML 审查确认）：
      P25: hyperlink > run[0]='实验一' run[1]='  ' run[2]='XXXX' ...（hyperlink 内）
      P26: hyperlink > run[0]='实验二' run[1]='  ' run[2]='XXXX' ...
      P27: hyperlink > run[0]='实验三' run[1]='  XXXX' ...（合并 run，前有空格）
      P28: 普通段落   > run[0]='综合项目' run[1]=' XXXX'（普通 run 前有空格）

    ⚠️ 扫描范围必须限制在目录区（「目  录」之后、「开课形式」之前），
       否则会误替换正文节标题中的 XXXX，导致 _fill_guide_experiment_sections 失效。
    """
    exps_sorted = sorted(experiments, key=_exp_sort_key)

    # 构建目录关键字 → 实验名映射
    # 模板目录区固定包含「实验一/二/三 + 综合项目」共 4 个条目
    # 超出 4 个的实验无法在目录中渲染，发出警告
    kw_to_name = {}
    for idx, exp in enumerate(exps_sorted):
        if idx == 3:
            kw_to_name['综合项目'] = exp.get('name', '')
        elif idx < 3:
            ordinal = _ORDINAL_CN.get(idx + 1, str(idx + 1))
            kw_to_name[f'实验{ordinal}'] = exp.get('name', '')
        else:
            print(f"    ⚠️ 实验 {exp.get('id')}「{exp.get('name', '')}」超出模板目录容量（第{idx+1}个），目录中无法渲染")

    # 定位目录区范围：从「目  录」段落开始，到「开课形式」或「广州南方学院课程实验项目一览表」所在行停止
    all_paras = list(body.iter(qn('w:p')))
    toc_start = None
    toc_end = None
    for pi, p in enumerate(all_paras):
        txt = ''.join((t.text or '') for t in p.iter(qn('w:t'))).strip()
        if toc_start is None and '目  录' in txt:
            toc_start = pi
        elif toc_start is not None and toc_end is None:
            if '开课形式' in txt or ('广州南方学院' in txt and '一览表' in txt and pi > toc_start + 3):
                toc_end = pi
                break
    if toc_start is None:
        toc_end = min(30, len(all_paras))  # 默认扫描前30段
        toc_start = 0
    if toc_end is None:
        toc_end = toc_start + 20  # 目录通常不超过 20 行

    toc_paragraphs = all_paras[toc_start:toc_end]

    for p in toc_paragraphs:
        full_text = ''.join((t.text or '') for t in p.iter(qn('w:t')))
        if 'XXXX' not in full_text:
            continue

        matched_name = None
        for kw, name in kw_to_name.items():
            if kw in full_text:
                matched_name = name
                break
        if matched_name is None:
            continue

        # 在段落内（含 hyperlink 内）找含 XXXX 的 run 替换（包含匹配，保留前置空格）
        for r in p.iter(qn('w:r')):
            t_el = r.find(qn('w:t'))
            if t_el is not None and t_el.text and 'XXXX' in t_el.text:
                t_el.text = t_el.text.replace('XXXX', matched_name)
                t_el.set(XML_SPACE, 'preserve')
                break


def _fill_guide_overview_table(body, experiments: list):
    """填充实验项目一览表。

    模板真实结构（6行）：
      R0: 表头（序号｜项目名称｜实验类型｜开出要求｜每组人数｜学时）
      R1: 1 | XXXX | XXXX | 必做 | XXXX | XXXX  ← 实验1-3 格式相同
      R2: 2 | XXXX | XXXX | 必做 | XXXX | XXXX
      R3: 3 | XXXX | XXXX | 必做 | XXXX | XXXX
      R4: 4 | 综合项目：XXXX | XXXX | 必做 | XXXX | XXXX  ← 实验4，项目名称列不同
      R5: 合计 | XXXX | ...  | XXXX

    模板已有4行数据（R1-R4），直接填充，不需要 clone。
    列顺序：序号(0) | 项目名称(1) | 实验类型(2) | 开出要求(3) | 每组人数(4) | 学时(5)
    """
    # 找到一览表（含「序号」表头）
    overview_table = None
    for tbl in body.findall('.//{%s}tbl' % qn('w:tbl').split('}')[0].lstrip('{')):
        first_row_text = ''
        rows = tbl.findall(qn('w:tr'))
        if rows:
            first_row_text = ''.join(
                (t.text or '') for t in rows[0].iter(qn('w:t'))
            )
        if '序号' in first_row_text and '项目名称' in first_row_text:
            overview_table = tbl
            break

    if overview_table is None:
        overview_table = find_table_by_header(body, '项目名称')
    if overview_table is None:
        print("    ⚠️ 未找到一览表，跳过")
        return

    rows = overview_table.findall(qn('w:tr'))
    exps_sorted = sorted(experiments, key=_exp_sort_key)

    # 数据行（去掉表头 R0 和合计行 R-1）
    data_rows = rows[1:-1]

    # 动态扩展：若实验数 > 模板数据行数，克隆最后一个数据行
    if len(exps_sorted) > len(data_rows):
        extra_needed = len(exps_sorted) - len(data_rows)
        last_data_row_idx = len(rows) - 2  # 合计行前一行
        new_rows = clone_table_row(overview_table, last_data_row_idx, extra_needed)
        # 更新序号列
        for ni, nr in enumerate(new_rows):
            tcs = nr.findall(qn('w:tc'))
            if tcs:
                # 序号列 (C0): 更新为 len(data_rows) + ni + 1
                for p in tcs[0].findall(qn('w:p')):
                    set_run_text(p, str(len(data_rows) + ni + 1))
        # 重新获取行列表
        rows = overview_table.findall(qn('w:tr'))
        data_rows = rows[1:-1]
        print(f"    📋 一览表已动态扩展 {extra_needed} 行（共 {len(data_rows)} 个实验）")

    for row_elem, exp in zip(data_rows, exps_sorted):
        tcs = row_elem.findall(qn('w:tc'))
        exp_id = exp.get('id', '')
        exp_name = exp.get('name', '')
        exp_type = exp.get('type', '')
        group_size = str(exp.get('group_size', ''))
        hours = str(exp.get('hours', ''))

        for ci, tc in enumerate(tcs):
            if ci == 0:
                continue  # 序号列：模板已有1/2/3/4，不覆盖
            elif ci == 1:
                # 项目名称：R4是「综合项目：XXXX」格式，其余是独立 XXXX
                _fill_table_cell_xxxx(tc, exp_name)
            elif ci == 2:
                # 实验类型
                _fill_table_cell_xxxx(tc, exp_type)
            elif ci == 3:
                continue  # 开出要求：模板已写「必做」，不覆盖
            elif ci == 4:
                # 每组人数
                _fill_table_cell_xxxx(tc, group_size)
            elif ci == 5:
                # 学时
                _fill_table_cell_xxxx(tc, hours)

    # 合计行（最后一行）
    last_row = rows[-1]
    last_cells = last_row.findall(qn('w:tc'))
    total_hours = sum(e.get('hours', 0) for e in exps_sorted)
    total_count = len(exps_sorted)

    # R5 结构：合计(0) | 项数XXXX(1) | ...(2-4空) | 总学时XXXX(5)
    for ci, tc in enumerate(last_cells):
        ct = get_paragraph_text(tc.findall(qn('w:p'))[0]) if tc.findall(qn('w:p')) else ''
        if 'XXXX' in ct:
            if ci == 1:
                _fill_table_cell_xxxx(tc, str(total_count))
            elif ci == len(last_cells) - 1:
                _fill_table_cell_xxxx(tc, str(total_hours))


def _fill_guide_experiment_sections(body, experiments: list):
    """填充实验节正文。

    模板真实结构：
      P34: 「实验一  XXXX」    ← 「实验一  」+「XXXX」两个 run
      P35: （空行/分隔）
      P36: 「一、实验目的」     ← 固定文本，不替换
      P37: 「XXXX」            ← 独立 XXXX 段落，填 objectives
      P38: 「二、实验设备与环境」
      P39: 「XXXX」            ← 填 equipment
      P40: 「三、实验要求」
      P41: 「XXXX」            ← 填 requirements
      P42: 「四、实验步骤与要点」
      P43: 「XXXX」            ← 填 methods
      P44: 「五、实验结论」
      P45: 「XXXX」            ← 填 conclusions
      P46: 「六、思考题」（实验3和综合项目无此节）
      P47: 「XXXX」            ← 填 questions
      P48: 「实验二  XXXX」    ← 下一实验节开始
      ...
      P73: 「综合项目  XXXX」  ← 最后实验节（类型标签不同！）

    关键：每个 XXXX 段落是**段落本身只有一个独立 XXXX run**。
    """
    # 收集所有段落（扁平列表，用于顺序扫描）
    all_paragraphs = list(body.iter(qn('w:p')))

    exps_sorted = sorted(experiments, key=_exp_sort_key)

    for idx, exp in enumerate(exps_sorted):
        exp_id = exp.get('id', idx + 1)
        exp_name = exp.get('name', '')

        # 确定节标题关键字
        # 模板固定结构：实验一/二/三 + 综合项目（共 4 个节）
        # 超出模板容量的实验无法渲染节正文
        if idx == 3:  # 第4个实验（综合项目）
            section_title_kw = '综合项目  '
        elif idx < 3:
            ordinal = _ORDINAL_CN.get(idx + 1, str(idx + 1))
            section_title_kw = f'实验{ordinal}  '
        else:
            ordinal = _ORDINAL_CN.get(idx + 1, str(idx + 1))
            section_title_kw = f'实验{ordinal}  '
            # 模板中大概率没有此节标题，后续会输出 ⚠️ 未找到实验节标题 警告

        # 1. 找到节标题段落，替换其中的 XXXX run
        # 目录行无 run（Word 域），正文节标题有 run，当且仅当有 XXXX 所在 run 才替换
        title_para_idx = None
        for pi, p in enumerate(all_paragraphs):
            text = get_paragraph_text(p)
            if section_title_kw in text and 'XXXX' in text:
                # 有 run 的才是正文节标题（目录行 runs=[]）
                runs = p.findall(qn('w:r'))
                if not runs:
                    continue
                # 在该段落内找含 XXXX 的 run，替换
                for r in runs:
                    t_el = r.find(qn('w:t'))
                    if t_el is not None and t_el.text and 'XXXX' in t_el.text:
                        # 保留前置空格，只替换 XXXX 部分
                        t_el.text = t_el.text.replace('XXXX', exp_name)
                        t_el.set(XML_SPACE, 'preserve')
                        title_para_idx = pi
                        break
                if title_para_idx is not None:
                    break

        if title_para_idx is None:
            print(f"    ⚠️ 未找到实验节标题: {section_title_kw.strip()}")
            continue

        # 2. 在节标题之后按内容标签顺序填充各小节
        # 小节内容映射：「小节标题关键字」→ 数据字段
        # 「四、实验步骤与要点」优先从 _overlay.steps 获取详细分步内容，
        # 无 overlay 时降级使用 course.yaml 的 methods 字段。
        overlay = exp.get('_overlay', {})
        overlay_steps = overlay.get('steps', [])
        if overlay_steps:
            methods_text = _format_steps_as_text(overlay_steps)
        else:
            methods_text = exp.get('methods', '')

        section_content_map = [
            ('一、实验目的',       exp.get('objectives', '')),
            ('二、实验设备与环境', exp.get('equipment', '')),
            ('三、实验要求',       exp.get('requirements', '')),
            ('四、实验步骤与要点', methods_text),
            ('五、实验结论',       exp.get('conclusions', '')),
        ]
        questions = exp.get('questions', '')
        if questions and idx < 2:  # 仅实验1-2有思考题
            section_content_map.append(('六、思考题', questions))

        # 从节标题后开始扫描
        scan_start = title_para_idx + 1
        next_section_title_idx = len(all_paragraphs)

        # 找下一个实验节的起始位置（用于限制扫描范围）
        for pi in range(scan_start, len(all_paragraphs)):
            txt = get_paragraph_text(all_paragraphs[pi])
            if any(f'实验{_ORDINAL_CN.get(j,"")}  ' in txt for j in range(1, 5)) or '综合项目  ' in txt:
                if pi > title_para_idx:
                    next_section_title_idx = pi
                    break

        # 在节内按顺序填充：找到小节标题关键字后的下一个 XXXX 段落
        subsection_paragraphs = all_paragraphs[scan_start:next_section_title_idx]
        for (kw, value) in section_content_map:
            if not value:
                continue
            kw_found_idx = None
            for pi, p in enumerate(subsection_paragraphs):
                if kw in get_paragraph_text(p):
                    kw_found_idx = pi
                    break
            if kw_found_idx is None:
                continue
            # 找关键字后的第一个「XXXX」段落（段落文本恰好是 XXXX）
            for pi in range(kw_found_idx + 1, len(subsection_paragraphs)):
                p = subsection_paragraphs[pi]
                text = get_paragraph_text(p)
                if text.strip() == 'XXXX':
                    # 直接替换该段落的 XXXX run
                    for r in p.findall(qn('w:r')):
                        t_el = r.find(qn('w:t'))
                        if t_el is not None and t_el.text == 'XXXX':
                            t_el.text = value
                            t_el.set(XML_SPACE, 'preserve')
                            break
                    break
                elif text.strip() and text.strip() != kw:
                    break  # 遇到非空非目标段落，停止


def _fill_guide(root, context: dict):
    """实验指导书填充主函数。"""
    body = root.find(qn('w:body'))
    experiments = context.get('experiments', [])

    _fill_guide_cover(body, context)
    _fill_guide_toc(body, experiments)
    _fill_guide_overview_table(body, experiments)
    _fill_guide_experiment_sections(body, experiments)


def gen_experiment_guide(base_dir: Path, output_dir: Path, context: dict):
    """生成实验指导书（每课程 1 份）。"""
    print("  - Generating Experiment Guide...")

    tpl_path = base_dir / "04_Experiment_Generator" / "Template_Exp_Guide.docx"
    if not tpl_path.exists():
        print("    ⚠️ Template_Exp_Guide.docx not found. Skipping.")
        return

    course_name = context.get('course', {}).get('name', '未命名')
    # 归档命名
    from scripts.docx_engine import archive_filename
    arch_name = archive_filename(context, '实验指导书')
    if arch_name:
        filename = arch_name
    else:
        filename = f"{course_name}_实验指导书.docx"
    out_path = output_dir / filename

    try:
        render_docx(
            template_path=tpl_path,
            output_path=out_path,
            fill_fn=_fill_guide,
            context=context,
        )
        print(f"    ✨ Saved: {filename}")
    except Exception as e:
        print(f"    ❌ Failed ({filename}): {e}")


# ═══════════════════════════════════════════════════════════════════════
# 4. 统一入口
# ═══════════════════════════════════════════════════════════════════════

def gen_experiment(base_dir: Path, output_dir: Path, context: dict):
    """实验材料统一生成入口。

    生成 3 类文档:
    - 实验报告封面（每实验×每班 1 份）
    - 实验认定表  （每综合/设计性实验 1 份）
    - 实验指导书  （每课程 1 份）

    注意: Template_Exp_Analysis.docx（达成度分析）不在自动生成范围内，
    由教师手动维护。
    """
    # 优雅降级：无实验数据时静默跳过
    if not context.get('experiments'):
        print("  📋 No experiments defined. Skipping experiment materials.")
        return

    print("  📋 Generating Experiment Materials...")

    # 注入 SemesterDateCalculator 供内部使用（避免重复实例化）
    start_date = context.get('semester_config', {}).get('start_date', '')
    if start_date:
        try:
            from scripts.utils.semester_utils import SemesterDateCalculator
            context['_calc'] = SemesterDateCalculator(start_date)
        except Exception:
            context['_calc'] = None
    else:
        context['_calc'] = None

    # 确保输出目录存在
    exp_output = output_dir / "实验材料"
    exp_output.mkdir(exist_ok=True)

    gen_experiment_reports(base_dir, exp_output, context)
    gen_experiment_recognition(base_dir, exp_output, context)
    gen_experiment_guide(base_dir, exp_output, context)

    print("  ✅ Experiment materials generation complete.")
