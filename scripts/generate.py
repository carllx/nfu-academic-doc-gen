import argparse
import re
import sys
import os
import yaml
from pathlib import Path
from datetime import datetime

# Add project root to sys.path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from scripts.utils.semester_utils import SemesterDateCalculator, HolidayManager
from scripts.course_schema import CourseSchema
from scripts.gen_syllabus_xml import gen_syllabus as gen_syllabus_xml
from scripts.gen_schedule_xml import gen_schedule as gen_schedule_xml
from scripts.gen_experiment_xml import gen_experiment as gen_experiment_xml
from scripts.gen_assessment_xml import gen_assessment as gen_assessment_xml
from scripts.gen_lessonplan_xml import gen_lessonplan as gen_lessonplan_xml

def load_yaml(path: Path):
    if not path.exists():
        print(f"❌ Config not found: {path}")
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def _collect_final_docx(output_dir: Path) -> list:
    """收集 Output 目录中需要转换为 PDF 的最终交付 docx 文件。

    规则：
      - 顶层 *.docx（大纲、进度表等）
      - 教案/ 下的归档命名文件或合并版（排除散页、首页、尾页署名）
      - 考核材料/ 下所有 *.docx
      - 实验材料/ 下的归档命名文件或合并版
    """
    finals = []

    # 1. 顶层文件（大纲、进度表等）
    for f in output_dir.glob('*.docx'):
        finals.append(f)

    # 2. 教案子目录
    lesson_dir = output_dir / '教案'
    if lesson_dir.exists():
        for f in lesson_dir.glob('*.docx'):
            name = f.name
            # 排除散页（教案_第N周_）、首页、尾页署名
            if re.match(r'教案_第\d+周_', name):
                continue
            if name in ('教案_首页.docx', '教案_尾页署名.docx'):
                continue
            # 保留：合并版 或 归档命名文件
            finals.append(f)

    # 3. 考核材料子目录
    exam_dir = output_dir / '考核材料'
    if exam_dir.exists():
        for f in exam_dir.glob('*.docx'):
            finals.append(f)

    # 4. 实验材料子目录
    exp_dir = output_dir / '实验材料'
    if exp_dir.exists():
        for f in exp_dir.glob('*.docx'):
            name = f.name
            # 排除散页实验单文件（实验N_xxx.docx），只保留合并版或归档命名
            if re.match(r'实验\d+_', name):
                continue
            finals.append(f)

    return sorted(finals)


def generate_documents(course_dir_name: str, base_dir: Path, output_pdf: bool = True):
    """
    Main generation logic
    """
    # 1. Locate Course Directory
    potential_roots = [
        base_dir / "2025-2026-2 课程" / course_dir_name,
        base_dir.parent / "2025-2026-2 课程" / course_dir_name
    ]
    
    course_root = None
    for p in potential_roots:
        if p.exists():
            course_root = p
            break
            
    if not course_root:
        print(f"❌ Course directory not found for: {course_dir_name}")
        return

    config_path = course_root / "course.yaml"
    print(f"📂 Processing: {course_dir_name}")
    print(f"📄 Config: {config_path}")

    # 2. Load Data
    data = load_yaml(config_path)
    if not data:
        return

    # 3. Load System Data (Requirements)
    reqs_path = base_dir / "00_Data_Context" / "graduation_requirements.yaml"
    system_reqs = load_yaml(reqs_path)

    # 构建毕业要求观测点字典 (e.g. {"2.2", "3.1", ...})
    valid_points = set()
    if system_reqs and 'requirements' in system_reqs:
        for req in system_reqs['requirements'].values():
            for pt_id in req.get('points', {}).keys():
                valid_points.add(str(pt_id))

    # Validation: 从 course.yaml 内嵌的 objectives 校验合规性
    # support_level (H/M/L) 已内嵌到每个 objective 中 (Schema 2.2)
    if 'objectives' in data:
        defined_points = {}  # {point_id: support_level}
        missing_level = []
        invalid_points = []
        for cat in ['knowledge', 'ability', 'quality']:
            for obj in data['objectives'].get(cat, []):
                for m in obj.get('mappings', []):
                    p_str = str(m.get('point', ''))
                    match = re.search(r"(\d+\.\d+)", p_str)
                    if match:
                        point_id = match.group(1)
                        level = m.get('support_level', '')
                        defined_points[point_id] = level
                        if level not in ('H', 'M', 'L'):
                            missing_level.append(f"{cat}[{obj.get('index','')}] point={point_id}")
                        if valid_points and point_id not in valid_points:
                            invalid_points.append(f"{cat}[{obj.get('index','')}] point={point_id}")

        if missing_level:
            print(f"  ⚠️  [Compliance] objectives 缺少 support_level (H/M/L): {missing_level}")
        if invalid_points:
            print(f"  ⚠️  [Compliance] objectives 引用了不存在的毕业要求观测点: {invalid_points}")

        if defined_points:
            print(f"  ✅  Course supports {len(defined_points)} graduation points: {set(defined_points.keys())}")
    
    # 4. Context Preparation
    context = data.copy()
    context['_output_pdf'] = output_pdf

    # 4a. 加载 schema_type（控制课程目标的输出格式：detailed/coarse/none）
    tp_version = data.get('course', {}).get('training_plan_version', '2025')
    grad_req_path = base_dir / "00_Data_Context" / "training_plans" / f"graduation_requirements_{tp_version}.yaml"
    if grad_req_path.exists():
        grad_req_data = load_yaml(grad_req_path)
        context['_schema_type'] = grad_req_data.get('schema_type', 'detailed') if grad_req_data else 'detailed'
        print(f"  📋 schema_type = '{context['_schema_type']}' (from training_plan v{tp_version})")
    else:
        context['_schema_type'] = 'detailed'
        print(f"  ⚠️  graduation_requirements_{tp_version}.yaml 未找到，默认 schema_type='detailed'")

    # Feature: Date Calculation with Holidays
    start_date_str = data.get('semester_config', {}).get('start_date')
    if not start_date_str:
        print("  ⚠️  semester_config.start_date 未设置，跳过日期计算")
    if start_date_str:
        calc = SemesterDateCalculator(start_date_str)
        context['calculated'] = {}
        
        # Prepare flat list for Schedule Table
        schedule_rows = []
        
        # Enrich calendar with dates
        if 'calendar' in context:
            for week in context['calendar']:
                w_num = week.get('week')
                if w_num:
                    s, e = calc.get_week_range(w_num)
                    week['date_start'] = s
                    week['date_end'] = e
                    week['date_range'] = f"{s}-{e}"
                    
                    # For classes generation (Schedule)
                    # We need to list specific dates for each class occurrence
                    if 'classes' in context['course']:
                         class_dates = []
                         weekday_map = {
                             "周一": 0, "周二": 1, "周三": 2, "周四": 3,
                             "周五": 4, "周六": 5, "周日": 6
                         }
                         
                         for cls in context['course']['classes']:
                             # Parse '周一1-2节' -> '周一'
                             # Simple heuristic: take first 2 chars
                             schedule_str = cls.get('schedule_time', '')
                             wd_match = re.search(r'(周[一二三四五六日])', schedule_str)
                             weekday_str = wd_match.group(1) if wd_match else ''

                             if weekday_str in weekday_map:
                                 offset = weekday_map[weekday_str]
                                 # Calculate date
                                 class_info = calc.get_class_date(w_num, weekday_str)
                                 
                                 cls_occurrence = {
                                     "name": cls['name'],
                                     "location": cls.get('classroom', ''),
                                     "time": schedule_str,
                                     "date": class_info['date'],
                                     "is_holiday": class_info['is_holiday'],
                                     "holiday_name": "节日" if class_info['is_holiday'] else ""
                                 }
                                 class_dates.append(cls_occurrence)
                                 
                                 # Add to flat rows
                                 schedule_rows.append({
                                     "week": w_num,
                                     "date": class_info['date'],
                                     "time": schedule_str,
                                     "location": cls.get('classroom', ''),
                                     "topic": week.get('topic', ''),
                                     "content": week.get('content', ''),
                                     "task": week.get('task', ''),
                                     "holiday_name": cls_occurrence['holiday_name']
                                 })
                         
                         week['class_dates'] = class_dates
        
        context['schedule_rows'] = schedule_rows

    # 5. 加载 exp_x.yaml 增量数据层
    # exp_x.yaml 位于课程工作区 practices/experiments/ 目录下，
    # 包含 steps（分步骤指导）、report_prompt、grading_rubric 等详细内容。
    # 按 exp_id 匹配 course.yaml 的 experiments[] 条目，挂载到 _overlay 子键。
    exp_overlay_dir = course_root / "practices" / "experiments"
    if exp_overlay_dir.is_dir():
        overlay_count = 0
        for exp_file in sorted(exp_overlay_dir.glob("exp_*.yaml")):
            exp_overlay = load_yaml(exp_file)
            if not exp_overlay:
                continue
            overlay_id = exp_overlay.get('exp_id')
            if overlay_id is None:
                print(f"    ⚠️ {exp_file.name} 缺少 exp_id 字段，跳过")
                continue
            # 按 exp_id 匹配 course.yaml 的 experiments[] 条目
            matched = False
            for exp in context.get('experiments', []):
                if exp.get('id') == overlay_id:
                    exp['_overlay'] = exp_overlay
                    overlay_count += 1
                    matched = True
                    break
            if not matched:
                print(f"    ⚠️ {exp_file.name} (exp_id={overlay_id}) 未匹配到 course.yaml 中的实验，跳过")
        if overlay_count:
            print(f"    📋 已加载 {overlay_count} 份实验增量配置 (exp_x.yaml)")

    # 6. Pipelines
    output_dir = course_root / "Output"
    output_dir.mkdir(exist_ok=True)

    # A. Syllabus (方案 A: 纯 XML 操作)
    gen_syllabus_xml(base_dir, output_dir, context)
    
    # B. Schedule (方案 A: 纯 XML 操作)
    gen_schedule_xml(base_dir, output_dir, context)
    
    # C. Lesson Plans (方案 A: 纯 XML 操作)
    gen_lessonplan_xml(base_dir, output_dir, context)

    # D. Experiment Materials (方案 A: 纯 XML 操作)
    gen_experiment_xml(base_dir, output_dir, context)

    # E. Assessment Materials (方案 A: 纯 XML 操作)
    gen_assessment_xml(base_dir, output_dir, context)

    # F. PDF 转换（后置步骤）
    if output_pdf:
        from scripts.pdf_converter import batch_convert_to_pdf
        final_docx = _collect_final_docx(output_dir)
        if final_docx:
            batch_convert_to_pdf(final_docx)
        else:
            print("  ⚠️ 未找到需要转换的 docx 文件")
    
    print(f"✅ All documents generated for {course_dir_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate course documents.")
    parser.add_argument("--course", help="Course directory name", required=True)
    parser.add_argument("--pdf", action="store_true", default=True,
                        help="同时输出 PDF（默认开启）")
    parser.add_argument("--no-pdf", dest="pdf", action="store_false",
                        help="仅输出 DOCX，不生成 PDF")
    args = parser.parse_args()
    
    root = Path(__file__).parent.parent
    generate_documents(args.course, root, output_pdf=args.pdf)
