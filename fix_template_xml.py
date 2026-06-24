import docx
from docx.shared import Cm
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn

template_path = "07_Internship_Generator/templates/Template_Internship_Stats.docx"
doc = docx.Document(template_path)

table = doc.tables[0]
table.autofit = False
table.allow_autofit = False

# Cm to twips (1 cm = 567 twips)
widths_cm = [1.2, 2.5, 2.5, 5.8, 3.5, 3.5]
widths_twips = [int(w * 567) for w in widths_cm]

# Update w:tblGrid
tbl = table._tbl
tblGrid = tbl.find(qn('w:tblGrid'))
if tblGrid is None:
    tblGrid = OxmlElement('w:tblGrid')
    tbl.insert(0, tblGrid) # simplistic, usually after tblPr
else:
    for child in list(tblGrid):
        tblGrid.remove(child)

for w in widths_twips:
    gridCol = OxmlElement('w:gridCol')
    gridCol.set(qn('w:w'), str(w))
    tblGrid.append(gridCol)

for row in table.rows:
    for idx, cell in enumerate(row.cells):
        if idx < len(widths_twips):
            cell.width = widths_twips[idx]
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.find(qn('w:tcW'))
            if tcW is None:
                tcW = OxmlElement('w:tcW')
                tcPr.append(tcW)
            tcW.set(qn('w:w'), str(widths_twips[idx]))
            tcW.set(qn('w:type'), 'dxa')

doc.save(template_path)
print("Template XML updated with exact grid widths.")
