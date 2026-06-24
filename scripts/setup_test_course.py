import yaml
from pathlib import Path

course_data = {
    "course": {
        "name": "排版测试课",
        "code": "TEST1001",
        "semester": "2025-2026-2",
        "nature": "专业选修",
        "credits": 2.0,
        "hours": {
            "total": 40,
            "theory": 0,
            "practice": 40
        },
        "classes": [
            {
                "name": "测班1",
                "schedule_time": "周一1-2节",
                "classroom": "实验楼A"
            }
        ]
    },
    "teacher": {
        "name": "张三",
        "title": "讲师",
        "office": "教研室1"
    },
    "semester_config": {
        "start_date": "2026-03-02"
    },
    "calendar": [
        {
            "week": 1,
            "topic": "实验1",
            "content": "1. 知识点1",
            "hours_theory": 0,
            "hours_practice": 12,
            "exp_id": 1
        },
        {
            "week": 2,
            "topic": "实验2",
            "content": "1. 知识点2",
            "hours_theory": 0,
            "hours_practice": 14,
            "exp_id": 2
        },
        {
            "week": 3,
            "topic": "实验3",
            "content": "1. 知识点3",
            "hours_theory": 0,
            "hours_practice": 14,
            "exp_id": 3
        }
    ],
    "experiments": [
        {"id": 1, "name": "测试实验一", "type": "设计性", "hours": 12, "group": 1},
        {"id": 2, "name": "测试实验二", "type": "设计性", "hours": 14, "group": 1},
        {"id": 3, "name": "测试实验三", "type": "综合性", "hours": 14, "group": 1}
    ]
}

base_path = Path("/Users/yamlam/Documents/nfu - 教务/2025-2026-2/TestCourse")

with open(base_path / "course.yaml", "w", encoding="utf-8") as f:
    yaml.dump(course_data, f, allow_unicode=True, sort_keys=False)

for i in range(1, 4):
    exp_data = {
        "exp_id": i,
        "steps": [
            {"title": "第一步", "content": "xxxx"},
            {"title": "第二步", "content": "xxxx"}
        ]
    }
    with open(base_path / f"practices/experiments/exp_{i}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(exp_data, f, allow_unicode=True, sort_keys=False)

print("Created YAML files.")
