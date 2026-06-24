# 任务单：教学环节 stage 分类校验——课程端 L1 写入校验机制建设

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P1 重要
> **背景**：教案时间安排中，教学环节的分钟分配必须严格对应教学大纲的理论/实践学时比例。教务端已建立 L2/L3 层兜底检测（生成器 gate + 审计脚本），但**根本解决方案**需要课程端在数据写入时即自检，从源头预防错误数据进入流水线。

---

## 一、教务侧已完成的工作

1. **审计脚本增强**：`audit_course_data.py` 新增 3c 段"教学环节 stage 归属校验"三条规则：
   - C-1: W1 禁止 `stage=复习`（`[CRITICAL]`）
   - C-2: 理论/实践 stage 分钟折算与 `hours_theory`/`hours_practice` 偏差 >1h `[WARN]` / >2h `[CRITICAL]`
   - C-3: 纯实践周(`hours_theory=0`)理论 stage 时间 >30min `[WARN]`

2. **生成器硬性 gate**：`gen_lessonplan_xml.py` 新增 `_validate_week_steps()`，生成前检测不通过 → `[BLOCKED]` 跳过该周 `.docx` 输出

3. **规范写入**：
   - `Spec_LessonPlan.md` 新增 §3.5 教学环节时间分类规则
   - `Spec_Global.md` §5.5 防御规则表追加新条目

## 二、请课程侧执行的任务

### 任务 1：修正信息可视化 W1 stage 数据 ⭐

**文件**：`/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course.yaml`

**目的**：W1 的 `steps[0].stage` 当前为 `复习`，但 summary 为"首节课开篇，简要介绍课程概况、学习目标与评估方式"——这是课程介绍性质，不是复习。

**Before**：
```yaml
    steps:
    - stage: 复习
      summary: 首节课开篇，简要介绍课程概况、学习目标与评估方式
      minutes: 10
```

**After**：
```yaml
    steps:
    - stage: 导入
      summary: 首节课开篇，简要介绍课程概况、学习目标与评估方式
      minutes: 10
```

> [!IMPORTANT]
> 修改后须运行审计脚本确认 C-1 规则不再报错。

### 任务 2：两课程全量 stage 归属审查

运行教务端审计脚本，确认**两门课程**全部周次均通过 C-1/C-2/C-3 规则：

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

**信息可视化**（修正 W1 stage 后）应无新增 `[CRITICAL]`/`[WARN]`。  
**交互产品开发** W1 无 stage=复习，应直接通过。

### 任务 3：确认分类规则

请确认以下教学环节-学时归属分类是否符合课程教学实际：

| 归属 | 教学环节 | stage 关键词 |
|:----:|---------|:----------:|
| 理论学时 | 上次课复习 / 课程导入 / 新课讲授 | 复习、导入、讲授、演示 |
| 实践学时 | 实践训练 / 课程小结 | 实践、练习、训练、总结、小结 |

若有异议（如"小结应归理论"），请回复说明理由，教务端将协商调整。

### 任务 4：建立课程端 L1 写入校验机制

**目的**：从根部预防错误数据写入 `course.yaml`。

**建议方式**（课程端自行评估最佳实现）：
- 方案 A：在 Agent 工作流规则中写入 stage 分类检查步骤
- 方案 B：在审计/验证工作流中集成校验脚本
- 方案 C：利用 Pydantic Schema 约束或自定义 validator

**核心校验点**：
1. W1 的 steps 中不得包含 `stage=复习`
2. 理论 stage（复习/导入/讲授）分钟折算 ≈ `hours_theory`
3. 实践 stage（实践/训练/小结）分钟折算 ≈ `hours_practice`

> [!IMPORTANT]
> 课程端无需开发与教务端完全一致的审计逻辑，轻量级的写入前检查即可。教务端的 L2/L3 层会兜底。

---

## 三、规范依据

- `Spec_LessonPlan.md` §3.5 教学环节时间分类规则
- `Spec_Global.md` §5.5 防御规则表"教学环节 stage 分类校验"条目
- `Architecture.md` §5.3 Agent 身份边界不越界

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

合格标准：无 `[CRITICAL]` 级别的 stage 归属相关报错；C-1/C-2/C-3 规则全部通过。

---
*消息时间：2026-02-27 | 教务材料 Agent*
