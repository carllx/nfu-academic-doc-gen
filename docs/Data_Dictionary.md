# 数据字典 (Data Dictionary)

本文档定义了课程数据的结构。
> **注意**：本文档仅作为参考。数据的**单一事实来源 (SSOT)** 是 `scripts/course_schema.py`。由此脚本定义的规则（如必填项、逻辑校验）为准。

> **ADR-044 数据源拆分**（自 2026-05-22 起生效）：课程端的单体 `course.yaml` 已按语义域拆分为以下子文件。原 `course.yaml` 保留为索引文件（含 `includes` 列表），由 `course_loader.py` 透明合并为与旧版完全一致的字典结构，生成器无需感知拆分细节。
>
> | 子文件 | 语义域 | 本文档对应章节 |
> |--------|--------|----------------|
> | `course_meta.yaml` | course, teacher, student_analysis, semester_config, agent | §2, §3, §7 |
> | `course_objectives.yaml` | objectives | （课程目标） |
> | `course_textbooks.yaml` | textbooks | §6 |
> | `course_calendar.yaml` | calendar | §4 |
> | `course_experiments.yaml` | experiments | §5 |
> | `course_assessment.yaml` | assessment_methods, exams | §8, §6(考核) |


## 1. 根对象 (Root)

| 字段名 | 类型 | 必填 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `course_info` | Object | Yes | 课程基本信息 | 全局 |
| `teacher_info` | Object | Yes | 教师信息 | 大纲, 教案, 进度表 |
| `calendar` | List | Yes | 教学周历 (1-18周) | 大纲, 进度表, 教案 |
| `experiments` | List | No | 实验项目列表 (有实验课必填) | 大纲, 实验指导书, 认定表 |
| `textbooks` | List | No | 教材与参考书 | 大纲 |
| `semester_config` | Object | No | 学期日历配置 | 进度表 |
| `exams` | Object | **Yes** | 试卷/考查结构配置。即使是考查课也必须填写，否则模板渲染报错 `'exams' is undefined` | 大纲, 试卷 |
| `assessment_methods` | Object | Yes | 考核方式与权重 | 大纲 |


## 2. 课程基本信息 (`course_info`)
来源子文件：`course_meta.yaml`

| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | "交互产品开发" | 课程名称 | 全局 |
| `code` | String | "DES12345" | 课程代码 | 大纲, 试卷, 成绩单 |
| `semester` | String | "2025-2026-2" | 学期 | 全局 |
| `nature` | String | "专业必修课" | 课程性质。合法值：`专业必修课` / `专业选修课` / `公共必修课` / `公共选修课` / `成长必修课` | 大纲 |
| `credits` | Number | 4 | 学分 | 大纲, 培养方案 |
| `classes` | List[Object] | [{"name": "1班", "schedule_time": "周一1-2"}] | 授课班级列表 | 全局 |
| `hours.total` | Number | 64 | 总学时 | 大纲, 进度表 |
| `hours.per_class` | Boolean | true | （Schema 2.4）多班级并行课程，明确 `hours.total` 表示单班学时 | 全局 |
| `hours.theory` | Number | 32 | 理论学时 | 大纲 |
| `hours.practice` | Number | 32 | 实践学时 | 大纲 |

| `department` | String | "设计学院" | 开课单位 | 大纲 |
| `major` | String | "数字媒体艺术" | 开课专业 | 大纲 |
| `prerequisites` | String | "用户体验设计" | 先修课程 | 大纲 |
| `introduction.content` | String/RichText | "..." | 课程主要内容简介 | 大纲 |
| `introduction.design` | String/RichText | "..." | 教学设计思路 | 大纲 |
| `resources_url` | String | "http://..." | 课程资源链接 | 大纲 |

## 2.1 班级信息 (`classes` Item)

如果多班级有不同的周次或节次，可以使用 Schema 2.2/2.4 扩展字段在此声明差异，**禁止在 `calendar` 复制冗余数据。**

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `name` | String | "23级数字媒体艺术1班" | 班级名称 |
| `student_count` | Number | 45 | 班级实际人数，用于自查表等考务材料的自动统计 |
| `schedule_time` | String | "周一1-2节" | 默认上课时间 |
| `classroom` | String | "A101" | 教室 (可选) |
| `week_range` | String | "10-18" | （Schema 2.2）实际教学自然周跨度。生成器会自动将 `calendar[0]` 偏移到该周 |
| `schedule_segments` | List | `[{weeks:"10-13", period:"1-5节"}, {weeks:"7,9", period:"1-5节"}, {weeks:"10", period:"1-5节, 11-15节", day:"周日"}]` | （Schema 2.2, 2.5 增强）分段排课。`weeks` 支持范围/枚举/混合；`period` 支持逗号分隔多时段；`day`（可选）指定上课星期，用于同一周多日上课 |
| `excluded_weeks` | List[Number] | `[16]` | （Schema 2.4）该班级因法定节假日或校庆等原因**停课的自然周次**。生成器自动跳过，不计学时 |
| `session_time_overrides` | List[Object] | `[{weeks:"14-18", max_minutes:180}]` | （Schema 2.4）节次缩水或合并导致的上课时长变更，自动压缩教案中各 step 的时长上限 |
| `archive_id` | Number | `45` | （Schema 2.5）班级归档序号，每学期由系部汇总表分配。**不同课程、不同班级有不同序号**。可选，缺失时回退 `teacher.archive_id` |


## 3. 教师信息 (`teacher`)
来源子文件：`course_meta.yaml`

| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | "张三" | 主讲教师姓名 | 全局 |
| `title` | String | "讲师" | 主讲教师职称 | 大纲, 教案 |
| `office` | String | "H1-201" | 办公室 | 大纲 |
| `department` | String | "设计学院" | 所属部门 | 教案首页 |
| `team` | String/List | `''` 或 `[{name, title}]` | **协作教师列表，不含主讲教师本人**。推荐对象列表格式 以保留职称信息；单人或无协作时留空。不得将主讲教师的 `title` 自动补准为团队成员职称 | 教案首页封面 |
| `archive_id` | Number | 55 | ⚠️ **已废弃**，迁移至 `classes[].archive_id`（见 §2.1）。向后兼容：函数优先读取 class 级别，缺失时回退此字段 | 归档命名 |


## 4. 教学周历 (`calendar`)
来源子文件：`course_calendar.yaml`

这是一个列表，每个元素代表一周。

| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `week` | Number | 1 | 周次 | 全局 |
| `date_range` | String | "2.24-3.02" | 日期范围 (自动生成时可忽略，手动填需精准) | 进度表 |
| `topic` | String | "课程介绍" | 教学主题 | 全局 |
| `content` | String | "1.1 讲解教学大纲..." | 详细内容 (主要知识点，**需自带编号前缀**) | 教案, 大纲(摘要) |
| `chapter_title` | String | "第一章 信息可视化概论" | 章标题 (WYSIWYG，直接用于大纲§三和教案R0)。**推荐必填**，缺失时回退 `topic` | 大纲, 教案 |
| `exp_id` | Number | 1 | 关联实验 ID (对应 `experiments[].id`)。可选 | 进度表, 教案 |
| `key_points` | String | "交互定义" | 重点/难点 | 大纲 |
| `hours_theory` | Number | 2 | 本周理论学时 (推荐整数) | 大纲, 进度表 |
| `hours_practice` | Number | 2 | 本周实践学时 (推荐整数) | 大纲, 进度表 |
| `task` | String | "安装环境" | 课后作业/任务 | 进度表, 教案 |
| `homework` | String | "..." | 详细作业要求 | 大纲 |
| `has_homework` | Boolean | true | 是否有作业 (用于进度表勾选) | 进度表 |
| `method` | String | "讲授+演示" | 教学方法 | 教案, 进度表 |
| `teaching_requirements` | String/Dict | "通过本章学习..." 或 `{knowledge, ability, quality, method}` | 本章教学要求 (Optional)。推荐结构化 dict 格式（教案分维度输出），大纲自动降级为分号拼接纯文本 | 大纲, 教案 |
| `focus` | String | "可视化有效性的三大基石" | 重点 (Optional) | 大纲 (课程内容和教学要求) |
| `difficulty` | String | "自然语言到视觉元素的映射" | 难点 (Optional) | 大纲 (课程内容和教学要求) |
| `ideology` | String | "结合中国大数据发展战略..." | 课程思政融入点 (Optional) | 大纲 (课程内容和教学要求) |
| `teaching_method` | String | "案例演示、小组讨论、实践操作" | 采用的教学方法 (Optional) | 大纲 (课程内容和教学要求) |
| `readings` | List[String] | `["《交互设计》第1章", "Munzner Ch5"]` | 本周指定阅读教材与章节（Optional）。显式填写时为 SSOT，教案 R7 直接使用；缺失时由 `reading_utils` 从 objectives/content 中自动正则提取 | 教案 (R7 课前阅读) |
| `lessons` | List | - | 教学单元列表 (用于生成细化教案) | 教案 |

### 4.1 教学单元 (`lessons` Item)
| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `topic` | String | "课程导论" | 单元主题 (通常对应2学时) |
| `objectives` | List[String] | ["了解...", "掌握..."] | 本次课教学目标 |
| `steps` | List[Object] | - | 教学步骤 (见下) |
| `review` | String | "预习下章" | 课后复习/作业 |

### 4.2 教学步骤 (`steps` Item)
| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `stage` | String | "导入" | 阶段（复习/导入/讲授/实践/小结）。注意：实际字段名为 `stage`，不是 `phase` |
| `summary` | String | "案例分析" | 展开描述/映射到教案【教学组织】子节 |
| `minutes` | Number | 15 | 预计时长（分钟） |
| `ideology` | String | "结合国家战略..." | 课程思政融入点，仅在 `stage=讲授` 时有效（映射到教案 R12【课程思政融入点】） |

## 5. 实验项目 (`experiments`)
来源子文件：`course_experiments.yaml`

| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `id` | Number | 1 | 实验序号 | 全局 |
| `name` | String | "Web交互基础" | 实验名称 | 全局 |
| `type` | String | "验证性" | 实验类型 (验证性/综合性/设计性) | 大纲, 实验项认定表 |
| `hours` | Number | 4 | 实验学时 | 大纲, 实验项认定表 |
| `group_size` | Number / String | 1 | 每组人数。若填写纯数字，生成器会自动追加"人"后缀；缺省时默认注入"1人" | 实验项认定表 |
| `requirement` | String | "必做" | 必做/选做。缺省时默认注入"必做" | 大纲 |

> [!CAUTION]
> **强合规校验规则 (教务新规)**：从 Schema 2.5 开始，每个实验项目必须在对应的 `exp_x.yaml` 增量配置中提供具体的 `steps`（步骤详情）或 `guide_text`（指导书文本占位）。若两者皆为空，生成引擎（`generate.py`）将直接报错拦截，拒绝生成残缺的实验指导书。


## 6. 教材与参考书 (`textbooks`)
来源子文件：`course_textbooks.yaml`

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `title` | String | "用户体验要素" | 书名 |
| `author` | String | "Jesse James Garrett" | 作者 |
| `publisher` | String | "机械工业出版社" | 出版社 |
| `isbn` | String | "978-7-111-35804-4" | ISBN (可选) |
| `year` | String | "2011" | 出版年份 |
| `type` | String | "textbook" | 类型: textbook(教材)/reference(参考书) |
| `toc` | List[TextbookChapter] | - | （Phase 2a 新增）教材目录结构。被 `resolve_chapter_titles()` 引擎消费，用于将 `readings` 自由文本解析为带章节标题的标准化引用。可选：无 TOC 时 readings 保持原文输出 |

### 6.1 教材章节 (`toc` Item — `TextbookChapter`)

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `chapter` | Number / String | `1` 或 `"Starting from Scratch"` | 章节号。数字用于传统编号教材，字符串用于无编号教材（如 Refactoring UI） |
| `title` | String | "什么是交互设计" | 章节标题（中文）。外文教材使用翻译后的中文标题 |
| `title_en` | String | "What is Interaction Design?" | 英文原标题（可选）。仅外文教材填写，用于交叉校验 |

### 6.2 教材引用解析链路 (Phase 2b-2d)

```
calendar[].readings  ──┐
                       ├─→  resolve_chapter_titles(fmt)  ──→  标准化引用文本
textbooks[].toc      ──┘
```

| 消费方 | 格式 | 插入位置 | 效果示例 |
| :--- | :--- | :--- | :--- |
| 大纲 `gen_syllabus_xml.py` | `full` | 知识点后、教学要求前 | `参考教材：《信息可视化设计》第一章 信息的设计与视觉传达` |
| 教案 `gen_lessonplan_xml.py` | `full` | R7 课前阅读材料 | `《交互设计精髓 (About Face 4)》第一章 数字产品的设计过程` |
| 进度表 `gen_schedule_xml.py` | `short` | 列4 教学内容末尾 | `（《信息可视化设计》§1-2；Munzner §1）` |


## 7. 学期配置 (`semester_config`)
来源子文件：`course_meta.yaml`

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `start_date` | String | "2026-02-17" | 学期开始日期 (YYYY-MM-DD)，用于计算进度表日期 |


## 8. 试卷结构 (`exams`)
来源子文件：`course_assessment.yaml`

**根对象**: `exams.final_exam` (List[ExamPaper])

### 8.1 试卷 (`ExamPaper`)
| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `name` | String | "A卷" | 试卷名称 |
| `duration` | Number | 120 | 考试时长 (分钟) |
| `total_score` | Number | 100 | 卷面总分 |
| `sections` | List | - | 大题列表 (见下) |

### 8.2 实操类 A/B 卷数据 (`PracticePaperVersion`)
当 `type`="practice_ab" 时，`practice_paper.ab_versions` 下的具体版本数据结构。

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `practice_theme` | String | "为图书馆设计一个..." | 创作主题（必须是一段描述具体设计/开发项目的详细文本；A/B卷必须具有平行的差异化场景） |
| `practice_requirements` | String | "需要包含登录、首页..." | 基本要求 |
| `practice_deliverables` | String | "提交ZIP包..." | 提交物要求及防抄袭条款 |
| `example_images` | List[String] | `["./A卷参考1.jpg", "./A卷参考2.jpg"]` | 参考图片路径列表。可选，生成器会自动横向平铺渲染到文档末尾。 |

### 8.3 大题 (`ExamSection`)
| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `section_name` | String | "一、选择题" | 大题名称 |
| `total_score` | Number | 20 | 大题总分 |
| `questions` | List | - | 题目列表 (见下) |

### 8.3 题目 (`Question`)
| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `content` | String | "题目内容..." | 题干 |
| `type` | String | "选择" | 题型 |
| `score` | Number | 2 | 分值 |
| `options` | List[String] | ["A", "B"] | 选项 (仅选择题) |
| `answer` | String | "A" | 参考答案 |


## 6. 考核方式 (`assessment_methods`)
来源子文件：`course_assessment.yaml`

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `normal_score_ratio` | Number | 50 | 平时成绩占比 (%) |
| `final_score_ratio` | Number | 50 | 期末成绩占比 (%) |
| `attendance_ratio` | Number | 10 | 考勤占平时成绩的比例 (%)，默认值为10%，由 Schema 单独校验 |
| `normal_items` | List | - | 平时成绩构成项（**不含考勤**，考勤由 `attendance_ratio` 独立控制） |

### 6.1 平时成绩项 (`normal_items`)

| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | "章节测试1" | 项目名称。必须标注测试类型（章节测试/命题测试），**禁止带括号**，**禁止内嵌实验名称** | 大纲 |
| `ratio` | Number | 15 | 占平时成绩的比例 (%) | 大纲 |
| `desc` | String | "对应实验1「概念设计与交互主线」。考核要求：..." | 评分标准。必须关联对应实验（外键）并注明考核要求 | 大纲 |

> [!IMPORTANT]
> **校验规则**：`normal_score_ratio + final_score_ratio` 必须 = 100；`attendance_ratio + Σ(normal_items.ratio)` 必须 = `normal_score_ratio`。

> [!WARNING]
> **命名规范 (ADR 005)**：`name` 格式为 `章节测试N` 或 `命题测试N`。`desc` 必须以 `对应实验N「实验名称」。考核要求：` 开头，明确外键关联后再给出具体指标。`exams.final_exam[].sections[].questions[].content` 同理。


| 字段名 | 类型 | 示例 | 说明 | 使用处 (Used In) |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | "考勤" | 项目名称 | 大纲 |
| `ratio` | Number | 20 | 占平时成绩的比例 (%) | 大纲 |
| `desc` | String | "缺勤扣分..." | 评分标准 | 大纲 |

## 9. 实习指导材料 (Internship)
*(非标准课程 Schema，独立于 CourseSchema)*

由于“实习指导”等课程结构与传统课程差异极大（如无明确排课表、考核形式主要依靠巡查等），故通过独立的 `InternshipSchema` 进行专门管理。为确保能够正确无误地渲染至 XML 模板，所有字段均被强制约定为**字符串类型 (`str`)**。

> [!WARNING]
> **Anti-Null 防御规则**：
> JSON/YAML 数据在喂给引擎前，所有 `score_*`、`teacher_advice`、`note` 等随时可能缺省的字段，必须转换为**空字符串 `""`**，严禁使用 `null`，否则会引发解析崩溃。
> 
> **多行文本换行机制**：
> `intern_content` 与 `teacher_advice` 等多行文本的换行，现已由底层的纯 Python-docx 引擎（`docx_engine.py`）自动拦截 `\n` 并转码为 `<w:br/>`。无需前端做特殊处理。
>
> **扩写机制**：
> `intern_content` 若字数过少，目前推荐的 SSOT 流程是直接在 YAML 数据层面进行专门扩写，而不是在读取/生成脚本中进行拦截和替换。

### 9.1 全局字段 (Global Data)

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `college` | String | "计算机学院" | 学院 |
| `major` | String | "软件工程" | 专业 |
| `school_teacher` | String | "林昕" | 校内指导教师（消除早期版本中 teacher 的指代歧义） |
| `teacher_advice` | String | "该生表现优异..." | 巡查教师意见建议及改进措施 |
| `teacher_signature` | String | "林昕" | 巡查教师签字 |

### 9.2 实习学生记录数组 (`students`)

| 字段名 | 类型 | 示例 | 说明 |
| :--- | :--- | :--- | :--- |
| `sequence_number` | String | "1" | 巡查记录详情表在统计表中的关联序号 |
| `student_name` | String | "张三" | 实习学生姓名 |
| `student_id` | String | "202200001" | 学号 |
| `student_phone` | String | "13800138000" | 学生联系电话 |
| `student_email` | String | "student@example.com" | 学生电子邮箱 |
| `class_name` | String | "22级软件1班" | 班级 |
| `base_name` | String | "广州某公司" | 巡查基地（单位） |
| `base_address` | String | "广州市天河区xxx" | 实习单位详细地址 |
| `position` | String | "前端开发实习生" | 实习岗位 |
| `intern_content` | String | "深入参与..." | 实习内容（多行文本需处理换行，如字数太少应在 YAML 直接扩写） |
| `intern_start_end` | String | "2026年2月2日 至 2026年5月31日" | 实习起止时间（由起止日期自动格式化而来） |
| `enterprise_teacher`| String | "李四" | 企业指导教师（消除歧义专用） |
| `enterprise_phone`| String | "13811112222" | 实习单位联系电话 |
| `decentralized_apply_student_date` | String | "2026年1月27日" | 学生申请签署日期 |
| `decentralized_apply_enterprise_date` | String | "2026年1月28日" | 企业审批签署日期 |
| `decentralized_apply_school_date` | String | "2026年1月29日" | 学院审批签署日期 |
| `inspect_year` | String | "2026" | 巡查时间-年 |
| `inspect_month` | String | "06" | 巡查时间-月 |
| `inspect_day` | String | "19" | 巡查时间-日 |
| `inspect_date` | String | "2026年6月19日" | 巡查时间全称 |
| `score_safety` | String | "10" | 安全纪律遵守情况得分（满分10） |
| `score_attendance` | String | "15" | 出勤率得分（满分15） |
| `score_learning` | String | "15" | 学习能力得分（满分15） |
| `score_teamwork` | String | "15" | 团队意识得分（满分15） |
| `score_attitude` | String | "15" | 工作态度得分（满分15） |
| `score_task` | String | "15" | 任务完成情况得分（满分15） |
| `score_suitability` | String | "10" | 适岗程度得分（满分15） |
| `score_total` | String | "95" | 总分（满分100） |
| `note` | String | "" | 备注 |

> [!TIP]
> 如果当前没有记录（`students: []`），前端处理逻辑应当手动植入一个全部为空的空对象字典，作为备用渲染行，避免在表格遍历时报索引越界或留下空白的非法表头。
