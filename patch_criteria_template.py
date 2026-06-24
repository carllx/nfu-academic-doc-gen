import docx

doc = docx.Document('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/Template_Exam_Criteria_AB.docx')

def replace_text_in_runs(paragraph, old_text, new_text):
    for run in paragraph.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)
            return True
    return False

# Since '{{ a_theme }}' might be split across runs, it's safer to just iterate paragraphs and if p.text == '{{ a_theme }}', modify the text.
# Actually we can just do p.text = new_text, but we lose formatting. 
# Let's check if the paragraph has a specific style.

for p in doc.paragraphs:
    if '{{ a_theme }}' in p.text:
        # To preserve formatting, we can just prepend a run or modify the first run.
        if len(p.runs) > 0:
            p.runs[0].text = p.runs[0].text.replace('{{ a_theme }}', '一、创作主题：\n{{ a_theme }}')
    if '{{ b_theme }}' in p.text:
        if len(p.runs) > 0:
            p.runs[0].text = p.runs[0].text.replace('{{ b_theme }}', '一、创作主题：\n{{ b_theme }}')

doc.save('/Users/yamlam/Downloads/教务材料/05_Assessment_Generator/Template_Exam_Criteria_AB.docx')
print("Patched Template_Exam_Criteria_AB.docx")
