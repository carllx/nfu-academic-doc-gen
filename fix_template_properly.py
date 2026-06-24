import docx
from docx.shared import Cm
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn

template_path = "07_Internship_Generator/templates/Template_Internship_Stats.docx"
doc = docx.Document(template_path)
table = doc.tables[0]
tbl = table._tbl

# 1. Set fixed layout in tblPr
tblPr = tbl.tblPr
tblLayout = tblPr.find(qn('w:tblLayout'))
if tblLayout is None:
    tblLayout = OxmlElement('w:tblLayout')
    tblPr.append(tblLayout)
tblLayout.set(qn('w:type'), 'fixed')

# 2. Add or update tblGrid in the exact correct spot (after tblPr)
tblGrid = tbl.find(qn('w:tblGrid'))
if tblGrid is not None:
    tbl.remove(tblGrid)

tblGrid = OxmlElement('w:tblGrid')
# Insert after tblPr
idx = tbl.index(tblPr) + 1
tbl.insert(idx, tblGrid)

widths_cm = [1.2, 2.5, 2.5, 5.8, 3.5, 3.5]
widths_twips = [int(w * 567) for w in widths_cm]

for w in widths_twips:
    gridCol = OxmlElement('w:gridCol')
    gridCol.set(qn('w:w'), str(w))
    tblGrid.append(gridCol)

# 3. Apply to cells
for row in table.rows:
    for idx, cell in enumerate(row.cells):
        if idx < len(widths_twips):
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.find(qn('w:tcW'))
            if tcW is None:
                tcW = OxmlElement('w:tcW')
                tcPr.append(tcW)
            tcW.set(qn('w:w'), str(widths_twips[idx]))
            tcW.set(qn('w:type'), 'dxa')

doc.save(template_path)
print("Template fixed properly.")
