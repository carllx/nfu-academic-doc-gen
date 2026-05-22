---
name: curriculum-versioning
description: 多版本人培方案（2023/2024/2025）的课程目标渲染适配与审计校验。当涉及 schema_type（none/coarse/detailed）分派、课程目标表格降级、人培交叉校验时触发。
---

# 跨版本课程目标适配引擎

本技能封装了教务材料生成系统中最复杂的业务逻辑：根据不同年级适用的人才培养方案版本，动态调整大纲和教案中「课程目标」的呈现格式。

## 适用场景

- 修改或新建 `gen_syllabus_xml.py` / `gen_lessonplan_xml.py` 中的课程目标渲染逻辑
- 新增人培方案版本（如 2026 版）
- 调试 `audit_course_data.py` 的 `[TRAINING_PLAN]` 校验
- 理解 `schema_type` 分派机制

## 版本映射总览

| 适用年级 | 人培版本 | `schema_type` | 课程目标格式 |
|:---|:---|:---|:---|
| 25级普本、**23级专升本** | 2025版 | `detailed` | **4列表格**：维度名、描述、毕业要求、观测点全量输出 |
| 24级普本、**22级专升本** | 2024版 | `coarse` | **3列表格**：物理删除最后一列（观测点） |
| 20-23级普本、20-21级专升本 | 2023版及以前 | `none` | **纯文字段落**：删除整个表格，渲染为段落组 |

> **专升本映射规则（教务行政要求，2026-05-15 确认）**：
> 专升本年级 + 2 = 对标普本年级。即 22级专升本 → 24级普本人培，23级专升本 → 25级普本人培。
> 虽然专升本有独立的人培文件（仅含"培养规格"，无毕业要求体系和课程支撑矩阵），
> 但教务要求专升本课程**对标本科人培的毕业要求体系**编写大纲。
> 源文件位置：`00_Data_Context/_archived/南方人培_源文件/`

## 分派入口

`schema_type` 存储于 `training_plans/graduation_requirements_{version}.yaml` 的顶层字段。生成器通过以下路径获取：

```
course.yaml → course.training_plan_version → graduation_requirements_{version}.yaml → schema_type
```

## 渲染逻辑

详见 [rendering_logic.md](references/rendering_logic.md)

主要函数：
- `_remove_table_last_column(table)`：`coarse` 模式，物理删除 `<w:tbl>` 最后一列
- `_build_objectives_paragraphs(objectives, insert_point)`：`none` 模式，删除表格并构建段落组

## 审计逻辑

详见 [audit_logic.md](references/audit_logic.md)

`audit_course_data.py` 的 `[TRAINING_PLAN]` 级别根据 `schema_type` 分派校验粒度：
- `detailed`：精确到观测点名称逐条比对
- `coarse`：仅校验大类编号
- `none`：跳过人培交叉校验

## 段落式格式示例（`schema_type: none`）

```
二、课程目标
（一）知识目标
1. 了解包装设计的定义与发展背景；
2. 掌握包装设计的基本任务、构成要素与设计原则；
（二）能力目标
1. 具备综合分析与方案设计能力...
```

## 关键约束

- `objectives[].mappings[]` 中的毕业要求编号和观测点**必须**与对应版本 YAML SSOT 精确匹配
- `schema_type` 决定渲染路径和审计粒度——两者必须一致
- 新增人培版本时须同时更新渲染逻辑和审计逻辑
