---
description: 检查跨 Agent 共享邮箱中发给教务材料端的待处理消息，按优先级展示并引导处理。
---

# 邮箱收件 (Mailbox In)

> 扫描共享邮箱中发往本端（教务材料）的活跃消息，展示待办清单。
> **配套工作流**：`/mailbox_out` — 判定修改归属并发送 MSG 到共享邮箱。

## 步骤

### 0. 同步 INDEX（前置，每次必做）

在扫描消息前，先从目录实际内容重建 INDEX 的本端视图，确保状态最新：

1. 读取 `/Users/yamlam/Downloads/cross_agent_mailbox/INDEX.md`
2. 扫描 `active/`、`rfc/` 和 `resolved/` 目录下所有 `.md` 文件的 frontmatter
3. **比对差异**：
   - 目录中有但 INDEX 未记录的文件 → 新消息，追加到 INDEX
   - INDEX 中记录为 active 但文件已移至 `resolved/` → 更新 INDEX 状态
   - frontmatter 的 `status` / `priority` 与 INDEX 不一致 → 以 frontmatter 为准
4. **写回 INDEX.md**

> [!IMPORTANT]
> 此步骤确保即使对方 Agent 已发送新消息或更新了状态，你都能看到最新情况。

### 1. 过滤本端消息

只显示 `to: 教务材料` 且 `status` 不为 `resolved` 的消息。

### 2. 按优先级排序

按 `priority` (P0 > P1 > P2) 和 `created` (最早优先) 排序。

### 3. 展示待办清单

格式：
```
📬 教务材料收件箱 — N 条待处理消息（INDEX 已同步 ✅）

[P0] MSG-006: ... (来自课程端, YYYY-MM-DD)
     状态: pending | 依赖: 无
```

空收件箱输出：`📬 收件箱为空，没有待处理的跨项目消息。（INDEX 已同步 ✅）`

### 4. 处理消息

1. 将 frontmatter `status` 改为 `in_progress`
2. `read_by` 追加 `教务材料`
3. **立即更新 INDEX.md** 对应行
4. 读取 `original` 字段指向的原始文件获取完整内容
   - ⚠️ 若原始文件不存在，使用邮箱副本中的摘要执行，并在回复中标注"`original` 引用断链"
5. 按任务要求执行

### 5. 完成后归档 + 同步 INDEX（后置，每次必做）

1. 将 frontmatter `status` 改为 `resolved`，添加 `resolved_date`
2. 将文件从 `active/` 移入 `resolved/`
3. **更新 INDEX.md**：活跃表 → 已关闭表，更新 ID 最大值，校验总数一致

### 6. 过期消息提醒

扫描时若发现 `status: pending` 且 `created` 距今 **> 7 天** 的消息，输出提醒：

```
⚠️ MSG-002 已挂起 8 天（创建于 2026-02-19），建议优先处理或与发送方确认是否仍需执行。
```

## 发送消息给课程端

如需向课程端发送消息，按 `/mailbox_out` 工作流执行完整的判定+投递流程。

## 注意事项

- **身份隔离**：只处理 `to: 教务材料` 的消息
- **原文不动**：邮箱消息仅在 frontmatter 层面更新状态
- **回复追加**：在消息文件末尾追加 `## 回复` 区块
- **INDEX 必同步**：任何对邮箱文件的增/删/改操作后必须同步更新 INDEX.md
