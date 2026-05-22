# 全局通用规则 (Global Rules)

> 来源：25-26-2 教学材料注意事项 - 总纲 & 执行要点
> 更新：2026-02-24 — 融入 04_Experiment 模板 XML 审查复盘经验：模板目录 TOC hyperlink 结构修复、全文扫描范围控制、run 格式变体包含匹配；追加六条新防御规则与模板维护规范。

## 1. 文件规范
*   **格式**：所有最终提交文件均为 PDF。`generate.py` 默认同时输出 `.docx` + `.pdf`（LibreOffice headless 转换），可用 `--no-pdf` 关闭。
*   **PDF 转换工具**：`scripts/pdf_converter.py`，带 5 次指数退避重试和 60s 超时保护。仅转换最终交付文件（排除教案散页、首页、尾页署名等中间文件）。
*   **链接**：本指南中引用的所有 Kdocs 链接文档均需下载使用（已下载至对应目录）。

## 2. 提交日程
*   **2月4日**：大纲编写。
*   **2月5-6日**：大纲最终版 & 进度表。
*   **2月9日**：前三次教案。
*   **2月25日**：所有纸质版。

## 3. 索引与参考
*   课程目录索引请见 `00_Data_Context/Course_Index.json` (如有)。

## 4. 数据与模板管理 (Data & Template Management)
*   **核心数据源**：所有教学材料生成的源数据（课程信息、教学日历等）统一存储于 `00_Data_Context/course.yaml`。
*   **Schema 2.2 能力**：
    *   **多班级排课**：支持定义多班级 (`classes` 列表)，允许不同班级有不同的排课时间。
    *   **分段排课** (2.2 新增, 2.5 增强)：`classes[].schedule_segments` 支持同一班级在不同周次使用不同节次。`weeks` 支持范围(`"10-13"`)、枚举(`"7,9"`)、混合(`"7,9,11-13"`)三种格式；`period` 支持逗号分隔多时段(`"1-5节, 11-15节"`)；可选 `day` 字段指定上课星期（用于同一周多日上课，如周四+周日）。生成器自动检测多日制模式（calendar 条目数 > 可用周数时激活）。
    *   **周次范围** (2.2 新增)：`classes[].week_range` 定义班级实际上课周次（如 `"10-18"`），生成器自动偏移映射 calendar 内容。
    *   **细化教案**：支持 `lessons` 单元，关联到每周的教学日历。
    *   **教材与考试**：新增 `textbooks` 和 `exams` 结构支持。
    *   **支撑度内嵌** (2.2 新增)：`objectives[].support_level` (H/M/L) 内嵌到每个课程目标中，取代独立的 `course_matrix.yaml`。
    *   **毕业要求映射数组** (2.3 新增)：`objectives[].mappings[]` 替代扁平的 `requirement`/`point`/`support_level`，支持一个课程目标映射多条毕业要求。旧版扁平字段仍向后兼容。
    *   **学情分析** (2.3 新增)：`student_analysis` 顶层可选字段，用于教案首页模板的学情分析区域。
    *   **`exams` 必填约束** (ADR 004)：`exams` 为模板渲染必需字段，即使考查课也必须填写。Schema 会在缺失时自动构造最小空结构（WARNING 级别）。
    *   **停课周声明** (2.4 新增)：`classes[].excluded_weeks`（`list[int]`）声明该班级的停课自然周次（节假日/调课），生成器自动跳过这些周次的教案生成，进度表中显示「节假日停课」并将学时记 0。
    *   **节次时长上限** (2.4 新增)：`classes[].session_time_overrides`（`list[{weeks: str, max_minutes: int}]`）声明指定周次范围的 steps 总时长上限，用于节次变化（如 1-5节→2-5节）导致的课时缩减。生成器按比例压缩各阶段 minutes。
    *   **单班学时语义** (2.4 新增)：`hours.per_class: true` 标注多班级课程（同一内容不同班级顺序开展）的 `hours.total` 表示**单班学时**，而非全部班级总学时之和。
*   **数据审计**：每次修改数据后，请运行 `python scripts/audit_course_data.py` 确保数据完整性。

## 5. 通用 docx 生成规范 (Universal Template Convention)

> 适用于所有生成器（01_Syllabus ~ 06_Presentation）

### 5.1 核心原则：模板即 SSOT

*   **格式唯一来源**：所有输出文件的格式（字体、字号、行距、缩进、合并单元格等）完全由原始模板 `.docx` 决定。
*   **代码只做文本替换**：生成脚本不构造任何格式属性，仅替换占位符文本。
*   **修改格式 = 修改模板**：如需调整输出格式，直接在 Word 中修改模板并保存，重新生成即自动继承。

### 5.2 占位符约定

| 符号 | 用途 | 说明 |
|------|------|------|
| `XXXX` | 通用数据占位 | 代码通过**位置上下文**（表格行列 / 段落前后文关键字）定位并替换 |
| `{{ variable }}` | ❌ **已弃用** | 旧 docxtpl Jinja 语法，新模板不应使用 |
| 硬编码值 | ❌ **禁止** | 模板中不应包含具体课程数据（如专业名、学期等），应全部用 `XXXX` |

### 5.3 生成流程

```
原始模板.docx (含 XXXX 占位符，格式完整)
    ↓ copy ZIP
course.yaml (结构化数据)
    ↓ lxml 解析 document.xml
    ↓ 替换 XXXX → 实际数据
输出.docx (格式与模板 100% 一致)
```

### 5.4 模板维护规范

*   模板文件命名：`XX_Generator/Template_*.docx`
*   所有需要替换的动态内容使用 `XXXX` 标记
*   模板中的静态文本（节标题、固定说明等）保留原文
*   章节内容等重复性区域：保留**一个完整示例**作为克隆模板
*   **模板评论标注**：建议在模板中为每个 `XXXX` 添加 Word 评论(Comment)，说明数据来源和填写规则，便于后续维护

> [!IMPORTANT]
> **模板变更强制 XML 审查序列**
>
> 任何模板的新占位符不得凭经验假设其 XML 结构，**必须**下列审查序列完成后再写代码：
> 1. 解包模板：`zipfile.ZipFile(path).read('word/document.xml')`
> 2. `lxml.etree` 解析，用 `body.iter(w:p)` 扇平扫描全文段落（**用 `iter` 而非 `findall`**）
> 3. 打印每个 XXXX 区域的实际 run 列表：`[r.find(w:t).text for r in p.iter(w:r)]`
> 4. 确认：段落层级（表格单元格内 P0/P1）、run 文本和数量、hyperlink 层级嵌套
> 5. 根据实际结构选择替换策略（见 §5.5 防御规则表）

> [!WARNING]
> **`textutil -convert docx` 陷阱**：macOS `textutil` 转换 `.doc → .docx` 时，**不保留表格 `<w:tbl>` 结构**（表格会被拆为纯段落），导致 XML 引擎无法定位表格。正确做法：**用 Word/WPS 手动打开 `.doc` 并另存为 `.docx`**，或使用 LibreOffice (`soffice --headless --convert-to docx`)。

### 5.5 防御性编程规范 (Defensive Rules)

> [!NOTE]
> **已重构：本节的 50+ 条防呆规范已被提取并下沉到 IDE 原生机制中。**
> 当修改 `course.yaml` 或生成器脚本时，IDE 将通过 glob 模式自动触发以下约束：
> 1. `.agent/rules/rule_xml_template_ops.md`：模板 XML 操作（iter/findall、XXXX 定位等）
> 2. `.agent/rules/rule_xml_data_safety.md`：数据安全防御（缺失兜底、异构兼容、标点叠加等）
> 3. `.agent/rules/rule_data_mapping.md`：数据映射与输出偏好

### 5.6 课程资料规范 (Textbooks & References)

> 来源：Ref_Submission_Req.md §二(一) + Ref_General_Notice.md §1.4

#### （一）选用教材

1.  涉及**马工程教材**的课程**必须**使用马工程教材。
2.  选用**近三年出版**教材，鼓励选用国家级、省级规划教材。
3.  教材**一本**（主教材），须注明完整出版信息。
4.  引用格式（专著 [M]）：`作者. 书名[M]. 出版地: 出版社, 出版年份.`
    *   示例：`斯蒂芬 A.罗斯. 公司理财[M]. 北京: 机械工业出版社, 2017.`
5.  **教材匹配**：教学内容体系与教材章节体系保持一致，一级/二级标题匹配度 ≥ **80%**。

#### （二）参考书目与文献

1.  参考书目**多本**，列出所有推荐参考资料。
2.  书籍引用格式（专著 [M]）：同上教材格式。
3.  期刊文章引用格式（期刊 [J]）：`作者. 题名[J]. 刊名, 年, 卷(期).`
    *   示例：`张三. 交互设计方法研究[J]. 设计学报, 2024, 10(2).`

#### （三）课程网站等支持条件

*   **数据字段**：`course.resources_url`
*   填写课程网站、在线教学平台（如省级一流课程网站、慕课平台等）等支持条件。
*   如无，填写 **"无"**。

### 5.7 多课程兼容策略

*   **标准课程**：含 `semester_config`、`calendar`、`experiments`、`exams` 的完整结构
*   **非标准课程**：如实习指导，Schema 结构完全不同，生成器应逐项检查所需字段后跳过不适用的模块
*   **数据来源**：课程数据统一存放于 `/Users/yamlam/Downloads/2025-2026-2 课程/[课程名]/course.yaml`

### 5.8 跨版本课程目标格式适配规则 (Course Objectives Formatting)

> [!NOTE]
> **已重构：多态渲染逻辑已封装为专属技能。**
> 详细的 `schema_type` 分派、降级渲染逻辑（3列表格/纯段落）和人培交叉校验机制，请通过以下方式调用：
> - 技能名：`curriculum-versioning`
> - 存放路径：`.agent/skills/curriculum-versioning/`

## 6. 用户偏好与协作约定 (User Preferences)

> 详细跨 IDE 协作纪律请参见项目根目录下的 `AGENTS.md`。

### 6.1 文件管理与规范精要
*   **归档不删除**：过时文件移至 `_archived/` 或 `_deprecated/`。
*   **SSOT 优先**：尽量让数据/模板自描述，避免创建需要额外同步的文档。
*   **输出隔离**：不同类型的输出放入各自子目录（教案/实验/考核）。
*   **中文优先**：所有指南、注释、计划、代码注释使用简体中文。
*   **Spec 体系**：每个生成器一份 `Spec_*.md`，全局通用规则在 `Spec_Global.md`。

> [!NOTE]
> 原 §6.3 代码规范、§6.4 数据映射偏好、§6.5 格式内容偏好已迁移至 `.agent/rules/` 中，按需触发。

## 7. 跨工作区同步规范 (Cross-Workspace Sync)

> 教务材料项目 (`教务材料/`) 与课程工作区 (`2025-2026-2 课程/`) 是两个独立目录。
> 前者定义 Schema、模板和生成器；后者存储每门课程的 `course.yaml` 数据。
> 两者必须保持同步，否则生成失败。

### 7.1 新课程接入与审计

> [!NOTE]
> **已重构：新课程接入清单与防冲突策略已封装为标准工作流。**
> 当需接入新课程或进行全量审计时，请直接执行以下工作流：
> - 命令：`/new_course`
> - 路径：`.agent/workflows/new_course.md`

### 7.4 跨项目字段协商协议

> 基于 03_LessonPlan 修复过程中与课程项目 Agent 的两轮协商经验。

当教务项目需要课程工作区提供**新字段**时，遵循以下流程：

1. **分类需求类型**：
   - **索引型/元数据**（`supported_objectives`、`task`、结构化 `teaching_requirements`）→ 直接要求写入 frontmatter/YAML
   - **显示型**（`chapter_title`）→ 课程端直接写入完整的带编号标题（WYSIWYG），生成器不再自动拼接
   - **过程性内容**（教学步骤、课堂详细安排）→ 协商「摘要级索引 vs 运行时提取」

2. **SSOT 权属判定**：
   - 数据的唯一定义位置在课程工作区（如 `scripts/W0X_*.md`）→ 教务侧不可要求全文复制
   - 合理的折中：课程侧提供**精简摘要**（每项 2-3 行），教务侧做格式扩展

3. **同步机制**：
   - 教案索引字段直接在 `course.yaml` 中维护（不经 frontmatter 中转）
   - 教务侧生成器从 `course.yaml` 读取（单一入口，不跨项目读文件）
   - 脚本 frontmatter 保持精简（仅 week/topic/title/hours/objectives/status）

4. **fallback 策略**：
   - 所有新字段必须在生成器中设计 fallback，确保字段缺失时仍可生成基本输出
   - 不可因字段缺失导致生成过程崩溃或输出空白文档

5. **⭐ SSOT 核查（跨项目字段请求的前置步骤）**：
   - 教务侧提出「需要课程侧提供新数据」前，**必须先评估该数据是否已可通过已有字段 + 生成器逻辑推导**（如 `week_range` 偏移已可解决多班映射，无须复制 calendar）。
   - 若要求课程侧写入大量重复内容（如为每个班级复制全量 `calendar` 条目），视为 **SSOT 违规提案**，应转为「生成器升级」任务而非「数据补全」任务。
   - 决策路径：数据在课程侧有唯一真值源 → 教务侧升级生成器读取；数据仅存在于教务侧逻辑 → 教务侧内部实现。

### 7.5 教案数据扩展字段清单（Schema 2.2+）

以下字段为 03_LessonPlan 修复后约定的扩展，由课程工作区负责维护：

| 字段 | 位置 | 必填 | 说明 |
|------|------|:---:|------|
| `supported_objectives` | `calendar[]` | Y | 本周支撑的课程目标引用列表（如 `["知识1", "素质2"]`） |
| `task` | `calendar[]` | Y | 课后作业描述 |
| `teaching_requirements` | `calendar[]` | Y | 支持纯文本或结构化 `{knowledge, ability, quality, method}` |
| `lessons[].steps[]` | `calendar[].lessons[]` | Y | 精简版教学步骤（5 stage x summary + minutes） |
| `lessons[].steps[].ideology` | 仅 stage=讲授 | N | 课程思政融入点 |
| `teaching_method` → 教案继承 | `calendar[]` | Y | 教案 R10-R13 的【教学方法】从此字段继承，无需 step 级重复 |
| `chapter_title` | `calendar[]` | **Y★** | **推荐必填**。大纲章标题、教案 R0 的直接数据源。缺失时回退为 `topic` 原文（不再自动拼接“第X章”） |
| `student_analysis` | 顶层 | N | 学情分析文本，用于教案首页模板 |

### 7.6 objectives 映射格式（Schema 2.3）

```yaml
# 新版 (推荐): mappings 数组，支持一对多
objectives:
  knowledge:
    - index: 1
      desc: "..."
      mappings:
        - requirement: 2 专业知识
          point: 2.2 跨学科知识整合
          support_level: M

# 旧版 (向后兼容): 扁平字段
objectives:
  knowledge:
    - index: 1
      desc: "..."
      requirement: 2 专业知识
      point: 2.2 跨学科知识整合
      support_level: M
```

**校验规则**：`generate.py` 优先读取 `mappings[]`，为空时回退到扁平字段。两种格式不可混用于同一个 objective 条目中。

## 8. 云盘归档命名规范 (Archive Naming Convention)

> 来源：25-26-2 教学材料注意事项 §5 归档编号 + 教务处提交通知
> 适用场景：文档生成后需上传阿里云盘 / 压缩包提交时的文件重命名

### 8.1 命名公式

```
{archive_id}{teacher.name}+{年级}+{专业}[+{班级}]+《{course.name}》+{文档类型}.{ext}
```

| 组成部分 | 数据来源 | 说明 |
|----------|----------|------|
| `archive_id` | `classes[].archive_id` | 班级归档序号，每学期由系部汇总表分配。**不同课程、不同班级有不同序号** |
| `teacher.name` | `teacher.name` | 教师姓名 |
| 年级 | 从 `classes[].name` 解析 | 如 `2024级`、`2023级` |
| 专业 | `course.major` | 如 `数字媒体艺术` |
| 班级 | 从 `classes[].name` 解析 | 如 `影视班`、`游戏班`。per-course 文档在多班时省略 |
| `course.name` | `course.name` | 课程名称，用《》包裹 |
| 文档类型 | 固定文本 | `教学大纲` / `教学进度表` / `教案` / `实验指导书` |

### 8.2 各文档类型规则

| 文档类型 | 粒度 | 班级字段 | 示例 |
|----------|:----:|:--------:|------|
| 教学大纲 | per-course | 单班含、多班省略 | `55林昕+2024级+数字媒体艺术+《信息可视化设计》+教学大纲.docx` |
| 教学进度表 | **per-class** | **必含** | `55林昕+2024级+数字媒体艺术+影视班+《信息可视化设计》+教学进度表.docx` |
| 教案 | per-course（合并版） | 单班含、多班省略 | `55林昕+2023级+数字媒体艺术+影视班+《交互产品开发》+教案.docx` |
| 实验指导书 | per-course | 单班含、多班省略 | `55林昕+2024级+数字媒体艺术+《信息可视化设计》+实验指导书.docx` |

### 8.3 考核材料命名（AB 卷 / 评分标准 / 自查表）

考核材料使用另一套命名体系（来源：25-26-2 教学材料注意事项 §5）：

```
{归档序号}{姓名}+{年级}+{专业}+{课程名称}+{文件类型}
```

文件类型取值：`A卷` / `B卷` / `评分标准（A卷）` / `评分标准（B卷）` / `自查表（A卷）` / `自查表（B卷）`

### 8.4 `classes[].archive_id` 字段约定

*   **存储位置**：`course.yaml` → `course.classes[].archive_id`
*   **数据类型**：`int`（可选）
*   **语义**：班级归档序号，每学期由系部汇总表分配。**不同课程、不同班级有不同序号**
*   **生命周期**：每学期更换。新学期开课前须从系部汇总表获取新序号并更新
*   **缺失处理**：`archive_id` 为空时，向后兼容读取 `teacher.archive_id`；两者均空时，归档命名函数返回 None，生成器 fallback 到旧格式文件名
*   **per-course 多班命名**：拼接所有班级的 `{id}{name}` 前缀（如 `45林昕46林昕+...`）
