"""
make_lessonplan_template.py — 从原模板提取教案表并制作 XXXX 占位符模板

从 '设计学院模版-附件3：课程教案模板.docx' 的 Table 3 (16行教案表) 提取，
清空数据单元格并填入 XXXX 占位符，生成 Template_LessonPlan.docx。

用法:
    python scripts/make_lessonplan_template.py
"""

import copy
import os
import shutil
import zipfile
from pathlib import Path

from lxml import etree

# ═══════════════════════════════════════════════════════════════════════
# 配置
# ═══════════════════════════════════════════════════════════════════════

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOURCE_TEMPLATE = PROJECT_ROOT / "03_LessonPlan_Generator" / "设计学院模版-附件3：课程教案模板.docx"
OUTPUT_TEMPLATE = PROJECT_ROOT / "03_LessonPlan_Generator" / "Template_LessonPlan.docx"

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'


def qn(tag: str) -> str:
    """Clark notation 转换。"""
    prefix, local = tag.split(':')
    ns_map = {
        'w': W,
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    }
    return f'{{{ns_map[prefix]}}}{local}'


def clear_cell_content(tc_elem, placeholder: str = "XXXX"):
    """清空单元格内容并填入占位符。
    
    保留第一个段落的格式属性 (pPr) 和第一个 run 的格式属性 (rPr)，
    仅替换文本内容为占位符。删除多余的段落。
    """
    paragraphs = tc_elem.findall(qn('w:p'))
    if not paragraphs:
        return
    
    # 保留第一个段落
    first_p = paragraphs[0]
    
    # 删除多余段落
    for p in paragraphs[1:]:
        tc_elem.remove(p)
    
    # 在第一个段落中处理 runs
    runs = first_p.findall(qn('w:r'))
    
    if runs:
        # 保留第一个 run 的 rPr，替换文本
        first_run = runs[0]
        t_elem = first_run.find(qn('w:t'))
        if t_elem is None:
            t_elem = etree.SubElement(first_run, qn('w:t'))
        t_elem.text = placeholder
        t_elem.set(XML_SPACE, 'preserve')
        
        # 删除多余 runs
        for r in runs[1:]:
            first_p.remove(r)
    else:
        # 创建新 run + text
        r = etree.SubElement(first_p, qn('w:r'))
        t = etree.SubElement(r, qn('w:t'))
        t.text = placeholder
        t.set(XML_SPACE, 'preserve')


def get_cell_text(tc_elem) -> str:
    """获取单元格的完整文本。"""
    return ''.join(t.text or '' for t in tc_elem.iter(qn('w:t')))


def main():
    print(f"📂 源模板: {SOURCE_TEMPLATE}")
    print(f"📄 输出模板: {OUTPUT_TEMPLATE}")
    
    if not SOURCE_TEMPLATE.exists():
        print(f"❌ 源模板不存在: {SOURCE_TEMPLATE}")
        return
    
    # Step 1: 复制源文件
    shutil.copy2(SOURCE_TEMPLATE, OUTPUT_TEMPLATE)
    print("✅ 复制源模板 → Template_LessonPlan.docx")
    
    # Step 2: 解析 XML
    with zipfile.ZipFile(OUTPUT_TEMPLATE, 'r') as z:
        xml_content = z.read('word/document.xml')
    
    root = etree.fromstring(xml_content)
    body = root.find(f'{{{W}}}body')
    children = list(body)
    
    # Step 3: 定位各元素
    # 结构:
    #   [0-6]   封面段落 + 封面表格
    #   [7]     封面表格 (课程名称/性质/学分...)  → 删除
    #   [8-16]  过渡段落                          → 删除
    #   [17]    Table 2 课程目标 (21行)           → 删除
    #   [18]    "第一次课教案" 标题段落            → 保留 (改标题为 XXXX)
    #   [19]    Table 3 教案表 (16行)             → 保留 (清空数据)
    #   [20-28] 注释/签名段落                     → 删除
    #   [29]    sectPr                            → 保留
    
    # 找到所有表格的索引
    table_indices = []
    title_para_idx = None
    lesson_table_idx = None
    sect_pr_idx = None
    
    for ci, child in enumerate(children):
        tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
        if tag == 'tbl':
            table_indices.append(ci)
            rows = child.findall(f'{{{W}}}tr')
            if rows:
                first_text = get_cell_text(rows[0].findall(f'{{{W}}}tc')[0]) if rows[0].findall(f'{{{W}}}tc') else ''
                if '授课章节' in first_text:
                    lesson_table_idx = ci
        elif tag == 'p':
            text = ''.join(t.text or '' for t in child.iter(f'{{{W}}}t'))
            if '次课教案' in text or '教案' in text.replace(' ', ''):
                # 找到最靠近教案表的标题段落
                if lesson_table_idx is None:
                    title_para_idx = ci
        elif tag == 'sectPr':
            sect_pr_idx = ci
    
    print(f"  表格索引: {table_indices}")
    print(f"  教案表索引: {lesson_table_idx}")
    print(f"  sectPr 索引: {sect_pr_idx}")
    
    if lesson_table_idx is None:
        print("❌ 未找到教案表（包含'授课章节'的表格）")
        return
    
    # Step 4: 保留教案表和 sectPr，删除其他所有内容
    # 策略: 重建 body，只保留需要的元素
    lesson_table = children[lesson_table_idx]
    sect_pr = children[sect_pr_idx] if sect_pr_idx else None
    
    # 找到 "第一次课教案" 标题段落 (紧邻教案表之前的段落)
    title_para = None
    for ci in range(lesson_table_idx - 1, -1, -1):
        if children[ci].tag == f'{{{W}}}p':
            text = ''.join(t.text or '' for t in children[ci].iter(f'{{{W}}}t'))
            if text.strip():
                title_para = children[ci]
                break
    
    # 清空 body
    for child in list(body):
        body.remove(child)
    
    # 添加标题段落 (修改文本)
    if title_para is not None:
        title_para_copy = copy.deepcopy(title_para)
        # 修改标题文本为通用格式 — 保留第一个 run 的格式，删除多余 run
        runs = title_para_copy.findall(f'{{{W}}}r')
        if runs:
            # 第一个 run: 设文本为 XXXX
            first_run = runs[0]
            t_elem = first_run.find(f'{{{W}}}t')
            if t_elem is None:
                t_elem = etree.SubElement(first_run, f'{{{W}}}t')
            t_elem.text = "XXXX"
            t_elem.set(XML_SPACE, 'preserve')
            # 删除所有后续 run，防止 "次课教案" 等残留文字拼接
            for r in runs[1:]:
                title_para_copy.remove(r)
        body.append(title_para_copy)
    
    # 添加教案表
    body.append(lesson_table)
    
    # 添加 sectPr
    if sect_pr is not None:
        body.append(sect_pr)
    
    # Step 5: 清空教案表的数据单元格，填入 XXXX
    rows = lesson_table.findall(f'{{{W}}}tr')
    print(f"  教案表共 {len(rows)} 行")
    
    # R0-R8: 基本信息区域 (2列: 标签 | 数据)
    for ri in range(9):
        cells = rows[ri].findall(f'{{{W}}}tc')
        if len(cells) >= 2:
            label = get_cell_text(cells[0])
            print(f"  R{ri} [{label.strip()[:15]}] → XXXX")
            clear_cell_content(cells[1], "XXXX")
    
    # R9: 教学环节表头 — 保持不变
    print(f"  R9  [教学环节表头] → 保持原样")
    
    # R10-R14: 教学环节详情区域 (3列: vMerge | 环节名 | 教学设计)
    for ri in range(10, min(15, len(rows))):
        cells = rows[ri].findall(f'{{{W}}}tc')
        if len(cells) >= 3:
            label = get_cell_text(cells[1])
            print(f"  R{ri} [{label.strip()[:15]}] → XXXX in C2")
            clear_cell_content(cells[2], "XXXX")
        elif len(cells) >= 2:
            # 可能 vMerge 列被省略
            label = get_cell_text(cells[0])
            print(f"  R{ri} [{label.strip()[:15]}] → XXXX in C1")
            clear_cell_content(cells[1], "XXXX")
    
    # R15: 课后作业 (2列: 标签 | 数据)
    if len(rows) >= 16:
        cells = rows[15].findall(f'{{{W}}}tc')
        if len(cells) >= 2:
            label = get_cell_text(cells[0])
            print(f"  R15 [{label.strip()[:15]}] → XXXX")
            clear_cell_content(cells[1], "XXXX")
    
    # Step 6: 写回 ZIP
    modified_xml = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
    
    tmp_path = OUTPUT_TEMPLATE.with_suffix('.tmp.docx')
    with zipfile.ZipFile(OUTPUT_TEMPLATE, 'r') as zin:
        with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, modified_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))
    
    os.replace(tmp_path, OUTPUT_TEMPLATE)
    
    # Step 7: 验证
    print("\n=== 验证 ===")
    with zipfile.ZipFile(OUTPUT_TEMPLATE, 'r') as z:
        xml_verify = z.read('word/document.xml')
    
    root_v = etree.fromstring(xml_verify)
    tables_v = root_v.findall(f'.//{{{W}}}tbl')
    print(f"表格数: {len(tables_v)}")
    
    if tables_v:
        rows_v = tables_v[0].findall(f'{{{W}}}tr')
        print(f"教案表行数: {len(rows_v)}")
        
        xxxx_count = 0
        for t in root_v.iter(f'{{{W}}}t'):
            if t.text and 'XXXX' in t.text:
                xxxx_count += 1
        print(f"XXXX 占位符数: {xxxx_count}")
    
    print(f"\n✅ Template_LessonPlan.docx 已生成: {OUTPUT_TEMPLATE}")


if __name__ == '__main__':
    main()
