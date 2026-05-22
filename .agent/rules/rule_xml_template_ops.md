---
trigger: glob
description: 当修改 XML 生成器或文档引擎时，注入模板 XML 操作的防呆规范（iter/findall、XXXX 定位、run 合并、TOC 克隆、hyperlink 访问）。
globs:
  - "scripts/gen_*_xml.py"
  - "scripts/docx_engine.py"
---

# 规则：模板 XML 操作防呆 (Template XML Operations Safety)

> **核心原则**：不得凭经验假设模板 XML 结构——必须先解包、先审查、再写代码。

## §1 模板审查前置序列

开发任何新生成器模块前，**必须**按以下审查序列完成后再写代码：

1. 解包模板：`zipfile.ZipFile(path).read('word/document.xml')`
2. `lxml.etree` 解析，用 `body.iter(w:p)` 扁平扫描全文段落（**用 `iter` 而非 `findall`**）
3. 打印每个 XXXX 区域的实际 run 列表：`[r.find(w:t).text for r in p.iter(w:r)]`
4. 确认：段落层级（表格单元格内 P0/P1）、run 文本和数量、hyperlink 层级嵌套
5. 根据实际结构选择替换策略

## §2 `iter()` vs `findall()` 严格区分

- `body.iter(w:p)`：递归扁平化所有嵌套段落（含表格单元格、hyperlink 内）
- `body.findall(w:p)`：仅返回直接子元素
- **全文扫描必须用 `iter`**；两种方式的段落索引不等价

## §3 XXXX 占位符操作

- **包含匹配**：XXXX 的 run.text 可能是 `'XXXX'`、`'  XXXX'`、`' XXXX'`。统一用 `'XXXX' in (t.text or '')` + `.replace('XXXX', value)`，禁止精确匹配 `==`
- **纯 XXXX 段落按位置定位**：无上下文关键字时，按文档结构位置定位（如"首个表格之前第一个含 XXXX 的段落"），不可用关键字匹配
- **跨段落标签匹配**：若 XXXX 在 P[N]，标签在 P[N-1]，须遍历时记录 `prev_label`，匹配到 XXXX 段落时根据前一段标签决定填充内容
- **占位符实际计数**：开发前须通过 XML 解析确认每个单元格内的**段落数**和 **XXXX 个数**

## §4 全文扫描区域限定

目录区 XXXX 与正文节标题 XXXX 文本相同时，不限定范围的全文替换会相互干扰。**必须通过锚点段落确定区域起止索引后切片扫描**。

## §5 run 合并与多段落

- **run 合并**：替换文本前，先合并 Word 拆分的多个 `<w:r>` 为单个 run。仅替换第一个 `<w:t>` 而不清理后续 run 会导致残留文字拼接
- **多行文本用多段落**：`fill_multiline()` 必须为每行创建独立 `<w:p>` 段落（克隆原始 `pPr`），不可使用 `<w:br>` 软换行——后者导致 `firstLine` 首行缩进仅对第一行生效

## §6 TOC 与 hyperlink

- **TOC 条目不可手写**：目录条目是三件套：`pStyle=TOC1` + `<hyperlink w:anchor>` + `<instrText>PAGEREF \h</instrText>`。**必须 `copy.deepcopy` 已有正确条目，修改 anchor 和文本**
- **hyperlink 子 run 用 `iter` 访问**：`<w:hyperlink>` 内的 `<w:r>` 是其子节点，`paragraph.findall(w:r)` 跳过 hyperlink 内的 run。**必须用 `paragraph.iter(w:r)`**

## §7 克隆与合并

- **克隆行须清除残留段落**：`copy.deepcopy()` 克隆模板行后，cell 中可能遗留多个段落。赋值前先删除多余段落，只保留第一个作为格式模板（`_clean_cell_paragraphs()`）
- **跨模板 docx 合并**：使用 `docxcompose` 合并时，必须在 append 前用 ZIP/lxml 预处理：剥离 comments 扩展树，全量随机化去重 `w14:paraId`
- **嵌套循环跳过须用标志变量**：内层 `continue` 无法跳过外层，必须用 `_skip` 标志变量模式

## §8 DrawingML vs VML

模板中嵌入的图片**必须**使用 DrawingML (`w:drawing` + `wp:inline` + `pic:pic`)，**禁止** VML (`v:shape` + `v:imagedata`)。VML 负裁剪参数在 LibreOffice headless 转 PDF 时被忽略，导致图片变形。

## §9 textutil 陷阱

macOS `textutil -convert docx` 转换 `.doc → .docx` 时**不保留表格结构**。正确做法：用 Word/WPS 手动另存为 `.docx`，或使用 LibreOffice headless。

## ❌ 禁止行为

- ❌ 不审查 XML 就写替换代码
- ❌ 用 `findall` 做全文段落扫描
- ❌ 用 `==` 精确匹配 XXXX
- ❌ 用 `<w:br>` 软换行替代多段落
- ❌ 手写 TOC 条目
- ❌ 在模板中使用 VML 图片
