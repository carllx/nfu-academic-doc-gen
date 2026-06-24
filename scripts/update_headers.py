import sys
from pathlib import Path
from lxml import etree
import zipfile
import os

sys.path.append('/Users/yamlam/Downloads/教务材料')
from scripts.docx_engine import NSMAP, XML_SPACE, qn

def replace_in_header(docx_path: Path):
    if not docx_path.exists():
        return

    tmp_path = docx_path.with_suffix('.tmp.docx')
    updated = False

    with zipfile.ZipFile(docx_path, 'r') as zin, zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename.startswith('word/header'):
                root = etree.fromstring(content)
                changed_this_file = False
                
                # Merge runs to avoid split text
                for p_elem in root.iter(qn('w:p')):
                    # basic merge runs
                    runs = p_elem.findall(qn('w:r'))
                    if len(runs) > 1:
                        combined = ""
                        for r in runs:
                            t = r.find(qn('w:t'))
                            if t is not None and t.text:
                                combined += t.text
                        if combined:
                            runs[0].find(qn('w:t')).text = combined
                            for r in runs[1:]:
                                p_elem.remove(r)
                
                # Now replace
                for t in root.iter(qn('w:t')):
                    if t.text and '②-1' in t.text:
                        t.text = t.text.replace('②-1', '{{卷面编号}}')
                        t.set(XML_SPACE, 'preserve')
                        changed_this_file = True
                
                if changed_this_file:
                    content = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
                    updated = True
                    print(f"  Updated {item.filename} in {docx_path.name}")
            
            zout.writestr(item, content)

    if updated:
        os.replace(tmp_path, docx_path)
        print(f"✅ Successfully updated {docx_path.name}")
    else:
        os.remove(tmp_path)
        print(f"ℹ️ No changes needed for {docx_path.name}")

if __name__ == '__main__':
    base_dir = Path('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator')
    templates = [
        'Template_Exam_Paper_AB.docx',
        'Template_Exam_Criteria_AB.docx',
        'Template_Exam_Checklist_AB.docx'
    ]
    for t in templates:
        replace_in_header(base_dir / t)
