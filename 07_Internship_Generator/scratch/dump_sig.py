import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/original_unpacked_new/word/document.xml')
root = tree.getroot()

for p in root.findall('.//w:p', namespaces=nsmap):
    text = ''.join(p.itertext())
    if '学生签名' in text or '指导教师意见' in text or '单位意见' in text or '签名' in text:
        print(ET.tostring(p, encoding='unicode'))
