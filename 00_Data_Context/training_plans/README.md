# 多版本人才培养方案数据管理说明

> 创建: 2026-05-14
> 适用专业: 数字媒体艺术 (130508)

## 目录结构

```
training_plans/
├── README.md                              ← 本文件
├── graduation_requirements_2023.yaml      ← 23版毕业要求（schema_type: none）
├── graduation_requirements_2024.yaml      ← 24版毕业要求（schema_type: coarse）
├── graduation_requirements_2025.yaml      ← 25版毕业要求（schema_type: detailed）
├── training_plan_2023.yaml                ← 23版人培数据
├── training_plan_2024.yaml                ← 24版人培数据
└── training_plan_2025.yaml                ← 25版人培数据
```

## Schema 类型说明

| `schema_type` | 含义 | 毕业要求结构 | 支撑矩阵 | 审计行为 |
|:---:|------|-------------|---------|---------|
| `none` | 该版本无毕业要求体系 | 无 | 无 | 跳过人培校验，输出 `[INFO]` |
| `coarse` | 仅大类，无观测点 | 9 条大类要求 | 仅打 ✓，无 H/M/L | 按大类编号校验 |
| `detailed` | 有观测点细分 | 9 大类 × 27 观测点 | H/M/L 三级支撑 | 按观测点 pid 精确校验 |

## 版本与年级对应关系

| 年级 | 适用人培版本 | 毕业要求特征 |
|:---:|:---:|-------------|
| 2022 级 | ⚠️ 未知（无源文件） | — |
| 2023 级 | 2023 版 | 无毕业要求体系，仅有培养规格 |
| 2024 级 | 2024 版 | 9 条粗粒度要求，无观测点 |
| 2025 级 | 2025 版 | 9 大类 × 27 观测点，H/M/L 支撑 |

## 课程引用方式

在 `course.yaml` 中通过以下字段声明适用的人培版本：

```yaml
course:
  training_plan_version: "2024"     # 适用的人培版本（SSOT）
  training_plan_track: "本科"       # 本科 / 专升本（默认本科，可省略）
```

审计脚本 (`audit_course_data.py`) 根据此字段自动加载对应版本的 YAML。

## 数据来源

| 版本 | 原始文件 | 存放位置 |
|:---:|---------|---------|
| 2023 | `23 级-设计学院-本科(含有专升本).pdf` | `_archived/南方人培_源文件/` |
| 2024 | `24级-设计学院-本科(含有专升本).pdf` | `_archived/南方人培_源文件/` |
| 2025 | `数艺-25本科-人培（文字）.docx` + `（表格）.xlsx` | `_archived/` |

## 维护规则

1. **新增课程**：须先在对应版本的 `training_plan_XXXX.yaml` 的 `course_matrix` 中录入。
2. **新增版本**：须同时创建 `graduation_requirements_XXXX.yaml` 和 `training_plan_XXXX.yaml`，并指定 `schema_type`。
3. **向后兼容**：旧版 `course.yaml` 缺失 `training_plan_version` 时，审计脚本尝试从 `classes[0].name` 提取年级，再 fallback 到最新版本 + `[WARN]`。
