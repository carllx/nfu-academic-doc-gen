# 任务单：教案数据丰富化（交互产品开发 & 信息可视化）

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-05-19
> **优先级**：P1
> **背景**：用户反映《交互产品开发》和《信息可视化》两门课程的教案输出内容“太过简单”。教务端查阅生成器规则发现，当 `course.yaml` 中缺少详细的 `lessons[].steps[]` 教学环节数据时，教案生成器会自动触发兜底逻辑，仅输出空白的“【教学组织】”、“【时间安排】”等框架占位符。

---

## 一、教务侧已完成的工作
教务端已完成问题定位：确认教案生成器（`gen_lessonplan_xml.py`）工作正常，实质缺陷在于源数据端缺乏教学环节详情支撑。

## 二、请课程侧执行的任务

### 任务 1：补充课程教案详细数据 ⭐
**目的**：为《交互产品开发》和《信息可视化》两门课补充教案数据，提升教案质量。
请在两门课程的 `course.yaml` 中，针对 `calendar[]` 的每一周配置，详细填写 `lessons` 以及 `steps` 数组。
`steps` 应至少包含：
- `stage`：说明该环节阶段（如导入、讲授、复习、实践、小结）
- `minutes`：预计耗时（确保总时长符合标准）
- `summary` / `content`：具体的教学组织和知识点内容
- `ideology`：思政融入点（适用于讲授环节）

> [!IMPORTANT]
> 必须确保每同类别 stage 的 `minutes` 累加转换成等效学时后，与声明的理论或实践学时数对齐，符合课程整体大纲设计，以通过教案前置审查规则。

---

## 三、规范依据
- 见 `教务材料/03_LessonPlan_Generator/Spec_LessonPlan.md` §3.3 及 §3.4 教学环节子节规范。

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

合格标准：没有教案生成器由于缺少 `steps` 导致的警告或数据空缺。
---
*消息时间：2026-05-19 | 教务材料 Agent*
