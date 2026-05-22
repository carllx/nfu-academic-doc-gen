---
description: 新课程接入检查清单——验证 course.yaml 的 Schema 兼容性、学时校验、OBE 合规性和人培交叉校验。
---

# 新课程接入检查 (New Course Onboarding)

当新课程的 `course.yaml` 创建或大幅修改时，按此清单逐项验证。

## 前置条件

- 已获取课程的真实排课信息（周次、节次、教室）
- 已确认适用的人培方案版本

## 检查步骤

### 1. 人培矩阵录入
在对应版本的 `training_plans/training_plan_{version}.yaml` 的 `course_matrix` 中录入人培官方数据（课程名/学分/学时/支撑矩阵）。

### 2. `training_plan_version` 声明
在 `course.yaml` 的 `course:` 节点下显式声明 `training_plan_version: "XXXX"`。

### 3. Schema 版本兼容
对照 `Spec_Global.md` §4 的 Schema 能力列表，确认所有必填字段存在。

### 4. `schedule_time` 准确性
与真实排课系统核对，格式为 `周X N-M节`。

### 5. 学时校验
- `hours.total = hours.theory + hours.practice`
- `∑ calendar[].hours_theory + hours_practice = hours.total`

### 6. `nature` 规范值
取值为：专业必修课 / 专业选修课 / 公共必修课 / 公共选修课 / 实践课程

### 7. `calendar` 完整性
每周必须含 `week` / `topic` / `hours_theory` / `hours_practice`。

### 8. 多班级字段
- 多班级且周次不同 → 设置 `week_range`
- 节次变化 → 设置 `schedule_segments`
- 停课周 → 声明 `excluded_weeks`
- 同内容多班次 → `hours.per_class: true`

### 8.5 教材 TOC 配置（推荐）
- 主教材推荐配置 `textbooks[].toc` 字段（章节目录结构）
- 参考书可选配置
- TOC 数据源：`knowledge/textbook/*/index.md` 中的目录翻译
- `chapter` 键使用 `int`（传统编号）或 `str`（无编号教材如 Refactoring UI）
- `readings` 字段须使用可被 `resolve_chapter_titles()` 自动解析的格式（详见 `rule_data_mapping.md` §3）
- 配置后验证：`resolve_chapter_titles(readings, textbooks)` 返回非原文即为成功

### 9. `exams` 字段
即使考查课也必须填写最小结构（ADR 004）。

### 10. `objectives` 结构
- 必须含 `knowledge` / `ability` / `quality` 三类
- 每项有 `index` / `desc` / `mappings[]`
- `desc` 不得以禁用动词开头（了解/熟悉/理解/掌握）

### 11. `supported_objectives` 覆盖度
汇总全课程周次确认每条目标至少被 1 个周次引用。

### 12. `teacher.team` 语义
协作教师，不含主讲教师本人。单人或无协作时填 `无`。

### 13. `student_analysis`（可选）
教案首页模板所需的学情分析文本。

## 验证命令

// turbo
```bash
# 验证单门课程
/opt/anaconda3/envs/mybase/bin/python scripts/audit_course_data.py --course 课程名
```

// turbo
```bash
# 全量生成并检查输出
/opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 课程名
```

## 完成标志

- `audit_course_data.py` 零 ERROR / 零 CRITICAL
- `generate.py` 输出 DOCX + PDF 无报错
- 输出文档人工抽检格式无异常
