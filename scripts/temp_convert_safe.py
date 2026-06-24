import os
import subprocess
import shutil

def convert_to_pdf_word_safe(docx_path, pdf_path):
    temp_docx = "/tmp/temp_convert.docx"
    temp_pdf = "/tmp/temp_convert.pdf"
    
    shutil.copy(docx_path, temp_docx)
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
        
    applescript = f'''
    tell application "Microsoft Word"
        set theDoc to open POSIX file "{temp_docx}"
        set theOutputPath to POSIX file "{temp_pdf}"
        save as theDoc file format format PDF file name theOutputPath
        close theDoc saving no
    end tell
    '''
    res = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
    if res.returncode != 0:
        print("AppleScript failed:", res.stderr)
    
    if os.path.exists(temp_pdf):
        shutil.copy(temp_pdf, pdf_path)
        os.remove(temp_pdf)
    os.remove(temp_docx)

out_dir = "/Users/yamlam/Downloads/2025-2026-2 课程/实习指导/Output/分散表"
for f in os.listdir(out_dir):
    if f.endswith('.docx'):
        docx = os.path.join(out_dir, f)
        pdf = os.path.join(out_dir, f.replace('.docx', '.pdf'))
        print(f"Converting {f}...")
        convert_to_pdf_word_safe(docx, pdf)
