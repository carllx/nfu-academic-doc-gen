from docx import Document
from pathlib import Path

def rebuild_template():
    base_path = Path('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator')
    template_path = base_path / 'Template_Exam_Criteria_AB.docx'
    
    if not template_path.exists():
        print("Template not found!")
        return

    doc = Document(template_path)
    
    # Update row 1 with standard Jinja tags instead of tr
    row = doc.tables[0].rows[1]
    row.cells[0].text = '{% for sec in sections %}{{ sec.content }}'
    row.cells[1].text = '{{ sec.total_score }}{% endfor %}'
    
    doc.save(template_path)
    print("Successfully patched Template_Exam_Criteria_AB.docx")

if __name__ == '__main__':
    rebuild_template()
