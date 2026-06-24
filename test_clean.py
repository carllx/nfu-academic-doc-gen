import re

def _clean_xml_illegal_chars(val):
    if not isinstance(val, str):
        return val
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

import yaml
with open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course_assessment.yaml") as f:
    data = yaml.safe_load(f)

a_theme = data['exams']['final_exam'][0]['practice_paper']['ab_versions']['A']['practice_theme']

base_data = {'a_theme': a_theme}
cleaned = _deep_clean_data(base_data)

print("Original:")
print(base_data['a_theme'][:50])
print("Cleaned:")
print(cleaned['a_theme'][:50])
