# 实习指导生成器规范 (Internship Generator Spec)

> 来源：25-26-2 学期数字媒体艺术实习指导重构架构

本规范定义了 `07_Internship_Generator` 模块的底层模板设计准则和数据流转要求。

## 1. 架构定位
由于“实习指导”类课程属于非标准课程，其数据结构与教学周历（`calendar`）、实验（`experiments`）截然不同。因此，系统设立独立的 `InternshipSchema`（详见 `scripts/course_schema.py` 与 `docs/Data_Dictionary.md`）并在本目录下统一定制相关模板，确保与 `04_Experiment_Generator` 等模块完全隔离。

## 2. 模板清单与映射关系

本生成器目前维护以下三个 Word (`.docx`) 模板，使用纯 `python-docx` 的底层 XML 库（`docx_engine.py`）作为渲染引擎（**注：已废弃早期的 `docxtpl`**）：

### 2.1 实习分散申请表
- **模板文件**：`templates/Template_Internship_Decentralized.docx`
- **数据源**：`course_internship.yaml` -> `students` 数组每一项
- **注入变量**：
  - **基础信息**：`student_name`, `student_id`, `class_name`, `student_phone`, `student_email`
  - **单位信息**：`base_name`, `base_address`, `enterprise_teacher`, `enterprise_phone`
  - **实习详情**：`intern_start_end`
  - **签署日期**：`decentralized_apply_student_date`, `decentralized_apply_school_date`, `decentralized_apply_enterprise_date`

### 2.2 实习巡查记录表
- **模板文件**：`templates/Template_Internship_Inspection.docx`
- **数据源**：`course_internship.yaml` -> `students` 数组中的每一项
- **注入变量**：
  - **基础信息**：`base_name`, `college`, `major`, `class_name`, `student_name`, `position`, `sequence_number`
  - **实习详情**：`intern_content` (支持多行文本), `inspect_year`, `inspect_month`, `inspect_day`
  - **考核得分**：`score_safety`, `score_attendance`, `score_learning`, `score_teamwork`, `score_attitude`, `score_task`, `score_suitability`, `score_total`
  - **总结评语**：`teacher_advice` (支持多行文本), `teacher_signature`

### 2.2 实习巡查统计表
- **模板文件**：`templates/Template_Internship_Stats.docx`
- **数据源**：`course_internship.yaml`
- **动态表格规则**：
  - 代码通过克隆（`clone_table_row`）生成学生的统计行。
  - **消除歧义**：“指导老师”一列统一读取 `global.school_teacher` 而非 `enterprise_teacher`。
  - **高亮机制**：当前生成的学生所在的那一行，其底层 XML 将被注入 `<w:b/>` 标签进行全局加粗。

## 3. 防弹渲染规则 (Anti-Fragility Rules)

为了防止严格的 OOXML 解析器（MS Word）在渲染后发生“文件损坏”或版面错位崩坏，任何上游调用生成脚本的端必须严格遵守以下预处理要求：

### 3.1 碎片化标签自动缝合 (XML Run Merge)
由于 Word 在保存时经常会将占位符 `{{ xxx }}` 打散在多个 `<w:t>` 碎片中，`gen_internship_xml.py` 必须在字符串替换前调用 `merge_runs(p)` 将同一段落的文本强制黏合，防止变量漏填。

### 3.2 自动软回车替换 (Soft Line Breaks)
早期的 `docxtpl.RichText` 经常引发标签嵌套非法已被彻底废弃。现阶段，`docx_engine.py` 里的 `replace_jinja_tag` 会在底层检测到文本含有 `\n` 时，自动利用 `set_run_text` 在 XML 里生成 `<w:br/>` 换行标签。

### 3.3 布局锁死策略 (Fixed Layout)
`Template_Internship_Stats.docx` 的表格在底层通过强制赋予 `w:tblLayout="fixed"` 与精确约束的 `w:tblGrid` 实现列宽锁死。修改模板时，强烈建议不要用外部工具（如 LibreOffice）随意拉扯表格，以防导出 PDF 时“序号”等窄列被非正常拉伸。

### 3.4 隐形边框渲染拦截 (Invisible Border Bug)
在将申请表转换至 PDF 时，由于 LibreOffice headless 默认对无显式边框设置的表格单元格渲染继承自 `Table Grid` 样式的黑框，特别是签署日期处的局部排版表格。在修改模板时，应务必在 XML 层面针对此类单元格彻底注入 `<w:tcBorders><w:top w:val="none"/>...` 或在生成脚本中清理，确保黑框被完全抑制。

## 4. 模板与数据管理
1. **数据源约束 (SSOT)**：`course_internship.yaml` 是唯一数据源 (Single Source of Truth)。早期的 `convert_csv_to_yaml.py` 脚本因存在数据覆盖风险已被归档至 `scripts/_archived/`。任何手动填写或扩写的数据均应直接在 YAML 中维护。如需额外提取新列，请确保使用增量合并而非直接覆盖。
2. **数据扩写**：如学生的 `intern_content` 字数过少，**严禁在提取或生成脚本中写死自动扩充逻辑**。必须直接修改并维护在 YAML 数据源中。
3. **编辑模板**：优先直接修改 `templates/` 下的 `.docx` 文件，**切勿使用 WPS 保存复杂格式**，强烈建议使用原版 Microsoft Word 编辑。若遇结构大幅调整，请参考根目录下的 `.agent/skills/docx/SKILL.md`，使用 unpack/pack 工具链安全编辑。

## 5. 运行生成
只要课程根目录存在 `course_internship.yaml`，即会触发实习材料独有的并行管线，无需额外标志：
```bash
python scripts/generate.py --course "实习指导"
```
系统会自动调用 `07_Internship_Generator/gen_internship_xml.py` 并进行批量 PDF 转换。
