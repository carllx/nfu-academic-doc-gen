import docx
from docx.shared import Pt
from docx.oxml.ns import qn

def fix_font(file_path):
    doc = docx.Document(file_path)
    changed = False
    for p in doc.paragraphs:
        if "{{" in p.text:
            # force paragraph style font to SimSun, Size 12
            for run in p.runs:
                if "{{" in run.text or "}}" in run.text or True:
                    run.font.name = 'SimSun'
                    run.font.size = Pt(12)
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')
                    changed = True
    if changed:
        doc.save(file_path)
        print(f"Fixed fonts in {file_path}")
    else:
        print(f"No changes in {file_path}")

fix_font('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/Template_Exam_Paper_AB.docx')
fix_font('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/Template_Exam_Paper_AB.docx')
