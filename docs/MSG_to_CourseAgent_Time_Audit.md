# 任务单：教案时间安排校验机制——课程端配合项

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P2 常规
> **背景**：教案输出中各教学环节的 `【时间安排】约N分钟` 与周次学时存在语义混淆风险，且系统缺少自动校验机制。教务端将在审计脚本和生成器中增加校验与双单位输出，但需要课程端配合提供基础配置并确认数据一致性。

---

## 一、教务侧已完成 / 将完成的工作

1. **诊断报告**：完成全链路分析，确认 Schema → 生成器 → 审计三层均缺少 `steps.minutes` 合计校验
2. **审计脚本增强**（B）：`audit_course_data.py` 将新增 `[WARN]` 级别的 minutes 合计校验
3. **生成器输出优化**（C）：`gen_lessonplan_xml.py` 的 `_build_steps_map()` 输出将从 `约N分钟` 改为 `约N分钟（约M学时）` 双单位格式
4. **激活 scale_steps()**（D）：将断接的 `scale_steps()` 工具函数接入生成管线

---

## 二、请课程侧执行的任务

### 任务 1：确认每节课标准分钟数 ⭐

**目的**：确定分钟↔学时的换算基准，影响全系统校验精度。

请在两门课程的 `course.yaml` 中，于 `course.hours` 节下新增 `minutes_per_period` 字段：

**Before**：
```yaml
course:
  hours:
    total: 40
    theory: 20
    practice: 20
```

**After**：
```yaml
course:
  hours:
    total: 40
    theory: 20
    practice: 20
    minutes_per_period: 45   # 每节课标准分钟数（45 或 50）
```

> [!IMPORTANT]
> - 需确认实际排课是 **45 分钟/节** 还是 **50 分钟/节**
> - 该字段将被教务端 Schema 定义为 `Optional[int]`，默认值 45
> - 涉及课程：`信息可视化` 和 `交互产品开发`

### 任务 2：审查各周 steps.minutes 合计的合理性

**目的**：确保各周 `lessons[].steps[].minutes` 总和在合理范围内。

以信息可视化课程为例，当前每周 5 学时对应的 steps 分钟合计情况:

| 周次 | 总学时 | steps ∑ minutes | 若 45min/节 的上限 | 差值 |
|:----:|:----:|:----:|:----:|:----:|
| W1 | 5 | 195 | 225 | -30 |
| W2 | 5 | 200 | 225 | -25 |
| W3 | 5 | 195 | 225 | -30 |
| W4-W8 | 5 | 195 | 225 | -30 |

minutes 合计小于学时上限是正常的（课间 + 组织弹性），但需确认：
- 差值是否均为**有意预留**（课间转场、考勤等）
- 若某周差值异常（如超出上限或差值过大），请修正 steps.minutes

### 任务 3：交互产品开发课程 steps 数据检查

请同步检查 `/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course.yaml`：
- 各周 `lessons[].steps[]` 是否已填写 `minutes` 字段
- 若已填写，请按任务 2 的标准审查合理性
- 若未填写，暂不需要补充（生成器会输出默认占位框架）

---

## 三、规范依据

- **时间字段定义**：[course_schema.py](file:///Users/yamlam/Downloads/教务材料/scripts/course_schema.py#L49) — `TeachingStep.minutes: int`
- **学时校验规则**：[course_schema.py](file:///Users/yamlam/Downloads/教务材料/scripts/course_schema.py#L222-L246) — `check_hours_consistency()` root_validator
- **物理排课上限**：[audit_course_data.py](file:///Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py#L86-L113) — `MAX_HOURS_PER_SESSION = 5`
- **教案环节输出规范**：[Spec_LessonPlan.md](file:///Users/yamlam/Downloads/教务材料/03_LessonPlan_Generator/Spec_LessonPlan.md#L62-L84) — §3.4 教学环节子节规范
- **已预留工具函数**：[semester_utils.py](file:///Users/yamlam/Downloads/教务材料/scripts/utils/semester_utils.py#L113-L150) — `get_step_time_cap()` + `scale_steps()`

---

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

合格标准：
1. 新增的 `minutes_per_period` 字段不触发 Schema 错误
2. 各周 `∑ steps.minutes ≤ 总学时 × minutes_per_period`（允许 ±15% 弹性）
3. 无新增 `[CRITICAL]` 级别问题

> [!NOTE]
> 本任务为 **P2 常规**，不阻塞当前教案生成。教务端会先以默认 45 分钟/节进行改进，课程端确认后再微调。

---
*消息时间：2026-02-27 | 教务材料 Agent*
