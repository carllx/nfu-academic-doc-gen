import lxml.etree as ET

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml')
root = tree.getroot()

def add_run(p, text):
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = text

def get_text(cell):
    return ''.join(cell.itertext())

cells = list(root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'))

for i, cell in enumerate(cells):
    text = get_text(cell).strip()
    if text == '姓名':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ student_name }}')
    elif text == '学号':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ student_id }}')
    elif text == '专业班级':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ class_name }}')
    elif text == '联系电话':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ student_phone }}')
    elif text == '电子邮箱':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ student_email }}')
    elif text == '实习单位名称':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ base_name }}')
    elif text == '实习单位地址':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ base_address }}')
    elif text == '实习单位联系人':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ enterprise_teacher }}')
    elif text == '实习单位联系电话':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ enterprise_phone }}')
    elif text == '实习起止时间':
        p = cells[i+1].find('.//w:p', namespaces=nsmap)
        add_run(p, '{{ intern_start_end }}')

# There might be other fields! Let's print out the text of all cells to see.
for cell in cells:
    print(get_text(cell).strip())

tree.write('/Users/yamlam/Downloads/教务材料/07_Internship_Generator/scratch/unpacked/word/document.xml', encoding='utf-8', xml_declaration=True)
