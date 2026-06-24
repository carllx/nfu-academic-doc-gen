import lxml.etree as ET
import copy
import re

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

tree = ET.parse('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/unpacked/word/document.xml')
root = tree.getroot()

# Find the row with the loop
target_tr = None
for tr in root.findall('.//w:tr', ns):
    text = "".join(t.text for t in tr.findall('.//w:t', ns) if t.text)
    if "{% for sec in sections %}" in text or "{%tr for sec in sections %}" in text:
        target_tr = tr
        break

if target_tr is not None:
    # We will create row 1 and row 3 by deepcopying target_tr
    row1 = copy.deepcopy(target_tr)
    row3 = copy.deepcopy(target_tr)
    
    def clear_tr(tr):
        for tc in tr.findall('w:tc', ns):
            for p in tc.findall('.//w:p', ns):
                for r in p.findall('w:r', ns):
                    p.remove(r)
            # Ensure at least an empty paragraph
            if len(tc.findall('.//w:p', ns)) == 0:
                ET.SubElement(tc, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')

    # Setup row 1
    clear_tr(row1)
    # Add tag to first cell
    cells1 = row1.findall('w:tc', ns)
    if cells1:
        p1 = cells1[0].find('.//w:p', ns)
        if p1 is None:
            p1 = ET.SubElement(cells1[0], '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
        r = ET.SubElement(p1, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
        t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
        t.text = '{%tr for sec in sections %}'

    # Setup row 3
    clear_tr(row3)
    # Add tag to first cell
    cells3 = row3.findall('w:tc', ns)
    if cells3:
        p3 = cells3[0].find('.//w:p', ns)
        if p3 is None:
            p3 = ET.SubElement(cells3[0], '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
        r = ET.SubElement(p3, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
        t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
        t.text = '{%tr endfor %}'

    # Clean target_tr (Row 2)
    for tc in target_tr.findall('w:tc', ns):
        for t_node in tc.findall('.//w:t', ns):
            if t_node.text:
                t_node.text = t_node.text.replace('{% for sec in sections %}', '')
                t_node.text = t_node.text.replace('{% endfor %}', '')
                t_node.text = t_node.text.replace('{%tr for sec in sections %}', '')
                t_node.text = t_node.text.replace('{%tr endfor %}', '')

    parent = target_tr.getparent()
    idx = list(parent).index(target_tr)
    parent.insert(idx, row1)
    parent.insert(idx + 2, row3)

    tree.write('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/unpacked/word/document.xml', encoding='utf-8', xml_declaration=True)
    print("Fixed table rows.")
else:
    print("Target row not found.")
