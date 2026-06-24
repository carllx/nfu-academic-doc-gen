import argparse
import os
import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from scripts.generate import load_yaml, _collect_final_docx
from scripts.utils.semester_utils import SemesterDateCalculator
from scripts.utils.experiment_adapter import sanitize_experiment_data
from scripts.gen_experiment_xml import gen_experiment as gen_experiment_xml
import re

def generate_documents(course_dir_name: str, base_dir: Path, output_pdf: bool = True):
    potential_roots = [
        base_dir / "2025-2026-2 课程" / course_dir_name,
        base_dir.parent / "2025-2026-2 课程" / course_dir_name,
        Path("/Users/yamlam/Documents/nfu - 教务/2025-2026-2") / course_dir_name
    ]
    course_root = None
    for p in potential_roots:
        if p.exists():
            course_root = p
            break
            
    if not course_root:
        return

    print(f"📂 Processing Experiments for: {course_dir_name}")

    import importlib.util
    _loader_path = str(Path(course_root).parent / "course_loader.py") if (Path(course_root).parent / "course_loader.py").exists() else None
    if _loader_path:
        _spec = importlib.util.spec_from_file_location("course_loader", _loader_path)
        _course_loader = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_course_loader)
        data = _course_loader.load_course(str(course_root))
    else:
        config_path = course_root / "course.yaml"
        data = load_yaml(config_path)
    if not data:
        return

    context = data.copy()
    context['_output_pdf'] = output_pdf

    tp_version = data.get('course', {}).get('training_plan_version', '2025')
    grad_req_path = base_dir / "00_Data_Context" / "training_plans" / f"graduation_requirements_{tp_version}.yaml"
    if grad_req_path.exists():
        grad_req_data = load_yaml(grad_req_path)
        context['_schema_type'] = grad_req_data.get('schema_type', 'detailed') if grad_req_data else 'detailed'
    else:
        context['_schema_type'] = 'detailed'

    start_date_str = data.get('semester_config', {}).get('start_date')
    if start_date_str:
        calc = SemesterDateCalculator(start_date_str)
        context['calculated'] = {}
        schedule_rows = []
        if 'calendar' in context:
            for week in context['calendar']:
                w_num = week.get('week')
                if w_num:
                    s, e = calc.get_week_range(w_num)
                    week['date_start'] = s
                    week['date_end'] = e
                    week['date_range'] = f"{s}-{e}"
                    if 'classes' in context['course']:
                         class_dates = []
                         weekday_map = {"周一": 0, "周二": 1, "周三": 2, "周四": 3, "周五": 4, "周六": 5, "周日": 6}
                         for cls in context['course']['classes']:
                             schedule_str = cls.get('schedule_time', '')
                             wd_match = re.search(r'(周[一二三四五六日])', schedule_str)
                             weekday_str = wd_match.group(1) if wd_match else ''
                             if weekday_str in weekday_map:
                                 offset = weekday_map[weekday_str]
                                 class_info = calc.get_class_date(w_num, weekday_str)
                                 cls_occurrence = {"name": cls['name'], "location": cls.get('classroom', ''), "time": schedule_str, "date": class_info['date'], "is_holiday": class_info['is_holiday'], "holiday_name": "节日" if class_info['is_holiday'] else ""}
                                 class_dates.append(cls_occurrence)
                                 schedule_rows.append({"week": w_num, "date": class_info['date'], "time": schedule_str, "location": cls.get('classroom', ''), "topic": week.get('topic', ''), "content": week.get('content', ''), "task": week.get('task', ''), "holiday_name": cls_occurrence['holiday_name']})
                         week['class_dates'] = class_dates
        context['schedule_rows'] = schedule_rows

    exp_overlay_dir = course_root / "practices" / "experiments"
    if exp_overlay_dir.is_dir():
        for exp_file in sorted(exp_overlay_dir.glob("exp_*.yaml")):
            exp_overlay = load_yaml(exp_file)
            if not exp_overlay: continue
            overlay_id = exp_overlay.get('exp_id')
            if overlay_id is None: continue
            for exp in context.get('experiments', []):
                if exp.get('id') == overlay_id:
                    exp['_overlay'] = exp_overlay
                    break

    for exp in context.get('experiments', []):
        overlay = exp.get('_overlay', {})
        steps = overlay.get('steps', [])
        guide_text = overlay.get('guide_text', [])
        if not steps and not guide_text:
            print(f"\n❌ [ERROR] 实验 '{exp.get('name')}' 缺失步骤！")

    context = sanitize_experiment_data(context)

    output_dir = course_root / "Output"
    output_dir.mkdir(exist_ok=True)

    # ONLY D: Experiment Materials
    gen_experiment_xml(base_dir, output_dir, context)

    if output_pdf:
        from scripts.pdf_converter import batch_convert_to_pdf
        # Only collect experiment materials to convert to pdf
        finals = []
        exp_dir = output_dir / '实验材料'
        if exp_dir.exists():
            for f in exp_dir.glob('*.docx'):
                name = f.name
                if re.match(r'实验\d+_', name):
                    continue
                finals.append(f)
        if finals:
            batch_convert_to_pdf(sorted(finals))
            
    print(f"✅ Experiment materials generated for {course_dir_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", help="Course directory name", required=False)
    args = parser.parse_args()
    
    root = Path(__file__).parent.parent
    if args.course:
        generate_documents(args.course, root, output_pdf=True)
    else:
        # Generate for all courses in 2025-2026-2
        course_dir = Path("/Users/yamlam/Downloads/2025-2026-2 课程")
        for d in course_dir.iterdir():
            if d.is_dir() and (d / "course.yaml").exists():
                generate_documents(d.name, root, output_pdf=True)
