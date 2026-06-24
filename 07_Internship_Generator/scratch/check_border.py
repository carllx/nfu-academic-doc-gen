import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml')
root = tree.getroot()

for p in root.findall('.//w:p', namespaces=nsmap):
    text = ''.join(p.itertext())
    if 'decentralized_apply_student_date' in text or 'decentralized_apply_school_date' in text or 'decentralized_apply_enterprise_date' in text:
        pPr = p.find('./w:pPr', namespaces=nsmap)
        if pPr is not None:
            pBdr = pPr.find('./w:pBdr', namespaces=nsmap)
            if pBdr is not None:
                print(f"Found borders on '{text}'!")
                print(ET.tostring(pBdr, encoding='unicode'))
            else:
                print(f"No borders found on '{text}'")
