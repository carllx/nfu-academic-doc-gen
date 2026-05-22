---
description: 跨项目边界检查——判定修改请求属于教务材料端（文档输出）还是课程端（内容/数据），若涉及课程端则生成 MSG 任务单委托课程 Agent 执行。
---

# 跨项目边界检查 (Boundary Check)

> **核心原则**：教务材料项目（`/Users/yamlam/Downloads/教务材料/`）**只负责文档输出**。课程内容/数据的修正由课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）执行。

---

## 何时触发

当 Agent 收到**任何修改请求**时，在动手之前必须先执行本工作流的判定逻辑。典型触发场景：

- 用户报告输出文档内容错误（如章节编号缺失、学时数异常）
- 审计脚本 (`audit_course_data.py`) 输出 `[CRITICAL]` / `[WARN]` 级别问题
- 用户要求调整课程目标、教学内容、实验安排等教学设计
- 用户要求统一术语/编号/措辞

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

## 步骤 3：编写 MSG 任务单

在共享邮箱和本地 `docs/` 下同时创建标准化的跨项目委托消息：

### 文件创建

1. **原始文件**（完整内容）：`docs/MSG_to_CourseAgent_{主题关键词}.md`
2. **邮箱副本**（摘要 + 引用）：`/Users/yamlam/Downloads/cross_agent_mailbox/active/{YYYY-MM-DD}_JW_{ID}_{主题关键词}.md`

### 原始文件模板（`docs/` 下）

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

### 邮箱副本模板（`cross_agent_mailbox/active/` 下）

```yaml
---
id: MSG-{序号}
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

### 同步更新 INDEX.md

在 `/Users/yamlam/Downloads/cross_agent_mailbox/INDEX.md` 的活跃消息表中新增对应行。

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
- 📨 **MSG 已生成**：提供 MSG 文件路径，说明课程端需做的工作
- ❓ **待确认**：如有需用户裁决的归属问题，一并列出

---

## 附录：在其他工作流中引用本检查

在其他工作流的**修改步骤前**，添加以下片段即可注入边界检查：

```markdown
### 前置：边界检查
在执行修改前，按 `/mailbox_out` 工作流判定每项修改的归属。
- 🟢 教务端项 → 直接执行
- 🔵🟡 课程端项 → 编写 MSG 任务单，**不得**直接修改课程工作区文件
```
