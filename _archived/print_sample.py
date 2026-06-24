import docx

doc = docx.Document("05_Assessment_Generator/Template_Exam_Checklist_A.docx")
for table in doc.tables[:1]:
    for row in table.rows[:3]:
        print([cell.text.strip() for cell in row.cells])
