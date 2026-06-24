import os
import subprocess

def convert_to_pdf_word(docx_path, pdf_path):
    applescript = f'''
    tell application "Microsoft Word"
        set theDoc to open POSIX file "{docx_path}"
        set theOutputPath to POSIX file "{pdf_path}"
        save as theDoc file format format PDF file name theOutputPath
        close theDoc saving no
    end tell
    '''
    subprocess.run(["osascript", "-e", applescript])

out_dir = "/Users/yamlam/Downloads/2025-2026-2 课程/实习指导/Output/分散表"
for f in os.listdir(out_dir):
    if f.endswith('.docx'):
        docx = os.path.join(out_dir, f)
        pdf = os.path.join(out_dir, f.replace('.docx', '.pdf'))
        print(f"Converting {f}...")
        convert_to_pdf_word(docx, pdf)
