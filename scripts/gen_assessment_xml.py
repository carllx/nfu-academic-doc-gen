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
    replace_jinja_tag,
)

import re
import jinja2
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
import yaml
from scripts.docx_engine import archive_filename

def _clean_xml_illegal_chars(val):
    if not isinstance(val, str):
        return val
    # Clean illegal XML characters and markdown/brackets
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x84\x86-\x9f]', '', val)
    return cleaned.replace('**', '').replace('【', '').replace('】', '')

def _deep_clean_data(data):
    if isinstance(data, dict):
        return {k: _deep_clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [_deep_clean_data(v) for v in data]
    elif isinstance(data, str):
        cleaned = _clean_xml_illegal_chars(data)
        if '\n' in cleaned:
            return cleaned.replace('\n', '\a')
        return cleaned
    elif isinstance(data, (int, float, bool)):
        return str(data)
    else:
        return data

def _generate_practice_materials(base_dir: Path, output_dir: Path, context: dict, exam_item: dict):
    assess_output = output_dir / "考核材料"
    assess_output.mkdir(exist_ok=True)
    gen_dir = base_dir / "05_Assessment_Generator"
    
    paper_tpl_path = gen_dir / "Template_Exam_Paper_AB.docx"
    criteria_tpl_path = gen_dir / "Template_Exam_Criteria_AB.docx"
    checklist_tpl_path = gen_dir / "Template_Exam_Checklist_AB.docx"

    if not paper_tpl_path.exists():
        print(f"    ⚠️ {paper_tpl_path.name} not found. Skipping practice generation.")
        return

    # Load global assessment config
    course_root = output_dir.parent
    global_cfg_path = course_root.parent / ".agent" / "config" / "global_assessment.yaml"
    global_cfg = {}
    if global_cfg_path.exists():
        with open(global_cfg_path, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f) or {}
            global_cfg = cfg.get('practice_exam_defaults', {})

    course = context.get('course', {})
    sem_str = course.get('semester', '')
    if len(sem_str) >= 9 and '-' in sem_str:
        parts = sem_str.split('-')
        if len(parts) >= 3:
            academic_year = f"{parts[0]}~{parts[1]}"
            semester_num = parts[2]
        else:
            academic_year = sem_str
            semester_num = '1'
    else:
        academic_year = sem_str
        semester_num = '1'

    grade = course.get('grade', '').replace('级', '')
    major = course.get('major', '')
    classes = course.get('classes', [])
    student_counts = []
    if classes:
        for c in classes:
            if c.get('student_count'):
                student_counts.append(str(c.get('student_count')))

    student_count_desc = "+".join(student_counts) if student_counts else ""
    department = course.get('department', '')
    course_nature = course.get('nature', '')
    teacher_name = context.get('teacher', {}).get('name', '')

    assessment_methods = context.get('assessment_methods', {})
    normal_score_ratio = assessment_methods.get('normal_score_ratio', 0)
    final_score_ratio = assessment_methods.get('final_score_ratio', 0)
    attendance_ratio = assessment_methods.get('attendance_ratio', 0)
    normal_other_ratio = normal_score_ratio - attendance_ratio
    assessment_ratio_desc = f"平时成绩 {normal_score_ratio}%（含考勤 {attendance_ratio}%），期末考核 {final_score_ratio}%"

    final_item_data = assessment_methods.get('final_item', {})
    ssot_method = final_item_data.get('assessment_type', exam_item.get("assessment_type", "大作业"))
    ssot_exam_type = "考查" if exam_item.get('type', '') == 'practice_ab' else ("考查" if "考查" in course_nature else "考试")

    base_data = {
        "academic_year": academic_year,
        "term": semester_num,
        "semester": semester_num,
        "semester_str": course.get('semester', ''),
        "grade_major": f"{grade}级 {major}" if major and grade else f"{grade}级",
        "grade": grade,
        "major": major,
        "course_name": course.get('name', ''),
        "department": department,
        "course_nature": course_nature,
        "teacher_name": teacher_name,
        "assessment_method": ssot_method,
        "exam_type": ssot_exam_type,
        "student_count_desc": student_count_desc,
        "assessment_ratio_desc": assessment_ratio_desc,
        "attendance_ratio": attendance_ratio,
        "normal_other_ratio": normal_other_ratio,
        "final_score_ratio": final_score_ratio,
    }
    
    practice_paper = exam_item.get('practice_paper', {})
    ab_versions = practice_paper.get('ab_versions', {})
    if not ab_versions:
        print("    ⚠️ No 'ab_versions' found in practice_paper. Skipping.")
        return

    # Extract A/B specific info for Criteria and Checklist
    a_theme = ab_versions.get('A', {}).get('practice_theme', '')
    b_theme = ab_versions.get('B', {}).get('practice_theme', '')
    a_reqs = ab_versions.get('A', {}).get('practice_requirements', '')
    b_reqs = ab_versions.get('B', {}).get('practice_requirements', '')
    a_delivs = ab_versions.get('A', {}).get('practice_deliverables', '')
    b_delivs = ab_versions.get('B', {}).get('practice_deliverables', '')
    a_deadline = ab_versions.get('A', {}).get('practice_deadline', '')
    b_deadline = ab_versions.get('B', {}).get('practice_deadline', '')

    base_data.update({
        'a_theme': a_theme, 'b_theme': b_theme,
        'a_reqs': a_reqs, 'b_reqs': b_reqs,
        'a_delivs': a_delivs, 'b_delivs': b_delivs,
        'a_deadline': a_deadline, 'b_deadline': b_deadline,
    })

    # Process Sections
    sections = exam_item.get('sections', [])
    chinese_numerals = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    processed_sections = []
    for i, sec in enumerate(sections):
        content = sec.get('questions', [{}])[0].get('content', '')
        processed_sections.append({
            'index_cn': chinese_numerals[i] if i < len(chinese_numerals) else str(i + 1),
            'section_name': sec.get('section_name', ''),
            'total_score': sec.get('total_score', ''),
            'content': content
        })
    base_data['sections'] = processed_sections

    jinja_env = jinja2.Environment(undefined=jinja2.StrictUndefined)

    # 1. Generate Papers A & B
    for version_key, version_data in ab_versions.items():
        doc_data = base_data.copy()
        doc_data["paper_version"] = version_key
        
        if version_key == 'A':
            doc_data["卷面编号"] = '②-1'
        elif version_key == 'B':
            doc_data["卷面编号"] = '②-2'
        else:
            doc_data["卷面编号"] = ''
        
        for k, v in global_cfg.items():
            doc_data[k] = v
        for k, v in version_data.items():
            doc_data[k] = v
            
        doc_data["total_questions"] = "1"
            
        processed_data = _deep_clean_data(doc_data)
                
        arch_name = archive_filename(context, f"{version_key}卷")
        out_name = arch_name if arch_name else f"实操试卷_{version_key}卷_{doc_data['course_name']}.docx"
        out_path = assess_output / out_name
        try:
            doc = DocxTemplate(paper_tpl_path)
            doc.render(processed_data, jinja_env)
            doc.save(out_path)
            print(f"    ✨ Saved Practice Paper {version_key}: {out_name}")
        except Exception as e:
            print(f"    ❌ Failed ({out_name}): {e}")

    # 2. Generate Criteria
    if criteria_tpl_path.exists():
        try:
            doc_criteria = DocxTemplate(criteria_tpl_path)
            
            # Load images for criteria
            a_img_path = ab_versions.get('A', {}).get('example_image', '')
            a_imgs_data = [a_img_path] if a_img_path else ab_versions.get('A', {}).get('example_images', [])
            b_img_path = ab_versions.get('B', {}).get('example_image', '')
            b_imgs_data = [b_img_path] if b_img_path else ab_versions.get('B', {}).get('example_images', [])

            a_imgs = []
            for img_path_str in a_imgs_data:
                img_path = course_root / img_path_str
                if img_path.exists():
                    a_imgs.append(InlineImage(doc_criteria, str(img_path), width=Inches(3.0)))

            b_imgs = []
            for img_path_str in b_imgs_data:
                img_path = course_root / img_path_str
                if img_path.exists():
                    b_imgs.append(InlineImage(doc_criteria, str(img_path), width=Inches(3.0)))
            
            criteria_data = base_data.copy()
            criteria_data = _deep_clean_data(criteria_data)
            criteria_data['a_imgs'] = a_imgs
            criteria_data['b_imgs'] = b_imgs
            
            arch_name = archive_filename(context, "期末考查评分标准")
            out_name = arch_name if arch_name else f"{base_data['course_name']}_期末考查评分标准.docx"
            out_criteria_path = assess_output / out_name
            
            doc_criteria.render(criteria_data, jinja_env)
            doc_criteria.save(out_criteria_path)
            print(f"    ✨ Saved Criteria: {out_name}")
        except Exception as e:
            print(f"    ❌ Failed Criteria for {base_data['course_name']}: {e}")

    # 3. Generate Checklist
    if checklist_tpl_path.exists():
        try:
            doc_checklist = DocxTemplate(checklist_tpl_path)
            
            arch_name = archive_filename(context, "期末考查自查表")
            out_name = arch_name if arch_name else f"{base_data['course_name']}_期末考查自查表.docx"
            out_checklist_path = assess_output / out_name
            
            checklist_data = base_data.copy()
            checklist_data = _deep_clean_data(checklist_data)
            
            doc_checklist.render(checklist_data, jinja_env)
            doc_checklist.save(out_checklist_path)
            print(f"    ✨ Saved Checklist: {out_name}")
        except Exception as e:
            print(f"    ❌ Failed Checklist for {base_data['course_name']}: {e}")

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
    if body is not None:
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

    # 注入卷面编号 (适用于 body 或 header)
    roll_id = context.get('_roll_id')
    if roll_id:
        for p in root.iter(qn('w:p')):
            replace_jinja_tag(p, '卷面编号', roll_id)


# ═══════════════════════════════════════════════════════════════════════
# 2. 命题自查表 (Checklist) — 表格填充
# ═══════════════════════════════════════════════════════════════════════

def _fill_checklist(root, context: dict):
    """填充命题自查表。

    Table[0] (24 rows): 基本信息
      row[1]: 课程名称
    """
    body = root.find(qn('w:body'))
    if body is None:
        return

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
    if assess_output.exists():
        import shutil
        shutil.rmtree(assess_output)
    assess_output.mkdir(exist_ok=True)

    exams = context.get('exams', {})
    final = exams.get('final_exam', [])
    if final and isinstance(final, list):
        exam_item = final[0]
        if exam_item.get('type') == 'practice_ab':
            print("  📝 Detected 'practice_ab' Exam Type. Switching to Practice Generator...")
            _generate_practice_materials(base_dir, output_dir, context, exam_item)
            return

    course_name = context.get('course', {}).get('name', '未命名')
    gen_dir = base_dir / "05_Assessment_Generator"

    # 归档命名支持
    from scripts.docx_engine import archive_filename

    # 定义 6 个模板及其填充函数和归档文件类型
    templates = [
        ("Template_Exam_Checklist_AB.docx", "自查表（A卷）", _fill_checklist),
        ("Template_Exam_Checklist_AB.docx", "自查表（B卷）", _fill_checklist),
        ("Template_Exam_Paper_AB.docx",     "A卷",           _fill_exam_header),
        ("Template_Exam_Paper_AB.docx",     "B卷",           _fill_exam_header),
        ("Template_Exam_Criteria_AB.docx",  "评分标准（A卷）", _fill_exam_header),
        ("Template_Exam_Criteria_AB.docx",  "评分标准（B卷）", _fill_exam_header),
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
        
        # Determine roll ID marker
        if 'A卷' in doc_type or doc_type == 'A卷':
            context['_roll_id'] = '②-1'
        elif 'B卷' in doc_type or doc_type == 'B卷':
            context['_roll_id'] = '②-2'
        else:
            context['_roll_id'] = ''

        try:
            render_docx(
                template_path=tpl_path,
                output_path=out_path,
                fill_fn=fill_fn,
                context=context,
                xml_files=['word/document.xml', 'word/header1.xml', 'word/header2.xml', 'word/header3.xml']
            )
            print(f"    ✨ Saved: {out_name}")
        except Exception as e:
            print(f"    ❌ Failed ({out_name}): {e}")

    print("  ✅ Assessment materials generation complete.")
