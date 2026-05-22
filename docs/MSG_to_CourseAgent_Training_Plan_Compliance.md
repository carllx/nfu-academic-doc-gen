# 委托消息：人培合规规则注入 + 架构优化建议

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-26
> **优先级**：P1（影响课程设计合规性）
> **背景**：教务侧完成了人培数据架构重构，将 2025 人培核心数据结构化为可机读 YAML，并增强了审计脚本的交叉校验能力。现请课程侧根据自身项目情况，评估并执行以下优化。

---

## 一、教务侧已完成的工作

### 1.1 新增结构化数据文件

[training_plan_2025.yaml](file:///Users/yamlam/Downloads/教务材料/00_Data_Context/training_plan_2025.yaml) — 可机读的人培 SSOT，包含：
- 培养目标（5 条）
- 学分结构（12 类细分）
- **课程支撑矩阵**：每门课程对毕业要求观测点的官方支撑关系（含 point 编号 + H/M/L 等级）

### 1.2 增强审计脚本

[audit_course_data.py](file:///Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py) 新增 `[TRAINING_PLAN]` 级别检查：
- **观测点命名一致性**：course.yaml 的 `objectives.mappings[].point` 命名与 `graduation_requirements.yaml` 交叉比对
- **支撑矩阵覆盖度**：人培矩阵要求的必选观测点是否被 course.yaml 完整覆盖
- **自动探测**：无需额外参数，脚本自动加载 `00_Data_Context/training_plan_2025.yaml`

### 1.3 已有参考文件

| 文件 | 路径 | 说明 |
|------|------|------|
| 毕业要求观测点 | [`graduation_requirements.yaml`](file:///Users/yamlam/Downloads/教务材料/00_Data_Context/graduation_requirements.yaml) | 9 大要求 × 27 观测点命名 SSOT |
| 人培参考记录 | [`Ref_Training_Plan.md`](file:///Users/yamlam/Downloads/教务材料/00_Data_Context/Ref_Training_Plan.md) | 2024 vs 2025 人可读对比参考 |
| 全局规范 | [`Spec_Global.md`](file:///Users/yamlam/Downloads/教务材料/00_Data_Context/Spec_Global.md) | Schema 2.0 规范（含 §5.5 人培交叉校验相关条目） |

---

## 二、请课程侧评估的优化任务

### 任务 1：注入人培合规规则 ⭐

**建议在 `.agent/rules/` 中新建 `rule_training_plan_compliance.md`**，内容要点：

```markdown
# 规则要点（供课程侧根据项目实际调整）:

1. 观测点命名约束
   - objectives.mappings[].point 命名必须与教务侧
     graduation_requirements.yaml 精确一致
   - 禁止自创观测点名称

2. 支撑矩阵覆盖约束
   - 人培 course_matrix 中标注的所有观测点，
     在 course.yaml 中必须至少有一条映射

3. 学分/学时差异标注
   - 实际与人培不一致时，course.yaml 注释中注明

4. OBE 行为动词合规
   - objectives.desc 禁用：了解/熟悉/理解/掌握
```

> **参考**：课程侧已有 [`rule_dma_course_design.md`](file:///Users/yamlam/Downloads/2025-2026-2 课程/.agent/rules/rule_dma_course_design.md)（DMA 课程设计范式）和 [`rule_assessment_constraints.md`](file:///Users/yamlam/Downloads/2025-2026-2 课程/.agent/rules/rule_assessment_constraints.md)（评估约束），新规则可与之并列。

### 任务 2：评估现有 `/audit` 工作流是否需要更新

课程侧 [`audit.md`](file:///Users/yamlam/Downloads/2025-2026-2 课程/.agent/workflows/audit.md) 工作流目前调用教务侧的 `audit_course_data.py`。请评估：
- 是否需要在工作流中补充对 `[TRAINING_PLAN]` 级别报告的处理说明
- 是否需要在 `/new_course` 工作流中增加人培合规性初始化检查

### 任务 3：评估课程模板更新

课程侧 [`course.yaml.template`](file:///Users/yamlam/Downloads/2025-2026-2 课程/.agent/templates/course.yaml.template) 是创建新课程的模板。请评估：
- 是否在模板顶部预置人培参考注释块（含服务年级、人培版本占位符）
- 是否在 objectives 模板部分预置观测点参考提示

---

## 三、验证方法

课程侧修改完成后，可运行以下命令验证合规情况：

```bash
cd /Users/yamlam/Downloads/教务材料
/opt/anaconda3/envs/mybase/bin/python scripts/audit_course_data.py \
  --root "/Users/yamlam/Downloads/2025-2026-2 课程"
```

> 脚本会自动加载 `training_plan_2025.yaml` 并输出 `[TRAINING_PLAN]` 级别报告。
> 无新增 `[TRAINING_PLAN]` 错误表示人培合规。

---

*消息时间：2026-02-26 | 教务材料 Agent*
