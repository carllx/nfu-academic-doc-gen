---
description: 跨项目修改请求的归属判定——判定属于教务材料端（文档输出）还是课程端（内容/数据），若涉及课程端则生成 MSG 任务单投递到共享邮箱。
---

# 邮箱发件 (Mailbox Out)

> **核心原则**：教务材料项目（`/Users/yamlam/Downloads/教务材料/`）**只负责文档输出**。课程内容/数据的修正由课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）执行。
> **配套工作流**：`/mailbox_in` — 接收并处理共享邮箱中的消息。

---

## 何时触发

当 Agent 收到**任何修改请求**时，在动手之前必须先执行本工作流的判定逻辑。典型触发场景：

- 用户报告输出文档内容错误（如章节编号缺失、学时数异常）
- 审计脚本 (`audit_course_data.py`) 输出 `[CRITICAL]` / `[WARN]` 级别问题
- 用户要求调整课程目标、教学内容、实验安排等教学设计
- 用户要求统一术语/编号/措辞

---

## 步骤 0：同步 INDEX（前置，每次必做）

在判定前先刷新共享邮箱状态，避免重复发送已有 MSG：

1. 读取 `/Users/yamlam/Downloads/cross_agent_mailbox/INDEX.md`
2. 扫描 `active/` 目录中所有 `.md` 文件的 frontmatter
3. 比对差异并写回 INDEX.md（规则同 `/mailbox_in` 步骤 0）
4. **去重检查**：检查当前修改请求的主题是否与 `active/` 中已有 MSG 重叠。若重叠，向用户确认是追加到现有 MSG 还是新建。

---

## 步骤 1：分类判定

将修改请求拆分为独立的修改项，逐项对照下表判定归属：

| 归属 | 修改范围 | 示例 |
|:----:|----------|------|
| **教务端** 🟢 | 生成器代码 (`scripts/gen_*.py`, `docx_engine.py`) | 修复表格渲染 bug、调整占位符替换逻辑 |
| **教务端** 🟢 | 模板文件 (`Template_*.docx`) | 调整输出文档排版/格式 |
| **教务端** 🟢 | Schema 定义 (`course_schema.py`) | 新增/修改字段定义 |
| **教务端** 🟢 | 规范文档 (`Spec_*.md`, `docs/`) | 更新编写规范、数据字典 |
| **教务端** 🟢 | 审计脚本 (`audit_course_data.py`) | 新增校验规则 |
| **课程端** 🔵 | `course.yaml` 数据内容 | 修改 topic/content/objectives/experiments 等字段值 |
| **课程端** 🔵 | 教学脚本 (`scripts/W*.md`) | 修改授课讲稿内容 |
| **课程端** 🔵 | 知识库 (`knowledge/`) | 修改教学参考资料 |
| **课程端** 🔵 | 课程设计决策 | OBE 动词语义确认、目标映射调整 |
| **双端协同** 🟡 | Schema 新字段 + 数据填充 | 教务端定义字段 → 课程端填充数据 |
| **双端协同** 🟡 | 审计发现 + 数据修正 | 教务端输出报告 → 课程端修正数据 |

### 判定规则

```
IF 修改项仅涉及生成器/模板/Schema/审计/规范:
    → 归属教务端 🟢，直接执行
    → 跳至【步骤 4】

ELIF 修改项涉及 course.yaml 数据内容或课程教学设计:
    → 归属课程端 🔵 或双端协同 🟡
    → 继续【步骤 2】

ELIF 不确定:
    → 向用户确认归属后再行动
```

> [!CAUTION]
> **严禁**跨区直接修改课程工作区文件。即使修改看似简单（如改一个 YAML 字段值），也必须通过 MSG 任务单委托。这是 `Architecture.md §5.3` 确立的铁律。

---

## 步骤 2：拆分任务——教务端先行部分

如果是**双端协同** 🟡，先完成教务端自身的准备工作：

1. **Schema 变更**：若需新字段，先更新 `course_schema.py`，确保含 fallback 默认值
2. **数据字典同步**：同步更新 `docs/Data_Dictionary.md`
3. **审计脚本增强**：若需新校验规则，更新 `audit_course_data.py`
4. **规范文档更新**：同步更新相关 `Spec_*.md`

> [!IMPORTANT]
> 遵守**三层原子同步**原则（`Architecture.md §5.3`）：`course_schema.py` → `Data_Dictionary.md` / `Spec_*.md` → 生成器 fallback 逻辑，必须在同一会话完成。

---

## 步骤 3：编写 MSG 任务单并投递到邮箱

### 3.1 获取下一个 MSG ID

读取 `INDEX.md` 底部的"ID 分配规则"获取当前最大值，+1 作为新 ID。

### 3.2 创建原始文件（完整内容）

路径：`docs/MSG_to_CourseAgent_{主题关键词}.md`

```markdown
# 任务单：{标题}

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：{YYYY-MM-DD}
> **优先级**：{P0 紧急 / P1 重要 / P2 常规}
> **背景**：{简述为什么需要课程端修改，引用相关规范条目}

---

## 一、教务侧已完成的工作
{列出教务端做了哪些准备，如 Schema 变更、审计报告等}

## 二、请课程侧执行的任务

### 任务 N：{任务标题} {⭐ 如果是关键任务}
**目的**：{一句话说明修改意图}
{详细的修改说明，包含 Before/After 对比示例}

> [!IMPORTANT]
> {关键约束或注意事项}

---

## 三、规范依据
{引用具体的规范条目，如 Spec_*.md §X.X、Architecture.md §X.X}

## 四、验证方法

\```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python \
  "/Users/yamlam/Downloads/教务材料/scripts/audit_course_data.py" --root .
\```

合格标准：{具体的通过条件}

---
*消息时间：{YYYY-MM-DD} | 教务材料 Agent*
```

### 3.3 创建邮箱副本（摘要 + 引用）

路径：`/Users/yamlam/Downloads/cross_agent_mailbox/active/{YYYY-MM-DD}_JW_MSG-{ID}_{主题关键词}.md`

```yaml
---
id: MSG-{ID}
from: 教务材料
to: 课程工作区
created: {YYYY-MM-DD}
priority: {P0/P1/P2}
status: pending
read_by: []
depends_on: []
original: "教务材料/docs/MSG_to_CourseAgent_{主题关键词}.md"
---
```

邮箱副本包含任务摘要和原始文件的链接引用，无需重复完整内容。

### 3.4 更新 INDEX.md

在活跃消息表中新增对应行 + 更新底部 ID 最大值。

### 编写要求

1. **自包含**：课程端 Agent 无需查阅其他文档即可理解并执行全部任务
2. **有据可依**：每项修改要求必须引用规范出处（Spec、ADR、Schema 定义）
3. **可验证**：必须附上自检命令和明确的合格标准
4. **Before/After**：数据变更类任务必须给出修改前后对比示例

---

## 步骤 4：通知用户

完成判定和 MSG 编写后，向用户报告：

- 📋 **判定结果**：哪些项归教务端、哪些项需委托课程端
- ✅ **教务端已完成**：列出本端已做的变更
- 📨 **MSG 已投递**：提供 MSG 文件路径，说明课程端需做的工作
- ❓ **待确认**：如有需用户裁决的归属问题，一并列出

---

## 步骤 5：归档输出（按需触发）

> 当用户要求上传云盘、提交压缩包或打印时触发。非常规修改判定流程，可独立执行。

### 5.1 前置检查

1. 确认 `course.yaml` 中每个班级的 `classes[].archive_id` 已填写。若缺失，提示用户提供归档序号。
2. 确认需要输出的文档类型（大纲 / 进度表 / 教案合并版 / 实验指导书 / 考核材料）。

### 5.2 命名与复制

按 `Spec_Global.md §8` 的命名公式重命名并复制到用户指定的输出目录：

```bash
# 示例：信息可视化设计（2024级，archive_id=55，多班）
55林昕+2024级+数字媒体艺术+《信息可视化设计》+教学大纲.docx        # per-course，多班省略班级
55林昕+2024级+数字媒体艺术+影视班+《信息可视化设计》+教学进度表.docx  # per-class，含班级
55林昕+2024级+数字媒体艺术+游戏班+《信息可视化设计》+教学进度表.docx
55林昕+2024级+数字媒体艺术+《信息可视化设计》+教案.docx            # 合并版
55林昕+2024级+数字媒体艺术+《信息可视化设计》+实验指导书.docx
```

### 5.3 PDF 转换（若需要）

```bash
cd <输出目录> && /opt/homebrew/bin/soffice --headless --convert-to pdf ./*.docx
```

> [!WARNING]
> LibreOffice 转换的 PDF 排版可能与 Word 略有差异。精确排版需用 Word/WPS 手动导出。

---

## 附录：在其他工作流中引用本检查

在其他工作流的**修改步骤前**，添加以下片段即可注入边界检查：

```markdown
### 前置：边界检查
在执行修改前，按 `/mailbox_out` 工作流判定每项修改的归属。
- 🟢 教务端项 → 直接执行
- 🔵🟡 课程端项 → 编写 MSG 任务单投递到邮箱，**不得**直接修改课程工作区文件
```
