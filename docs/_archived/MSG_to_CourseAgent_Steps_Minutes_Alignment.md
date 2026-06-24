# 任务单：教案 steps 分钟归类偏差修正 + 大纲学时字段补填

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P1 重要
> **背景**：教务端诊断发现教案 `steps[].minutes` 的理论/实践归类分钟与声明 `hours_theory`/`hours_practice` 存在系统性偏差。教务端已将时间输出简化为分钟制（不再显示学时），但课程端的数据精确性仍需修正。

---

## 一、教务侧已完成的工作

1. `gen_lessonplan_xml.py` 时间输出改为 `约{minutes}分钟（理论/实践）`，不再显示约学时
2. `Spec_LessonPlan.md` §3.4/§3.5 和 `Spec_Global.md` 同步更新
3. 自动诊断脚本扫描发现以下偏差

## 二、请课程侧执行的任务

### 任务 1：修正 `steps[].minutes` 理论/实践归类偏差 ⭐

**目的**：确保每周的理论 stage 分钟之和 = `hours_theory × minutes_per_period`，实践 stage 分钟之和 = `hours_practice × minutes_per_period`。

**分类规则**：
- 理论 stage 关键词：复习、导入、讲授、演示
- 实践 stage 关键词：实践、练习、训练、总结、小结

**信息可视化** — 1/8 周有偏差：

| 周 | hours_theory | hours_practice | 理论实际min | 理论应min | 实践实际min | 实践应min | 偏差 |
|:--:|:-----------:|:--------------:|:----------:|:---------:|:----------:|:---------:|------|
| W2 | 3 | 2 | 150 | 135 | 75 | 90 | 理论+15/实践-15 |

W2 偏差原因：`stage=演示`（30min）被归为理论，使理论超出声明。需要调整 W2 的某些 stage 分钟分配，使理论组总和 = 135min、实践组总和 = 90min。

**交互产品开发** — 13/15 周有偏差：

W3-W14（每周相同模式）：

| stage | minutes | 归类 |
|:-----:|:-------:|:----:|
| 复习 | 10 | 理论 |
| 导入 | 10 | 理论 |
| 讲授 | 60 | 理论 |
| 实践 | 90 | 实践 |
| 小结 | 10 | 实践 |

理论 = 80min（应 90min，差 -10min），实践 = 100min（应 90min，多 +10min）

修正建议（任选一）：
- **方案A**：讲授改为 70min、实践改为 80min（讲授+10，实践-10）
- **方案B**：复习改为 15min、小结改为 5min（理论+5，实践-5 → 各差5min，再微调讲授/实践）

W15（路演周，hours_theory=0, hours_practice=4）：

| stage | minutes | 归类 | 问题 |
|:-----:|:-------:|:----:|------|
| 导入 | 10 | 理论 | ❌ 纯实践周不应有理论 stage |
| 实践 | 150 | 实践 | ✅ |
| 小结 | 20 | 实践 | ✅ |

修正建议：W15 的 `stage=导入` 改为 `stage=实践`（内容描述可保留"课程回顾"，但归类应为实践）。或将 hours_theory 改为 0.2、hours_practice 改为 3.8。

> [!IMPORTANT]
> 修正时**保持每周总分钟不变**（信息可视化=225min，交互产品开发=180min），仅调整各 stage 之间的分钟分配。

### 任务 2：补填大纲 `hours.theory` 和 `hours.practice` 顶层字段

当前两门课程的 `course.yaml` 中 `hours.theory` 和 `hours.practice` 均为 0。请根据各周的 `hours_theory`/`hours_practice` 累加值填入正确数据：

**信息可视化**：
```yaml
hours:
  total: 40   # 已有
  theory: 20  # 需补填：∑ 各周 hours_theory
  practice: 20  # 需补填：∑ 各周 hours_practice
```

**交互产品开发**：
```yaml
hours:
  total: 60   # 已有
  theory: 30  # 需补填
  practice: 30  # 需补填
```

---

## 三、规范依据

- `Spec_LessonPlan.md` §3.5 — stage 分类规则及校验规则 C-2
- `Spec_Global.md` §5.5 — 教学环节 stage 分类校验
- `Spec_Global.md` §7.1 序号3 — 学时校验：`hours.total = hours.theory + hours.practice`

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python /tmp/diagnose_hours.py
```

合格标准：
1. 每周理论/实践分钟 **零偏差**
2. 大纲 `hours.theory` / `hours.practice` 非零且等于各周累加值

---
*消息时间：2026-02-27 | 教务材料 Agent*
