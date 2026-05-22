# 同步指令：与教务材料项目 Schema 2.2 对齐

> **发起方**：教务材料项目 (2026-02-23)
> **目标**：确保本工作区所有课程数据与教务材料项目的 Schema 2.2、生成器和指导文件保持一致

## 背景

教务材料项目刚完成了一轮重大审计修复，涉及以下变更：

1. **Schema 升级到 2.2** — `objectives` 新增 `support_level` 字段 (H/M/L)
2. **`course_matrix.yaml` 废弃** — 支撑度数据已内嵌到各课程 `course.yaml` 的 `objectives[].support_level`
3. **多班级排课增强** — 新增 `classes[].week_range` 和 `classes[].schedule_segments` 字段
4. **`generate.py` 合规校验重写** — 不再依赖外部 `course_matrix.yaml`，直接从 `objectives` 校验

## 你需要执行的任务

### 任务 1：审查所有 course.yaml 的 Schema 合规性

逐门课程检查以下字段，参照 `/Users/yamlam/Downloads/教务材料/docs/Handover_Course_Data_Audit.md` 中的完整清单：

```
对每门课程 (信息可视化, 交互产品开发, 实习指导 等)：
□ objectives 每项是否都有 support_level (H/M/L)
□ schedule_time 是否与真实排课系统一致 (格式: 周X N-M节)
□ hours.total == hours.theory + hours.practice
□ ∑ calendar[].hours_theory == hours.theory
□ ∑ calendar[].hours_practice == hours.practice
□ 多班级是否需要 week_range / schedule_segments
□ exams 字段是否存在 (即使考查课也需最小结构)
```

**信息可视化和交互产品开发的 `support_level` 已由教务材料项目添加完毕，无需重复。** 仅需检查是否有其他课程遗漏。

### 任务 2：验证生成器兼容性

```bash
cd /Users/yamlam/Downloads/教务材料
/opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 信息可视化
/opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 交互产品开发
# 对其他课程也执行同样操作
```

期望输出：
- `✅ Course supports N graduation points: {...}` — 无 Compliance Warning
- 所有文档 `✨ Saved` — 无 ❌ 报错

### 任务 3：更新本项目文档

如果本工作区有 README、规范文件或 agent 指令文件涉及以下内容，请同步更新：

| 旧内容 | 新内容 |
|--------|--------|
| 引用 `course_matrix.yaml` | 改为 `objectives[].support_level` 内嵌 |
| Schema 2.1 | Schema 2.2 |
| `schedule_time` 无校验说明 | 必须与真实排课核对 |
| objectives 字段列表 `{index, desc, point}` | `{index, desc, point, support_level}` |

### 任务 4：交叉检查排课数据

对每门课程的 `classes[].schedule_time` 进行以下检查：
1. 星期几是否正确（必须与教务系统一致）
2. 节次范围是否正确
3. 如有多班级不同周次上课，是否已设置 `week_range`
4. 如有同一班级不同周次节次变化，是否已设置 `schedule_segments`

### 任务 5：教案数据字段同步（2026-02-23 新增）

> 基于 03_LessonPlan 修复中与课程项目 Agent 的协商结果。详见 `Spec_Global.md` §7.4-7.5。

为每门课程的 `course.yaml` 补充以下教案专属字段（由课程侧在 frontmatter 中维护，通过 `sync_syllabus.py` 同步）：

```
对每门课程的 calendar[] 中每周：
□ supported_objectives 是否存在（引用全局 objectives 的索引，如 ["知识1", "素质2"]）
□ task 是否存在（课后作业描述）
□ teaching_requirements 是否已结构化为 {knowledge, ability, quality, method}
□ lessons[].steps[] 是否包含 5 个 stage（复习/导入/讲授/实践/小结）
□ lessons[].steps[] 的讲授 stage 是否含 ideology（思政融入点）
□ ∑ steps[].minutes ≈ 该周总学时（分钟）
```

**字段协商协议**：
- **索引型**字段（`supported_objectives`、`task`）→ 直接写入 frontmatter
- **过程性**字段（`steps[]`）→ 仅写**精简摘要**（每 stage 2-3 行 summary + minutes），不复制脚本全文
- **派生型**字段（`chapter_title`）→ 不存储，由生成器拼接 `第X章 {topic}`

## 关键参考文件

| 文件 | 路径 | 用途 |
|------|------|------|
| **自审指南** | `/Users/yamlam/Downloads/教务材料/docs/Handover_Course_Data_Audit.md` | 完整审查清单和已知陷阱 |
| **全局规范** | `/Users/yamlam/Downloads/教务材料/00_Data_Context/Spec_Global.md` | Schema 2.2 定义、防御性规范、跨工作区同步 §7 |
| **毕业要求** | `/Users/yamlam/Downloads/教务材料/00_Data_Context/graduation_requirements.yaml` | point 字段的合法值参考 |
| **已归档矩阵** | `/Users/yamlam/Downloads/教务材料/00_Data_Context/_archived/course_matrix.yaml` | 旧数据参考（已废弃） |
| **教案规范** | `/Users/yamlam/Downloads/教务材料/03_LessonPlan_Generator/Spec_LessonPlan.md` | 教案 16 行映射规范和子节格式 |

## 完成标准

- [ ] 所有课程 `course.yaml` 通过 Schema 2.2 合规检查
- [ ] 所有课程 `generate.py` 运行无 Warning 无 Error
- [ ] 本项目文档中无 `course_matrix.yaml` 的过时引用
- [ ] 排课数据经过真实核对确认
- [ ] 教案字段（`supported_objectives`/`task`/`steps[]`/结构化 `teaching_requirements`）已同步

