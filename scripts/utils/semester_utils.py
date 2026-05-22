from datetime import datetime, timedelta, date
from typing import Tuple, List, Optional, Dict

class HolidayManager:
    """
    节假日管理器
    """
    def __init__(self, holidays: List[str] = None):
        # 默认无硬编码假日，应通过 from_yaml() 从 semester_calendar.yaml 加载
        self.holidays = set()
        if holidays:
            self.holidays.update(holidays)
            
    def is_holiday(self, date_obj: date) -> bool:
        return date_obj.strftime("%Y-%m-%d") in self.holidays

    @classmethod
    def from_yaml(cls, yaml_path) -> "HolidayManager":
        """从 semester_calendar.yaml 加载节假日数据，不依赖硬编码。
        若文件不存在或解析失败，回退至默认硬编码列表。
        """
        try:
            import yaml
            with open(yaml_path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            dates = [h["date"] for h in data.get("holidays", [])]
            return cls(holidays=dates)
        except Exception:
            return cls()  # fallback 到硬编码默认列表

class SemesterDateCalculator:
    """
    计算学期日期的工具类
    假设 start_date 总是学期第一周的周一
    """
    def __init__(self, start_date_str: str, holiday_manager: Optional[HolidayManager] = None):
        try:
            self.start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {start_date_str}. Expected YYYY-MM-DD.")
        
        self.holiday_manager = holiday_manager or HolidayManager()

    def get_week_range(self, week_num: int) -> Tuple[str, str]:
        """
        获取指定周的起止日期 (周一 ~ 周日)
        返回格式: ("2026.02.17", "2026.02.23")
        """
        if week_num < 1:
            return "", ""
        
        monday = self.start_date + timedelta(weeks=week_num - 1)
        sunday = monday + timedelta(days=6)
        
        return monday.strftime("%Y.%m.%d"), sunday.strftime("%Y.%m.%d")

    def get_class_date(self, week_num: int, weekday_str: str) -> Dict[str, str]:
        """
        获取具体的上课日期，包含节假日检查
        返回: {
            "date": "2026.05.01", 
            "is_holiday": True/False,
            "desc": "劳动节" (Todo)
        }
        """
        weekday_map = {
            "周一": 0, "周二": 1, "周三": 2, "周四": 3,
            "周五": 4, "周六": 5, "周日": 6
        }
        
        offset = weekday_map.get(weekday_str)
        if offset is None:
            return {"date": "", "is_holiday": False}
            
        monday = self.start_date + timedelta(weeks=week_num - 1)
        target_day = monday + timedelta(days=offset)
        date_str = target_day.strftime("%Y.%m.%d")
        
        is_holiday = self.holiday_manager.is_holiday(target_day)
        
        return {
            "date": date_str,
            "is_holiday": is_holiday,
            "raw_date": target_day # internal use
        }

    def is_class_holiday(self, week_num: int, weekday_str: str) -> bool:
        """判断指定周次的上课日（星期X）是否为节假日。
        即 get_class_date() 的快捷封装，供生成器直接调用。
        """
        result = self.get_class_date(week_num, weekday_str)
        return result.get("is_holiday", False)


# ═══════════════════════════════════════════════════════════════════════
# 模块级工具函数（供生成器直接调用，无需实例化）
# ═══════════════════════════════════════════════════════════════════════

def get_effective_weeks(class_config: dict, all_weeks: list) -> list:
    """
    返回某班级实际有效的教学周次列表（排除 excluded_weeks）。

    Args:
        class_config: classes[] 中单个班级的配置字典
        all_weeks:    原始周次列表，如 [10, 11, 12, 13, 14, 15, 16, 17, 18]
    Returns:
        过滤后的有效周次列表，如 [10, 11, 12, 13, 14, 15, 17, 18]
    """
    excluded = [int(w) for w in class_config.get("excluded_weeks", [])]
    return [w for w in all_weeks if int(w) not in excluded]


def get_step_time_cap(class_config: dict, week: int):
    """
    返回指定自然周的 steps 步骤总时长上限（分钟）。
    若该周无 session_time_overrides 配置，返回 None（不裁剪）。

    Args:
        class_config: classes[] 中单个班级的配置字典
        week:         自然周周次（整数）
    Returns:
        int (max_minutes) 或 None
    """
    import re as _re
    for override in class_config.get("session_time_overrides", []):
        weeks_str = str(override.get("weeks", ""))
        m = _re.match(r'(\d+)[\-~](\d+)', weeks_str)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            if start <= int(week) <= end:
                return override.get("max_minutes")
    return None


def scale_steps(steps: list, max_minutes: int) -> list:
    """
    按比例压缩 steps 各阶段时长，使总和不超过 max_minutes。

    Args:
        steps:       steps 列表，每项为含 'minutes' 键的 dict
        max_minutes: 压缩目标上限（分钟）
    Returns:
        压缩后的 steps 新列表（原列表不变）
    """
    total = sum(s.get("minutes", 0) for s in steps)
    if total <= max_minutes or total == 0:
        return steps
    ratio = max_minutes / total
    return [{**s, "minutes": round(s.get("minutes", 0) * ratio)} for s in steps]
