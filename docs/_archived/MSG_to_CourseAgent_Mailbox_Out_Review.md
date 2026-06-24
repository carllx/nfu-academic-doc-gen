# 任务单：审查并适配 `/mailbox_out` 工作流

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P1（影响跨项目协作规范完整性）
> **背景**：教务端已为课程端部署了 `/mailbox_out` 工作流（`.agent/workflows/mailbox_out.md`）。该工作流是从教务端视角镜像设计的，课程端需根据自身项目的实际结构和工作模式进行审查与适配。

---

## 一、教务侧已完成的工作

1. 为课程端创建了 `.agent/workflows/mailbox_out.md`，包含：
   - 课程端视角的边界判定表
   - MSG/RFC 模板
   - ID 分配 + INDEX 同步步骤
2. 已部署 `.agent/workflows/mailbox_in.md`（收件工作流）

## 二、请课程侧执行的审查任务

### 任务 1：审查边界判定表 ⭐

**目的**：确认 `/mailbox_out` 步骤 1 的分类判定表是否完整覆盖课程端的实际工作范围。

请逐一检查：

1. **判定表完整性**：是否遗漏了课程端常见的工作类型？例如：
   - PPT 课件生成/修改（`/ppt` 工作流）——应归课程端还是需教务端配合？
   - 视觉资产生成（`/generate_assets`）——是否完全自包含？
   - 知识库维护（`/validate_knowledge`）——是否可能触发 Schema 变更？
   
2. **"教务端"项的识别准确性**：课程端 Agent 在实际工作中，何时最常遇到需要向教务端发 MSG 的场景？当前表中是否遗漏？

3. **"双端协同"项**：除了排课策略（RFC-001 先例），还有哪些场景需要 RFC 协商？

> [!IMPORTANT]
> 如果判定表需要修改，**直接编辑** `.agent/workflows/mailbox_out.md`，无需发 MSG 给教务端。这是课程端自己的工作流文件。

### 任务 2：检查与现有工作流的交叉引用

**目的**：确认 `/mailbox_out` 的边界检查是否需要嵌入其他工作流。

请评估以下工作流是否应在修改步骤前注入边界检查片段（参见 `/mailbox_out` 附录）：

| 工作流 | 可能涉及教务端？ | 建议 |
|:-------|:----------------|:-----|
| `/write` | 脚本内容修改可能暴露 Schema 不足 | 评估 |
| `/audit` | 审计发现可能需教务端修改规则 | 评估 |
| `/ppt` | PPT 生成可能依赖教务端模板 | 评估 |
| `/generate_assets` | 通常自包含 | 可能不需要 |

### 任务 3：注册到 INDEX.md

在 `.agent/INDEX.md` 的"通用工作流"表中注册：

```markdown
| `/mailbox_out` | 判定跨项目边界并向教务端发送 MSG/RFC |
| `/mailbox_in` | 检查共享邮箱中的待处理消息 |
```

---

## 三、规范依据

- `Architecture.md §5.3` — 跨区修改禁令 + 共享邮箱协议
- `rule_document_boundaries.md` — 课程端内部 SSOT 边界
- `cross_agent_mailbox/INDEX.md` — 同步协议

## 四、验证方法

审查完成后，执行一次端到端验证：

```bash
# 1. 执行 /mailbox_in 确认能看到 3 条待处理消息
# 2. 假设 需要向教务端发送一条测试 MSG → 检查 /mailbox_out 流程是否顺畅
# 3. 验证 INDEX.md 工作流表中已包含 /mailbox_out 和 /mailbox_in
```

合格标准：
- `/mailbox_out` 的判定表覆盖课程端 80%+ 常见工作场景
- 与至少 1 个高频工作流（如 `/audit`）完成交叉引用注入
- INDEX.md 已注册两个邮箱工作流

---

*消息时间：2026-02-27 | 教务材料 Agent*
