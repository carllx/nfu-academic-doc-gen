# 教学进度表编写指南 (Spec_Schedule)

> 来源：25-26-2 教学材料注意事项 - 第3节
> 参考：Template_Schedule.doc 模板结构分析 + 模板末尾红字批注
> 整合：Ref_Submission_Req.md 审核流程 · Ref_General_Notice.md 执行要点 · Spec_Global.md 通用规范

## 1. 核心规则 (Core Rules)
*   **一班一份**：每人一份进度表；若不同班级的课时/进度不同，需分别制作。
*   **一致性**：内容必须与**教学大纲**和**教案**完全一致——包括教学内容、课时分配（理论/实践学时须与大纲 §三·课程内容和教学要求 完全对齐）。
*   **一次课一行**：进度表中每一行对应一次课，即一份教案。
*   **封面精确到班级**：封面"授课对象"须写到具体的年级+专业+班级。
*   **提交时限**：2月5-6日提交教学进度表至系部负责人。

## 2. 模板结构 (Template Layout)

模板文件为 `.doc` 格式，引擎使用前须用 **Word/WPS 手动另存为 `.docx`**（勿用 `textutil`，详见 Spec_Global §5.4）。
模板分为 **4 个逻辑区域**，以下逐一说明各区域的字段和填写规则。

### 2.1 封面页 (Page 1)

| 序号 | 字段 | 数据来源 (`course.yaml`) | 说明 |
|------|------|--------------------------|------|
| ① | 学年学期 `20__～20__ 学年第__学期` | `course.semester` | 解析 `"2025-2026-2"` → `20**25**～20**26** 学年第 **二** 学期` |
| ② | 课 程 名 称 | `course.name` | |
| ③ | 课程类别 | `course.nature` | 如 "专业选修课" |
| ④ | 总学时 | `course.hours.total` | |
| ⑤ | 总学分 | `course.credits` | |
| ⑥ | 授课对象 | `classes[].name` | **（年级专业班级）**，红字提示；每班一份，封面须具体到班 |
| ⑦ | 开课单位 | `course.department` | 如 "设计学院" |
| ⑧ | 主 讲 教 师 | `teacher.name` | |
| ⑨ | 职 称 | `teacher.title` | |
| ⑩ | 课程团队教师（职称） | `teacher.team`（可选） | 如无可留空 |
| — | 广州南方学院教务处制 | 静态文本 | |

### 2.2 课程基本信息表 (Page 2 ‒ 一、课程基本信息)

| 行标签 | 数据来源 | 说明 |
|--------|----------|------|
| 课程名称 | `course.name` | |
| 课程代码 | `course.code` | |
| 学分 | `course.credits` | |
| 考核方式 | 考试 / 考查 | 必修课 → "考试"；选修课按实际填写 |
| 总学时 | `course.hours.total` | |
| 周学时 | 自动计算 | `hours.total / 教学周数` |
| 理论 | `course.hours.theory` | |
| 实践 | `course.hours.practice` | |
| 课程目标 | `course.objectives` | **红字批注**：填知识目标、能力目标及素质目标，**与教学大纲保持一致** |
| 教材和主要参考资料 | `textbooks[]` | 分 `1.选用教材` / `2.参考书目与文献` / `3.课程网站等支持条件`；各类下子项单项无序号，多项用 `(1)` `(2)` 格式；引用格式见 Spec_Global.md §5.6 |
| 课程网站等支持条件 | `course.resources_url` | 如无写"无"；详见 Spec_Global.md §5.6(三) |

### 2.3 教学进度安排表 (Page 3~4 ‒ 二、教学进度安排)

**表头列结构（7列）**：

| 列号 | 列标题 | 数据来源 | 填写规则 |
|------|--------|----------|----------|
| 1 | 周次 | `calendar[].week` | |
| 2 | 星期几 | `classes[].schedule_time` | 从 `"周一1-2节"` 中提取星期几 |
| 3 | 上课节次 | `classes[].schedule_time` | **按具体节次填写**，如 `1-2`、`12-14`，**不是填上了几节课** |
| 4 | 教学内容（章、节） | `calendar[].topic` + `calendar[].content` | **左对齐**，参考教案格式。Phase 2d 新增：末尾自动追加教材引用摘要（短格式），如`（《书名》§1-2；Munzner §5）`。数据源为 `calendar[].readings` + `textbooks[].toc`，由 `resolve_chapter_titles(fmt='short')` 渲染。无 readings 时不追加。 |
| 5 | 授课教师 | `teacher.name` | |
| 6~8 | 教学安排（课时安排） | — | 三个子列，详见下方 |

**教学安排子列详情**：

| 子列 | 含义 | 数据来源 | 说明 |
|------|------|----------|------|
| 课堂教学 | 理论学时 | `calendar[].hours_theory` | **仅理论学时（教务通知 2026-02 修正）** |
| 课内实验或实践 | 实践学时 | `calendar[].hours_practice` | 含上机、实验、演示操作等 |
| 课外实践 | 课外学时 | 手动标注（通常为 0） | **仅限**去企业交流/参观调研等，需走调停课流程 |

**数据行**：模板固定 23 行（R0-R1 表头 + R2~R19 为 18 个数据行 + R20~R22 签名区）。生成器根据 `week_range` 跨度**动态裁剪或扩展数据行**，使最终文档仅包含实际教学周数对应的行。周次列从 `start_week` 开始递增（非固定从 1 开始）。R2 (Week 1) 全部 7 个值列均为 `XXXX` 占位符，R3~R19 的周次列已预填 2~18。每周一行，无多行子行。

> [!NOTE]
> **动态行数规则**：有多少周就显示多少行。例如 `week_range: "10-18"` → 9 行，首行周次 = 10；`week_range: "1-8"` → 8 行，首行周次 = 1。行数由 `_calc_needed_rows()` 计算，裁剪/扩展在填充前执行。

> [!IMPORTANT]
> **学时校验**：∑课堂教学 = `course.hours.theory`；∑课内实验或实践 = `course.hours.practice`。
> 节假日停课周仍记原定学时（从节次推导），确保总学时与课程计划一致。

> [!WARNING]
> **物理课时红线**：`audit_course_data.py` 已内置逐周上限校验。`hours_theory` 或 `hours_practice` 单项 > 5 即报 `[CRITICAL]`；总和 > 5 亦报。路演/答辩/汇报周强制 `hours_theory == 0`。（2026-02-27）

### 2.4 签名区 (尾部)

| 签名栏 | 签署人 | 说明 |
|--------|--------|------|
| 任课教师签名 | 教师本人 | 保留空白待手签，附日期 |
| 专业负责人（教研室主任）签名 | 审核人 | 保留空白 |
| 单位负责人（签名/签章） | 终审人 | 保留空白 |
| — | 注 | "本表一式两份，自留一份，交开课单位一份。" |

## 3. 审核流程 (Review Flow)

> 来源：Ref_Submission_Req.md §二(二)2

1.  任课教师按要求编写教学进度表。
2.  专业负责人/教研室主任审核并签字。
3.  教学单位分管教学的副院长终审并签字。
4.  报教务处备查。

## 4. 提交与命名规范 (Submission)

> 来源：Ref_Submission_Req.md §四

*   **格式**：最终提交 **PDF**。
*   **纸质版**：签名加盖公章，2月26日 17:00 前报送。
*   **电子版命名**：`序号-教学单位-教师姓名-2025-2026-2《课程名称》教学进度表`
*   **压缩包命名**：`XX教学单位2025-2026-2 教学进度表`

## 5. 数据与模板管理 (Data & Template Management)

### 5.1 Schema 映射

| 模板字段 | YAML 路径 | 类型 | 备注 |
|----------|-----------|------|------|
| 学年学期 | `course.semester` | `str` | 解析为 "20XX～20XX 学年第X学期" |
| 课程名称 | `course.name` | `str` | |
| 课程代码 | `course.code` | `str` | |
| 课程类别 | `course.nature` | `str` | |
| 学分 | `course.credits` | `float` | |
| 总学时 | `course.hours.total` | `int` | |
| 理论学时 | `course.hours.theory` | `int` | |
| 实践学时 | `course.hours.practice` | `int` | |
| 周学时 | 计算值 | `int` | `total / 教学周数` |
| 考核方式 | 由 `nature` 推导 | `str` | 必修→考试，选修→可考查 |
| 授课对象 | `classes[].name` | `str` | 每班一份 |
| 排课时间 | `classes[].schedule_time` | `str` | 解析星期几+节次 |
| 教室 | `classes[].classroom` | `str` | 封面暂不用，进度表内亦无此列 |
| 教师 | `teacher.name` | `str` | |
| 职称 | `teacher.title` | `str` | |
| 开课单位 | `course.department` | `str` | 如 "设计学院" |
| 专业(系) | `course.major` / `teacher.department` | `str` | 如 "数字媒体艺术"，用于授课对象前缀 |
| 课程团队 | `teacher.team` | `str` | 可选 |
| 课程目标 | `course.objectives` | `dict` | 与大纲一致 |
| 教材 | `textbooks[]` | `list` | type=textbook / reference |
| 课程网站 | `course.resources_url` | `str` | 可选 |
| 周次/内容 | `calendar[].week/topic/content` | `list` | |
| 每周学时 | `calendar[].hours_theory/hours_practice` | `Number` | 进度表课时子列数据源（推荐整数） |
| 学期起始日 | `semester_config.start_date` | `str` | 用于具体日期计算 |

### 5.2 多班级与分段排课支持

*   若需为不同班级生成进度表，在 `course.yaml` 的 `classes` 列表中定义每个班级的 `schedule_time`。
*   生成器根据班级信息自动调整封面授课对象和进度表中的星期几/节次。
*   `schedule_time` 支持 `周X` 和 `星期X` 两种格式（如 `周四2-5节`、`星期日(分段排课)`），引擎自动归一化为 `周X` 输出。

**动态行数与周次映射**：
*   生成器根据 `week_range` 跨度动态调整 Table 2 的数据行数。
*   `week_range: "1-8"` → 8 行，周次 1~8；`week_range: "10-18"` → 9 行，周次 10~18。
*   无 `week_range` 时按 `calendar` 条目数决定行数。
*   多余行从模板 XML 中物理删除，不足行通过 `clone_table_row()` 克隆补足。
*   停课周行学时记 0，教学内容为"节假日停课"。

**分段排课**（Schema 2.2+）：
*   同一班级在不同周次有不同节次时，通过 `schedule_segments` 声明。
*   **weeks 字段**支持三种格式：
    - 范围：`"10-13"` → 第 10~13 周
    - 枚举：`"7,9"` → 第 7、9 周
    - 混合：`"7,9,11-13"` → 第 7、9、11~13 周
*   **period 字段**支持逗号分隔的多个时段：`"1-5节, 11-15节"` → 拆分为 2 个独立 session
*   **day 字段**（可选）：指定该 segment 的上课星期，用于同一周多日上课场景（如周四+周日）。缺省时继承 `schedule_time` 中的星期。

    ```yaml
    schedule_segments:
      - weeks: "9-18"           # W9-W18 全程周四
        period: "2-5节"
        day: "周四"
      - weeks: "13-17"          # W13-W17 增加周日
        period: "2-5节"
        day: "周日"
      - weeks: "7,9"            # 逗号枚举周次
        period: "1-5节"
      - weeks: "10"             # 单周双时段
        period: "1-5节, 11-15节"
    ```

**双模式自动检测**（`_fill_schedule_table`）：
*   **标准模式**：`calendar` 条目数 ≤ `week_range` 可用周数 → 每周一行，线性映射
*   **多日制模式**：`calendar` 条目数 > 可用周数 → 按 `calendar` 顺序逐条分配，同一周可占多行
*   模式由 `_fill_schedule_table()` 自动检测，无需手动配置。
*   多日制下，`_resolve_all_sessions()` 按节次起始值升序排列所有 session（确保 1-5 排在 7-11 前面）。

### 5.3 具体日期计算
*   **配置**：`semester_config.start_date`（如 `"2026-02-17"`）。
*   **自动化**：生成器利用 `scripts/utils/semester_utils.py` 自动计算每周的具体日期范围 (Monday–Sunday)，自动排除法定节假日。
*   **人工校验**：生成后务必核对节假日调整的准确性。

### 5.4 模板文件

*   **源文件**：`02_Schedule_Generator/Template_Schedule.docx`
*   **转换历史**：原始 `.doc` → Word/WPS 手动另存为 `.docx`（❗ 勿用 `textutil`，会丢失表格结构）→ VML 图片已替换为 DrawingML (2026-02-28)
*   **占位符**：模板中动态内容使用 `XXXX` 标记，建议每个 `XXXX` 附加 Word 评论(Comment)标注数据来源
*   **模板结构审计**：每次更新模板后，应通过 XML 解析确认表格数、行数、单元格内段落数、XXXX 数量是否符合预期
*   **图片格式**：已从 VML (`v:shape`) 迁移至 DrawingML (`wp:inline`)，确保 LibreOffice PDF 转换时 logo 宽高比正确

## 6. 代码生成方案 (Generation Architecture)

> **方案：XML 直接操作**（与 Syllabus 生成器一致）

*   **流程**：`Template_Schedule.docx`(ZIP) → 解压 `document.xml` → lxml 精确替换 XXXX → 重新打包 ZIP
*   **模板即 SSOT**：所有格式属性由 `.docx` 原始 XML 决定，代码不构造任何格式
*   **核心引擎**：`scripts/docx_engine.render_docx()` 统一入口
*   **填充策略**：
    *   封面表 (Table 0)：逐行 C2 替换 XXXX
    *   基本信息表 (Table 1)：R2 数据行置值 + R3/R4 多段落 XXXX 替换
    *   进度安排表 (Table 2)：动态裁剪/扩展行数至 `week_range` 跨度，周次列从 `start_week` 递增，线性填充 calendar 内容（仅跳过 excluded_weeks 和节假日）
*   **多班级**：循环 `classes` 列表，每个班级独立生成一份文件，文件名含班级名

