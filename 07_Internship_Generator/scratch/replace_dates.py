import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml')
root = tree.getroot()

def get_text(p):
    return ''.join(p.itertext())

def replace_p_text(p, text):
    # Preserve formatting from the first run if possible
    first_rPr = None
    for r in p.findall('.//w:r', namespaces=nsmap):
        if first_rPr is None:
            rPr = r.find('./w:rPr', namespaces=nsmap)
            if rPr is not None:
                import copy
                first_rPr = copy.deepcopy(rPr)
        r.getparent().remove(r)
    
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    if first_rPr is not None:
        r.append(first_rPr)
    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = text

date_paragraphs = []
for p in root.findall('.//w:p', namespaces=nsmap):
    text = get_text(p)
    if '年' in text and '月' in text and '日' in text:
        date_paragraphs.append(p)

print(f"Found {len(date_paragraphs)} date paragraphs.")
if len(date_paragraphs) == 3:
    replace_p_text(date_paragraphs[0], '{{ decentralized_apply_student_date }}')
    replace_p_text(date_paragraphs[1], '{{ decentralized_apply_school_date }}')
    replace_p_text(date_paragraphs[2], '{{ decentralized_apply_enterprise_date }}')
    print("Replaced tags.")
    tree.write('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml', encoding='utf-8', xml_declaration=True)
else:
    print("Unexpected number of date paragraphs. Aborting replacement.")
    for p in date_paragraphs:
        print(get_text(p))

