import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Optional

# Add project root to sys.path to allow importing from scripts
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

try:
    from scripts.course_schema import CourseSchema
    from scripts.utils.semester_utils import HolidayManager, SemesterDateCalculator
    from pydantic import ValidationError
except ImportError:
    # Fallback for when running directly without package structure
    sys.path.append(str(Path(__file__).parent))
    from course_schema import CourseSchema
    from utils.semester_utils import HolidayManager, SemesterDateCalculator
    from pydantic import ValidationError

def load_yaml(file_path: Path) -> Optional[Dict]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None

def check_date_validity(start_date_str: str) -> List[str]:
    issues = []
    hm = HolidayManager()
    
    try:
        date_obj = SemesterDateCalculator(start_date_str).start_date
        if hm.is_holiday(date_obj):
            issues.append(f"Start date {start_date_str} falls on a known holiday/break.")
        
        # Specific check for Spring 2026 CNY which is early Feb
        # 2026 CNY is Feb 17. 
        if start_date_str == "2026-02-17":
            issues.append(f"Start date {start_date_str} is Lunar New Year (Spring Festival).")
            
    except ValueError as e:
        issues.append(f"Invalid date format: {e}")
        
    return issues

def audit_course_dir(course_dir: Path, training_plans_dir: Path = None) -> List[str]:
    """审计单门课程的 course.yaml，动态加载对应版本的人培数据"""
    report = []
    yaml_path = course_dir / "course.yaml"
    
    if not yaml_path.exists():
        return [f"[MISSING] course.yaml not found in {course_dir.name}"]
    
    # 优先使用 course_loader（支持 includes 合并）
    import importlib.util
    _loader_path = str(course_dir.parent / "course_loader.py") if (course_dir.parent / "course_loader.py").exists() else None
    if _loader_path:
        _spec = importlib.util.spec_from_file_location("course_loader", _loader_path)
        _course_loader = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_course_loader)
        data = _course_loader.load_course(str(course_dir))
    else:
        # 回退：无 course_loader 时走旧路径
        data = load_yaml(yaml_path)
    if not data:
        return [f"[ERROR] Failed to parse course.yaml in {course_dir.name}"]
    
    # ─── 动态加载人培数据（按课程声明的版本） ───────────────
    training_plan = None
    grad_reqs = None
    if training_plans_dir:
        tp_version = data.get('course', {}).get('training_plan_version', '')
        if not tp_version:
            # Fallback: 从 classes[0].name 提取年级
            classes = data.get('course', {}).get('classes', [])
            if classes:
                m = re.search(r'(20\d{2})', classes[0].get('name', ''))
                if m:
                    # 年级 → 人培版本映射（23级→2023版，24级→2024版，25级→2025版）
                    grade_year = int(m.group(1))
                    tp_version = str(grade_year)
                    report.append(
                        f"[WARN] {course_dir.name}: 缺少 training_plan_version 字段，"
                        f"从班级名推断为 {tp_version} 版人培（建议显式声明）"
                    )
        if tp_version:
            tp_path = training_plans_dir / f'training_plan_{tp_version}.yaml'
            gr_path = training_plans_dir / f'graduation_requirements_{tp_version}.yaml'
            if tp_path.exists():
                training_plan = load_yaml(tp_path)
            if gr_path.exists():
                grad_reqs = load_yaml(gr_path)
            if not training_plan:
                report.append(
                    f"[WARN] {course_dir.name}: 未找到 {tp_version} 版人培数据文件 "
                    f"({tp_path.name})，跳过人培校验"
                )
        
    # 1. Schema Validation
    try:
        CourseSchema(**data)
    except ValidationError as e:
        for err in e.errors():
            loc = " -> ".join(str(l) for l in err['loc'])
            report.append(f"[SCHEMA] {course_dir.name}: {loc} - {err['msg']}")
            
    # 2. Business Logic & Date Checks
    semester_config = data.get('semester_config')
    if semester_config:
        start_date = semester_config.get('start_date')
        if start_date:
            date_issues = check_date_validity(start_date)
            for issue in date_issues:
                report.append(f"[CRITICAL] {course_dir.name}: {issue}")
    else:
        report.append(f"[WARN] {course_dir.name}: Missing semester_config (cannot validate dates)")

    # 3. Calendar vs Hours consistency (Rough check)
    calendar = data.get('calendar', [])
    if len(calendar) < 16:
        report.append(f"[WARN] {course_dir.name}: Calendar has only {len(calendar)} weeks (Standard is 16-18)")

    # 3a. 逐周物理课时红线校验 + 路演周卡控
    MAX_HOURS_PER_SESSION = 5  # 单次排课物理容量上限（节）
    PRESENTATION_KEYWORDS = ('路演', '答辩', '汇报', '展示', '评审')
    for week in calendar:
        wk = week.get('week', '?')
        h_t = week.get('hours_theory', 0) or 0
        h_p = week.get('hours_practice', 0) or 0
        h_total = h_t + h_p
        topic = str(week.get('topic', ''))

        # 3a-1: 单项或总和超出物理容量
        if h_t > MAX_HOURS_PER_SESSION:
            report.append(
                f"[CRITICAL] {course_dir.name}: W{wk} hours_theory={h_t} "
                f"超出单次排课上限({MAX_HOURS_PER_SESSION}节)")
        if h_p > MAX_HOURS_PER_SESSION:
            report.append(
                f"[CRITICAL] {course_dir.name}: W{wk} hours_practice={h_p} "
                f"超出单次排课上限({MAX_HOURS_PER_SESSION}节)")
        if h_total > MAX_HOURS_PER_SESSION:
            report.append(
                f"[CRITICAL] {course_dir.name}: W{wk} 理论({h_t})+实践({h_p})={h_total} "
                f"超出单次排课物理容量({MAX_HOURS_PER_SESSION}节)")

        # 3a-2: 路演/答辩周，理论学时必须为 0
        if any(kw in topic for kw in PRESENTATION_KEYWORDS) and h_t > 0:
            report.append(
                f"[CRITICAL] {course_dir.name}: W{wk} '{topic}' 属路演/答辩周，"
                f"但 hours_theory={h_t}(应为0)")

    # 3b. steps.minutes 合计与学时一致性校验
    hours_cfg = data.get('course', {}).get('hours', {})
    if isinstance(hours_cfg, dict):
        min_per_period = hours_cfg.get('minutes_per_period', 45)
    else:
        min_per_period = 45
    TOLERANCE = 0.15  # 允许 ±15% 弹性（MSG-013 收紧：原 30% 过宽，30min/周缺失曾静默通过）

    for week in calendar:
        wk = week.get('week', '?')
        h_t = week.get('hours_theory', 0) or 0
        h_p = week.get('hours_practice', 0) or 0
        h_total = h_t + h_p
        if h_total == 0:
            continue

        # 收集该周所有 steps 的 minutes
        total_minutes = 0
        step_count = 0
        for les in week.get('lessons', []):
            for step in les.get('steps', []):
                m = step.get('minutes', 0) or 0
                total_minutes += m
                step_count += 1

        if step_count == 0:
            continue  # 无 steps 数据，跳过（生成器使用默认占位）

        max_minutes = h_total * min_per_period
        min_minutes = max_minutes * (1 - TOLERANCE)

        # C-4: steps 总分钟与声明学时一致性（MSG-013 建议增强）
        diff_minutes = abs(total_minutes - max_minutes)
        if total_minutes > max_minutes:
            report.append(
                f"[WARN] {course_dir.name}: W{wk} steps分钟合计({total_minutes}min) "
                f"超出学时上限({h_total}×{min_per_period}={max_minutes}min)")
        elif diff_minutes > min_per_period:
            # 偏差超过 1 课时 → CRITICAL
            report.append(
                f"[CRITICAL] {course_dir.name}: W{wk} steps分钟合计({total_minutes}min) "
                f"与声明学时({max_minutes}min)偏差{diff_minutes}min(>1课时)")
        elif total_minutes < min_minutes:
            usage_pct = round(total_minutes / max_minutes * 100)
            report.append(
                f"[WARN] {course_dir.name}: W{wk} steps分钟合计({total_minutes}min) "
                f"仅占学时容量的{usage_pct}%({h_total}×{min_per_period}={max_minutes}min)")

    # 3c. 教学环节 stage 归属校验（双检测架构 L3 审计报告层）
    # 分类定义：理论 stage = 复习/导入/讲授 → 对应 hours_theory
    #           实践 stage = 实践/练习/训练/总结/小结 → 对应 hours_practice
    THEORY_STAGE_KEYWORDS = ('复习', '导入', '讲授', '演示')
    PRACTICE_STAGE_KEYWORDS = ('实践', '练习', '训练', '总结', '小结')

    for week in calendar:
        wk = week.get('week', '?')
        h_t = week.get('hours_theory', 0) or 0
        h_p = week.get('hours_practice', 0) or 0

        # 收集该周所有 steps
        all_steps = []
        for les in week.get('lessons', []):
            all_steps.extend(les.get('steps', []))

        if not all_steps:
            continue

        # C-1: 第一周禁止 stage=复习
        if wk == 1 or str(wk) == '1':
            for step in all_steps:
                stage = step.get('stage', '')
                if '复习' in stage:
                    report.append(
                        f"[CRITICAL] {course_dir.name}: W{wk} 出现 stage='{stage}'，"
                        f"第一周不应有「上次课复习」教学环节"
                    )

        # C-2: stage 分钟归属与学时比例一致性
        # 注：当 course.hours.theory == 0（人培规定全实践课程）时，
        #     教学中的"讲授"环节在文档层面也算实践学时，跳过此校验
        course_total_theory = data.get('course', {}).get('hours', {}).get('theory', -1)
        is_all_practice = (course_total_theory == 0)
        
        theory_min = 0
        practice_min = 0
        for step in all_steps:
            stage = step.get('stage', '')
            m = step.get('minutes', 0) or 0
            if any(kw in stage for kw in THEORY_STAGE_KEYWORDS):
                theory_min += m
            elif any(kw in stage for kw in PRACTICE_STAGE_KEYWORDS):
                practice_min += m

        if not is_all_practice and theory_min + practice_min > 0:
            t_hours_actual = round(theory_min / min_per_period, 1)
            p_hours_actual = round(practice_min / min_per_period, 1)

            t_diff = abs(t_hours_actual - h_t)
            p_diff = abs(p_hours_actual - h_p)

            if t_diff > 1:  # 收紧：>1h → CRITICAL（原 >2h）
                report.append(
                    f"[CRITICAL] {course_dir.name}: W{wk} 理论stage折算"
                    f"({t_hours_actual}h)与hours_theory({h_t}h)偏差{t_diff}h(>1h)"
                )
            elif t_diff > 0.5:  # 收紧：>0.5h → WARN（原 >1h）
                report.append(
                    f"[WARN] {course_dir.name}: W{wk} 理论stage折算"
                    f"({t_hours_actual}h)与hours_theory({h_t}h)偏差{t_diff}h(>0.5h)"
                )

            if p_diff > 1:  # 收紧：>1h → CRITICAL（原 >2h）
                report.append(
                    f"[CRITICAL] {course_dir.name}: W{wk} 实践stage折算"
                    f"({p_hours_actual}h)与hours_practice({h_p}h)偏差{p_diff}h(>1h)"
                )
            elif p_diff > 0.5:  # 收紧：>0.5h → WARN（原 >1h）
                report.append(
                    f"[WARN] {course_dir.name}: W{wk} 实践stage折算"
                    f"({p_hours_actual}h)与hours_practice({h_p}h)偏差{p_diff}h(>0.5h)"
                )

        # C-3: 纯实践周不应有大量理论 stage minutes（人培全实践课程除外）
        if not is_all_practice and h_t == 0 and theory_min > 30:
            report.append(
                f"[WARN] {course_dir.name}: W{wk} hours_theory=0(纯实践周)，"
                f"但理论stage时间={theory_min}min(>30min)，请检查学时分配"
            )

    # 4. Exams 节点存在性检查 (ADR 004)
    if 'exams' not in data or data['exams'] is None:
        report.append(f"[WARN] {course_dir.name}: Missing 'exams' node. Templates will fail with 'exams is undefined'")

    # 5. Assessment 命名规范检查 (ADR 005)
    assessment = data.get('assessment_methods', {})
    normal_items = assessment.get('normal_items', [])
    for idx, item in enumerate(normal_items):
        name = item.get('name', '')
        if name != '考勤' and not re.match(r'^(章节测试|命题测试)\d+$', name):
            report.append(f"[WARN] {course_dir.name}: normal_items[{idx}].name='{name}' 不符合命名规范 (应为 '章节测试N' 或 '命题测试N')")
        desc = item.get('desc', '') or ''
        if name != '考勤' and '对应实验' not in desc:
            report.append(f"[WARN] {course_dir.name}: normal_items[{idx}].desc 缺少 '对应实验N' 外键关联")

    # 6. 人培交叉校验 (Training Plan Cross-Validation)
    if training_plan:
        report.extend(_audit_training_plan(course_dir.name, data, training_plan, grad_reqs))

    return report


def _audit_training_plan(course_name: str, data: dict, training_plan: dict, grad_reqs: dict = None) -> List[str]:
    """人培交叉校验：根据 schema_type 分派不同的校验逻辑"""
    issues = []
    tp_version = training_plan.get('version', '未知')
    schema_type = 'detailed'  # 默认向后兼容
    
    if grad_reqs:
        schema_type = grad_reqs.get('schema_type', 'detailed')
    
    # 注：schema_type: none 仍需通过课程矩阵匹配进行学分/学时校验
    #     仅毕业要求校验会被跳过（在匹配成功后分派）
    
    # ─── 通用：课程矩阵匹配 ────────────────────────────────
    matrix = training_plan.get('course_matrix', {})
    actual_name = data.get('course', {}).get('name', course_name)
    matched_entry = None

    def _bigram_similarity(a: str, b: str) -> float:
        """双字符 n-gram 相似度"""
        if not a or not b:
            return 0.0
        bg_a = {a[i:i+2] for i in range(len(a) - 1)}
        bg_b = {b[i:i+2] for i in range(len(b) - 1)}
        if not bg_a or not bg_b:
            return 0.0
        return len(bg_a & bg_b) / min(len(bg_a), len(bg_b))

    best_score = 0.0
    for key, entry in matrix.items():
        official = entry.get('official_name', key)
        if actual_name in official or official in actual_name or key in actual_name:
            matched_entry = entry
            break
        score = max(_bigram_similarity(actual_name, official),
                    _bigram_similarity(actual_name, key))
        if score > best_score:
            best_score = score
            if score >= 0.5:
                matched_entry = entry

    if not matched_entry:
        issues.append(
            f"[INFO] {course_name}: 未在 training_plan_{tp_version}.yaml 的 course_matrix 中找到匹配条目"
        )
        return issues
    # ─── 通用：学分/学时交叉校验 ──────────────────────────────
    course_data = data.get('course', {})
    course_hours = course_data.get('hours', {})
    plan_hours = matched_entry.get('hours', {})
    
    # 学分校验
    course_credits = course_data.get('credits')
    plan_credits = matched_entry.get('credits')
    if plan_credits and course_credits and float(course_credits) != float(plan_credits):
        issues.append(
            f"[TRAINING_PLAN] {course_name}: 学分不一致 "
            f"(course.yaml: {course_credits}, {tp_version}版人培: {plan_credits})"
        )
    
    # 总学时校验
    course_total = course_hours.get('total')
    plan_total = plan_hours.get('total')
    if plan_total and course_total and int(course_total) != int(plan_total):
        issues.append(
            f"[TRAINING_PLAN] {course_name}: 总学时不一致 "
            f"(course.yaml: {course_total}, {tp_version}版人培: {plan_total})"
        )
    
    # 理论/实践学时比例校验（严格比对）
    course_theory = course_hours.get('theory')
    course_practice = course_hours.get('practice')
    plan_theory = plan_hours.get('theory')
    plan_practice = plan_hours.get('practice')
    if plan_theory is not None and course_theory is not None:
        if int(course_theory) != int(plan_theory):
            issues.append(
                f"[TRAINING_PLAN] {course_name}: 理论学时不一致 "
                f"(course.yaml: {course_theory}, {tp_version}版人培: {plan_theory})"
            )
    if plan_practice is not None and course_practice is not None:
        if int(course_practice) != int(plan_practice):
            issues.append(
                f"[TRAINING_PLAN] {course_name}: 实践学时不一致 "
                f"(course.yaml: {course_practice}, {tp_version}版人培: {plan_practice})"
            )
    
    # ─── schema_type: none → 仅做学时校验，跳过毕业要求校验 ──
    if schema_type == 'none':
        return issues

    # ─── schema_type: coarse → 仅按大类编号校验 ────────────
    if schema_type == 'coarse':
        issues.extend(_audit_coarse(course_name, data, training_plan, grad_reqs, matched_entry, tp_version))
        return issues
    
    # ─── schema_type: detailed → 按观测点 pid 精确校验 ─────
    issues.extend(_audit_detailed(course_name, data, training_plan, grad_reqs, matched_entry, tp_version))
    return issues


def _audit_coarse(course_name: str, data: dict, training_plan: dict, 
                  grad_reqs: dict, matched_entry: dict, tp_version: str) -> List[str]:
    """粗粒度校验（2024版等）：仅检查 objectives.mappings 中的毕业要求大类编号"""
    issues = []
    
    # 构建大类名称查找表
    req_names = {}
    if grad_reqs:
        for req_id, req in grad_reqs.get('requirements', {}).items():
            req_names[str(req_id)] = req.get('name', '')
    
    # 收集课程中映射的毕业要求大类编号
    objectives = data.get('objectives', {})
    course_req_ids = set()
    for cat in ['knowledge', 'ability', 'quality']:
        for item in objectives.get(cat, []):
            for m in item.get('mappings', []):
                req_str = m.get('requirement', '')
                parts = req_str.split(' ', 1)
                if parts:
                    course_req_ids.add(parts[0])
    
    # 检查人培矩阵要求的大类是否被覆盖
    required_reqs = {sp['point'] for sp in matched_entry.get('support_map', [])}
    missing = required_reqs - course_req_ids
    if missing:
        for mr in sorted(missing):
            rname = req_names.get(mr, '')
            issues.append(
                f"[TRAINING_PLAN] {course_name}: {tp_version}版人培矩阵要求支撑 "
                f"毕业要求{mr}({rname})，但 objectives 中无对应映射"
            )
    
    extras = course_req_ids - required_reqs
    if extras:
        extra_list = ', '.join(sorted(extras))
        issues.append(
            f"[INFO] {course_name}: 课程映射毕业要求 ({extra_list}) 超出{tp_version}版人培矩阵"
            f"（方案B务实扩展，仅供参考）"
        )
    
    return issues


def _audit_detailed(course_name: str, data: dict, training_plan: dict,
                    grad_reqs: dict, matched_entry: dict, tp_version: str) -> List[str]:
    """细粒度校验（2025版等）：按观测点 pid 精确校验命名和覆盖度"""
    issues = []
    
    # 构建观测点权威名称查找表
    point_names = {}
    if grad_reqs:
        for req_id, req in grad_reqs.get('requirements', {}).items():
            for pid, pname in req.get('points', {}).items():
                point_names[str(pid)] = pname

    # 收集课程中所有 objectives.mappings 的 point 编号
    objectives = data.get('objectives', {})
    course_points = set()

    for cat in ['knowledge', 'ability', 'quality']:
        for item in objectives.get(cat, []):
            for m in item.get('mappings', []):
                point_str = m.get('point', '')
                parts = point_str.split(' ', 1)
                if len(parts) == 2:
                    pid, pname = parts
                    course_points.add(pid)
                    expected = point_names.get(pid)
                    if expected and expected != pname:
                        issues.append(
                            f"[TRAINING_PLAN] {course_name}: 观测点 {pid} 命名不一致 "
                            f"(当前: '{pname}', 应为: '{expected}')"
                        )

    required_points = {sp['point'] for sp in matched_entry.get('support_map', [])}
    missing = required_points - course_points
    if missing:
        for mp in sorted(missing):
            pname = point_names.get(mp, '')
            issues.append(
                f"[TRAINING_PLAN] {course_name}: {tp_version}版人培矩阵要求支撑 {mp} ({pname})，"
                f"但 objectives 中无对应映射"
            )
    extras = course_points - required_points
    if extras:
        extra_list = ', '.join(sorted(extras))
        issues.append(
            f"[INFO] {course_name}: 课程扩展映射 ({extra_list}) 超出{tp_version}版人培矩阵（合理扩展，仅供参考）"
        )

    return issues

def audit_root(root_path: str, deep: bool = False, training_plans_dir: str = None):
    root = Path(root_path)
    if not root.exists():
        print(f"❌ Root path does not exist: {root}")
        return False

    # 定位人培数据目录
    tp_dir = None
    if training_plans_dir:
        tp_dir = Path(training_plans_dir)
        if tp_dir.exists():
            print(f"📋 使用指定人培目录: {tp_dir}")
        else:
            print(f"⚠️ 指定人培目录不存在: {tp_dir}")
            tp_dir = None
    else:
        # 自动探测教务材料项目中的人培目录（新版多版本架构）
        edu_base = Path(__file__).parent.parent / '00_Data_Context'
        tp_dir_auto = edu_base / 'training_plans'
        if tp_dir_auto.exists():
            tp_dir = tp_dir_auto
            print(f"📋 自动探测人培目录: {tp_dir}")
        else:
            # 向后兼容：旧版单文件架构
            tp_auto = edu_base / 'training_plan_2025.yaml'
            gr_auto = edu_base / 'graduation_requirements.yaml'
            if tp_auto.exists() and gr_auto.exists():
                # 创建临时兼容：告知用户迁移
                print(f"⚠️ 使用旧版人培文件（建议迁移到 training_plans/ 目录）")
                tp_dir = edu_base  # 兼容模式

    print(f"🔍 Scanning root: {root}")
    all_issues = []

    # Identify course directories (excluding hidden/systems)
    if root.is_dir():
        # Check if root itself is a course dir
        if (root / "course.yaml").exists():
             all_issues.extend(audit_course_dir(root, tp_dir))
        else:
            # Audit children
            for child in root.iterdir():
                if child.is_dir() and not child.name.startswith('.'):
                    if (child / "course.yaml").exists():
                        all_issues.extend(audit_course_dir(child, tp_dir))
                    elif deep:
                         if child.name not in ['docs', 'node_modules', 'scripts', 'Output']:
                             all_issues.append(f"[INFO] {child.name}: No course.yaml found (Skipping)")

    if not all_issues:
        print("✅ No issues found.")
    else:
        print("\n⚠️  Audit Report:")
        for issue in all_issues:
            print(issue)
            
    return len(all_issues) == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit course data and structure.")
    parser.add_argument("--root", default=".", help="Root directory to scan (default: current)")
    parser.add_argument("--deep", action="store_true", help="Deep scan (report skipped dirs)")
    parser.add_argument("--training-plans-dir", default=None,
                        help="Path to training_plans/ directory (auto-detected if omitted)")
    
    args = parser.parse_args()
    
    success = audit_root(args.root, args.deep, args.training_plans_dir)
    sys.exit(0 if success else 1)
