import os
import shutil
import copy
from pathlib import Path
from lxml import etree
import yaml

from scripts.docx_engine import (
    render_docx,
    qn,
    clone_table_row,
    replace_jinja_tag,
    set_run_text,
    archive_filename,
    XML_SPACE,
    merge_runs
)

# Template paths
TEMPLATE_INSPECTION = Path("07_Internship_Generator/templates/Template_Internship_Inspection.docx")
TEMPLATE_STATS = Path("07_Internship_Generator/templates/Template_Internship_Stats.docx")
TEMPLATE_DECENTRALIZED = Path("07_Internship_Generator/templates/Template_Internship_Decentralized.docx")

def safe_str(val):
    if val is None:
        return ""
    return str(val).strip()

def process_multiline(text: str) -> str:
    # docx_engine replace_jinja_tag and native text injection doesn't automatically convert \n to <w:br/> 
    # unless using fill_multiline, but for simple scalar replacement, we replace \n with \a for word soft return.
    # Actually, in docx XML, a soft break is <w:br/>. But using \a usually only works with docxtpl.
    # docx_engine's `replace_jinja_tag` just sets `t.text`. 
    # We should use `docx_engine.fill_multiline` if we want real paragraphs, but our templates use `replace_jinja_tag` pattern.
    # Since we manually injected the templates to have `{{ tag }}`, we can just replace the \n with \n and see if it works, or manually insert <w:br/>.
    # In docx_engine `replace_xxxx`, there is logic for \n -> <w:br/>. 
    # Wait! `replace_jinja_tag` in docx_engine DOES NOT handle \n !
    # Let's write a custom safe replacement for tags in inspection.
    return safe_str(text)

def generate_internship_docs(course_dir: str):
    yaml_path = os.path.join(course_dir, "course_internship.yaml")
    if not os.path.exists(yaml_path):
        print(f"Skipping internship generation: {yaml_path} not found.")
        return False
        
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    global_data = data.get('global', {})
    students = data.get('students', [])
    
    out_dir = Path(course_dir) / "Output"
    out_dir.mkdir(exist_ok=True)
    
    # Generate Inspection for each student
    for student in students:
        # Merge global + student
        ctx = copy.deepcopy(global_data)
        ctx.update(student)
        
        # Ensure Anti-Null
        for k in ['score_safety', 'score_attendance', 'score_learning', 'score_teamwork', 'score_attitude', 
                  'score_task', 'score_suitability', 'score_total', 'teacher_advice', 'teacher_signature', 'note']:
            if k not in ctx or ctx[k] is None:
                ctx[k] = ""
                
        def fill_inspection(root, context):
            # Custom replacement handling \n
            for p in root.iter(qn('w:p')):
                # 必须先合并 run，否则 Word 保存模板时可能将 {{ tag }} 拆分到多个 w:t 中导致无法匹配
                merge_runs(p)
                # Replace tags
                for k, v in context.items():
                    tag = f"{{{{ {k} }}}}"
                    tag_nospace = f"{{{{{k}}}}}"
                    
                    # Manual traversal to find and replace
                    for t in p.iter(qn('w:t')):
                        if t.text:
                            if tag in t.text or tag_nospace in t.text:
                                val_str = safe_str(v)
                                # If multiline
                                if '\n' in val_str:
                                    lines = val_str.split('\n')
                                    t.text = t.text.replace(tag, lines[0]).replace(tag_nospace, lines[0])
                                    t.set(XML_SPACE, 'preserve')
                                    # Insert <w:br/> and <w:t> for remaining lines
                                    parent_r = t.getparent()
                                    idx = parent_r.index(t)
                                    for line in reversed(lines[1:]):
                                        br = etree.Element(qn('w:br'))
                                        t_new = etree.Element(qn('w:t'))
                                        t_new.text = line
                                        t_new.set(XML_SPACE, 'preserve')
                                        parent_r.insert(idx + 1, br)
                                        parent_r.insert(idx + 2, t_new)
                                else:
                                    t.text = t.text.replace(tag, val_str).replace(tag_nospace, val_str)
                                    t.set(XML_SPACE, 'preserve')
        
        # Generate Inspection Form (记录表)
        doc_name = f"实习巡查记录表_{ctx.get('student_name', '未知')}.docx"
        out_dir_record = out_dir / "记录表"
        out_dir_record.mkdir(exist_ok=True)
        out_path = out_dir_record / doc_name
        
        render_docx(
            template_path=TEMPLATE_INSPECTION,
            output_path=out_path,
            fill_fn=fill_inspection,
            context=ctx
        )
        print(f"Generated: {doc_name}")
        # Generate Decentralized form
        ctx_dec = copy.deepcopy(ctx)
        # Ensure computed fields exist so that jinja tags get properly replaced
        if 'student_id' not in ctx_dec:
            email = ctx_dec.get('student_email', '')
            ctx_dec['student_id'] = email.split('@')[0] if '@' in email else ''
            
        # Ensure all possible template tags exist so jinja replace doesn't skip them
        placeholders = {
            'student_phone': '           ',
            'student_email': '           ',
            'enterprise_phone': '           ',
            'decentralized_apply_enterprise_date': '      年   月   日',
            'decentralized_apply_school_date': '      年   月   日',
            'decentralized_apply_student_date': '      年   月   日',
            'base_address': '',
            'intern_start_end': ''
        }
        for k, default_val in placeholders.items():
            if not ctx_dec.get(k):
                ctx_dec[k] = default_val
            
        # Synthesize any missing fields or specific logic if needed
        # We will use fill_inspection as it is a generic placeholder replacer
        doc_name_dec = f"分散实习申请表_{ctx.get('student_name', '未知')}.docx"
        out_dir_dec = out_dir / "分散表"
        out_dir_dec.mkdir(exist_ok=True)
        out_path_dec = out_dir_dec / doc_name_dec
        
        render_docx(
            template_path=TEMPLATE_DECENTRALIZED,
            output_path=out_path_dec,
            fill_fn=fill_inspection,
            context=ctx_dec
        )
        print(f"Generated: {doc_name_dec}")
        
    # Generate Stats for each student
    def fill_stats(root, context):
        # Fill global tags in header (college, major) and specific tags (sequence_number)
        for p in root.iter(qn('w:p')):
            replace_jinja_tag(p, 'college', safe_str(global_data.get('college')))
            replace_jinja_tag(p, 'major', safe_str(global_data.get('major')))
            replace_jinja_tag(p, 'sequence_number', safe_str(context.get('sequence_number')))
            
        tbls = list(root.iter(qn('w:tbl')))
        if not tbls:
            return
        tbl = tbls[0]
        
        # Determine how many records
        records = students
        if not records:
            records = [{
                'sequence_number': '', 'teacher': '', 'student_name': '', 
                'base_name': '无记录', 'inspect_date': '', 'note': ''
            }]
            
        rows = list(tbl.iter(qn('w:tr')))
        if len(rows) < 2:
            return
            
        template_row = rows[1]
        
        # Clone rows
        extra_needed = len(records) - 1
        new_rows = []
        if extra_needed > 0:
            new_rows = clone_table_row(tbl, 1, extra_needed)
            
        all_data_rows = [template_row] + new_rows
        
        for row_idx, row_elem in enumerate(all_data_rows):
            item = records[row_idx]
            is_current = (item.get('student_name') == context.get('student_name'))
            tcs = list(row_elem.iter(qn('w:tc')))
            if len(tcs) >= 6:
                p0 = tcs[0].find(qn('w:p'))
                set_run_text(p0, safe_str(item.get('sequence_number')))
                
                p1 = tcs[1].find(qn('w:p'))
                set_run_text(p1, safe_str(global_data.get('school_teacher')))
                
                p2 = tcs[2].find(qn('w:p'))
                set_run_text(p2, safe_str(item.get('student_name')))
                
                p3 = tcs[3].find(qn('w:p'))
                set_run_text(p3, safe_str(item.get('base_name')))
                
                # Check if inspect_date is missing, try to infer or leave blank
                date_val = item.get('inspect_date', global_data.get('inspect_year', '') + '年' + global_data.get('inspect_month', '') + '月' + global_data.get('inspect_day', '') + '日')
                p4 = tcs[4].find(qn('w:p'))
                set_run_text(p4, date_val)
                
                p5 = tcs[5].find(qn('w:p'))
                set_run_text(p5, safe_str(item.get('note')))
                
                if is_current:
                    for p in [p0, p1, p2, p3, p4, p5]:
                        if p is not None:
                            for r in p.findall(qn('w:r')):
                                rPr = r.find(qn('w:rPr'))
                                if rPr is None:
                                    rPr = etree.Element(qn('w:rPr'))
                                    r.insert(0, rPr)
                                if rPr.find(qn('w:b')) is None:
                                    rPr.append(etree.Element(qn('w:b')))
                                if rPr.find(qn('w:bCs')) is None:
                                    rPr.append(etree.Element(qn('w:bCs')))
                
    for student in students:
        stats_name = f"实习巡查统计表_{student.get('student_name', '未知')}.docx"
        out_dir_stats = out_dir / "统计表"
        out_dir_stats.mkdir(exist_ok=True)
        stats_out = out_dir_stats / stats_name
        
        ctx = copy.deepcopy(global_data)
        ctx.update(student)
        
        render_docx(
            template_path=TEMPLATE_STATS,
            output_path=stats_out,
            fill_fn=fill_stats,
            context=ctx
        )
        print(f"Generated: {stats_name}")
    return True

if __name__ == "__main__":
    generate_internship_docs("/Users/yamlam/Downloads/2025-2026-2 课程/实习指导")
