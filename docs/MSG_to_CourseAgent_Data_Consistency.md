# 任务单：源数据结构化整改（章节编号 & 学时校验）

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27 (V3)
> **背景**：教务端生成器全面升级为 **WYSIWYG（所见即所得）** 模式——不再自动拼接"第X章"或知识点编号。`course.yaml` 中的文本就是最终文档中的文本。因此，课程端必须确保源数据本身结构完整。

---

## 一、 章节编号体系固化

### 问题
教务端大纲生成器 (`gen_syllabus_xml.py`) 和教案生成器 (`gen_lessonplan_xml.py`) 过去会自动拼接 `第{周次}章 {topic}` 和 `{周次}.{序号} {content行}`。现已废弃此逻辑。如果 YAML 中没写编号，输出文档中就不会有编号。

### 您的任务

#### (A) 在每周添加 `chapter_title` 字段

`chapter_title` 是大纲章标题和教案 R0"授课章节"的直接来源。请在 `calendar[]` 各周中加入此字段。

**Before:**
```yaml
- week: 1
  topic: 信息可视化概论
  content: |-
    可视化定义与分类
    Anscombe 四重奏与数据可视化动机
```

**After:**
```yaml
- week: 1
  chapter_title: "第一章 信息可视化概论"
  topic: 信息可视化概论
  content: |-
    1.1 可视化定义与分类
    1.2 Anscombe 四重奏与数据可视化动机
```

> [!IMPORTANT]
> `content` 中每一行都将直接作为大纲"主要知识点"输出。请确保每行自带编号前缀（如 `1.1`、`2.3`），且各周之间的编号体系连贯。

#### (B) `topic` 保持简洁标题即可
`topic` 仍作为进度表"教学内容(章、节)"列的主标题使用。它**不需要**加"第X章"前缀。

---

## 二、 物理排课学时核实

### 问题
`交互产品开发` 出现了 `hours_theory: 4, hours_practice: 2`（总计 6）的极端配置，超出单次课 4 节的物理容量。路演周（W15）不应有理论学时。

### 您的任务
- 逐周核对 `hours_theory` 和 `hours_practice`，使总和 ≤ 排课系统实际分配的节次数。
- 特殊周次（路演/答辩/汇报）：`hours_theory` 必须为 `0`。

> [!NOTE]
> **已修正（2026-02-27 V3）**：进度表中「课堂教学」列 = `hours_theory`（仅理论学时），「课内实践」列 = `hours_practice`（仅实践学时）。此前的合计定义有误，已在 `Spec_Schedule.md §2.3` 和 `gen_schedule_xml.py` 中同步修正。

---

## 三、 实验 ID 挂载

若某周包含实验内容，请在对应 `calendar[]` 条目中添加 `exp_id`:
```yaml
- week: 3
  exp_id: 1   # 对应实验1
```

---

## 五、 实验编号措辞统一

### 问题
教务端全部生成器已使用 `实验N` 中文格式（如"实验1"、"实验报告封面_实验2"）。但课程端的 `scripts/W*.md` 和 `knowledge/notes/*.md` 中大量使用裸 `Exp1`~`Exp4` 简写（约 60+ 处），与教务文档输出风格不一致。提交打印后教务审查时可能质疑"Exp"非规范用语。

### 您的任务

将所有**面向教务/学生可见的正式行文**中的裸 `Exp[n]` 统一为以下格式之一：

| 场景 | 格式 | 示例 |
|------|------|------|
| 正式描述（首次出现） | `实验N（ExpN）` | 实验3（Exp3） |
| 后续简称 | `实验N` | 实验3 |
| 纯技术/内部引用 | `Exp[n]` 保留 | 文件名、变量名等 |

**范围**：`scripts/W*.md` 中扫描以下模式并按规则替换：
```
Exp1 → 实验1（Exp1）或 实验1
Exp2 → 实验2（Exp2）或 实验2
Exp3 → 实验3（Exp3）或 实验3
Exp4 → 实验4（Exp4）或 实验4
```

> [!TIP]
> `knowledge/notes/*.md` 属于内部教学参考，可酌情保留 `Exp[n]` 简写。但若笔记中有学生可见的段落（如课后阅读），也建议统一。

---

## 六、 自检命令

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
```

合格标准：输出 `✅ No issues found.`，无 `[CRITICAL]` 级错误。

---
*消息时间：2026-02-27 | 教务材料 Agent*
