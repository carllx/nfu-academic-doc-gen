import zipfile
import os
from lxml import etree

NSMAP = {
    'w':  'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
}

def qn(tag: str) -> str:
    prefix, local = tag.split(':')
    return f'{{{NSMAP[prefix]}}}{local}'

TEMPLATE_PATH = '/Users/yamlam/Downloads/教务材料/07_Internship_Generator/templates/Template_Internship_Decentralized.docx'

def fix_borders():
    output_path = TEMPLATE_PATH + '.tmp'
    modified_xml = None
    
    with zipfile.ZipFile(TEMPLATE_PATH, 'r') as zin:
        xml_content = zin.read('word/document.xml')
        root = etree.fromstring(xml_content)
        
        # Find all tables. The signature tables are at the end, typically nested or just regular tables.
        # Let's add <w:tcBorders> with w:val="none" to ALL cells in tables that have no borders defined, 
        # or specifically the last 3 tables. Actually, we can just find the tables containing 
        # {{ decentralized_apply_student_date }}, {{ decentralized_apply_enterprise_date }}, {{ decentralized_apply_school_date }}
        
        signature_tags = ['decentralized_apply_student_date', 'decentralized_apply_enterprise_date', 'decentralized_apply_school_date']
        
        for tbl in root.iter(qn('w:tbl')):
            # check if tbl contains any of the signature tags
            tbl_text = "".join(t.text for t in tbl.iter(qn('w:t')) if t.text)
            if any(tag in tbl_text for tag in signature_tags):
                # This table contains a signature tag. We should strip its borders.
                # Find all <w:tc> in this table
                for tc in tbl.iter(qn('w:tc')):
                    tcPr = tc.find(qn('w:tcPr'))
                    if tcPr is None:
                        tcPr = etree.Element(qn('w:tcPr'))
                        tc.insert(0, tcPr)
                        
                    tcBorders = tcPr.find(qn('w:tcBorders'))
                    if tcBorders is None:
                        tcBorders = etree.Element(qn('w:tcBorders'))
                        tcPr.append(tcBorders)
                    else:
                        # Clear existing borders
                        for child in list(tcBorders):
                            tcBorders.remove(child)
                            
                    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                        b = etree.Element(qn(f'w:{border_name}'))
                        b.set(qn('w:val'), 'none')
                        b.set(qn('w:sz'), '0')
                        b.set(qn('w:space'), '0')
                        b.set(qn('w:color'), 'auto')
                        tcBorders.append(b)

                # Also clear tblBorders just in case
                tblPr = tbl.find(qn('w:tblPr'))
                if tblPr is not None:
                    tblBorders = tblPr.find(qn('w:tblBorders'))
                    if tblBorders is not None:
                        for child in list(tblBorders):
                            tblBorders.remove(child)
                        for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                            b = etree.Element(qn(f'w:{border_name}'))
                            b.set(qn('w:val'), 'none')
                            b.set(qn('w:sz'), '0')
                            b.set(qn('w:space'), '0')
                            b.set(qn('w:color'), 'auto')
                            tblBorders.append(b)

        modified_xml = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, modified_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))
                    
    os.replace(output_path, TEMPLATE_PATH)
    print("Fixed borders in template.")

if __name__ == '__main__':
    fix_borders()
