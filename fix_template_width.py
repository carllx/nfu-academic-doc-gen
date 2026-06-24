import docx
from docx.shared import Cm

template_path = "07_Internship_Generator/templates/Template_Internship_Stats.docx"
doc = docx.Document(template_path)

# Ensure the table is set to autofit window = False and use fixed layout
table = doc.tables[0]
table.autofit = False
table.allow_autofit = False

# We have 6 columns
widths = [Cm(1.5), Cm(2.5), Cm(2.5), Cm(5.5), Cm(3.5), Cm(3.5)]

for row in table.rows:
    for idx, cell in enumerate(row.cells):
        if idx < len(widths):
            cell.width = widths[idx]

doc.save(template_path)
print("Template widths updated.")
