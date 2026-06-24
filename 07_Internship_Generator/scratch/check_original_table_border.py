import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/original_unpacked/word/document.xml')
root = tree.getroot()

for tbl in root.findall('.//w:tbl', namespaces=nsmap):
    text = ''.join(tbl.itertext())
    if '学生签名' in text:
        tblPr = tbl.find('./w:tblPr', namespaces=nsmap)
        if tblPr is not None:
            tblBorders = tblPr.find('./w:tblBorders', namespaces=nsmap)
            if tblBorders is not None:
                print("Found tblBorders on original!")
                print(ET.tostring(tblBorders, encoding='unicode'))
            else:
                print("No tblBorders on original!")
