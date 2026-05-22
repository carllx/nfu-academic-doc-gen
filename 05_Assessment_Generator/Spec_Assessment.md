# 考核与试卷编写指南 (Spec_Assessment)

> 来源：25-26-2 教学材料注意事项 - 第5, 9, 10节
> 更新：2026-02-22 — 补充生成器实现细节

## 1. 试卷 (AB卷)
*   **重复率**：
    *   考试课：近三年重复率 ≤ 30%。
    *   考查课：近三年 **完全不重复**。
*   **提交**：需预先提交系主任检查。

## 2. 评分标准
*   **规则**：10分对应一个采分点。

## 3. 成绩评定
*   **依据**：《设计学院课程考核成绩评定与分布规范》。
*   **告知**：第一次上课必须告知学生。

## 4. 阅卷与归档
*   **阅卷**：遵循附件1阅卷规范。
*   **封面/评语**：文字类考核需使用指定封面和评语表。
*   **自查**：使用试卷袋自查表进行核对。

## 5. 数据与模板管理 (Data & Template Management)

### 5.1 数据源
*   平时/期末成绩比例必须与 `course.yaml` 的 `assessment_methods` 一致。
    *   **Strict Validation**: `normal_score_ratio + final_score_ratio` 必须严格等于 100%。
    *   **Strict Validation**: `normal_items` 中各分项比例之和必须严格等于 100%。
*   期末试卷结构/题目在 `course.yaml` 的 `exams.final_exam` 中定义。

### 5.2 模板清单 (6 模板)
| 模板 | 格式 | 用途 | 填充逻辑 |
|------|------|------|----------|
| `Template_Exam_Checklist_A.docx` | `.docx` | 命题自查表 A卷 | 课程名称填入表格 row[1] |
| `Template_Exam_Checklist_B.docx` | `.docx` | 命题自查表 B卷 | 同上 |
| `Template_Exam_Paper_A.docx` | `.doc→.docx` | 期末试卷 A卷 | 表头填充（年级/专业/课程名/学期/大题数） |
| `Template_Exam_Paper_B.docx` | `.doc→.docx` | 期末试卷 B卷 | 同上 |
| `Template_Exam_Criteria_A.docx` | `.doc→.docx` | 评分标准 A卷 | 同 Paper 表头填充 |
| `Template_Exam_Criteria_B.docx` | `.doc→.docx` | 评分标准 B卷 | 同上 |

> ⚠️ Paper/Criteria 的 `.doc` 原件已用 `textutil -convert docx` 预转换。原 `.doc` 文件保留备查。

### 5.3 生成器
*   **脚本路径**：`scripts/gen_assessment_xml.py`
*   **统一入口**：`gen_assessment(base_dir, output_dir, context)`
*   **输出目录**：`output/考核材料/`

### 5.4 执行经验
*   Paper/Criteria 模板是纯段落结构（66 个 `<w:p>`，0 个表格），表头信息通过段落索引定位
*   Checklist 模板含 2 个表格（24 行基本信息 + 39 行题目分析），结构较复杂
*   `.doc` 格式不能被 XML 引擎直接处理，必须先转换为 `.docx`
