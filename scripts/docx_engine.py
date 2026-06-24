"""
docx_engine.py — 通用 DOCX 生成引擎 (纯 XML 操作)

所有生成器共享的核心工具库。

核心策略：
  1. 复制原始模板 .docx (ZIP) 到输出目录
  2. 从 ZIP 中解压指定 XML 文件 (document.xml, header*.xml 等)
  3. 用 lxml 替换 XXXX 占位符为实际数据
  4. 写回 ZIP

设计原则：
  - 模板即 SSOT：代码不构造任何格式属性
  - 深克隆优于构造：保留格式时用 copy.deepcopy()
  - 函数签名为 public（去掉前缀下划线），因为是公共 API
"""

import copy
import os
import shutil
import zipfile
from pathlib import Path
from typing import Callable, List, Optional

from lxml import etree

# ═══════════════════════════════════════════════════════════════════════
# 0. 常量与命名空间
# ═══════════════════════════════════════════════════════════════════════

NSMAP = {
    'w':  'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r':  'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
}

# xml:space="preserve" 的完整属性键
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'

# 需要从输出文件中移除的 comment 相关 ZIP 部件
COMMENT_PARTS = {
    'word/comments.xml',
    'word/commentsIds.xml',
    'word/commentsExtended.xml',
    'word/commentsExtensible.xml',
    'word/people.xml',
}

# comment 关系类型后缀（用于匹配 Relationship Type URI）
COMMENT_REL_TYPES = {
    'comments', 'commentsIds', 'commentsExtended',
    'commentsExtensible', 'people',
}


def qn(tag: str) -> str:
    """将 'w:t' 格式转为 Clark notation '{ns}t'。

    示例:
        qn('w:t')  → '{http://...wordprocessingml/2006/main}t'
        qn('r:id') → '{http://...officeDocument/2006/relationships}id'
    """
    prefix, local = tag.split(':')
    return f'{{{NSMAP[prefix]}}}{local}'


# ═══════════════════════════════════════════════════════════════════════
# 1. XML 底层工具
# ═══════════════════════════════════════════════════════════════════════

def get_paragraph_text(p_elem) -> str:
    """获取段落的完整文本。"""
    texts = []
    for t in p_elem.iter(qn('w:t')):
        if t.text:
            texts.append(t.text)
    return ''.join(texts)


def get_cell_text(tc_elem) -> str:
    """获取单元格的完整文本。"""
    texts = []
    for t in tc_elem.iter(qn('w:t')):
        if t.text:
            texts.append(t.text)
    return ''.join(texts)


def strip_comment_marks(root) -> None:
    """从 XML 根元素中移除所有 comment 相关标记。

    移除 commentRangeStart、commentRangeEnd 元素，
    以及包含 commentReference 的整个 w:r run。
    用于 render_docx() 和 merge 流程的统一清理。
    """
    ns_w = NSMAP['w']
    for tag_name in ['commentRangeStart', 'commentRangeEnd']:
        for elem in list(root.iter(f'{{{ns_w}}}{tag_name}')):
            parent = elem.getparent()
            if parent is not None:
                parent.remove(elem)
    # commentReference 通常嵌套在专用 w:r 内，整个 run 一起删除
    for cr in list(root.iter(f'{{{ns_w}}}commentReference')):
        run = cr.getparent()
        if run is not None and run.tag == f'{{{ns_w}}}r':
            run_parent = run.getparent()
            if run_parent is not None:
                run_parent.remove(run)


def merge_runs(p_elem):
    """合并段落中相邻且格式相同的 <w:r> 元素。

    解决 XXXX 被 Word 拆分到多个 run 的问题。
    策略: 将所有 w:r 的文本合并到第一个 run 中, 删除后续 run。
    注意: 只合并纯文本 run (不含图片/嵌入对象等)。
    """
    runs = p_elem.findall(qn('w:r'))
    if len(runs) <= 1:
        return

    # 收集纯文本 run 的连续分组
    groups = []
    current_group = []

    for r in runs:
        t_elem = r.find(qn('w:t'))
        # 如果 run 包含非文本内容(如 drawing, sym 等), 断开分组
        has_non_text = any(
            child.tag != qn('w:rPr') and child.tag != qn('w:t')
            for child in r
        )
        if has_non_text or t_elem is None:
            if len(current_group) > 1:
                groups.append(current_group)
            current_group = []
        else:
            current_group.append(r)

    if len(current_group) > 1:
        groups.append(current_group)

    # 对每个分组执行合并
    for group in groups:
        combined_text = ''
        for r in group:
            t = r.find(qn('w:t'))
            if t is not None and t.text:
                combined_text += t.text

        # 将合并文本写入第一个 run
        first_t = group[0].find(qn('w:t'))
        first_t.text = combined_text
        first_t.set(XML_SPACE, 'preserve')

        # 删除后续 run
        for r in group[1:]:
            r.getparent().remove(r)


# ═══════════════════════════════════════════════════════════════════════
# 2. 文本替换工具
# ═══════════════════════════════════════════════════════════════════════

def clean_text_for_docx(text: str) -> str:
    """清理多余的 Markdown 标记和特定禁止符号。"""
    if not isinstance(text, str):
        return text
    return text.replace('**', '').replace('【', '').replace('】', '')


def set_run_text(p_elem, text: str):
    """设置段落中第一个 run 的文本。

    如果段落有 run，保留第一个 run 的格式并设置文本，删除多余 run。
    如果段落无 run，创建一个新的。
    """
    runs = p_elem.findall(qn('w:r'))
    if runs:
        # 保留第一个 run, 清空其文本
        first_run = runs[0]
        t = first_run.find(qn('w:t'))
        if t is None:
            t = etree.SubElement(first_run, qn('w:t'))
        t.text = clean_text_for_docx(text)
        t.set(XML_SPACE, 'preserve')
        # 删除多余 run
        for r in runs[1:]:
            p_elem.remove(r)
    else:
        # 创建新 run，从段落默认格式 (pPr > rPr) 继承字体/字号
        r = etree.SubElement(p_elem, qn('w:r'))
        pPr = p_elem.find(qn('w:pPr'))
        if pPr is not None:
            pPr_rPr = pPr.find(qn('w:rPr'))
            if pPr_rPr is not None:
                r.insert(0, copy.deepcopy(pPr_rPr))
        t = etree.SubElement(r, qn('w:t'))
        t.text = clean_text_for_docx(text)
        t.set(XML_SPACE, 'preserve')


def replace_xxxx(p_elem, replacement: str):
    """替换段落中所有 <w:t> 的 XXXX 为指定文本。

    先合并 runs, 再执行文本替换。
    """
    merge_runs(p_elem)
    for t in p_elem.iter(qn('w:t')):
        if t.text and 'XXXX' in t.text:
            cleaned_replacement = clean_text_for_docx(replacement)
            t.text = t.text.replace('XXXX', cleaned_replacement)
            t.set(XML_SPACE, 'preserve')


def replace_jinja_tag(p_elem, tag: str, replacement: str):
    """替换段落中 {{ tag }} 形式的 Jinja 变量。

    向后兼容旧模板中的 Jinja 占位符。
    """
    merge_runs(p_elem)
    patterns = [f'{{{{ {tag} }}}}', f'{{{{{tag}}}}}']
    for t in p_elem.iter(qn('w:t')):
        if t.text:
            for pat in patterns:
                if pat in t.text:
                    cleaned_replacement = clean_text_for_docx(replacement)
                    t.text = t.text.replace(pat, cleaned_replacement)
                    t.set(XML_SPACE, 'preserve')


def fill_multiline(p_elem, text: str, clear_list_indent: bool = False, fix_spacing: bool = False):
    """将多行文本填入段落，每行创建独立 <w:p> 段落。

    使用多段落替代 <w:br> 软换行，确保每行都继承模板的
    pPr 段落属性（对齐方式、行间距等）。

    Args:
        p_elem: 原始段落 XML 元素
        text: 多行文本内容
        clear_list_indent: 如果为 True，将清除 pPr 中的首行缩进 (firstLine)，
                           确保多行列表内容左侧对齐（符合教务文档列表规范）。
        fix_spacing: 如果为 True，将清除 pPr 中的段前段后间距 (before/after)，
                     使多行列表项之间更加紧凑。
    """
    if not text:
        set_run_text(p_elem, '')
        return

    text = clean_text_for_docx(text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        set_run_text(p_elem, '')
        return

    # 获取并处理原始段落的 pPr
    template_pPr = None
    pPr = p_elem.find(qn('w:pPr'))
    if pPr is not None:
        template_pPr = copy.deepcopy(pPr)
        if clear_list_indent:
            # 清除 firstLine 缩进
            ind = template_pPr.find(qn('w:ind'))
            if ind is not None:
                for attr in ['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}firstLine', 
                            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}firstLineChars']:
                    if attr in ind.attrib:
                        del ind.attrib[attr]
        
        if fix_spacing:
            # 清除段前段后间距
            spacing = template_pPr.find(qn('w:spacing'))
            if spacing is not None:
                for attr in ['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}before',
                            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after',
                            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}beforeLines',
                            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}afterLines']:
                    if attr in spacing.attrib:
                        del spacing.attrib[attr]

    # 更新第一行的 pPr
    if (clear_list_indent or fix_spacing) and pPr is not None:
        # 替换原始 pPr 以应用清理后的属性
        p_elem.replace(pPr, copy.deepcopy(template_pPr))

    # 获取现有 run 的 rPr（字体、字号等）
    runs = p_elem.findall(qn('w:r'))
    template_rPr = None
    if runs:
        rPr = runs[0].find(qn('w:rPr'))
        if rPr is not None:
            template_rPr = copy.deepcopy(rPr)
        # 删除所有现有 run
        for r in runs:
            p_elem.remove(r)

    # 第一行：填入原始段落
    first_line = lines[0].strip()
    text_run = etree.SubElement(p_elem, qn('w:r'))
    if template_rPr is not None:
        text_run.insert(0, copy.deepcopy(template_rPr))
    t = etree.SubElement(text_run, qn('w:t'))
    t.text = first_line
    t.set(XML_SPACE, 'preserve')

    # 后续行：在父元素（w:tc）中追加新的 <w:p>
    if len(lines) > 1:
        parent = p_elem.getparent()
        p_index = list(parent).index(p_elem)

        for li, line in enumerate(lines[1:], start=1):
            line = line.strip()
            new_p = etree.Element(qn('w:p'))
            if template_pPr is not None:
                new_p.insert(0, copy.deepcopy(template_pPr))
            
            new_run = etree.SubElement(new_p, qn('w:r'))
            if template_rPr is not None:
                new_run.insert(0, copy.deepcopy(template_rPr))
            new_t = etree.SubElement(new_run, qn('w:t'))
            new_t.text = line
            new_t.set(XML_SPACE, 'preserve')
            parent.insert(p_index + li, new_p)


def replace_in_runs(p_elem, replacement: str, full_replace: bool = False):
    """在深克隆的段落中替换文本。

    Args:
        p_elem: 段落 XML 元素 (已深克隆)
        replacement: 替换文本
        full_replace: True=替换整个 run 文本(章标题/知识点), False=仅替换 XXXX
    """
    if full_replace:
        runs = p_elem.findall(qn('w:r'))
        if runs:
            first_t = runs[0].find(qn('w:t'))
            if first_t is not None:
                first_t.text = clean_text_for_docx(replacement)
                first_t.set(XML_SPACE, 'preserve')
            for r in runs[1:]:
                p_elem.remove(r)
    else:
        for t in p_elem.iter(qn('w:t')):
            if t.text and 'XXXX' in t.text:
                cleaned_replacement = clean_text_for_docx(replacement)
                t.text = t.text.replace('XXXX', cleaned_replacement)
                t.set(XML_SPACE, 'preserve')


# ═══════════════════════════════════════════════════════════════════════
# 3. 表格工具
# ═══════════════════════════════════════════════════════════════════════

def find_table_by_header(root, keyword: str):
    """通过表头关键字定位表格。

    遍历所有 <w:tbl>，检查第一行的文本是否包含关键字。
    返回找到的 <w:tbl> 元素，未找到返回 None。
    """
    for tbl in root.iter(qn('w:tbl')):
        rows = tbl.findall(qn('w:tr'))
        if rows:
            header_text = get_cell_text(rows[0])
            if keyword in header_text:
                return tbl
    return None


def get_table_cell(table, row: int, col: int):
    """获取指定行列的单元格 <w:tc> 元素。

    Args:
        table: <w:tbl> 元素
        row: 行索引 (0-based)
        col: 列索引 (0-based)

    Returns:
        <w:tc> 元素，越界返回 None。
    """
    rows = table.findall(qn('w:tr'))
    if row >= len(rows):
        return None
    cells = rows[row].findall(qn('w:tc'))
    if col >= len(cells):
        return None
    return cells[col]


def clone_table_row(table, row_index: int, count: int):
    """克隆表格行 N 次并插入到原始行之后。

    用于进度表周次行、实验项目行等需要动态扩展的场景。

    Args:
        table: <w:tbl> 元素
        row_index: 要克隆的行索引 (0-based)
        count: 克隆次数

    Returns:
        新插入的所有 <w:tr> 元素列表。
    """
    rows = table.findall(qn('w:tr'))
    if row_index >= len(rows):
        return []

    template_row = rows[row_index]
    new_rows = []
    insert_after = template_row

    for _ in range(count):
        new_row = copy.deepcopy(template_row)
        insert_after.addnext(new_row)
        insert_after = new_row
        new_rows.append(new_row)

    return new_rows


def remove_table_row(table, row_index: int):
    """删除表格中指定的行。

    用于 40 学时锁死 3 个实验时，裁切掉多余的模板行。

    Args:
        table: <w:tbl> 元素
        row_index: 要删除的行索引 (0-based)

    Returns:
        bool: 是否成功删除
    """
    rows = table.findall(qn('w:tr'))
    if row_index >= len(rows) or row_index < 0:
        return False
        
    row_to_remove = rows[row_index]
    row_to_remove.getparent().remove(row_to_remove)
    return True


# ═══════════════════════════════════════════════════════════════════════
# 4. 区域克隆工具
# ═══════════════════════════════════════════════════════════════════════

def extract_paragraph_group(body, start_keyword: str, end_keyword: str):
    """提取两个关键字之间的段落组作为克隆模板。

    在 <w:body> 的直接子元素中，查找包含 start_keyword 的段落
    和包含 end_keyword 的段落之间的所有 <w:p> 元素。

    Args:
        body: <w:body> 元素
        start_keyword: 起始段落中的关键字
        end_keyword: 结束段落中的关键字

    Returns:
        (start_idx, end_idx, paragraphs) 三元组。
        paragraphs 是原始 XML 元素列表（未克隆）。
    """
    all_children = list(body)
    start_idx = None
    end_idx = None

    for ci, child in enumerate(all_children):
        if child.tag == qn('w:p'):
            text = get_paragraph_text(child)
            if start_keyword in text and start_idx is None:
                start_idx = ci
            elif end_keyword in text and start_idx is not None:
                end_idx = ci
                break

    if start_idx is None or end_idx is None:
        return None, None, []

    paragraphs = [
        child for child in all_children[start_idx + 1: end_idx]
        if child.tag == qn('w:p')
    ]
    return start_idx, end_idx, paragraphs


def remove_elements_between(body, start_idx: int, end_idx: int):
    """删除 body 中 start_idx 和 end_idx 之间的所有子元素（不含两端）。"""
    all_children = list(body)
    for elem in all_children[start_idx + 1: end_idx]:
        body.remove(elem)


# ═══════════════════════════════════════════════════════════════════════
# 5. ZIP 操作框架
# ═══════════════════════════════════════════════════════════════════════

def render_docx(
    template_path: Path,
    output_path: Path,
    fill_fn: Callable[[etree._Element, dict], None],
    context: dict,
    xml_files: Optional[List[str]] = None,
):
    """通用 docx 渲染入口。

    流程:
    1. 复制 template ZIP → output
    2. 解压指定 XML 文件
    3. 对每个 XML 调用 fill_fn(root, context)
    4. 写回 ZIP

    Args:
        template_path: 原始模板 .docx 路径
        output_path: 输出文件路径
        fill_fn: 填充回调函数（由各生成器实现）
            签名: fill_fn(root: etree._Element, context: dict) -> None
        context: 数据上下文
        xml_files: 需要处理的 ZIP 内 XML 文件列表。
            默认 ['word/document.xml']。
            可扩展到 header/footer: ['word/document.xml', 'word/header1.xml']
    """
    if xml_files is None:
        xml_files = ['word/document.xml']

    # Step 1: 复制 ZIP
    shutil.copy2(template_path, output_path)

    try:
        # Step 2: 读取并解析所有目标 XML
        modified_xmls = {}
        with zipfile.ZipFile(output_path, 'r') as zin:
            zip_entries = zin.namelist()
            for xml_file in xml_files:
                if xml_file not in zip_entries:
                    print(f"    ⚠️ ZIP 中未找到 {xml_file}，跳过")
                    continue
                xml_content = zin.read(xml_file)
                root = etree.fromstring(xml_content)

                # Step 3: 调用填充回调
                fill_fn(root, context)
                # Step 3.5: 清理 w14:paraId 和 w14:textId 以防止克隆导致的 ID 重复
                # Word 要求这些 ID 全局唯一，重复会导致 "内容不可读" 错误
                for elem in root.iter():
                    for attr in list(elem.attrib.keys()):
                        if attr in [
                            '{http://schemas.microsoft.com/office/word/2010/wordml}paraId',
                            '{http://schemas.microsoft.com/office/word/2010/wordml}textId'
                        ]:
                            del elem.attrib[attr]

                # Step 3.6: 剥离模板中的 comment 标记
                # 模板保留 comments 作为填写说明，但输出文件不应携带
                strip_comment_marks(root)

                # 序列化
                modified_xmls[xml_file] = etree.tostring(
                    root, xml_declaration=True, encoding='UTF-8', standalone=True
                )

        # Step 4: 重建 ZIP 写回（同时剥离 comment 相关 ZIP 部件）
        tmp_path = output_path.with_suffix('.tmp.docx')
        with zipfile.ZipFile(output_path, 'r') as zin:
            entries = zin.namelist()
            parts_to_skip = {p for p in COMMENT_PARTS if p in entries}

            # 清理 [Content_Types].xml 中的 comment Override
            if parts_to_skip and '[Content_Types].xml' in entries:
                ct = etree.fromstring(zin.read('[Content_Types].xml'))
                for override in list(ct):
                    part_name = override.get('PartName', '').lstrip('/')
                    if part_name in parts_to_skip:
                        ct.remove(override)
                modified_xmls['[Content_Types].xml'] = etree.tostring(
                    ct, xml_declaration=True, encoding='UTF-8', standalone=True
                )

            # 清理 document.xml.rels 中的 comment Relationship
            rels_path = 'word/_rels/document.xml.rels'
            if parts_to_skip and rels_path in entries:
                rels = etree.fromstring(zin.read(rels_path))
                for rel in list(rels):
                    target = rel.get('Target', '')
                    full_target = ('word/' + target) if not target.startswith('/') else target.lstrip('/')
                    rel_type = rel.get('Type', '').split('/')[-1]
                    if full_target in parts_to_skip or rel_type in COMMENT_REL_TYPES:
                        rels.remove(rel)
                modified_xmls[rels_path] = etree.tostring(
                    rels, xml_declaration=True, encoding='UTF-8', standalone=True
                )

            with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    if item.filename in parts_to_skip:
                        continue  # 跳过 comment 相关文件
                    if item.filename in modified_xmls:
                        zout.writestr(item, modified_xmls[item.filename])
                    else:
                        zout.writestr(item, zin.read(item.filename))

        # 替换原文件
        os.replace(tmp_path, output_path)

    except Exception:
        # 清理临时文件
        tmp_path = output_path.with_suffix('.tmp.docx')
        if tmp_path.exists():
            os.remove(tmp_path)
        raise


# ═══════════════════════════════════════════════════════════════════════
# 6. 多文件合并
# ═══════════════════════════════════════════════════════════════════════

def merge_docx_files(
    parts: List[Path],
    output_path: Path,
    page_break: bool = True,
) -> None:
    """合并多个 docx 文件为一个文档。

    策略：使用 docxcompose 进行文档合并，但在合并前对每个文档
    进行预处理，清除 comments、w14 重复 ID 等会导致 docxcompose
    合并后触发 Word "Unreadable Content" 错误的元素。

    Args:
        parts: 要合并的 docx 文件路径列表（至少 1 个）
        output_path: 合并输出路径
        page_break: 各部分之间是否插入分页符（默认 True）
    """
    if not parts:
        raise ValueError("merge_docx_files: parts 不能为空")

    if len(parts) == 1:
        shutil.copy2(parts[0], output_path)
        return

    import docx
    from docxcompose.composer import Composer

    # ── 预处理：清理每个文档的 comments 和 w14 冲突 ──
    # docxcompose 不会重新映射 comment IDs，
    # 导致多个文档中 id=0,1,2... 重复 → Word 报 "Unreadable Content"。
    # 解决方案：在合并前从所有文档中剥离 comments 相关标记。
    cleaned_parts = []
    try:
        import tempfile
        tmp_dir = tempfile.mkdtemp(prefix='docx_merge_')
        
        for idx, part_path in enumerate(parts):
            cleaned = Path(tmp_dir) / f"part_{idx}.docx"
            _clean_docx_for_merge(part_path, cleaned)
            cleaned_parts.append(cleaned)

        master = docx.Document(cleaned_parts[0])
        composer = Composer(master)
        
        for part_path in cleaned_parts[1:]:
            if page_break:
                master.add_page_break()
            doc_part = docx.Document(part_path)
            composer.append(doc_part)
            
        composer.save(output_path)
    except Exception as e:
        print(f"合并失败: {e}")
        raise
    finally:
        # 清理临时文件
        for cp in cleaned_parts:
            if cp.exists():
                os.remove(cp)
        if cleaned_parts:
            tmp_parent = cleaned_parts[0].parent
            if tmp_parent.exists():
                try:
                    os.rmdir(tmp_parent)
                except OSError:
                    pass


def _clean_docx_for_merge(src: Path, dst: Path) -> None:
    """清理 docx 文件以准备合并。
    
    移除所有 comments 相关内容和去重 w14 IDs，
    防止 docxcompose 合并后的 ID 冲突。
    """
    W14_PARA = '{http://schemas.microsoft.com/office/word/2010/wordml}paraId'
    W14_TEXT = '{http://schemas.microsoft.com/office/word/2010/wordml}textId'
    
    modified = {}
    parts_to_remove = set()
    
    with zipfile.ZipFile(src, 'r') as zin:
        entries = zin.namelist()
        parts_to_remove = {p for p in COMMENT_PARTS if p in entries}
        
        # 1. 清理 document.xml：移除 comment 标记和去重 w14 ID
        if 'word/document.xml' in entries:
            doc = etree.fromstring(zin.read('word/document.xml'))
            
            # 移除 comment 相关 XML 标记
            strip_comment_marks(doc)
            
            # 去重 w14:paraId 和 w14:textId（生成新的唯一 ID）
            import random
            seen_para = set()
            seen_text = set()
            for elem in doc.iter():
                pid = elem.get(W14_PARA)
                if pid:
                    if pid in seen_para:
                        # 生成新的唯一 ID
                        new_id = f'{random.randint(0, 0xFFFFFFFF):08X}'
                        while new_id in seen_para:
                            new_id = f'{random.randint(0, 0xFFFFFFFF):08X}'
                        elem.set(W14_PARA, new_id)
                        seen_para.add(new_id)
                    else:
                        seen_para.add(pid)
                
                tid = elem.get(W14_TEXT)
                if tid:
                    if tid in seen_text:
                        new_id = f'{random.randint(0, 0xFFFFFFFF):08X}'
                        while new_id in seen_text:
                            new_id = f'{random.randint(0, 0xFFFFFFFF):08X}'
                        elem.set(W14_TEXT, new_id)
                        seen_text.add(new_id)
                    else:
                        seen_text.add(tid)
            
            modified['word/document.xml'] = etree.tostring(
                doc, xml_declaration=True, encoding='UTF-8', standalone=True
            )
        
        # 2. 清理 [Content_Types].xml
        if parts_to_remove:
            ct = etree.fromstring(zin.read('[Content_Types].xml'))
            for override in list(ct):
                part_name = override.get('PartName', '').lstrip('/')
                if part_name in parts_to_remove:
                    ct.remove(override)
            modified['[Content_Types].xml'] = etree.tostring(
                ct, xml_declaration=True, encoding='UTF-8', standalone=True
            )
        
        # 3. 清理 document.xml.rels
        rels_path = 'word/_rels/document.xml.rels'
        if parts_to_remove and rels_path in entries:
            rels = etree.fromstring(zin.read(rels_path))
            for rel in list(rels):
                target = rel.get('Target', '')
                full_target = 'word/' + target if not target.startswith('/') else target.lstrip('/')
                rel_type = rel.get('Type', '').split('/')[-1]
                if full_target in parts_to_remove or rel_type in COMMENT_REL_TYPES:
                    rels.remove(rel)
            modified[rels_path] = etree.tostring(
                rels, xml_declaration=True, encoding='UTF-8', standalone=True
            )
        
        # 4. 重建 ZIP
        with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename in parts_to_remove:
                    continue
                if item.filename in modified:
                    zout.writestr(item, modified[item.filename])
                else:
                    zout.writestr(item, zin.read(item.filename))


# ═══════════════════════════════════════════════════════════════════════
# 7. 归档命名工具
# ═══════════════════════════════════════════════════════════════════════

def archive_filename(
    context: dict,
    doc_type: str,
    class_info: dict = None,
    ext: str = '.docx',
) -> str:
    """生成云盘归档命名格式的文件名 (Spec_Global §8)。

    命名公式:
        {archive_id}{teacher.name}+{年级}+{专业}[+{班级}]+《{course.name}》+{文档类型}.ext

    archive_id 为**班级级别**（classes[].archive_id），非教师级别。
    - per-class 文档：使用指定班级的 archive_id
    - per-course 单班文档：使用该班的 archive_id
    - per-course 多班文档：拼接所有班级的 "{id}{name}" 前缀

    Args:
        context: 全局上下文 (含 course, teacher)
        doc_type: 文档类型 (教学大纲/教学进度表/教案/实验指导书/A卷/B卷...)
        class_info: 班级字典。per-class 文档必传。
        ext: 文件扩展名 (默认 '.docx')

    Returns:
        归档格式文件名字符串。若 archive_id 缺失返回 None。
    """
    import re as _re

    course = context.get('course', {})
    teacher = context.get('teacher', {})
    teacher_name = teacher.get('name', '')
    course_name = course.get('name', '')
    major = course.get('major', '')
    classes = course.get('classes', [])

    # ── 年级推断 ──
    def _extract_grade(cls_name: str) -> str:
        m = _re.match(r'(\d{2,4})', cls_name)
        if m:
            yr = m.group(1)
            return f"20{yr}级" if len(yr) == 2 else f"{yr}级"
        return ''

    # ── 班级缩写 ──
    def _extract_class_abbr(cls_name: str) -> str:
        """从 '24数字媒体艺术影视班' 提取 '影视班'。"""
        stripped = _re.sub(r'^\d{2,4}级?', '', cls_name).strip()
        if major and stripped.startswith(major):
            stripped = stripped[len(major):]
        return stripped if stripped else cls_name

    # ── 构建 ID 前缀 ──
    def _get_cls_archive_id(cls: dict):
        """从班级获取 archive_id，向后兼容 teacher.archive_id。"""
        aid = cls.get('archive_id')
        if aid:
            return aid
        # 向后兼容：如果班级没有 archive_id，回退到 teacher.archive_id
        return teacher.get('archive_id', '')

    if class_info:
        # ── per-class 文档 ──
        aid = _get_cls_archive_id(class_info)
        if not aid:
            return None
        prefix = f"{aid}{teacher_name}"
        ref_cls = class_info
    elif len(classes) == 1:
        # ── per-course 单班 ──
        aid = _get_cls_archive_id(classes[0])
        if not aid:
            return None
        prefix = f"{aid}{teacher_name}"
        ref_cls = classes[0]
    elif len(classes) > 1:
        # ── per-course 多班：拼接所有班级的 {id}{name} ──
        id_parts = []
        for cls in classes:
            aid = _get_cls_archive_id(cls)
            if not aid:
                return None
            id_parts.append(f"{aid}{teacher_name}")
        prefix = ''.join(id_parts)
        ref_cls = classes[0]
    else:
        return None

    grade = _extract_grade(ref_cls.get('name', ''))

    # ── 组装文件名 ──
    parts = [prefix]
    if grade:
        parts.append(grade)
    if major:
        parts.append(major)

    # 班级字段逻辑
    if class_info:
        abbr = _extract_class_abbr(class_info.get('name', ''))
        if abbr:
            parts.append(abbr)
    elif len(classes) == 1:
        abbr = _extract_class_abbr(classes[0].get('name', ''))
        if abbr:
            parts.append(abbr)
    # 多班 per-course：省略班级

    parts.append(f"《{course_name}》")
    parts.append(doc_type)

    filename = '+'.join(parts) + ext
    return filename
