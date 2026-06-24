import csv
import yaml
import os
import sys
from datetime import datetime, timedelta

# 加载 HolidayManager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.semester_utils import HolidayManager

CSV_PATH1 = '/Users/yamlam/Downloads/教务材料/07_Internship_Generator/templates/source_实习材料登记.csv'
CSV_PATH2 = '/Users/yamlam/Downloads/实习材料登记-实习成绩.csv'
YAML_PATH = '/Users/yamlam/Downloads/2025-2026-2 课程/实习指导/course_internship.yaml'
CALENDAR_PATH = '/Users/yamlam/Downloads/教务材料/semester_calendar.yaml'

def get_inspect_date_from_start(start_date_str, holiday_manager):
    """
    巡查时间规则：在学生实习开始日期的前三周（21天内）进行，且在非节假日的时间进行巡查。
    """
    try:
        if '/' in start_date_str:
            start_date = datetime.strptime(start_date_str, "%Y/%m/%d").date()
        else:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    except Exception:
        start_date = datetime(2025, 12, 1).date()
    
    # 从开始时间起，在 21天（三周内）寻找一个工作日且非节假日
    for i in range(1, 22):
        check_date = start_date + timedelta(days=i)
        # weekday(): 0是周一, 4是周五
        if check_date.weekday() < 5 and not holiday_manager.is_holiday(check_date):
            return check_date
    
    # 如果极端情况找不到，默认返回开始时间后的第14天
    return start_date + timedelta(days=14)

def convert():
    if not os.path.exists(CSV_PATH1):
        print(f"File not found: {CSV_PATH1}")
        return
    if not os.path.exists(CSV_PATH2):
        print(f"File not found: {CSV_PATH2}")
        return

    # 初始化节假日管理器
    hm = HolidayManager.from_yaml(CALENDAR_PATH)

    data = {
        'global': {
            'college': '设计学院',
            'major': '数字媒体艺术',
            'school_teacher': '林昕',
            'teacher_advice': '实习期间表现优异，态度端正，能够很好地将理论知识与实际工作相结合。',
            'teacher_signature': ''
        },
        'students': []
    }

    # 预加载成绩表和班级信息，以学生姓名为 key
    student_grades = {}
    with open(CSV_PATH2, 'r', encoding='utf-8-sig') as f2:
        reader2 = csv.DictReader(f2)
        for row in reader2:
            name = row.get('姓名', '').strip()
            if not name:
                continue
            class_name = row.get('班级', '').strip()
            student_id = row.get('学号', '').strip()
            school_score_str = row.get('校内导师分数(70%)', '0').strip()
            try:
                school_score = float(school_score_str)
            except ValueError:
                school_score = 0.0
            
            student_grades[name] = {
                'class': class_name,
                'student_id': student_id,
                'score': school_score
            }

    with open(CSV_PATH1, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        seq = 1
        for row in reader:
            student_name = row.get('填写人（自动）', '').strip()
            if not student_name:
                continue

            base_name = row.get('实习单位名称（必填）', '').strip()
            position = row.get('实习岗位（必填）', '').strip()
            intern_content = row.get('实习内容描述（必填）', '').strip()
            
            # 去除学生手填数据里自带的“实习内容：”前缀（兼容全半角冒号），防止与模板重复
            if intern_content.startswith('实习内容：'):
                intern_content = intern_content[5:].strip()
            elif intern_content.startswith('实习内容:'):
                intern_content = intern_content[5:].strip()
                
            enterprise_teacher = row.get('企业指导人员姓名（必填）', '').strip()
            end_date_str = row.get('实习结束时间（必填）', '').strip()
            start_date_str = row.get('实习开始时间（必填）', '').strip()
            base_address = row.get('实习详细地址（必填）', '').strip()

            if not intern_content:
                intern_content = position
                
            # 格式化实习起止时间
            def format_zh_date(date_string):
                if not date_string: return ""
                try:
                    if '/' in date_string:
                        dt = datetime.strptime(date_string, "%Y/%m/%d").date()
                    else:
                        dt = datetime.strptime(date_string, "%Y-%m-%d").date()
                    return f"{dt.year}年{dt.month}月{dt.day}日"
                except Exception:
                    return date_string
            
            start_zh = format_zh_date(start_date_str)
            end_zh = format_zh_date(end_date_str)
            intern_start_end = ""
            if start_zh and end_zh:
                intern_start_end = f"{start_zh} 至 {end_zh}"
            elif start_zh:
                intern_start_end = f"{start_zh} 起"
            elif end_zh:
                intern_start_end = f"至 {end_zh}"

            # 取出成绩与班级信息
            grade_info = student_grades.get(student_name, {'class': '', 'student_id': '', 'score': 100.0})
            class_name = grade_info['class']
            student_id = grade_info['student_id']
            total_score = grade_info['score']
            
            # 分配整数子成绩以精确构成总分
            total_int = int(round(total_score))
            weights = [
                ("score_safety", 0.10),
                ("score_attendance", 0.15),
                ("score_learning", 0.15),
                ("score_teamwork", 0.15),
                ("score_attitude", 0.15),
                ("score_task", 0.15),
                ("score_suitability", 0.15)
            ]
            
            floors = {}
            remainders = []
            
            for key, weight in weights:
                exact = total_int * weight
                f_val = int(exact)
                floors[key] = f_val
                remainders.append((exact - f_val, key))
                
            sum_floors = sum(floors.values())
            leftover = total_int - sum_floors
            
            # 优先补齐小数部分最大的项
            remainders.sort(key=lambda x: x[0], reverse=True)
            for i in range(leftover):
                floors[remainders[i][1]] += 1
                
            score_safety = str(floors["score_safety"])
            score_attendance = str(floors["score_attendance"])
            score_learning = str(floors["score_learning"])
            score_teamwork = str(floors["score_teamwork"])
            score_attitude = str(floors["score_attitude"])
            score_task = str(floors["score_task"])
            score_suitability = str(floors["score_suitability"])
            str_total_score = str(total_int)

            # 巡查时间推断
            inspect_date_obj = get_inspect_date_from_start(start_date_str, hm)
            inspect_year = str(inspect_date_obj.year)
            inspect_month = str(inspect_date_obj.month).zfill(2)
            inspect_day = str(inspect_date_obj.day).zfill(2)
            inspect_date_str = f"{inspect_year}年{inspect_date_obj.month}月{inspect_date_obj.day}日"

            data['students'].append({
                'sequence_number': str(seq),
                'student_id': student_id,
                'student_name': student_name,
                'class_name': class_name,
                'base_name': base_name,
                'base_address': base_address,
                'position': position,
                'intern_content': intern_content,
                'intern_start_end': intern_start_end,
                'enterprise_teacher': enterprise_teacher,
                'inspect_year': inspect_year,
                'inspect_month': inspect_month,
                'inspect_day': inspect_day,
                'inspect_date': inspect_date_str,
                'score_safety': score_safety,
                'score_attendance': score_attendance,
                'score_learning': score_learning,
                'score_teamwork': score_teamwork,
                'score_attitude': score_attitude,
                'score_task': score_task,
                'score_suitability': score_suitability,
                'score_total': str_total_score,
                'note': ''
            })
            seq += 1

    # Dump yaml nicely
    class Dumper(yaml.SafeDumper):
        def ignore_aliases(self, data):
            return True

    def str_presenter(dumper, data):
        if len(data.splitlines()) > 1:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter, Dumper=Dumper)

    with open(YAML_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=Dumper, allow_unicode=True, sort_keys=False)

    print(f"Successfully converted CSV to YAML at {YAML_PATH}")
    print(f"Generated {len(data['students'])} student records.")

if __name__ == '__main__':
    convert()
