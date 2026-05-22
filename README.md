# Teaching Materials Automation (TMA)

## 项目简介
本项目旨在通过 **“领域驱动 (Domain Driven)”** 的方式，实现高校教学材料的自动化生成。通过将结构化的课程数据 (`course.yaml`) 与标准的 Word 模板 (`.docx`) 结合，自动生成符合 2025-2026-2 学期规范的教学文档。

## 核心特性
*   **单一数据源**：所有文档基于同一份 `course.yaml` 生成，确保数据一致性。
*   **Schema 2.5**：支持**多班级排课**、**停课/调课自适应**、**OBE 目标映射数组**、**班级归档序号**与**试卷结构定义**。
*   **XML 直操模板**：通过 `lxml` 直接操作 Word XML，深克隆保全 100% 原始格式（已弃用 docxtpl/Jinja2）。
*   **进度表动态行数**：自动根据 `week_range` 实际周数增删表格行，不再固定 18 行。
*   **领域驱动**：按输出成果（大纲、进度表、教案等）组织生成器包。
*   **规范集成**：每个生成器包内含对应的编写规范 (`Spec_*.md`)。
*   **云盘归档命名**：内置归档命名规范（Spec_Global §8），支持按教务汇总表格式自动重命名。
*   **双格式输出**：默认同时输出 `.docx` + `.pdf`（LibreOffice headless 转换），支持 `--no-pdf` 跳过。

## 目录结构
```text
/
├── 00_Data_Context/        # 数据上下文
│   ├── References/         # 原始参考文件 (Markdown & PDF)
│   ├── Course_Index.json   # 课程数据索引
│   └── Spec_Global.md      # 全局通用规范
├── 01_Syllabus_Generator/  # [生成器] 教学大纲
├── 02_Schedule_Generator/  # [生成器] 教学进度表
├── 03_LessonPlan_Generator/# [生成器] 教案
├── 04_Experiment_Generator/# [生成器] 实验材料 (指导书/报告/认定表)
├── 05_Assessment_Generator/# [生成器] 考核材料 (试卷/分析表)
├── 06_Presentation_Generator/ # [生成器] PPT 课件
├── .agent/workflows/       # Agent 工作流
│   ├── mailbox_out.md      # 跨项目边界判定 + MSG 投递
│   ├── mailbox_in.md       # 共享邮箱收件处理
│   └── ...                 # regenerate_all, update_docs 等
├── docs/                   # 项目文档 (架构/工作流/数据字典/MSG 任务单)
├── scripts/                # 核心工具链
│   ├── generate.py         # [核心] 全量文档生成脚本
│   ├── docx_engine.py      # [核心] 通用 XML 操作引擎
│   ├── course_schema.py    # 数据模式定义 (Pydantic)
│   ├── gen_syllabus_xml.py # 大纲生成器
│   ├── gen_schedule_xml.py # 进度表生成器
│   ├── gen_lessonplan_xml.py # 教案生成器
│   ├── gen_experiment_xml.py # 实验材料生成器
│   ├── gen_assessment_xml.py # 考核材料生成器
│   ├── pdf_converter.py      # PDF 转换工具 (LibreOffice headless)
│   ├── audit_course_data.py  # 数据审计 + 人培交叉校验
│   └── utils/              # 工具库 (日期计算等)
└── README.md               # 本文件
```

> **跨 Agent 共享邮箱**：`/Users/yamlam/Downloads/cross_agent_mailbox/` —— 教务材料端与课程工作区端的统一消息索引与任务委托通道。

## 快速开始 (Quick Start)

### 1. 准备环境
确保安装 Python 3.8+ 及必要的依赖：
```bash
pip install pyyaml pydantic lxml python-docx docxcompose openpyxl
```

### 2. 准备数据
在 `00_Data_Context/` 目录下，确保 `course.yaml` 存在且数据完整。
数据结构由 `scripts/course_schema.py` 定义。

### 3. 数据审计 (Audit)
验证 `course.yaml` 的数据完整性与人培合规性：
```bash
# 审计指定课程
python scripts/audit_course_data.py --course 交互产品开发

# 全量审计
python scripts/audit_course_data.py --root "/Users/yamlam/Downloads/2025-2026-2 课程"
```

### 4. 一键生成 (Generation)
运行全量生成脚本，自动产出大纲、进度表和分周教案：
```bash
# 生成《交互产品开发》的所有文档
python scripts/generate.py --course "交互产品开发"

# 生成《信息可视化》的所有文档
python scripts/generate.py --course "信息可视化"

# 仅输出 DOCX（跳过 PDF 转换）
python scripts/generate.py --course "信息可视化" --no-pdf
```

文档将输出至：`[Course_Dir]/Output/`（默认同时生成 `.docx` + `.pdf`）

## 规范与参考
所有原始的 `.docx` 和 `.pdf` 规范文件已归档至 `00_Data_Context/References`，并转换为 Markdown 格式以便检索。

## 维护者
*   **Yam Lam**
*   **Antigravity Agent**

## 更新日志
*   **2026-02-16 (Automation)**: 
    *   在课程目录下生成 `Output` 文件夹，包含归档格式命名的文档：
    *   `{archive_id}{教师}+{年级}+{专业}+《{课程}》+教学大纲.docx`
    *   `{archive_id}{教师}+{年级}+{专业}+{班级}+《{课程}》+教学进度表.docx`
    *   `教案_第X周_xxx.docx` (分周版) + 归档命名合并版
    *   实验指导书、考核材料 (A/B卷、评分标准、自查表)格式标准化。
*   **2026-02-16 (Schema 2.1)**: 新增教材管理、学期日期配置、期末试卷结构定义。
*   **2026-02-18 (Hybrid & Safe Mode)**:
    *   **混合生成模式**: 结合 Jinja2 模板与 python-docx 编程模式，解决复杂表格生成问题。
    *   **上下文隔离**: 修复了多文档生成时的数据污染问题。
    *   **安全模式**: 默认启用 Safe Mode (纯文本降级)，确保生成的 Word 文档在任何环境下均可打开。
    *   **模板增强**: 新增 `create_syllabus_template_v2.py`，支持 `safe_replace` 格式保留技术。
*   **2026-02-20 (Schema 2.2 / 考核规范)**:
    *   **4实验模型规范化**: 确立“4实验 = 3平时实验 + 1期末综合项目”为课程标准结构。
    *   **指导文件更新**: 更新 `Spec_Global.md`、`Spec_Experiment.md`、`Spec_Syllabus.md`。
    *   **数据字典补全**: `Data_Dictionary.md` 补充 `attendance_ratio` 字段说明及 Schema 校验规则。
    *   **模板对齐**: `00_Data_Context/course.yaml` 更新为4实验默认结构。
*   **2026-02-22 (批注审核 R2 / ADR 004-005)**:
    *   **`generate.py` 修复**: 启用 `fill_tables_programmatically` 动态填充评分表实验行；课程性质勾选框改为不换行；新增 `doc.init_docx()` 兼容 `docxtpl >= 0.20`。
    *   **`Spec_Syllabus.md` 重写**: 整合 `note1.md` OBE 规范和 37 条最新批注，重构 §5 评分体系。
    *   **Schema 强化 (ADR 004)**: `exams` 添加兜底 `root_validator`（缺失时自动构造空结构）。
    *   **命名规范 (ADR 005)**: `AssessmentItem.name` 统一为 `章节测试N`/`命题测试N`；`desc` 强制关联 `对应实验N`。
    *   **审计增强**: `audit_course_data.py` 新增 exams 存在性、name 命名规范、desc 外键关联 3 项检查。
*   **2026-02-24 (Schema 2.4 / 全域 XML 引擎 / 跨 Agent 协作)**:
    *   **全域 XML Docx 引擎**: 01~05 所有生成器（大纲、进度表、教案、实验、考核）全部剥离旧 `docxtpl` 依赖，统一接入基于 `lxml` 的 `docx_engine.py`。实现「深克隆、vMerge 保全、防重叠换行」100% 格式还原。
    *   **跨 Agent 协作协议 (SSOT)**: 确立以 `docs/Cross_Agent_RFC.md` 作为工作区间协商的沟通规范。严禁 A 项目跨区重写 B 项目且破坏 SSOT；遇到新字段需求，统一在生成器侧降级处理或推演派生。
    *   **停课/调课自适应 (Schema 2.4)**: 新增 `classes[].excluded_weeks` 声明法定节假日停课（自动跳过教案及进度表占位）和 `session_time_overrides`（节次变化动态压缩每次课 minutes 上限），实现全自动的多班级差分排课适配。
    *   **单班学时标注**: 增加 `hours.per_class: true` 以防多班累加误解。
*   **2026-02-27 (WYSIWYG / 跨 Agent 邮箱系统 / Schema 2.5)**:
    *   **WYSIWYG 原则**: 生成器禁止自动拼接"第X章"或知识点编号。课程端在 YAML 直接写入带编号的完整文本，生成器原样输出。
    *   **共享邮箱系统**: 新建 `cross_agent_mailbox/` 目录，提供统一 `INDEX.md` 索引、`active/` → `resolved/` 生命周期管理、标准 frontmatter（id/from/to/status/priority）。
    *   **工作流对**: `/mailbox_out`（边界判定 + MSG 投递 + 归档输出）和 `/mailbox_in`（收件 + INDEX 同步 + 处理），两端对称部署，按 `to` 字段过滤确保身份隔离。
    *   **三层原子同步**: 确立 `course_schema.py` → `Data_Dictionary.md` / `Spec_*.md` → 生成器 fallback 逻辑必须同一会话完成。
    *   **Schema 2.5 / 归档命名**: 新增 `teacher.archive_id`（已废弃，迁移至 `classes[].archive_id`）。`Spec_Global.md §8` 定义云盘归档命名规范，`/mailbox_out` 步骤 5 支持一键归档输出 + PDF 转换。
    *   **进度表学时修正**: `gen_schedule_xml.py` 课堂教学列从 `theory+practice`（合计）修正为仅 `theory`。`Spec_Schedule.md §2.3` 同步更新定义和校验公式。
*   **2026-02-27 (教案学时精确对应 / 双检测增强)**:
    *   **双单位消歧时间输出**: `gen_lessonplan_xml.py` 的 `_build_steps_map()` 输出格式为 `约{minutes}分钟（{hours_equiv}理论/实践学时）`，采用末项补正策略确保各 step 逐项学时之和精确等于大纲声明 `hours_theory`/`hours_practice`。修复 `stage=演示` 映射遗漏（归入新课讲授行）。
    *   **Gate/审计阈值收紧**: Gate-2 从 >2h BLOCK 收紧为 **>1h BLOCK**；审计 C-2 从 >2h CRITICAL 收紧为 **>1h CRITICAL / >0.5h WARN**；审计 TOLERANCE 从 30% 收紧为 **15%**。
    *   **stage 分类规则**: 理论 stage = 复习/导入/讲授/演示；实践 stage = 实践/练习/训练/总结/小结。第一周禁止 `stage=复习`。
    *   **跨 Agent 协作强化**: MSG-014 (P0) 要求课程端建立严谨的 steps 数据审查机制。
*   **2026-02-28 (归档序号迁移 / 进度表动态行数)**:
    *   **archive_id 迁移到班级级别**: `classes[].archive_id` 替代 `teacher.archive_id`（废弃）。每个班级有独立序号，多班 per-course 文档拼接所有班级 `{id}{name}` 前缀。
    *   **统一归档命名**: 5 个生成器（大纲/进度表/教案/实验/考核）全部接入 `docx_engine.archive_filename()`，自动按 `Spec_Global §8` 命名。
    *   **进度表动态行数**: `gen_schedule_xml.py` 根据 `week_range` 自动增删表格行（克隆或删除），不再固定 18 行。
*   **2026-02-28 (双格式输出 DOCX+PDF / 归档序号迁移)**:
    *   **PDF 同步输出**: 新增 `scripts/pdf_converter.py`，集成 LibreOffice headless 转换（5 次指数退避重试 + 60s 超时）。`generate.py` 在所有生成器执行完毕后批量转换最终交付文件为 PDF。默认开启，`--no-pdf` 可关闭。
    *   **智能文件筛选**: `_collect_final_docx()` 仅收集最终交付件（大纲、进度表、教案合并版、考核材料等），排除中间文件（教案散页、首页、尾页署名）。
*   **2026-02-28 (教案多班级授课时间感知)**:
    *   **R2 多班级周次映射**: `gen_lessonplan_xml.py` 新增 `_resolve_actual_week()`，根据 `week_range` + `excluded_weeks` 将 calendar 序号映射为各班级实际教学周次（如影视班第1周、游戏班第10周），复用进度表的分段排课逻辑 `_resolve_period_lp()` 查询 `schedule_segments` 获取当前周次的实际节次。
    *   **节次压缩注释**: 当某班级实际节次 < 教学设计标准节次时，R2 末尾自动追加说明（如"※ 游戏班本周实际4节，教学设计按5节编排，授课时等比压缩"），仅差异周出现。
    *   **实验报告日期修复**: `gen_experiment_xml.py` 的 `_get_class_experiment_dates()` 从固定等间距公式改为基于 `calendar[].exp_id` 查找实验对应周次，再通过 `week_range` + `excluded_weeks` 映射为班级实际教学周日期。
*   **2026-02-28 (VML→DrawingML 模板修复)**:
    *   **PDF logo 变形修复**: 4 个模板（`Syllabus.docx`、`Template_Schedule.docx`、`Template_LessonPlan_Cover.docx`、`设计学院模版-附件3：课程教案模板.docx`）中的 VML `v:shape` 图片替换为 DrawingML (`wp:inline` + `pic:pic`)。VML 负裁剪参数导致 LibreOffice headless 转 PDF 时 logo 被压扁约 10.8%。修复后宽高比从 4.81:1 修正为原图 4.34:1。
    *   **模板图片格式统一**: 全部模板（含实验模板）现均使用 DrawingML 格式嵌入图片，确保跨渲染引擎的宽高比一致性。
