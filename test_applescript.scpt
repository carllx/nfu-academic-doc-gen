tell application "Microsoft Word"
    set word_path to POSIX file "/Users/yamlam/Downloads/2025-2026-2 课程/实习指导/Output/实习巡查统计表_卢思彤.docx"
    set pdf_path to POSIX file "/Users/yamlam/Downloads/2025-2026-2 课程/实习指导/Output/实习巡查统计表_卢思彤_test.pdf"
    open word_path
    set theDoc to active document
    save as theDoc file format format PDF file name pdf_path
    close theDoc saving no
end tell
