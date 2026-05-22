# 渲染降级逻辑 (Rendering Logic)

> 本文档说明生成器如何根据 `schema_type` 动态调整课程目标的 XML 渲染输出。

## 1. `detailed` 模式（2025版，4列表格）

保留模板原貌，不做任何结构修改。直接填充 4 列：

| 列 | 内容 | 数据源 |
|:---|:---|:---|
| 维度名 | 知识目标1 | `objectives.knowledge[0].index` |
| 描述 | 描述文本 | `objectives.knowledge[0].desc` |
| 毕业要求 | 2 专业知识 | `mappings[].requirement` |
| 观测点 | 2.2 跨学科知识整合 | `mappings[].point` |

## 2. `coarse` 模式（2024版，3列表格）

### 核心函数：`_remove_table_last_column(table)`

**原理**：物理删除 `<w:tbl>` 中每一行的最后一个 `<w:tc>` 单元格。

**实现要点**：
1. 遍历 `table.findall(w:tr)` 获取所有行
2. 对每行，找到所有 `<w:tc>` 子元素
3. 删除最后一个 `<w:tc>`（`row.remove(cells[-1])`）
4. **注意**：必须同时调整 `<w:tblGrid>` 的列定义（`<w:gridCol>`），删除最后一个 gridCol
5. 如果表头行有合并单元格（`<w:gridSpan>`），须相应调整 span 值

**陷阱**：
- 不可仅隐藏列（设置宽度为0），必须物理删除——否则 Word 打开时仍显示空列
- 删列后须检查表格总宽度是否需要重新分配

## 3. `none` 模式（2023版，纯段落）

### 核心函数：`_build_objectives_paragraphs(objectives, insert_point)`

**原理**：删除整个课程目标表格，在原位置插入纯文本段落组。

**实现步骤**：
1. 定位课程目标表格（通过前置段落锚点或表格索引）
2. 记录表格在 body 中的位置索引
3. `body.remove(table)` 删除表格
4. 在记录的位置插入段落组：
   - 标题段落：「二、课程目标」
   - 分类标题：「（一）知识目标」「（二）能力目标」「（三）素质目标」
   - 每条目标作为独立段落，带序号

**段落格式**：
- 克隆模板中已有段落的 `<w:pPr>`（保持字体、字号、缩进一致）
- 每条目标为独立 `<w:p>`，不使用 `<w:br>` 软换行
- 序号格式：`1. ` + 目标描述文本 + `；`（最后一条用 `。`）

**陷阱**：
- 段落插入须用 `body.insert(index, new_p)` 并递增 index
- 不可用 `addnext`/`addprevious`——在循环中会错位
- 必须处理教案和大纲两处的课程目标表格（位置不同）
