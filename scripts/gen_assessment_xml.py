"""
gen_assessment_xml.py — 纯 XML 操作的考核材料生成器

生成 3 类文档 (每类 A/B 两套):
  1. Checklist  — 命题自查表 (表格填充: 课程名/比例/题目分析)
  2. Paper      — 期末试卷   (表头填充: 年级/专业/课程名)
  3. Criteria   — 评分标准   (表头填充: 年级/专业/课程名)

数据来源:
  - course.yaml → course, teacher, assessment_methods, exams
"""

import copy
from pathlib import Path
from lxml import etree

from scripts.docx_engine import (
    qn,
    get_paragraph_text,
    get_cell_text,
    merge_runs,
    replace_xxxx,
    set_run_text,
    render_docx,
)


# ═══════════════════════════════════════════════════════════════════════
# 1. 通用表头填充 (Paper / Criteria 共用)
# ═══════════════════════════════════════════════════════════════════════

def _fill_exam_header(root, context: dict):
    """填充试卷/评分标准的表头信息。

    段落结构:
      [3]: "（     级           专业... 学年度 第  1 学期）"
      [4]: "课程名称                              A  卷"
      [5]: "考试形式 闭（开）卷          考核类型  考试"
      [6]: "本试卷共    大题，..."
    """
    body = root.find(qn('w:body'))
    children = list(body)

    course = context.get('course', {})
    course_name = course.get('name', '')
    semester = course.get('semester', '')
    major = course.get('major', '')

    # 从 classes 推断年级
    classes = course.get('classes', [])
    grade = ''
    if classes:
        import re
        match = re.match(r'(\d{4})', classes[0].get('name', ''))
        if match:
            grade = match.group(1)

    # P[3]: 填年级和专业
    if len(children) > 3:
        p = children[3]
        for t_elem in p.iter(qn('w:t')):
            if t_elem.text:
                # 替换年级空位
                if '级' in t_elem.text and grade:
                    t_elem.text = t_elem.text.replace('     级', f' {grade} 级', 1)
                # 替换专业空位
                if '专业' in t_elem.text and major:
                    t_elem.text = t_elem.text.replace('           专业', f' {major} 专业', 1)
                    t_elem.text = t_elem.text.replace('          专业', f' {major} 专业', 1)
                # 替换学期
                if '第  1 学期' in t_elem.text and semester:
                    sem_num = '2' if '-2' in semester else '1'
                    t_elem.text = t_elem.text.replace('第  1 学期', f'第 {sem_num} 学期')

    # P[4]: 填课程名称
    if len(children) > 4 and course_name:
        p = children[4]
        for t_elem in p.iter(qn('w:t')):
            if t_elem.text and '课程名称' in t_elem.text:
                # 在 "课程名称" 后面的空白处填入
                t_elem.text = t_elem.text.replace(
                    '课程名称',
                    f'课程名称  {course_name}',
                    1
                )

    # P[5]: 考查课 vs 考试课
    if len(children) > 5:
        p = children[5]
        nature = course.get('nature', '')
        if '考查' in nature:
            for t_elem in p.iter(qn('w:t')):
                if t_elem.text and '考试' in t_elem.text:
                    t_elem.text = t_elem.text.replace('考试', '考查')

    # P[6]: 填大题数
    if len(children) > 6:
        p = children[6]
        exams = context.get('exams', {})
        final = exams.get('final_exam', [])
        if final and isinstance(final, list):
            sections = final[0].get('sections', [])
            num_sections = len(sections)
            for t_elem in p.iter(qn('w:t')):
                if t_elem.text and '共    大题' in t_elem.text:
                    t_elem.text = t_elem.text.replace(
                        '共    大题',
                        f'共 {num_sections} 大题'
                    )


# ═══════════════════════════════════════════════════════════════════════
# 2. 命题自查表 (Checklist) — 表格填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_checklist(root, context: dict):
    """填充命题自查表。

    Table[0] (24 rows): 基本信息
      row[1]: 课程名称
    """
    body = root.find(qn('w:body'))

    course = context.get('course', {})
    course_name = course.get('name', '')

    # 定位第一个表格
    tables = list(body.iter(qn('w:tbl')))
    if not tables:
        return

    table = tables[0]
    rows = table.findall(qn('w:tr'))

    # row[1]: "课程名称：" — 填入课程名
    if len(rows) > 1:
        cells = rows[1].findall(qn('w:tc'))
        if cells:
            for t_elem in cells[0].iter(qn('w:t')):
                if t_elem.text and '课程名称：' in t_elem.text:
                    t_elem.text = t_elem.text.rstrip()
                    if not t_elem.text.endswith('：'):
                        pass
                    else:
                        t_elem.text = f'课程名称：{course_name}'


# ═══════════════════════════════════════════════════════════════════════
# 3. 生成入口函数
# ═══════════════════════════════════════════════════════════════════════

def gen_assessment(base_dir: Path, output_dir: Path, context: dict):
    """考核材料统一生成入口。

    生成 6 个文档 (A/B 各 3 种):
    - 命题自查表 Checklist A/B
    - 期末试卷 Paper A/B
    - 评分标准 Criteria A/B
    """
    print("  📝 Generating Assessment Materials...")

    assess_output = output_dir / "考核材料"
    assess_output.mkdir(exist_ok=True)

    course_name = context.get('course', {}).get('name', '未命名')
    gen_dir = base_dir / "05_Assessment_Generator"

    # 归档命名支持
    from scripts.docx_engine import archive_filename

    # 定义 6 个模板及其填充函数和归档文件类型
    templates = [
        ("Template_Exam_Checklist_A.docx", "自查表（A卷）", _fill_checklist),
        ("Template_Exam_Checklist_B.docx", "自查表（B卷）", _fill_checklist),
        ("Template_Exam_Paper_A.docx",     "A卷",           _fill_exam_header),
        ("Template_Exam_Paper_B.docx",     "B卷",           _fill_exam_header),
        ("Template_Exam_Criteria_A.docx",  "评分标准（A卷）", _fill_exam_header),
        ("Template_Exam_Criteria_B.docx",  "评分标准（B卷）", _fill_exam_header),
    ]

    for tpl_name, doc_type, fill_fn in templates:
        tpl_path = gen_dir / tpl_name
        if not tpl_path.exists():
            print(f"    ⚠️ {tpl_name} not found. Skipping.")
            continue

        # 优先使用归档命名
        arch_name = archive_filename(context, doc_type)
        if arch_name:
            out_name = arch_name
        else:
            out_name = f"{doc_type}_{course_name}.docx"

        out_path = assess_output / out_name
        try:
            render_docx(
                template_path=tpl_path,
                output_path=out_path,
                fill_fn=fill_fn,
                context=context,
            )
            print(f"    ✨ Saved: {out_name}")
        except Exception as e:
            print(f"    ❌ Failed ({out_name}): {e}")

    print("  ✅ Assessment materials generation complete.")
