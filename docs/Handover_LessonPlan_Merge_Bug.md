# [已解决] 交接文档 (Handover): 教案合并 (Lesson Plan Merge) "Unreadable Content" Bug 排查

## 1. 核心问题描述

**问题总结**：
在重构教案生成体系后，各周次的教案模板、封面模板和尾页署名模板被拆分为 3 份（`Template_LessonPlan_Cover.docx`, `Template_LessonPlan.docx`, `Template_LessonPlan_Footer.docx`）。当使用 `gen_lessonplan_xml.py` 单独生成这 3 个部分时，文件均结构正常，可顺利通过 Word 打开。
**然而，当我们将生成的几十份单文件拼接合并为最终的 `教案_合并版.docx` 后，用户在使用 MS Word 打开该合并文档时触发弹窗报警：**
> *“Word found unreadable content in 教案_合并版.docx. Do you want to recover the contents of this document? If you trust the source of this document, click Yes.”* (Word 发现不可读内容)

## 2. 期望目标

*   分析合并后 `教案_合并版.docx` 的底层 XML（`word/document.xml` 及其周边关联定义，如 `_rels`、`[Content_Types].xml` 等），找出真正引发 Word 解析器报错（Unreadable Content）的 OOXML 结构缺陷。
*   解决该缺陷，使得多份单页教案文档，能完美合并为一份没有任何报警弹窗的 `教案_合并版.docx`。

## 3. 已尝试的修复手段与避坑记录 (Failed Attempts)

接手的 Agent 需要重点注意，**以下方向已经充分验证过，且均未彻底解决弹窗爆破问题**，请不要重复踩坑：

### ❌ 尝试一：纯 XML 文本拼接 `<w:body>` (最初方案)
*   **做法**：把每份后续文件的 `<w:body>` 内部 `w:p`/`w:tbl` 等子元素克隆并插入基础模板体内，跳过后续模板的 `w:sectPr`。
*   **失效原因**：虽然 lxml 解析正常，并手动插入了分页符，但纯 XML 克隆破坏了诸如样式 (`w:pStyle`) 继承、`rId` 关系索引以及页眉页脚的正确映射；导致 Word 报该错。

### ❌ 尝试二：切入使用专业库 `docxcompose`
*   **做法**：在 `docx_engine.py` 中引入了 `docxcompose`，期望该库自动处理不同文档合并时的计数器、rId 关系映射等。
*   **进展**：`docxcompose.Composer` 的运行未抛出任何 Python 侧异常，成功合并出目标文档，也能被 `python-docx` 库正常加载。
*   **失效原因**：生成的合并版拿到真机用 MS Word 打开，弹窗报错**依然存在**。

### ❌ 尝试三：修复 ID 冲突 (`w14:paraId` 和 `w14:textId`)
*   **背景**：Office 2010+ 的机制会给段落附加唯一十六进制 ID（`w14:paraId` 等）。因为多周教案是从同一个模板克隆的表格和段落，导致合并后内部存在大量相同的 `w14:paraId`。
*   **做法**：修改 `docx_engine.py` 内部写入逻辑，在保存新教案生成的 XML 时，全量 `del` 清除这些 `w14` 属性。
*   **失效原因**：重新合并后排查证明 XML DOM 确实变得极其纯净，但打开 Word 依然弹窗报警。说明 ID 碰撞并不是致命原因。

### ❌ 尝试四：修复末尾 `<w:tbl>` 无 `<w:p>` 规范问题
*   **背景**：查阅 OOXML (ECMA-376) 规范，`<w:body>` 结尾（或任何一节结尾）不能直接以表格 `<w:tbl>` 作为最终子节点，必须有至少一个 `<w:p>`。此前为了去掉“签署”区域在模板拆分时让模板底层变成了 `<w:tbl>` 接 `<w:sectPr>`。
*   **做法**：通过隔离脚本遍历所有 3 个 Template docx，在其末端 `w:sectPr` （或尾部）之前强行注入了一行空的 `<w:p></w:p>` 以满足 OOXML 基本闭环。
*   **失效原因**：所有生成物内部都补齐了尾随段落。合并后问题依旧。

## 4. 后续排查建议 (Next Steps for Agent)

目前猜测该问题潜伏在更深层的关联性或不合规的模板特定节点里。请依以下思路开启研究：

1.  **逐段溯源法 (TDD Isolation)**：
    *   在刚才的排查中，在 `/tmp/merge_tests/` 下存在数个组合（如「封面+第一周」、「单第一周+第二周」等）。
    *   利用苹果脚本或借助用户手动打开测试件，看究竟是“任何两份合并”都会炸，还是“特定带有封面的合并”才会炸（因为封面的格式/页眉页脚与后面不一样）。若是“特定相加”爆炸，那大概率是 Section 属性（`w:sectPr`）不兼容导致。
2.  **Schema Linter (OpenXML Validator)**：
    *   将未报错的单周文档与报错的合并版文档解压：`python scripts/office/unpack.py <docx> unpacked/`。
    *   对比它们，或者看是否有某些 `sectPr` 重复了，或者由于合并导致跨域的 `Bookmark` 冲撞、超链接/交叉引用断裂，甚至可能是合并前的教案 `Template_LessonPlan.docx` 结构深处其实就带有隐形错误，被 composer 放大。
3.  **替代合并方案**：
    *   考虑使用 `pandoc`，但 `pandoc` 往往重制样式并丢失排版细节（学校模板要求极高），不太适用。
    *   考虑是否有其它更低级的 XML 检查方式能定位 `document.xml` 中未闭合的结构或遗漏的命名空间。例如 `w:trHeight` 设置、不合法的图像格式，或者在拆解合并时对 `word/_rels/document.xml.rels` 处理漏掉的关系节点。

**接盘的 Agent 启动动作**：
阅读此文档后，直接用 CLI unpack 解压生成物，检查生成的 XML 和 `rels` 文件，查清到底是哪个节点引发了 "unreadable content"！

---

## 5. 最终根因与解决方案 (Resolution)

> **状态: ✅ Bug 已彻底修复 (2026-02-25)**

### 5.1 终极根因 (Root Cause)
经过深入的逐层解构和二分法交叉合并测试，最终确认报错由 **两个叠加因素** 导致：
1. `docxcompose` 的 ID 映射缺陷：它只会重组关系 `rId`，但**不会重映射段落级别 ID（`w14:paraId` / `w14:textId`）以及批注/评论（Comments）系统**。
2. 悬空引用与冲突：在对单文档执行去重（如删除了 `document.xml` 里的多余段落）时，孤立的微软特有批注文件（`commentsIds.xml`, `commentsExtended.xml`, `commentsExtensible.xml`）残留在了 ZIP `word/` 目录下，并继续通过相同的 `paraId` 引用主文档中已不存在的段落；同时，由于多个教案部分均拷贝自同一底层模板（如 id=0-9），合并并入后文档中出现了数十个 `paraId` 冲突。Word 严格的 OOXML 解析器一并触发拦截。

### 5.2 解决方案 (The Fix)
在 `scripts/docx_engine.py` 的 `merge_docx_files` 逻辑中，**必须在喂给 `docxcompose` 前增加对单个文档的预处理（Pre-cleaning）步骤**：
- **清理文档 Comments**：从 `word/document.xml` 中剔除所有的 `commentRangeStart`/`commentRangeEnd`/`commentReference`；将 `comments.xml` 乃至所有的 extensions (Id/Extended/Extensible 等) 以及 `people.xml` 直接从 ZIP 中 `os.remove`。同时清理 `document.xml.rels` 和 `[Content_Types].xml` 里关于 comments 的绑定节点。
- **重新随机化全量 W14 IDs**：遍历洗干净的 `document.xml`，重塑所有的 `w14:paraId` 和 `textId`（生成全新防撞 8 字符 HEX 字符串）。
  
清洗完毕的子文档通过 `docxcompose` 合并，MS Word 再也不会触发展示 "Unreadable Content" 错误，且合并版格式完美无瑕。相关经验已升格纳入 `Spec_Global.md` 与 `.agent/skills/docx/SKILL.md` 中以防后人再次踩坑。
