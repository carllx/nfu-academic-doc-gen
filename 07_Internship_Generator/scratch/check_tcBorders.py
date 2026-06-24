import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/original_unpacked/word/document.xml')
root = tree.getroot()

for tc in root.findall('.//w:tc', namespaces=nsmap):
    text = ''.join(tc.itertext())
    if '学生签名：' in text or '签名（盖章）：' in text:
        tcPr = tc.find('./w:tcPr', namespaces=nsmap)
        if tcPr is not None:
            tcBorders = tcPr.find('./w:tcBorders', namespaces=nsmap)
            if tcBorders is not None:
                print(f"Found tcBorders on '{text.strip()}'!")
                print(ET.tostring(tcBorders, encoding='unicode'))
            else:
                print(f"No tcBorders on '{text.strip()}'")
