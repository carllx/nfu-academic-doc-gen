---
description: 更新各生成器目录下的 Spec_*.md 文件，使其与当前 Schema 和生成器代码保持一致。
---

# 更新 Spec 规范文件

当 Schema 变更、生成器代码改造或新增数据流后，按此工作流同步所有 Spec 文件。

## 1. 发现所有 Spec 文件

不假设固定列表，动态查找：

// turbo
```bash
find /Users/yamlam/Downloads/教务材料 -maxdepth 2 -name "Spec_*.md" | sort
```

## 2. 加载上下文

更新 Spec 前须先读取"法律"（Schema）和"地图"（架构文档）：

- 读取 `scripts/course_schema.py` — 当前数据模型
- 读取 `docs/Architecture.md` — 整体设计意图
- 读取 `docs/Data_Dictionary.md` — 字段语义定义

## 3. 逐文件检查与更新

对步骤 1 发现的每个 Spec 文件，执行以下检查：

### 3.1 标题与来源
- 标题清晰（如 `# 教学进度表编写指南 (Spec_Schedule)`）
- 保留原始 `> 来源：25-26-2 ...` 引用块

### 3.2 术语一致性
- 确认字段路径与 Schema 一致（如 `hours.total` 非 `total_hours`）
- 确认评分体系命名与 ADR 005 一致（`章节测试N` / `命题测试N`）
- 确认 `textbooks[].toc` 和 `resolve_chapter_titles()` 相关描述存在（Phase 2d+）
- 确认 `calendar[].readings` 的解析增强链路有记录

### 3.3 数据与模板管理章节
- **必须存在**：每个 Spec 须包含数据源与模板管理相关章节
- 内容须链接到相关 Schema 字段（如"字段 `calendar` 控制此区域"）
- 提供该生成器的专属验证命令

### 3.4 新增功能同步检查
检查以下 Phase 2 新增能力是否已在 Spec 中记录：

| 生成器 | 新增能力 | Spec 中应记录的位置 |
|--------|----------|---------------------|
| 大纲 | 参考教材引用行（4c′ 段落） | §5 教学内容与要求 |
| 教案 | R7 resolve 增强 | §3.3 row[7] 数据源说明 |
| 进度表 | 列4 教材引用短格式摘要 | §2.3 列4 填写规则 |

## 4. 同步 Architecture

- 如发现步骤 1 中有 Spec 对应的生成器未列入 `docs/Architecture.md`，须补充

## 5. 验证

// turbo
```bash
cd /Users/yamlam/Downloads/教务材料 && /opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 信息可视化 --no-pdf 2>&1 | tail -5
```
