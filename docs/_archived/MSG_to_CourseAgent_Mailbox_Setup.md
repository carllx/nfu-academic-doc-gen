# 任务单：邮箱系统配置对接

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P1（影响跨项目协作效率）
> **背景**：教务端建立了跨 Agent 共享邮箱系统（`/Users/yamlam/Downloads/cross_agent_mailbox/`），用于统一管理两端的任务委托、RFC 协商和状态追踪。课程端已有 `/mailbox_in` 工作流文件，但项目内部配置尚未对接。请根据自身项目情况完成以下配置。

---

## 一、教务侧已完成的基础设施

### 1.1 共享邮箱目录

```
/Users/yamlam/Downloads/cross_agent_mailbox/
├── INDEX.md                ← 统一消息索引（双端共享、同步协议）
├── active/                 ← 待处理消息（3 条发给课程端的活跃 MSG）
├── resolved/               ← 已关闭消息（4 条历史记录）
└── rfc/                    ← RFC 协商（1 条已关闭）
```

### 1.2 消息 frontmatter 标准

每条消息包含以下 YAML frontmatter：

```yaml
---
id: MSG-{序号}
from: 教务材料 | 课程工作区       # 发送方
to: 课程工作区 | 教务材料         # 接收方
created: YYYY-MM-DD
priority: P0 | P1 | P2
status: pending | acknowledged | in_progress | resolved
read_by: []                      # 接收方处理后追加自己
depends_on: []                   # 前置依赖的 MSG/RFC ID
original: "相对路径/原始文件.md"   # 完整内容的原始文件路径
---
```

### 1.3 已部署的工作流

教务端已部署 3 个工作流：
- **`/mailbox_out`**：判定修改归属 + 生成 MSG 投递到邮箱
- **`/mailbox_in`**：接收并处理来自课程端的消息
- **`/boundary_check`**：纯边界判定逻辑（可由 `/mailbox_out` 调用）

---

## 二、请课程侧执行的配置任务

### 任务 1：更新 INDEX.md 工作流表 ⭐

在 `.agent/INDEX.md` 的"通用工作流"表中注册新工作流：

```markdown
| `/mailbox_in` | 检查跨 Agent 共享邮箱中的待处理消息 |
```

### 任务 2：更新 WORKFLOWS.md（如有）

在 `docs/WORKFLOWS.md` 中添加邮箱系统说明（如果该文件存在）。

### 任务 3：评估是否需要边界规则

教务端有 `Architecture.md §5.3` 作为跨区修改的铁律。课程端可评估是否在 `.agent/rules/` 中新建类似规则，例如：

```markdown
# 规则：跨项目协作协议 (Cross-Agent Protocol)

1. **严禁**直接修改教务材料项目的文件
2. 需要教务端配合时，通过共享邮箱发送 MSG
3. 每次开始新工作前，建议执行 `/mailbox_in` 检查待办
4. 处理 MSG 后必须更新 INDEX.md
```

> [!TIP]
> 课程端已有 `rule_document_boundaries.md` 定义了内部 SSOT 边界。跨项目规则可作为其补充，或合并到该文件中。

### 任务 4：确认 `/mailbox_in` 工作流可用

`.agent/workflows/mailbox_in.md` 已就位，请确认：
1. 能正确扫描 `/Users/yamlam/Downloads/cross_agent_mailbox/active/`
2. 能读取 frontmatter 并按 `to: 课程工作区` 过滤
3. 当前应能看到 3 条待处理消息（MSG-001/002/003）

---

## 三、当前邮箱中发给课程端的待处理消息

| ID | 优先级 | 主题 | 创建日期 |
|:---|:-------|:-----|:---------|
| MSG-001 | P0 | OBE 合规性二次审查 | 2026-02-26 |
| MSG-002 | P1 | 人培合规规则注入 | 2026-02-26 |
| MSG-003 | P1 | 源数据结构化整改 | 2026-02-27 |

> [!IMPORTANT]
> 完成本配置任务后，建议立即执行 `/mailbox_in` 查看并处理以上 3 条消息。

---

## 四、验证方法

配置完成后，执行 `/mailbox_in`，预期输出：

```
📬 课程工作区收件箱 — 3 条待处理消息（INDEX 已同步 ✅）

[P0] MSG-001: OBE 合规性二次审查 (来自教务端, 2026-02-26)
[P1] MSG-002: 人培合规规则注入 (来自教务端, 2026-02-26)
[P1] MSG-003: 源数据结构化整改 (来自教务端, 2026-02-27)
```

---

*消息时间：2026-02-27 | 教务材料 Agent*
