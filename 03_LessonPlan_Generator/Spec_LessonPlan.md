# 教案编写指南 (Spec_LessonPlan)

> 来源：25-26-2 教学材料注意事项 - 第2节
> 更新：2026-02-23 — 新增 §4 教案首页模板结构；mappings 数组支持一对多毕业要求；新增 §5 首页生成注意事项（6 条漏洞复盘）

## 1. 团队分工
*   **负责人**：主讲教师（课程负责人）。
*   **团队**：课程组所有老师使用同一份教案。
*   **例外**：课时不同需分开编写。

## 2. 内容要求
*   **一致性**：教学方法、思政内容必须与大纲一致。
*   **详细度**：
    *   2月9日前完成前三次教案。
    *   2月24日前提交其余教案。
*   **试讲要求**：必须包含大纲、评分标准讲解（第一周）。

## 3. 数据与模板管理 — 每周教案表 (Per-Week Lesson Plan)

### 3.1 数据源
*   教案中的章节名称、学时分配必须与 `course.yaml` 完全一致。
*   教学单元在 `course.yaml` 的 `calendar` 中为每周定义具体的 `lessons`。
*   教学环节数据从 `lessons[].steps[]` 获取，无数据时生成默认框架。
*   支撑课程目标优先使用 `supported_objectives` 引用字段。
*   **WYSIWYG 章节标题**：R0「授课章节」优先使用 `chapter_title` 字段（推荐必填），缺失时回退为 `topic` 原文。**生成器不再自动拼接“第X章”**。
*   **毕业要求映射**：兼容 `mappings[]` 数组（一对多）与旧版 `requirement`/`point` 扁平字段。

### 3.2 模板状态 ✅

| 文件 | 状态 | 说明 |
|------|------|------|
| `Template_LessonPlan_Cover.docx` | ✅ **已就绪** | 教案首页（封面 + 基本信息 Table 0 + 规划 Table 1）。logo 已从 VML 迁移至 DrawingML (2026-02-28) |
| `Template_LessonPlan.docx` | ✅ **已就绪** | 16 行教案表结构，仅包含表格结构无署名字段 |
| `Template_LessonPlan_Footer.docx` | ✅ **已就绪** | 署名页，包含填表人和专业负责人签名等末尾信息 |
| `设计学院模版-附件3：课程教案模板.docx` | 📋 原始文件 | 学校官方 `.docx` 教案模板。logo 已从 VML 迁移至 DrawingML (2026-02-28) |

### 3.3 16 行表格结构

```
row[0]:     授课章节        ← week.chapter_title (WYSIWYG, 回退 week.topic)
row[1]:     授课内容        ← week.content
row[2]:     授课时间        ← classes + 实际教学周次 (按 week_range 映射，跳过 excluded_weeks)
                              + 分段节次 (按 schedule_segments 查询，回退 schedule_time)
row[3]:     学时数          ← hours_theory + hours_practice
row[4]:     支撑课程目标    ← objectives + supported_objectives 交叉引用
                              兼容 mappings[] 数组（一对多）与旧版扁平字段
                              格式：{seq}. {desc}。支撑课程{类型}目标（{idx}），
                              对应毕业要求{req_num}（观测点{point}）[；...]。
row[5]:     教学目标与要求  ← week.teaching_requirements
                              支持结构化 {knowledge, ability, quality, method}
row[6]:     教学重点与难点  ← week.focus + week.difficulty (段落分隔)
row[7]:     课前阅读材料    ← reading_utils.extract_readings_from_week()
                              + resolve_chapter_titles() 增强（Phase 2d）
                              优先级: (1) week.readings 显式字段
                                      (2) 正则提取《书名》+章节
                                      (3) 正则匹配作者姓氏+ChX
                              增强: 提取后自动调用 resolve_chapter_titles(fmt='full')
                                    将章节引用解析为带标题全称（需 textbooks[].toc）
                              回退: textbooks (type=textbook) 全书目
row[8]:     教学方法        ← week.teaching_method
row[9]:     教学环节表头 (保持不变)
row[10]:    上次课复习      ← steps[] (stage=复习) / 默认框架
row[11]:    课程导入        ← steps[] (stage=导入) / 默认框架
row[12]:    新课讲授        ← steps[] (stage=讲授) / 默认框架 + 思政融入点
row[13]:    实践训练        ← steps[] (stage=实践/练习) / 默认框架
row[14]:    课程小结        ← steps[] (stage=总结/小结) / 默认框架
row[15]:    课后作业        ← week.task / week.assignment
```

### 3.4 教学环节子节规范

**有 steps 数据时**：组装规则与无数据时结构对齐：
```
R10-R13 (复习/导入/讲授/实践):
  【教学组织】{summary}
  【教学方法】{week.teaching_method}  ← 继承 week 级字段
  【时间安排】约{minutes}分钟（{hours_equiv}理论/实践学时）
  【课堂思考】  ← 占位框架，教师手填
  R12 额外: 【课程思政融入点】{ideology}

R14 (小结):
  【教学组织】{summary}
  【时间安排】约{minutes}分钟（{hours_equiv}实践学时）
  【课程回顾与反思】  ← 占位框架
```

**无 steps 数据时**：自动填入默认框架占位符：
```
R10-R13: 【教学组织】¶【教学方法】¶【时间安排】¶【课堂思考】
R12 额外: 【课程思政融入点】{ideology}
R14:     【教学组织】¶【时间安排】¶【课程回顾与反思】
```

### 3.5 教学环节时间分类规则（2026-02-27 新增）

教案 R10-R14 的五个教学环节按学时类别归类如下：

| 归属 | 教学环节 | 表格行 | stage 关键词 |
|:----:|---------|:------:|:----------:|
| **理论学时** | 上次课复习 | R10 | 复习 |
| **理论学时** | 课程导入 | R11 | 导入 |
| **理论学时** | 新课讲授 | R12 | 讲授、演示 |
| **实践学时** | 实践训练 | R13 | 实践、练习、训练 |
| **实践学时** | 课程小结 | R14 | 总结、小结 |

> **动态学时纠正（2026-05-19 修正）**：当课程/周次为纯实践课（`hours_theory: 0` 且 `hours_practice > 0`）时，所有教学环节（包含导入、讲授等）将自动全部划归为 **实践学时**；同理，纯理论课将全部划归为理论学时，覆盖上述关键词匹配逻辑。

**双检测架构校验规则**：
*   **L1 课程端写入校验**：课程 Agent 修改 `steps[]` 时须自检分钟归属与学时比例
*   **L2 生成器 gate**：`_validate_week_steps()` 硬性检测，不通过不产出 `.docx`
*   **L3 审计报告**：`audit_course_data.py` 3c 段全量巡检

**生成器时间输出（MSG-017 双单位消歧）**：
*   使用 `steps[].minutes / minutes_per_period` 计算等效学时，保留一位小数
*   输出格式：`【时间安排】约{minutes}分钟（{hours_equiv}理论/实践学时）`
*   末项补正：最后一个同类 step 的学时 = 声明学时 - 前面之和，确保逐项加总 = 大纲声明

| 规则 | 级别 | 说明 |
|:----:|:----:|------|
| C-1 | CRITICAL | **第一周禁止** `stage=复习`（首次课无上次课内容可复习） |
| C-2 | WARN/CRITICAL | 理论/实践 stage 分钟折算与 `hours_theory`/`hours_practice` 偏差 >0.5h WARN、>1h CRITICAL |
| C-3 | WARN | 纯实践周（`hours_theory=0`）理论 stage 时间 >30min |

### 3.6 标题格式
*   使用**中文数字**：`第一次课教案`、`第二次课教案`...
*   由 `_to_cn_num()` 函数自动转换

### 3.7 生成器
*   **脚本**：`scripts/gen_lessonplan_xml.py` — 纯 XML 操作（方案 A）
*   **引擎**：`scripts/docx_engine.py` 的 `render_docx()` 和 `merge_docx_files()` 框架
*   **制作脚本**：`scripts/make_lessonplan_template.py` — 从原模板提取并制作 XXXX 模板
*   **输出结构**：各部分独立输出（`教案_首页.docx`, `教案_第N周_xxx.docx`, `教案_尾页署名.docx`），最终合并拼接为 `教案_合并版.docx`。统一保存在 `output/教案/`。
*   **前置检测 gate**：`_validate_week_steps()` 在每周教案生成前执行硬性校验，不通过则跳过该周输出（`[BLOCKED]`）。

### 3.8 多班级授课时间规则（2026-02-28 新增）

教案是 **per-course** 文档（多班共用一份）。R2 授课时间需准确反映各班级的实际排课差异。

**R2 周次映射**：
*   `_resolve_actual_week()` 将 calendar 序号（1-based）映射为班级实际教学周次
*   映射依据 `classes[].week_range` 起止周 + 跳过 `excluded_weeks`
*   无 `week_range` 的班级，calendar 序号即为实际周次

**R2 分段节次查询**：
*   `_resolve_period_lp()` 根据 `schedule_segments` 查找当前实际周次的具体节次
*   `weeks` 支持范围(`"10-13"`)、枚举(`"7,9"`)、混合(`"7,9,11-13"`)格式
*   `schedule_time` 支持 `周X` 和 `星期X` 两种格式，自动归一化为 `周X`
*   无 `schedule_segments` 时回退 `schedule_time` 中的默认节次

**R2 节次压缩注释**（仅差异周出现）：
*   当某班级实际节次 < 教学设计标准节次时，R2 末尾自动追加：
    ```
    ※ {班级简称}本周实际{N}节（{M}分钟），以下教学设计按{P}节编排，授课时等比压缩。
    ```
*   R10-R14 教学设计时间以 `steps[].minutes`（按完整节次设计）为准，不做 per-class 拆分

**输出示例（W5，影视班5节/游戏班4节）**：
```
24数字媒体艺术影视班：第 5 周，周五1-5节
24数字媒体艺术游戏班：第 14 周，周五2-5节
※ 游戏班本周实际4节（180分钟），以下教学设计按5节编排，授课时等比压缩。
```

---

## 4. 教案首页模板结构 (Cover Page)

> 模板文件：`Template_LessonPlan_Cover.docx`
> 整个教案只用一个封面，不随每周教案重复。

### 4.1 文档整体结构

```
P[0]-P[3]:  封面 — "教   案" (大标题)
P[4]:       学年学期 — 纯 XXXX 占位（生成器解析 semester 字段，输出格式：202X～202X学年第X学期）
P[5]-P[12]: 空行
P[13]:      "广州南方学院教务处制"
─── 分页 ───
P[14]:      "教案首页" (标题)
TABLE 0:    基本信息表 (9行 × 3列)
TABLE 1:    教学规划表 (11行 × 6列, 含嵌套课程目标子表)
```

### 4.2 Table 0 — 基本信息 (9行)

| Row | 标签 | 数据源 (`course.yaml`) |
|:---:|------|------|
| 0 | 课程名称 | `course.name` |
| 1 | 课程性质 | `course.nature` |
| 2 | 学分数 | `course.credits` |
| 3 | 学时数 | `hours.total` |
| 4 | 授课对象 | `course.classes[].name` 汇总 |
| 5 | 开课单位 | `course.department` |
| 6 | 主讲教师 | `teacher.name` |
| 7 | 职称 | `teacher.title` |
| 8 | 课程团队教师（职称） | `teacher.team` → `_format_team()` 格式化；**不含主讲教师本人**；推荐 `[{name, title}]` 对象列表；空就流空；兼容字符串/列表/对象列表 |

### 4.3 Table 1 — 教学规划 (11行)

| Row | 标签 | 数据源 |
|:---:|------|------|
| 0 | 课程学分 + 学时安排 | `course.credits`, `hours.theory`, `hours.practice` |
| 1 | 教材和主要参考资料 | `textbooks[]` 分选用教材/参考书 + `course.resources_url` |
| 2 | 授课对象学情分析 | `student_analysis` (顶层字段) |
| 3 | **课程目标** | 嵌套子表 — 见 §4.4 |
| 4 | 内容课时分配 (表头) | 静态：章节 / 课程内容 / 学时数 |
| 5-10 | 内容课时分配 (数据) | `calendar[]` 汇总 — 见 §4.5 |

### 4.4 课程目标嵌套表 (动态行数)

嵌套在 Table 1 Row[3] Cell[1] 中，4列结构：

```
[维度名(vMerge)] [课程目标描述] [对应毕业要求] [对应观测点]
```

*   每个维度（知识/能力/素质）的行数 = `len(objectives[cat])`，**动态生成**
*   维度名列使用 vMerge 合并（首行 restart，后续 continue）
*   毕业要求/观测点**严格遵守 25 年人培方案**，一一对应

**数据映射**：

| 列 | 数据源 | 格式 |
|:---:|------|------|
| C0 | 类别 | 知识目标 / 能力目标 / 素质目标 |
| C1 | `objectives[cat][i].desc` | `{index}. {desc}` |
| C2 | `mappings[].requirement` | `毕业要求{id}.{name}` 用分号连接 |
| C3 | `mappings[].point` | `{point_id}.{point_name}` 用分号连接 |

**生成策略**：保留嵌套表表头行 + 首个数据行作为格式模板，生成器动态克隆行并按 `objectives` 实际数量填充。

### 4.5 内容课时分配表 (动态行数)

Table 1 Row[5]-[10] 的数据行，按 `calendar[]` 的章节汇总填充。

| 列 | 数据 | 对齐 |
|:---:|------|:---:|
| 章节 | `chapter_title` (WYSIWYG, 回退 `topic`) | 居中 |
| 课程内容 | `content` (各节) | 左对齐 |
| 学时数 | `hours_theory + hours_practice` | 居中 |

*   行数动态：根据课程章节数量增减
*   须与教学大纲、教材、教学进度表、PPT 完全一致

---

## 5. 首页生成注意事项 (2026-02-23 复盘)

> 以下陷阱均已修复并沉淀入 `Spec_Global.md` §5.5，记录于此作为本生成器的快速参考。

| # | 问题现象 | 根因 | 修复方案 |
|:--:|------|------|----------|
| 1 | `NameError: name 'etree' is not defined` | `lxml.etree` 在子函数中使用但顶部未显式 `import` | 顶部添加 `from lxml import etree` |
| 2 | 课程目标输出含其他课程残留内容 | `deepcopy` 克隆模板行后 cell 含多个段落（示例数据），`set_run_text()` 只修改第一段 | 赋值前调用 `_clean_cell_paragraphs(tc)` 清除多余段落 |
| 3 | 学期段落（P[4]）未替换，输出 `XXXX` | 模板改为纯 XXXX 后，原来依赖 `学年/学期` 关键字的匹配失效 | 改为按位置定位：首个 `<w:tbl>` 之前第一个含 XXXX 的段落 |
| 4 | 学期显示原始编码 `2025-2026-2` | `semester` 字段非空不触发 fallback，编码字符串直接传入模板 | `prepare_cover_context` 中正则解析：`(\d{4})-(\d{4})-([12])` → 中文学期 |
| 5 | 教材参考资料区显示 XXXX | XXXX 在独立段落（P[1]），标签在上一段（P[0]），同段落关键字查找失败 | 遍历时记录 `prev_label`，遇 XXXX 段落按前一段标签决定填充 |
| 6 | 课程团队显示原始字符串 `林昕` | `teacher.team` 直接写入，未格式化为 `姓名（职称）` | 封装 `_format_team(teacher)` 兼容字符串/列表/对象列表 |
| 7 | 课程团队字段显示主讲教师自身 | `team` 字段填写了主讲教师姓名；`_format_team()` 单字符串分支将 `teacher.title` 补充为团队职称，语义错误 | 数据层：`team` 就流空（或填其他协作教师）；代码层：去除 `default_title` 回退，字符串/列表无职称时直接输出姓名 |

---

## 6. 教案合并输出规范 (Merge Workflow)

> 整个教案打印时需要一份封面，各次课教案相连续，末尾才要求署名和时间。

基于此打印需求，我们采用了物理三段模板加 `python-docx` 式的纯 XML 拼接来合成最终输出：

### 6.1 模板拆解策略
1. **Cover (头部)**: `Template_LessonPlan_Cover.docx` — 只含大标题、Table 0、Table 1。
2. **Body (中部)**: `Template_LessonPlan.docx` — 只含单次课的题目和 16 行教学结构表，**移除了末尾的署名字段**。
3. **Footer (尾部)**: `Template_LessonPlan_Footer.docx` — 只含注意事项及所有的签名占位符。

### 6.2 合并机制
在 `scripts/gen_lessonplan_xml.py` 完成基础输出（首页、N 周教案、署名尾页）后，会自动触发 `docx_engine.py` 的 `merge_docx_files()` 方法。

*   **拼接对象**: 仅拼接 `word/document.xml` 内的 `<w:body>` 子元素（不含 `<w:sectPr>`）。
*   **分页策略**: 拼接时除首页外，每部分 `<w:body>` 首段强制插入 `<w:br w:type="page"/>`，保证排版的干净隔离。
*   **兼容性保留**: `教案_第N周_xxx.docx` 依然会保留输出。如遇个别小问题可单独改单个文件，最终可用代码一键仅触发合并，提高容错度。
