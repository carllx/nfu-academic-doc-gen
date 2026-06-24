# 任务单：补充考核期末大作业截止日期 (practice_deadline)

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-06-15
> **优先级**：P1
> **背景**：在生成 2025-2026-2 学期的《信息可视化》与《交互产品开发》这两门课程的期末考查试卷（A/B卷）时，发现第 4 项要求填入的“提交时间”缺失。试卷底层模板依赖确切的占位符变量 `practice_deadline`。目前源数据中并没有把截止时间单独提取出来。

---

## 一、教务侧已完成的工作
- 已经在生成器中修复了遗留旧文件导致的重名及信息串联错误问题。
- 已统一考核方式为 SSOT 取值。

## 二、请课程侧执行的任务

### 任务 1：提取《信息可视化》截止时间
**目的**：为试卷提供截止时间注入变量。
- 读取课程下的 `course_assessment.yaml`。
- 在 `final_item` 或 `exam` 的 `ab_versions` 下找到 `A` 和 `B` 分支。
- 从当前的 `practice_deliverables`（如“2026年6月21日前”）提炼具体截止时间。
- 为 `A` 和 `B` 分支各新增一个字段 `practice_deadline`，并填入提取出的日期。

### 任务 2：提取《交互产品开发》截止时间
**目的**：为试卷提供截止时间注入变量。
- 同样读取课程下的 `course_assessment.yaml`。
- 在 `ab_versions` 的 `A` 和 `B` 选项下新增对应的 `practice_deadline` 字段。

> [!IMPORTANT]
> - 确保 YAML 语法正确无误。
> - 只需增加新字段，不要修改现有的 `practice_deliverables`，以防影响原有展示。

---

## 三、规范依据
相关规则可参见教务材料端试卷模板与 `gen_assessment_xml.py` 内部对于占位符 `practice_deadline` 的映射读取。由于教务端只负责格式化输出，数据补全需由课程端完成。

## 四、验证方法

```bash
# 验证 yaml 是否合法（替换为实际的课程目录）
python -c 'import yaml; data = yaml.safe_load(open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course_assessment.yaml")); print("practice_deadline" in str(data))'
```

合格标准：YAML 无解析错误，且已在 A/B 分支中补充了 `practice_deadline` 字段。

---
*消息时间：2026-06-15 | 教务材料 Agent*
