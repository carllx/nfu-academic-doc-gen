# Handover: 通用 docx 生成引擎 — 架构规划需求

> **日期**: 2026-02-24 (最后更新)
> **状态**: ✅ 全部完成 — 01~05 全部生成器已实现并验证
> **前置成果**: 01~05 全部生成器已实现/迁移，03_LessonPlan 已修复并验证

---

## 一、目标

**构建一个通用的 docx 生成引擎**，统一处理项目中所有生成器的 Word 文档输出。

核心流程：
```
原始模板.docx (含 XXXX 占位符)  +  course.yaml (结构化数据)
    → 通用引擎替换 XXXX → 输出.docx (格式 100% 一致)
```

**最终愿景**：不仅适用于当前 6 个教务生成器，还能通用于任意新 docx 模板需求——用户只需准备一个含 XXXX 的模板和数据 YAML，即可输出。

---

## 二、当前状态

### 2.1 已验证的方案 (01_Syllabus)

| 项 | 状态 | 说明 |
|----|:---:|------|
| XML 直接操作 | ✅ 生产验证 | 复制 ZIP → lxml 替换 `document.xml` → 写回 ZIP |
| 模板深克隆 | ✅ 生产验证 | `copy.deepcopy()` 段落组，仅替换 XXXX 文本 |
| vMerge 保全 | ✅ 生产验证 | 不触碰表格合并属性，100% 保留 |
| 格式零偏差 | ✅ 生产验证 | spacing/indent/bold 全部继承自原始 XML |
| 自动化验证 | ✅ | `verify_syllabus.py` 检查表格/vMerge/残留 |

**通用引擎代码**: `scripts/docx_engine.py` (~310 行) — 所有生成器的共享基础

### 2.2 各生成器现状 (2026-02-24 更新)

| 生成器 | 脚本 | 模板 | 状态 | 输出 |
|--------|------|------|:----:|------|
| **01_Syllabus** | `gen_syllabus_xml.py` | 1 | ✅ 已部署 | 1 份大纲 |
| **02_Schedule** | `gen_schedule_xml.py` | 1 (XXXX) | ✅ 已全量迁移 XML | 1 份进度表 |
| **03_LessonPlan** | `gen_lessonplan_xml.py` | 1 (XXXX) | ✅ 已全量迁移 XML | 8 份教案/课程 |
| **04_Experiment** | `gen_experiment_xml.py` | 4 | ✅ 已部署 | 10 份/课程 |
| **05_Assessment** | `gen_assessment_xml.py` | 6 | ✅ 已部署 | 6 份/课程 |
| **06_Presentation** | ❌ 未实现 | 2 pptx | ❌ | 非 docx 范围 |

### 2.3 核心成就：全域告别 docxtpl (2026-02-24)

随着 02_Schedule 和 03_LessonPlan 在 2 月 24 日重构完毕，**所有基于 Word 的生成器已全部切换至纯基于 `lxml` 的按节点深克隆替换方案**。
这意味着我们彻底规避了此前困扰项目的：
1. `docxtpl` 渲染导致的复杂表格 vMerge 属性合并损坏问题。
2. `<w:br/>` 软换行导致的缩进错位和首行格式破损问题。
3. jinja 模板引擎和 python-docx 混合操纵所带来的 OOXML 层节点被篡改问题。

现在的生成器引擎拥有了真正的**「模板即排版」(WYSIWYG 保证)**机制。

> ⚠️ **docxtpl 致命陷阱（历史记录）**
>
> 曾经出现过的教训记录如下，以为后人鉴：
>
> 1. **禁用 `RichText` 注入多行文本**：`RichText("Line1\nLine2")` 会在 `<w:t>` 内嵌套 `<w:r>`，产生非法 XML 并**永久腐败文档**。正确做法：传纯字符串并用 `\a` 替换 `\n`（docxtpl 会将 `\a` 转为合规的 `<w:br/>`）。
> 2. **禁止 docxtpl→python-docx 串联**：`python-docx` 加载 docxtpl 渲染后的文件会剥离关键 OOXML 节点，导致 Word 无法打开。所有逻辑必须在 `docxtpl.render()` 一次性完成，不可后用 `python-docx` 再操作。

---

## 三、需要分析的关键问题

### 3.1 架构决策

1. **统一引擎 vs 分模块引擎**
   - 方案 A: 一个通用函数 `render_docx(template, data, mapping)` 替代所有生成器
   - 方案 B: 共享工具库 + 每个生成器保留独立逻辑
   - 需权衡：通用性 vs 各模板的特殊需求（如 Syllabus 的章节克隆逻辑）

2. **XXXX 定位策略**
   - 当前方案：靠**位置上下文**（如"表格 R3 C1"或"段落关键字后的下一个 XXXX"）
   - 可选方案：使用**带标识的占位符** (`XXXX_COURSE_NAME`, `XXXX_01`) 实现精确定位
   - 需权衡：模板可读性 vs 代码复杂度

3. **映射配置化**
   - 当前方案：映射关系硬编码在 Python 函数中（如 `fill_table0`, `fill_table1`）
   - 可选方案：外部配置文件（YAML/JSON）定义 `位置 → 数据字段` 映射
   - 需权衡：灵活性 vs 复杂度 vs SSOT 原则（用户不希望增加同步负担）

4. **`.doc` 格式处理**
   - `05_Assessment` 有 4 个 `.doc`（旧格式）模板
   - 需决定：转换为 `.docx` 后统一处理？还是用其他工具链？

### 3.2 模板规范化

1. **哪些模板需要 XXXX 化**？
   - `02_Schedule/Template_Schedule.docx` 和 `03_LessonPlan/Template_LessonPlan.docx` 当前使用 `{{ }}` Jinja 变量
   - 需要盘点所有模板中的变量/占位符，统一为 XXXX

2. **重复性区域的处理模式**
   - Syllabus 的章节内容：深克隆一组段落 × N
   - Schedule 的周次行：可能需要深克隆表格行 × N
   - LessonPlan 的教学步骤：可能需要深克隆段落 × N
   - 需要抽象出通用的"模板区域克隆"机制

3. **模板中的特殊元素**（附技术方向）
   - **勾选框（☑/☐）**：OOXML 有两种实现 — `<w14:checkbox>` (结构化) 和 `<w:sym w:font="Wingdings">` (字符模拟)。需先 unpack 确认模板用哪种，再决定替换策略
   - **表格合并（vMerge/gridSpan）**：✅ 已验证 — 深克隆 + 不触碰合并属性即可保全
   - **页眉页脚**：存储在独立的 `word/header*.xml` / `word/footer*.xml` 中，通过 `word/_rels/document.xml.rels` 引用。**若页眉/页脚含 XXXX 占位符，ZIP 框架必须同时处理这些文件**（见 §4.1）
   - **图片/Logo**：替换需操作三处 — ①`word/media/` 目录中的图片文件 ②`word/_rels/document.xml.rels` 中的关系引用 ③`[Content_Types].xml` 中的 MIME 类型声明

---

## 四、已验证的技术模式 (可复用)

以下模式在 01_Syllabus 中已验证通过，新 Agent 可直接复用：

### 4.1 ZIP 操作框架
```python
shutil.copy2(src, out)                    # 1. 复制 ZIP
with zipfile.ZipFile(out, 'r') as zin:
    xml = zin.read('word/document.xml')    # 2. 读取 XML
root = etree.fromstring(xml)               # 3. 解析
# ... 替换 ...                             # 4. 修改
modified = etree.tostring(root, ...)       # 5. 序列化
# 重建 ZIP 写回                            # 6. 保存
```

> ⚠️ **必须处理的完整文件列表**（不止 `document.xml`）：
>
> | ZIP 内路径 | 何时需要处理 |
> |---|---|
> | `word/document.xml` | 始终（主内容） |
> | `word/header*.xml` / `word/footer*.xml` | 页眉/页脚含 XXXX 时 |
> | `word/_rels/document.xml.rels` | 替换图片/添加关系时 |
> | `[Content_Types].xml` | 添加新媒体类型时 |
> | `word/media/*` | 替换 Logo/图片时 |

### 4.2 核心工具函数
| 函数 | 用途 | 所在文件 |
|------|------|---------|
| `_merge_runs()` | 合并被 Word 拆分的 `<w:r>` | `gen_syllabus_xml.py` |
| `_replace_xxxx_in_text()` | 替换段落中的 XXXX | 同上 |
| `_set_run_text()` | 设置段落文本（保留格式） | 同上 |
| `fill_multiline()` | 多行文本填入（独立 `<w:p>` 段落，克隆 pPr 确保缩进对齐） | `docx_engine.py` |
| `_replace_xxxx_in_runs()` | 深克隆段落的文本替换 | 同上 |
| `copy.deepcopy()` | 段落/行克隆（保留所有 XML 属性） | Python 标准库 |

### 4.3 已知陷阱 (必读)

详见 `docs/Architecture.md` §5，核心要点：
- XXXX 可能被 Word 拆分到多个 `<w:r>` → 先 `_merge_runs()`
- `<w:numPr>` 自动编号 → 代码不写手动序号
- 深克隆全段落 vs 手动构造 → 永远选择深克隆
- 模板即 SSOT → 代码不构造任何格式属性
- **多行文本禁止 `<w:br>` 软换行** → `fill_multiline()` 必须为每行创建独立 `<w:p>` 段落（克隆原始 `pPr`），否则模板的 `firstLine` 首行缩进仅对第一行生效
- **文本拼接防标点叠加** → 拼接 `desc` 等用户填写的文本前，先 `.rstrip('。.')` 去除尾部标点
- **模板制作时必须清理多余 run** → Word 常将一个文本元素拆分为多个 `<w:r>`，模板制作脚本替换占位符时仅修改第一个 run 而不删除后续 run，会导致残留文字拼接（如 03_LessonPlan 的「第1次课教案一次课教案」）。正确做法：保留第一个 run 的格式属性，删除所有后续 run
- **克隆行 cell 的残留段落** → `deepcopy` 复制的模板行的 cell 中可能含多个段落（模板中填入的示例内容）。`set_run_text()` 只修改第一个段落，后续段落会原样残留在输出中。**正确做法**：赋值前调用 `_clean_cell_paragraphs(tc)` 清除多余段落，仅保留第一个作格式模板
- **纯 XXXX 段落不可用关键字定位** → 若模板段落内容是纯 `XXXX`（不含上下位）用关键字匹配会失效。**正确策略**：按文档结构位置定位（如"首个 `<w:tbl>` 之前第一个含 XXXX 的段落"）。开发前必须通过 XML 解析确认段落所属位置
- **跨段落 XXXX 须前置标签匹配** → 若 XXXX 占独立段落（P[N]），标签在上一段（P[N-1]），同段落关键字查找会失败。**正确做法**：遍历段落时记录 `prev_label`，遇到 XXXX 段落时依 `prev_label` 决定填充内容（见教材行填充逻辑）
- **编码化字段须解析** → `semester: '2025-2026-2'` 等编码格式字段非空，不会触发 fallback，但直接传入模板会输出原始编码。**所有编码字段必须在 `prepare_*_context` 中用正则解析成可读格式**
- **复合格式字段须格式化函数** → `teacher.team` 等需特定显示格式（`姓名（职称）`）的字段，必须封装专用格式化函数并兼容字符串/列表/对象列表三种输入，不可直接写入 YAML 原始值
- **模板示例数据不等于字段语义** → 官方模板中的示例内容（如封面「李小狼（无）」）仅为填表示范，**不可反推字段的角色限定或输出格式**。字段语义必须通过逻辑推断 + 官方文字说明确认。典型易错场景：「课程团队教师」仅含协作教师，不含主讲教师本人
- **格式化函数不跨字段借用数据** → 格式化函数（如 `_format_team()`）必须仅使用目标字段自身的数据。不得以「补全缺失值」为由从其他无关字段（如主讲教师 `title`）取值——这会混淆两个独立字段的语义边界。缺失时应直接输出原始姓名或返回空字符串
- **第三方库模块须显式导入** → `lxml.etree`、`copy` 等在文件顶部未 `import` 时会在运行时报 `NameError`，不会因宿主已加载而自动可用
- **⭐ 模板 XML 必须先审查再写代码** → 对每个 `XXXX` 区域必须通过 `zipfile + lxml` 实际解析模板，确认 run 数量、段落层级、hyperlink 嵌套等，**不得凭经验假设**。尤其注意：①同一区域的不同条目格式可能不同；②段落数量（P0=标题、P1=XXXX）可能与直觉相反
- **⭐ `body.iter(w:p)` vs `body.findall(w:p)` 本质不同** → `iter` 递归扁平化所有嵌套段落（含表格、hyperlink 内段落），顺序与光标视图一致；`findall` 仅取 body 直接子元素，会跳过嵌套段落。全文扫描替换必须用 `iter`；段落索引在不同获取方式下不等价
- **⭐ 全文扫描替换必须限定区域范围** → 目录区 XXXX（如「实验一  XXXX」）与正文节标题 XXXX（相同文本！）并存于同一文档，若不限定扫描范围执行替换，会相互干扰：目录替换先于正文节替换执行时，正文节标题失去 XXXX → `_fill_guide_experiment_sections` 无法定位节标题并跳过全部内容填充。**必须通过定位锚点段落（如「目  录」/「开课形式」）确定区域起止索引，限制 iter 范围**
- **⭐ Word TOC/PAGEREF 域结构不可手写平替** → 目录含页码的条目结构是三件套：`pStyle=TOC1` + `<hyperlink w:anchor="_TocXXX">` + `<instrText>PAGEREF _TocXXX \h</instrText>`。手写普通段落（如「综合项目 XXXX」两个 `<r>`）缺少 TOC1 样式、hyperlink 跳转和 PAGEREF 域，Word 打开时无法自动更新页码，也不可点击跳转。**正确做法：clone 已有的 TOC1 条目，修改 anchor 值和文本，写回模板**
- **⭐ 同一组条目的 XXXX run 格式不统一** → 模板中同功能的不同行，XXXX 的 run.text 可能是 `'XXXX'`（精确）、`'  XXXX'`（含前置空格）或 `' XXXX'`（一个空格）。精确匹配（`t.text == 'XXXX'`）会漏掉后两种。**统一改为包含匹配** `'XXXX' in (t.text or '')` + `.replace('XXXX', value)` 以兼容所有格式变体

**OOXML Schema 层面的额外约束**（来源：`.agent/skills/docx/SKILL.md`）：

| 约束 | 说明 | 触发场景 |
|------|------|---------|
| `xml:space="preserve"` | `<w:t>` 含前后空格时必须设置此属性，否则空格被 XML 解析器吞掉 | 替换后文本含空格 |
| `<w:pPr>` 元素顺序 | 子元素必须按 `pStyle → numPr → spacing → ind → jc → rPr` 顺序排列 | 手动构造/拼接段落属性时 |
| RSID 格式 | 必须为 8 位十六进制数（如 `00AB1234`） | 生成新元素需要 RSID 时 |
| 智能引号 | 应使用 XML 实体：`&#x2018;`/`&#x2019;`（单引号）、`&#x201C;`/`&#x201D;`（双引号） | course.yaml 数据含引号/撇号时 |

> 💡 深克隆策略天然规避了大部分 Schema 约束（因为不手动构造属性），但在区域克隆后的**拼接边界**和**文本替换结果**中仍需注意上述规则。

---

## 五、参考文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| 全局规范 | `00_Data_Context/Spec_Global.md` | §5 通用 docx 生成规范 · §6 用户偏好 |
| 大纲规范 | `01_Syllabus_Generator/Spec_Syllabus.md` | 已完成的生成器规范参考 |
| 架构说明 | `docs/Architecture.md` | §5 已知陷阱与经验教训 |
| 工作流 | `docs/Workflow.md` | 用户操作流程 |
| 数据字典 | `docs/Data_Dictionary.md` | course.yaml 字段定义 |
| XML 引擎 | `scripts/gen_syllabus_xml.py` | 已验证的参考实现 |
| 主控脚本 | `scripts/generate.py` | 当前入口 |
| 数据模式 | `scripts/course_schema.py` | Pydantic Schema |
| **DOCX Skill** | `.agent/skills/docx/SKILL.md` | docx-js / docxtpl / XML 编辑完整经验库 |

---

## 六、建议的工作计划

### Phase 1: 调研分析 (✅ 已完成)
- [x] 盘点所有模板的变量/占位符/特殊元素
- [x] 分析 02/03 现有 docxtpl 模板的 XML 结构
- [x] 评估 04/05 中 `.doc` 格式的处理策略
- [x] 确定统一引擎 vs 分模块的架构方向

### Phase 2: 方案设计 (✅ 已完成)
- [x] 设计通用引擎的 API（函数签名、配置格式）
- [x] 设计 XXXX 定位策略（位置上下文 vs 带标识占位符）
- [x] 设计"区域克隆"通用机制
- [x] 撰写实施计划 → 用户审批

### Phase 3: 实施 (✅ 已完成 2026-02-24)
- [x] 提取 `gen_syllabus_xml.py` 中的通用函数到共享模块
- [x] 迁移 02_Schedule → XML 方案
- [x] 迁移 03_LessonPlan → XML 方案
- [x] 实现 04_Experiment / 05_Assessment

### Phase 4: 验证 (✅ 已完成)
- [x] 构建通用 `validate_docx.py` 或由引擎内建的 `audit` 来验证工具，检查项包括：
  - XML 有效性
  - XXXX 残留检测
  - vMerge/gridSpan 完整性
- [x] 各生成器输出验证（用 Word 打开 + 自动化脚本双重确认）
- [x] 更新 Spec_*.md 文档


---

## 七、用户偏好 (必遵守)

> 详见 `Spec_Global.md` §6

- **SSOT 原则**：不创建需要额外同步的映射文档。模板即格式源，Schema 即数据源
- **归档不删除**：旧文件移至 `_archived/` 或 `_deprecated/`
- **中文优先**：所有文档和注释使用简体中文
- **验证驱动**：每次修改后运行验证脚本
- **深克隆优于构造**：保留格式时用 `copy.deepcopy()` 而非手动构造 XML
- **格式字段封装化**：`team`/`semester` 等需转换成显示格式的字段，封装为专用格式化函数（`_format_team()`），兼容字符串/列表/对象列表三种数据类型
- **首页模板偏好**：team = `姓名（职称）`，多人 `；` 分隔；semester 编码 `2025-2026-2` 自动解析为 `2025～2026学年第二学期`；objectives 各维度 ≥3 条；毕业要求/观测点严格依 25 年人培方案标注
