from pathlib import Path
import yaml
from scripts.gen_assessment_xml import _deep_clean_data

with open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course.yaml") as f:
    course = yaml.safe_load(f)
with open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course_assessment.yaml") as f:
    assess = yaml.safe_load(f)

exam_item = assess['exams']['final_exam'][0]
practice_theme = exam_item['practice_paper']['ab_versions']['A']['practice_theme']

base_data = {'a_theme': practice_theme}
cleaned = _deep_clean_data(base_data)
print(repr(cleaned['a_theme'][:50]))
