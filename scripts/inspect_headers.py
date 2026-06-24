import zipfile
import re
from pathlib import Path

def print_header_texts(docx_path: Path):
    if not docx_path.exists():
        return
    print(f"--- {docx_path.name} ---")
    with zipfile.ZipFile(docx_path, 'r') as zin:
        for item in zin.infolist():
            if item.filename.startswith('word/header'):
                content = zin.read(item.filename).decode('utf-8')
                # Extract text from w:t tags
                texts = re.findall(r'<w:t(?:[^>]*)>([^<]*)</w:t>', content)
                joined = "".join(texts)
                if '②' in joined or '2-1' in joined:
                    print(f"[{item.filename}] Found matching text: {joined}")

if __name__ == '__main__':
    base_dir = Path('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator')
    print_header_texts(base_dir / 'Template_Exam_Paper_AB.docx')
