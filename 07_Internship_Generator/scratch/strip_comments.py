import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml')
root = tree.getroot()

# Remove comment references, range starts, range ends
tags_to_remove = [
    '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}commentReference',
    '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}commentRangeStart',
    '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}commentRangeEnd'
]

removed_count = 0
for tag in tags_to_remove:
    for elem in root.findall('.//' + tag):
        # The parent might be <w:r> or something else
        elem.getparent().remove(elem)
        removed_count += 1

# Also sometimes <w:r> becomes empty, we can clean them up but word ignores empty <w:r>
print(f"Removed {removed_count} comment elements from document.xml")

tree.write('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml', encoding='utf-8', xml_declaration=True)
