# 任务单：信息可视化_实验与评估合规性清理

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-06-23
> **优先级**：P1
> **背景**：根据信息可视化课程合规性审计结果，发现存在 "Experiment 4" (20实践学时只能有3个实验)、AB卷评估表头违规、以及实验数据内保留废弃的 `questions:` 字段等严重违规。为确保教务材料正常生成，需委托课程端清理脏数据。

---

## 一、教务侧已完成的工作
1. **Schema 变更**：已更新 `course_schema.py` 中的 `check_experiment_hours` 校验逻辑，增加“20 实践学时必须恰好有 3 个实验”的严格校验。

## 二、请课程侧执行的任务

### 任务 1：处理 "Experiment 4" (20学时限3次实验) ⭐
**目的**：确保《信息可视化》实验配置符合合规性。
- 梳理《信息可视化》课程的所有 `exp_*.yaml`，如果存在 "Experiment 4"，请删减、合并或重构，使其恰好满足 **3次正式实验**。
- 清理任何引用了 "Experiment 4" 的其他课程或脚本，消除多余调用的隐患。
- （可选）请调用 `agent-architect` 更新 `.agent/rules/rule_experiment_compliance.md`，显式记录“20 实践学时课程铁律：总次数必须恰好 3 次正式实验”。

### 任务 2：修复 AB卷评估配置模板 (course_assessment.yaml)
**目的**：使 AB卷配置符合 `ab-practice-generator` 的严格 Header。
- 请清理和重构 `信息可视化/course_assessment.yaml`。确保表头完全按照 `ab-practice-generator` 技能规范，特别是 `**五、提交途径：**` 等核心锚点必须恢复原貌。

### 任务 3：清理所有废弃的 `questions:` 字段
**目的**：去除 `practices/experiments/exp_*.yaml` 中非法的 `questions:` 配置。
- 扫描 `信息可视化/practices/experiments/exp_*.yaml`，彻底移除 `questions:` 字段（该字段已废弃，且实验规范明确取消思考题）。

---

## 三、规范依据
- 见 `.agent/rules/rule_experiment_compliance.md` 关于实验与练习的隔离原则，以及废弃思考题的硬性规定。
- `ab-practice-generator` 技能对评估提示词 Headers 的要求。

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

合格标准：不再报与实验数量和 Schema 相关的错误。

---
*消息时间：2026-06-23 | 教务材料 Agent*
