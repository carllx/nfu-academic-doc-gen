import logging

def sanitize_experiment_data(context: dict) -> dict:
    """
    教务端实验数据清洗适配层
    1. 业务学时全局对账
    2. 字段剪裁与降级防崩溃
    """
    course = context.get('course', {})
    experiments = context.get('experiments', [])
    
    # 1. 业务学时全局对账
    practice_hours = course.get('hours', {}).get('practice', 0)
    
    total_exp_hours = 0
    for exp in experiments:
        hours = exp.get('hours')
        # 降级处理：如果没有 hours，给默认值 0
        if not isinstance(hours, (int, float)):
            hours = 0
            exp['hours'] = hours
        total_exp_hours += hours
        
    if practice_hours > 0 and total_exp_hours != practice_hours:
        print(f"⚠️ [WARNING] 业务学时全局对账失败！实验总学时 ({total_exp_hours}) 与 课程实践学时 ({practice_hours}) 不一致！")
        logging.warning(f"业务学时全局对账失败：实验学时={total_exp_hours}, 课程实践学时={practice_hours}")

    # 2. 字段剪裁与降级防崩溃
    for exp in experiments:
        # 填补缺失的核心键，防止 KeyError
        exp.setdefault('id', 999)
        exp.setdefault('name', '未命名实验')
        exp.setdefault('type', '设计性')
        exp.setdefault('hours', 0)
        exp.setdefault('summary', '')
        exp.setdefault('objectives', '')
        exp.setdefault('equipment', '')
        exp.setdefault('methods', '')
        
        # 处理 _overlay 增量数据
        if '_overlay' in exp:
            overlay = exp['_overlay']
            # 强制裁剪大篇幅且容易引发 XML 闭合异常的字段
            if 'grading_rubric' in overlay:
                del overlay['grading_rubric']
            if 'report_prompt' in overlay:
                del overlay['report_prompt']
            
            # 清洗 steps (防止包含非法结构)，这里我们保留基本的 guide_text，但防止深层嵌套导致 XML 异常
            # 也可以直接裁剪以避免问题
            if 'steps' in overlay:
                # 简化 steps，仅保留 id, name, guide_text
                safe_steps = []
                for step in overlay['steps']:
                    if isinstance(step, dict):
                        safe_steps.append({
                            'id': step.get('id', ''),
                            'name': step.get('name', ''),
                            'guide_text': step.get('guide_text', [])
                        })
                overlay['steps'] = safe_steps

    return context
