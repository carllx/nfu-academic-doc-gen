# 使用工作流指南 (Workflow)

本文档面向 **教师** 与 **助教**，指导如何使用本系统自动化生成教学材料。

## 阶段一：数据准备 (Data Preparation)

### 1. 定位课程目录
找到您的课程文件夹，例如：
`2025-2026-2 课程/交互产品开发/`

### 2. 填写 `course.yaml`
这是最关键的一步。所有文档的内容都来自这里。
*   **基础信息**：课程名、代码、学分、性质（须为规范 5 类之一）。
*   **班级信息** (`classes`)：定义所有授课班级及其上课时间。
*   **教学日历** (`calendar`)：
    *   **简要模式**：仅填写周主题 (`topic`)、内容 (`content`)、作业。
    *   **详细模式**（推荐）：在 `lessons` 中定义每节课的教学目标与步骤（用于教案）。
    *   **大纲扩展字段**：`teaching_requirements`、`focus`、`difficulty`、`ideology`、`teaching_method`（用于大纲章节）。
*   **实验项目** (`experiments`)：如有实验，需详细列出项目名称、学时、类型。
*   **教材与学期** (`textbooks`, `semester_config`)：填写教材信息与学期开始日期。
*   **考试配置** (`exams`)：**必填**，即使是考查课也必须填写。
*   **课程目标** (`objectives`)：分为知识/能力/素质三类，每项使用 `mappings` 数组映射到毕业要求观测点。**编号必须与人培方案矩阵精确匹配**。
*   **学情分析** (`student_analysis`)：可选字段，用于教案首页模板。
*   **课程性质** (`nature`)：合法值为 `专业必修课` / `专业选修课` / `公共必修课` / `公共选修课` / `成长必修课`

> **Tip**: 参考 `docs/Data_Dictionary.md` 查看完整字段定义。
> **Check**: 填写完成后运行 `python scripts/audit_course_data.py --root "课程根目录"` 进行数据审计。脚本自动加载 `training_plan_2025.yaml` 进行人培交叉校验。
> 审计输出级别：`[SCHEMA]` = 结构错误、`[TRAINING_PLAN]` = 人培合规差距、`[WARN]` = 业务警告、`[INFO]` = 参考信息。

> [!IMPORTANT]
> **评分项命名规范 (ADR 005)**：`normal_items.name` 格式为 `章节测试N` 或 `命题测试N`。`desc` 必须以 `对应实验N「实验名称」。考核要求：…` 格式开头。


## 阶段二：规范检查 (Spec Check)

在生成之前，建议快速浏览各生成器目录下的 `Spec_*.md` 文件。
例如，打开 `01_Syllabus_Generator/Spec_Syllabus.md`，确认：
*   最新的 OBE 目标写法是否变更？（禁用动词：了解/熟悉/理解/掌握）
*   学时分配是否符合人才培养方案？（参考 `training_plan_2025.yaml` 的 `course_matrix`）
*   观测点命名是否与 `graduation_requirements.yaml` 精确一致？
*   课程性质是否使用规范 5 类？
*   平时成绩各项比例之和是否严格等于平时总占比 (normal_score_ratio)？（**切勿被模板示范的 100 分误导**）

## 阶段三：运行生成 (Execution)

```bash
# 生成指定课程的全部文档（默认 DOCX + PDF）
python scripts/generate.py --course "交互产品开发"

# 仅输出 DOCX（跳过 PDF 转换）
python scripts/generate.py --course "交互产品开发" --no-pdf
```

系统将：
1.  读取 `course.yaml`。
2.  加载原始模板（`Syllabus.docx` 等）。
3.  通过 XML 引擎替换 `XXXX` 占位符为实际数据。
4.  在课程目录下生成 `Output` 文件夹，包含归档格式命名的文档：
    *   `{archive_id}{教师}+{年级}+{专业}+《{课程}》+教学大纲.docx`
    *   `{archive_id}{教师}+{年级}+{专业}+{班级}+《{课程}》+教学进度表.docx`
    *   `教案_第X周_xxx.docx` (分周版) + `...教案.docx` (归档命名合并版)
5.  **默认同步 PDF 转换**：通过 LibreOffice headless 将最终交付文件转换为 PDF（排除散页等中间文件）。

## 阶段四：人工复核 (Human Review)

虽然自动化能完成 90% 的工作，但 **人工复核是必须的**。
请打开生成的 Word 文档和 PDF，检查：
*   **排版**：章节段落格式是否与原始模板一致？PDF 与 DOCX 是否一致？
*   **逻辑**：自动生成的日期是否遇到节假日需要调整？
*   **签字**：打印后，记得手写签名。

### 自动化验证
```bash
# 验证大纲结构（表格行数、vMerge、XXXX 残留、Jinja 残留）
python scripts/verify_syllabus.py "Output/2025-2026-2_教学大纲_xxx.docx"
```

## 阶段五：故障排查 (Troubleshooting)

### 1. 文件打不开 ("Word experienced an error")
通常是 XML 损坏导致的。
*   **检查**: 确认模板 `.docx` 本身可以正常打开。
*   **排查**: 运行 `verify_syllabus.py` 检查表格结构和 vMerge 完整性。

### 2. 输出中有 `XXXX` 残留
代码未成功定位并替换某个占位符。
*   **常见原因**: Word 将 `XXXX` 拆分到多个 `<w:r>` 元素中（跨 run 分裂）。
*   **解决**: 在模板中删除该 XXXX 后重新输入，或在代码中对该段落先调用 `_merge_runs()`。

### 3. 输出中有 `{{ }}` 残留
模板仍包含旧的 Jinja 变量。当前方案已弃用 docxtpl。
*   **解决**: 在模板中将所有 `{{ variable }}` 替换为 `XXXX`，并更新代码中的替换逻辑。

### 4. 勾选框/课程性质显示异常
*   确认 `course.yaml` 中 `nature` 值为规范 5 类之一。
*   当前使用 Unicode ☑/☐ 字符，不需要 Wingdings 字体。

### 5. PDF 中 logo 图片变形（压扁/拉伸）
*   **根因**：模板中使用 VML (`v:shape`) 格式嵌入图片，LibreOffice headless 不支持 VML 负裁剪参数。
*   **检查**：解包 docx → 检查 `word/document.xml` 中是否存在 `v:shape` + `v:imagedata`。
*   **修复**：运行 `/tmp/fix_vml_logo.py` 将 VML 替换为 DrawingML (`wp:inline` + `pic:pic`)。修复后需重新生成所有文档。
*   **预防**：新模板的图片**必须**使用 DrawingML 格式嵌入，禁止 VML。详见 `Spec_Global.md §5.5`。

## 阶段六：模板维护 (Template Maintenance) - 仅限管理员

### 1. 修改输出格式
直接在 Word 中修改原始模板（如 `Syllabus.docx`），调整格式后保存。重新运行生成即可。
**无需修改代码** — 模板即 SSOT。

### 2. 添加新数据字段
1. 在模板相应位置添加 `XXXX` 占位符。
2. 在 `course_schema.py` 中添加对应字段定义。
3. 在生成脚本中添加替换逻辑（通过位置上下文定位 XXXX）。

### 3. 引入新模板
为新文档类型创建 Generator 目录（如 `07_xxx_Generator/`），遵循通用规范（参见 `Spec_Global.md` §5）。

---

## 阶段七：跨 Agent 协作 (Cross-Agent Collaboration)

教务材料端与课程工作区端通过**共享邮箱**协作。邮箱目录：`/Users/yamlam/Downloads/cross_agent_mailbox/`。

### 1. 修改请求的边界判定

收到修改请求时，先执行 `/mailbox_out`（或 `/boundary_check`）判定归属：

| 归属 | 处理方式 |
|:----:|:---------|
| 🟢 教务端 | 直接修改本项目代码/模板/规范 |
| 🔵 课程端 | 生成 MSG 任务单投递到共享邮箱 |
| 🟡 双端协同 | 先完成教务端准备 → 再发 MSG |

### 2. 查收共享邮箱

执行 `/mailbox_in` 查看来自课程端的待处理消息，处理完毕自动归档。

### 3. 关键约束

- **严禁**直接修改课程工作区文件（`Architecture.md §5.3`）
- 每次邮箱操作后**必须同步** `INDEX.md`
- MSG 必须自包含、有据可依、可验证

### 4. 归档输出（上传云盘）

归档命名已集成到生成器中，生成的文档自动采用 `Spec_Global.md §8` 格式命名：

1. 确认 `course.yaml` 中每个班级的 `classes[].archive_id` 已填写（每学期由系部汇总表分配）
2. 运行 `python scripts/generate.py --course "课程名"` 即可获得归档命名的文档 + PDF 副本
3. PDF 默认自动生成，无需手动转换。如需关闭可加 `--no-pdf`
