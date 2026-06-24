import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/original_unpacked_new/word/document.xml')
root = tree.getroot()

print("SDT count:", len(root.findall('.//w:sdt', namespaces=nsmap)))
print("fldChar count:", len(root.findall('.//w:fldChar', namespaces=nsmap)))
