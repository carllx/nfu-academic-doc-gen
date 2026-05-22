"""
gen_syllabus_xml.py — 纯 XML 操作的教学大纲生成器 (方案 A)

核心策略：
  1. 复制 Syllabus.docx (ZIP) 到输出目录
  2. 从 ZIP 中解压 word/document.xml
  3. 用 lxml 精确替换所有 XXXX 占位符为实际数据
  4. 不触碰 <w:tcPr> 中的 vMerge/gridSpan 等合并属性
  5. 将修改后的 XML 写回 ZIP

依赖: lxml, pyyaml (已在环境中安装)
"""

import copy
import re
from pathlib import Path
from lxml import etree

# ─── 通用引擎导入 ────────────────────────────────────────────────────
from scripts.docx_engine import (
    qn as _qn,
    get_paragraph_text as _get_paragraph_text,
    get_cell_text as _get_cell_text,
    merge_runs as _merge_runs,
    set_run_text as _set_run_text,
    replace_xxxx as _replace_xxxx_in_text,
    replace_jinja_tag as _replace_jinja_in_text,
    fill_multiline as _fill_multiline_paragraph,
    replace_in_runs as _replace_xxxx_in_runs,
    find_table_by_header as _find_table_by_header,
    render_docx,
)
from scripts.utils.chapter_utils import build_chapter_title as _build_chapter_title
from scripts.utils.reading_utils import resolve_chapter_titles as _resolve_chapter_titles


# ═══════════════════════════════════════════════════════════════════════
# 2. 表格填充函数 (业务逻辑 — Syllabus 专用)
# ═══════════════════════════════════════════════════════════════════════


def fill_table0(root, context: dict):
    """填充 Table 0 — 课程信息 (9行4列)
    
    替换规则:
    - R1 C1: course.code (已有 Jinja 标签)
    - R1 C3: course.name (已有 Jinja 标签)
    - R2 C1: course.department
    - R2 C3: course.semester
    - R3 C1: course.grade → XXXX
    - R3 C3: course.major
    - R4 C1: course.credits (已有 Jinja 标签)  
    - R4 C3: course.hours.total (已有 Jinja 标签)
    - R5 C1: course.nature_rt (gridSpan=3)
    - R6 C1: course.prerequisites (gridSpan=3, XXXX)
    """
    tbl = _find_table_by_header(root, '课程信息')
    if tbl is None:
        print("    ⚠️ 未找到课程信息表")
        return
    
    rows = tbl.findall(_qn('w:tr'))
    course = context.get('course', {})
    
    # R1: 替换 Jinja 标签
    r1_cells = rows[1].findall(_qn('w:tc'))
    for p in r1_cells[1].iter(_qn('w:p')):
        _replace_jinja_in_text(p, 'course.code', str(course.get('code', '')))
    for p in r1_cells[3].iter(_qn('w:p')):
        _replace_jinja_in_text(p, 'course.name', str(course.get('name', '')))
    
    # R2: department + semester
    r2_cells = rows[2].findall(_qn('w:tc'))
    for p in r2_cells[1].iter(_qn('w:p')):
        _set_run_text(p, str(course.get('department', '设计学院')))
    for p in r2_cells[3].iter(_qn('w:p')):
        _set_run_text(p, '2025-2026学年第二学期')
    
    # R3: grade (XXXX) + major
    r3_cells = rows[3].findall(_qn('w:tc'))
    for p in r3_cells[1].iter(_qn('w:p')):
        _replace_xxxx_in_text(p, str(course.get('grade', '2023级')))
    for p in r3_cells[3].iter(_qn('w:p')):
        _set_run_text(p, str(course.get('major', '数字媒体艺术')))
    
    # R4: credits + hours
    r4_cells = rows[4].findall(_qn('w:tc'))
    for p in r4_cells[1].iter(_qn('w:p')):
        _replace_jinja_in_text(p, 'course.credits', str(course.get('credits', '')))
    for p in r4_cells[3].iter(_qn('w:p')):
        _replace_jinja_in_text(p, 'course.hours.total', str(course.get('hours', {}).get('total', '')))
    
    # R5: nature (gridSpan=3) — 替换勾选框文本
    r5_cells = rows[5].findall(_qn('w:tc'))
    nature_rt = context.get('course', {}).get('nature_rt', '')
    if nature_rt:
        for p in r5_cells[1].iter(_qn('w:p')):
            _set_run_text(p, nature_rt)
    
    # R6: prerequisites (XXXX, gridSpan=3)
    r6_cells = rows[6].findall(_qn('w:tc'))
    for p in r6_cells[1].iter(_qn('w:p')):
        _replace_xxxx_in_text(p, str(course.get('prerequisites', '无')))


def _remove_table_last_column(tbl):
    """物理删除表格最后一列（观测点列），并将其宽度归还给倒数第二列。

    操作：
      1. 从 <w:tblGrid> 中移除最后一个 <w:gridCol>，宽度加到前一列
      2. 每行移除最后一个 <w:tc>
    """
    # 1. 调整 gridCol
    tbl_grid = tbl.find(_qn('w:tblGrid'))
    if tbl_grid is not None:
        grid_cols = tbl_grid.findall(_qn('w:gridCol'))
        if len(grid_cols) >= 2:
            last_gc = grid_cols[-1]
            prev_gc = grid_cols[-2]
            # 将被删列的宽度加到前一列
            last_w = int(last_gc.get(_qn('w:w'), '0'))
            prev_w = int(prev_gc.get(_qn('w:w'), '0'))
            prev_gc.set(_qn('w:w'), str(prev_w + last_w))
            tbl_grid.remove(last_gc)

    # 2. 每行移除最后一个单元格
    for row in tbl.findall(_qn('w:tr')):
        cells = row.findall(_qn('w:tc'))
        if cells:
            row.remove(cells[-1])


def _build_objectives_paragraphs(root, context: dict):
    """将课程目标表替换为纯文字段落（适用于 schema_type='none'）。

    输出格式:
      （一）知识目标
      1. desc1；
      2. desc2。
      （二）能力目标
      ...
    """
    tbl = _find_table_by_header(root, '课程目标')
    if tbl is None:
        print("    ⚠️ [none] 未找到课程目标表，跳过段落替换")
        return

    body = root.find(_qn('w:body'))
    children = list(body)
    tbl_idx = children.index(tbl)

    # 从文档中找一个普通段落作为格式模板（用于克隆 pPr/rPr）
    tpl_para = None
    for child in children:
        if child.tag == _qn('w:p'):
            text = _get_paragraph_text(child)
            if text.strip() and '课程' not in text and 'XXXX' not in text:
                tpl_para = child
                break

    # 删除原表格
    body.remove(tbl)

    # 构建段落内容
    objectives = context.get('course', {}).get('objectives', {})
    cat_map = [
        ('knowledge', '知识目标'),
        ('ability', '能力目标'),
        ('quality', '素质目标'),
    ]
    cn_nums = ['一', '二', '三']

    insert_pos = tbl_idx
    for ci, (cat_key, cat_cn) in enumerate(cat_map):
        items = objectives.get(cat_key, [])

        # 子标题段落：（一）知识目标
        p_heading = copy.deepcopy(tpl_para) if tpl_para is not None else etree.SubElement(body, _qn('w:p'))
        # 设为加粗
        for r in p_heading.findall(_qn('w:r')):
            rpr = r.find(_qn('w:rPr'))
            if rpr is None:
                rpr = etree.SubElement(r, _qn('w:rPr'))
                r.insert(0, rpr)
            b = rpr.find(_qn('w:b'))
            if b is None:
                etree.SubElement(rpr, _qn('w:b'))
        _set_run_text(p_heading, f"（{cn_nums[ci]}）{cat_cn}")
        body.insert(insert_pos, p_heading)
        insert_pos += 1

        # 各条目段落
        for idx, item in enumerate(items, 1):
            desc = item.get('desc', '')
            if not desc:
                continue
            p_item = copy.deepcopy(tpl_para) if tpl_para is not None else etree.SubElement(body, _qn('w:p'))
            # 确保不加粗
            for r in p_item.findall(_qn('w:r')):
                rpr = r.find(_qn('w:rPr'))
                if rpr is not None:
                    b = rpr.find(_qn('w:b'))
                    if b is not None:
                        rpr.remove(b)
            # 标点：最后一条用句号，其余用分号
            desc_clean = desc.rstrip('。.；;')
            suffix = '。' if idx == len(items) else '；'
            _set_run_text(p_item, f"{idx}. {desc_clean}{suffix}")
            body.insert(insert_pos, p_item)
            insert_pos += 1

    print("    ✅ [none] 课程目标已替换为段落格式")


def fill_table1(root, context: dict):
    """填充 Table 1 — 课程目标

    根据 _schema_type 路由：
      - detailed: 4列表格（维度名 | 描述 | 毕业要求 | 观测点）
      - coarse:   物理删除最后一列后填充 3 列表格（维度名 | 描述 | 毕业要求）
      - none:     不调用此函数（由 _build_objectives_paragraphs 处理）
    """
    schema_type = context.get('_schema_type', 'detailed')

    tbl = _find_table_by_header(root, '课程目标')
    if tbl is None:
        print("    ⚠️ 未找到课程目标表")
        return

    # coarse: 先物理删除观测点列
    if schema_type == 'coarse':
        _remove_table_last_column(tbl)
        print("    ✂️ [coarse] 已删除课程目标表的观测点列")

    rows = tbl.findall(_qn('w:tr'))
    objectives = context.get('course', {}).get('objectives', {})

    # 三组目标: (row_start, category_key)
    groups = [
        (1, 'knowledge'),   # R1-R3
        (4, 'ability'),     # R4-R6
        (7, 'quality'),     # R7-R9
    ]

    for row_start, cat_key in groups:
        items = objectives.get(cat_key, [])
        for i in range(3):
            row_idx = row_start + i
            if row_idx >= len(rows):
                break
            cells = rows[row_idx].findall(_qn('w:tc'))

            item = items[i] if i < len(items) else {}
            desc = item.get('desc', '')
            index = item.get('index', i + 1)
            obj_mappings = item.get('mappings', [])
            first_m = obj_mappings[0] if obj_mappings else {}
            requirement = first_m.get('requirement', '')
            point = first_m.get('point', '')

            # C1: "N. XXXX" → "N. desc"
            if len(cells) > 1:
                for p in cells[1].iter(_qn('w:p')):
                    _merge_runs(p)
                    text = _get_paragraph_text(p)
                    if 'XXXX' in text:
                        _replace_xxxx_in_text(p, desc)
                    elif not text.strip():
                        _set_run_text(p, f"{index}. {desc}")

            # C2: "XXXX" → requirement
            if len(cells) > 2:
                for p in cells[2].iter(_qn('w:p')):
                    _replace_xxxx_in_text(p, str(requirement))

            # C3: "XXXX" → point（仅 detailed 模式有此列）
            if schema_type == 'detailed' and len(cells) > 3:
                for p in cells[3].iter(_qn('w:p')):
                    _replace_xxxx_in_text(p, str(point))


def fill_table2(root, context: dict):
    """填充 Table 2 — 评分体系 (9行5列, 含多组 vMerge)
    
    结构:
    - R0: Header
    - R1-R4: 考勤区域 (C0/C1/C2/C4 全部 vMerge, C3有4条描述)
    - R5-R7: 实验评分项 (C0/C1 仍 vMerge, C2=名称+比例, C3=描述, C4=100)
    - R8: 期末考核
    
    注意: C2 段落含 <w:numPr> (Word 自动编号), 不需要手动写序号。
    """
    tbl = _find_table_by_header(root, '评分构成')
    if tbl is None:
        print("    ⚠️ 未找到评分体系表")
        return
    
    rows = tbl.findall(_qn('w:tr'))
    assessment = context.get('assessment_methods', {})
    normal_ratio = assessment.get('normal_score_ratio', '')
    final_ratio = assessment.get('final_score_ratio', '')
    attendance_ratio = assessment.get('attendance_ratio', 5)
    filtered_items = assessment.get('filtered_items', [])
    
    # R1 C1: 替换 "平时成绩（XXXX %）" 中的 XXXX
    r1_cells = rows[1].findall(_qn('w:tc'))
    if len(r1_cells) > 1:
        for p in r1_cells[1].iter(_qn('w:p')):
            _replace_xxxx_in_text(p, str(int(normal_ratio) if isinstance(normal_ratio, (int, float)) else normal_ratio))
            
    # R1 C4: 分值保留模板默认 100（卷面满分），不做替换
    # 注：占比已通过 C2 中的百分比体现

    # R5-R7: 实验评分项
    xxxx_rows = [5, 6, 7]
    for slot_idx, ri in enumerate(xxxx_rows):
        if ri >= len(rows):
            break
        cells = rows[ri].findall(_qn('w:tc'))
        
        if slot_idx < len(filtered_items):
            item = filtered_items[slot_idx]
            item_name = item.get('name', '')
            item_ratio = item.get('ratio', '')
            item_desc = item.get('desc', '')
            
            # C2: 替换 XXXX → "名称（比例%）"
            # 注意: 不写手动序号 — 段落含 numPr, Word 自动编号
            if len(cells) > 2:
                c2_paras = list(cells[2].iter(_qn('w:p')))
                ratio_str = str(int(item_ratio) if isinstance(item_ratio, (int, float)) else item_ratio)
                display_text = f"{item_name}（{ratio_str}%）"
                if c2_paras:
                    _set_run_text(c2_paras[0], display_text)
                    # 删除多余段落
                    for extra_p in c2_paras[1:]:
                        cells[2].remove(extra_p)
            
            # C3: XXXX → desc
            if len(cells) > 3:
                for p in cells[3].iter(_qn('w:p')):
                    text = _get_paragraph_text(p)
                    if 'XXXX' in text:
                        _replace_xxxx_in_text(p, str(item_desc))
                    elif not text.strip():
                        _set_run_text(p, str(item_desc))
                        
            # C4: 分值保留模板默认 100（卷面满分），不做替换
    
    # R8: 期末考核
    if len(rows) > 8:
        r8_cells = rows[8].findall(_qn('w:tc'))
        
        # C1: 替换 "课程考核成绩（XXXX%）"
        if len(r8_cells) > 1:
            for p in r8_cells[1].iter(_qn('w:p')):
                _replace_xxxx_in_text(p, str(int(final_ratio) if isinstance(final_ratio, (int, float)) else final_ratio))
        
        # C3: 替换末尾的 XXXX (考核描述)
        if len(r8_cells) > 3:
            exam_desc = context.get('exams', {}).get('final_exam_desc_rt', '')
            for p in r8_cells[3].iter(_qn('w:p')):
                text = _get_paragraph_text(p)
                if 'XXXX' in text:
                    _replace_xxxx_in_text(p, str(exam_desc))
        
        # C4: 分值保留模板默认 100（卷面满分），不做替换


# ═══════════════════════════════════════════════════════════════════════
# 3. 段落填充函数
# ═══════════════════════════════════════════════════════════════════════

def fill_paragraphs(root, context: dict):
    """填充独立段落区域的 XXXX
    
    目标段落 (通过上下文文本定位):
    - "一、课程简介" 下的 "（一）主要内容" 之后: XXXX → introduction.content
    - "（二）教学设计思路" 之后: XXXX → introduction.design
    - "（一）选用教材" 之后: XXXX → 教材列表
    - "（二）参考书目与文献" 之后: XXXX → 参考书列表
    - "（三）课程网站等支持条件" 之后: XXXX → resources_url
    """
    body = root.find(_qn('w:body'))
    paragraphs = list(body.iter(_qn('w:p')))
    course = context.get('course', {})
    intro = course.get('introduction', {}) or {}
    
    # 遍历段落, 根据上下文定位 XXXX
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i]
        text = _get_paragraph_text(p)
        
        # 课程简介-主要内容
        if '主要内容' in text and '（一' in text:
            # 下一个含 XXXX 的段落
            for j in range(i + 1, min(i + 5, len(paragraphs))):
                pj = paragraphs[j]
                if 'XXXX' in _get_paragraph_text(pj):
                    content = str(intro.get('content', '') or '').strip()
                    # 将 \n 替换为 \a (软回车 = w:br)
                    _fill_multiline_paragraph(pj, content)
                    break
        
        # 教学设计思路
        elif '教学设计思路' in text and '（二' in text:
            for j in range(i + 1, min(i + 5, len(paragraphs))):
                pj = paragraphs[j]
                if 'XXXX' in _get_paragraph_text(pj):
                    design = str(intro.get('design', '') or '').strip()
                    _fill_multiline_paragraph(pj, design)
                    break
        
        # 选用教材
        elif '选用教材' in text and '（一' in text:
            for j in range(i + 1, min(i + 5, len(paragraphs))):
                pj = paragraphs[j]
                if 'XXXX' in _get_paragraph_text(pj):
                    def clean_prefix(s):
                        """剥离行首已存在的序号"""
                        return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())

                    # 教材逻辑
                    textbooks = context.get('textbooks', [])
                    tb_list = [tb for tb in textbooks if tb.get('type') == 'textbook']
                    tb_lines = []
                    for k, tb in enumerate(tb_list, 1):
                        title = clean_prefix(tb.get('title', ''))
                        author = clean_prefix(tb.get('author', ''))
                        entry = f"{author}.{title}[M].{tb.get('publisher', '')},{tb.get('year', '')}."
                        tb_lines.append(f"({k}){entry}" if len(tb_list) > 1 else entry)
                    res = '\n'.join(tb_lines) if tb_lines else '无'
                    _fill_multiline_paragraph(pj, res, clear_list_indent=True, fix_spacing=True)
                    break
        
        # 参考书目
        elif '参考书目' in text and '（二' in text:
            for j in range(i + 1, min(i + 5, len(paragraphs))):
                pj = paragraphs[j]
                if 'XXXX' in _get_paragraph_text(pj):
                    def clean_prefix(s):
                        return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())
                    
                    textbooks = context.get('textbooks', [])
                    ref_list = [tb for tb in textbooks if tb.get('type') == 'reference']
                    # 子项序号规则：单项无序号，多项用 (1)(2) 格式
                    ref_lines = []
                    for k, ref in enumerate(ref_list, 1):
                        title = clean_prefix(ref.get('title', ''))
                        author = clean_prefix(ref.get('author', ''))
                        entry = f"{author}.{title}[M].{ref.get('publisher', '')},{ref.get('year', '')}."
                        ref_lines.append(f"({k}){entry}" if len(ref_list) > 1 else entry)
                    res = '\n'.join(ref_lines) if ref_lines else '无'
                    _fill_multiline_paragraph(pj, res, clear_list_indent=True, fix_spacing=True)
                    break
        
        # 课程网站
        elif '课程网站' in text and '支持条件' in text:
            for j in range(i + 1, min(i + 5, len(paragraphs))):
                pj = paragraphs[j]
                if 'XXXX' in _get_paragraph_text(pj):
                    def clean_prefix(s):
                        return re.sub(r'^(\d+[\.\、\s]+|\(\d+\)\s*)', '', s.strip())

                    url_raw = str(course.get('resources_url', '无')).strip()
                    # 网站序号逻辑：如果是多行，也应用 (1)(2)
                    url_lines_raw = [clean_prefix(line) for line in url_raw.split('\n') if line.strip()]
                    url_lines = []
                    for k, line in enumerate(url_lines_raw, 1):
                        url_lines.append(f"({k}){line}" if len(url_lines_raw) > 1 else line)
                    url_text = '\n'.join(url_lines)
                    
                    _fill_multiline_paragraph(pj, url_text, clear_list_indent=True, fix_spacing=True)
                    break
        
        i += 1


# ═══════════════════════════════════════════════════════════════════════
# 4. 章节内容填充
# ═══════════════════════════════════════════════════════════════════════

def fill_chapter_content(root, context: dict):
    """在"三、课程内容和教学要求"标题后插入实际章节段落。
    
    方案②: 模板深克隆
    ────────────────
    从原始模板提取一章的完整 XML 段落组(11段), 为每个 calendar 条目
    深克隆该组并仅替换 XXXX 文本。所有格式(pPr/rPr/spacing/bold)
    100% 来自原始模板, 无需手动构造。
    
    模板结构 (body 直接子元素中的段落):
      P[0]: "第1章  XXXX"             — 1 run, bold
      P[1]: "主要知识点："             — 1 run, bold
      P[2]: "1.1 XXXX"               — 1 run, non-bold
      P[3]: "1.2 XXXX"               — 1 run, non-bold
      P[4]: "教学要求：XXXX"          — 2 runs (bold + non-bold)
      P[5]: "重点：XXXX"             — 2 runs
      P[6]: "难点：XXXX"             — 2 runs
      P[7]: "课程思政融入点：XXXX"    — 2 runs
      P[8]: "采用的教学方法：XXXX"    — 2 runs
      P[9]: "理论学时：XXXX学时"      — 2 runs
      P[10]: "实践学时：XXXX学时"     — 2 runs
    """
    calendar = context.get('calendar', [])
    if not calendar:
        return
    
    body = root.find(_qn('w:body'))
    all_children = list(body)
    
    # ── 1. 定位标题段落和结束段落 ──
    title_idx = None
    end_idx = None
    for ci, child in enumerate(all_children):
        if child.tag == _qn('w:p'):
            text = _get_paragraph_text(child)
            if '课程内容和教学要求' in text and title_idx is None:
                title_idx = ci
            elif '课程资料' in text and title_idx is not None:
                end_idx = ci
                break
    
    if title_idx is None or end_idx is None:
        print("    ⚠️ 未找到'课程内容和教学要求'或'课程资料'段落")
        return
    
    # ── 2. 提取模板段落组 (深克隆前保存) ──
    template_paragraphs = []
    for ci in range(title_idx + 1, end_idx):
        child = all_children[ci]
        if child.tag == _qn('w:p'):
            text = _get_paragraph_text(child)
            if text.strip() and '。。。注' not in text:
                template_paragraphs.append(child)
    
    if len(template_paragraphs) < 10:
        print(f"    ⚠️ 模板段落不足 (找到 {len(template_paragraphs)}, 期望 ≥10)")
        return
    
    # 按角色命名模板段落
    tpl_chapter_title  = template_paragraphs[0]   # "第1章  XXXX"
    tpl_knowledge_head = template_paragraphs[1]   # "主要知识点："
    tpl_knowledge_item = template_paragraphs[2]   # "1.1 XXXX"
    tpl_teaching_req   = template_paragraphs[4]   # "教学要求：XXXX"
    tpl_focus          = template_paragraphs[5]   # "重点：XXXX"
    tpl_difficulty     = template_paragraphs[6]   # "难点：XXXX"
    tpl_ideology       = template_paragraphs[7]   # "课程思政融入点：XXXX"
    tpl_method         = template_paragraphs[8]   # "采用的教学方法：XXXX"
    tpl_hours_theory   = template_paragraphs[9]   # "理论学时：XXXX学时"
    tpl_hours_practice = template_paragraphs[10]  # "实践学时：XXXX学时"
    
    # 空行模板
    tpl_empty = copy.deepcopy(tpl_knowledge_item)
    for r in tpl_empty.findall(_qn('w:r')):
        t = r.find(_qn('w:t'))
        if t is not None:
            t.text = ''
    
    # ── 3. 删除模板段落区域 ──
    to_remove = all_children[title_idx + 1: end_idx]
    for elem in to_remove:
        body.remove(elem)
    
    # 重新定位 title_idx
    all_children = list(body)
    for ci, child in enumerate(all_children):
        if child.tag == _qn('w:p') and '课程内容和教学要求' in _get_paragraph_text(child):
            title_idx = ci
            break
    
    # ── 4. 为每章克隆并插入 ──
    insert_pos = title_idx + 1
    
    for ch_idx, unit in enumerate(calendar, start=1):
        topic = unit.get('topic', '')
        content = unit.get('content', '')
        teaching_req = unit.get('teaching_requirements', '')
        # 兼容结构化 dict 格式：拼接为纯文本供大纲模板使用
        if isinstance(teaching_req, dict):
            parts = []
            if teaching_req.get('knowledge'):
                parts.append(teaching_req['knowledge'])
            if teaching_req.get('ability'):
                parts.append(teaching_req['ability'])
            if teaching_req.get('quality'):
                parts.append(teaching_req['quality'])
            if teaching_req.get('method'):
                parts.append(teaching_req['method'])
            teaching_req = '；'.join(parts)
        focus = unit.get('focus', '')
        difficulty = unit.get('difficulty', '')
        ideology = unit.get('ideology', '')
        method = unit.get('teaching_method', unit.get('method', ''))
        hours_t = unit.get('hours_theory', 0)
        hours_p = unit.get('hours_practice', 0)
        
        paragraphs_to_insert = []
        
        # 4a. 章节标题 (自动合成前缀: "第1章 xxx" 或 "项目一 xxx")
        course = context.get('course', {})
        chapter_title = _build_chapter_title(course, unit, ch_idx)
        p = copy.deepcopy(tpl_chapter_title)
        _replace_xxxx_in_runs(p, chapter_title, full_replace=True)
        paragraphs_to_insert.append(p)
        
        # 4b. "主要知识点：" (原样克隆)
        paragraphs_to_insert.append(copy.deepcopy(tpl_knowledge_head))
        
        # 4c. 知识点条目 (WYSIWYG: 直接使用 content 原文行, 不自动编号)
        if content:
            for cl in str(content).split('\n'):
                cl = cl.strip()
                if cl:
                    p = copy.deepcopy(tpl_knowledge_item)
                    _replace_xxxx_in_runs(p, cl, full_replace=True)
                    paragraphs_to_insert.append(p)

        # 4c′. 参考教材引用行（知识点后、教学要求前）
        readings = unit.get('readings', [])
        textbooks = context.get('textbooks', [])
        if readings and textbooks:
            resolved = _resolve_chapter_titles(readings, textbooks, fmt='full')
            if resolved:
                ref_text = "参考教材：" + "；".join(resolved)
                p = copy.deepcopy(tpl_knowledge_item)
                _replace_xxxx_in_runs(p, ref_text, full_replace=True)
                paragraphs_to_insert.append(p)

        # 4d-4j. 标签：内容 型段落 (克隆 → 替换 XXXX 部分)
        for tpl, value in [
            (tpl_teaching_req, teaching_req),
            (tpl_focus, focus),
            (tpl_difficulty, difficulty),
            (tpl_ideology, ideology),
            (tpl_method, method),
            (tpl_hours_theory, str(hours_t)),
            (tpl_hours_practice, str(hours_p)),
        ]:
            p = copy.deepcopy(tpl)
            _replace_xxxx_in_runs(p, value)
            paragraphs_to_insert.append(p)
        
        # 4k. 章间空行
        paragraphs_to_insert.append(copy.deepcopy(tpl_empty))
        
        # 批量插入
        for pi_p in paragraphs_to_insert:
            body.insert(insert_pos, pi_p)
            insert_pos += 1


def prepare_context(global_context: dict) -> dict:
    """准备 Syllabus 专用上下文 (从原 gen_syllabus 中的数据转换逻辑迁移)"""
    context = copy.deepcopy(global_context)
    course = context.get('course', {})
    
    # 1. Introduction: 保留原始文本, XML 填充时处理换行
    intro = course.get('introduction', {}) or {}
    if intro:
        if 'content' in intro and intro['content']:
            intro['content'] = str(intro['content']).strip()
        if 'design' in intro and intro['design']:
            intro['design'] = str(intro['design']).strip()
        course['introduction'] = intro
    
    # 2. Objectives 重组
    if 'objectives' in context and isinstance(context['objectives'], dict):
        objs = context['objectives']
        if 'objectives' not in course:
            course['objectives'] = {}
        target = course['objectives']
        
        schema_type = context.get('_schema_type', 'detailed')
        for key in ['knowledge', 'ability', 'quality']:
            if key in objs:
                items = objs[key]
                if schema_type == 'none':
                    # none 模式: 保留原始数量，不强制补齐到 3 项
                    target[key] = list(items)
                else:
                    # detailed / coarse: 保证恰好 3 项, 不足补空
                    padded = list(items)
                    empty_item = {'desc': '', 'mappings': [], 'index': ''}
                    while len(padded) < 3:
                        padded.append(empty_item)
                    target[key] = padded[:3]
    
    # 3. Calendar: 确保 hours 默认值
    if 'calendar' in context:
        for unit in context['calendar']:
            if 'hours_theory' not in unit:
                unit['hours_theory'] = 0
            if 'hours_practice' not in unit:
                unit['hours_practice'] = 0
    
    # 4. Course Nature 勾选框 (规范5类)
    nature = course.get('nature', '')
    categories = [
        ('专业必修', '专业必修课'),
        ('专业选修', '专业选修课'),
        ('公共必修', '公共必修课'),
        ('公共选修', '公共选修课'),
        ('成长必修', '成长必修课'),
    ]
    parts = []
    for key, label in categories:
        is_checked = (nature == key) or (nature == label)
        symbol = '☑' if is_checked else '☐'
        parts.append(f"{symbol}{label}")
    course['nature_rt'] = ' '.join(parts)
    
    # 5. Assessment filtered items
    if 'assessment_methods' in context and 'normal_items' in context['assessment_methods']:
        items = context['assessment_methods']['normal_items']
        context['assessment_methods']['filtered_items'] = [
            i for i in items if i.get('name') != '考勤'
        ]
    
    # 6. Exam description
    if 'exams' in context and 'final_exam' in context['exams']:
        papers = context['exams'].get('final_exam', [])
        paper_names = [p['name'] for p in papers]
        desc = '、'.join(paper_names) + ' (具体见试卷)'
        context['exams']['final_exam_desc_rt'] = desc
    
    context['course'] = course
    return context


# ═══════════════════════════════════════════════════════════════════════
# 6. 主入口
# ═══════════════════════════════════════════════════════════════════════

def _fill_syllabus(root, context: dict):
    """Syllabus 专用的填充回调函数，供 render_docx() 调用。

    根据 _schema_type 路由课程目标区域的处理方式：
      - detailed: fill_table1() 填充 4 列表格
      - coarse:   fill_table1() 删列后填充 3 列表格
      - none:     _build_objectives_paragraphs() 替换为段落
    """
    schema_type = context.get('_schema_type', 'detailed')

    fill_table0(root, context)

    if schema_type == 'none':
        _build_objectives_paragraphs(root, context)
    else:
        fill_table1(root, context)  # 内部处理 detailed / coarse 分支

    fill_table2(root, context)
    fill_paragraphs(root, context)
    fill_chapter_content(root, context)


def gen_syllabus(base_dir: Path, output_dir: Path, global_context: dict):
    """教学大纲生成主函数 — 方案 A: 纯 XML 操作
    
    流程:
    1. 复制 Syllabus.docx (ZIP) 到输出目录
    2. 解压 word/document.xml
    3. 用 lxml 替换所有 XXXX / Jinja 占位符
    4. 写回 ZIP
    """
    print("  - Generating Syllabus (XML direct)...")
    
    src_path = base_dir / "01_Syllabus_Generator" / "Syllabus.docx"
    if not src_path.exists():
        print("    ⚠️ Syllabus.docx not found. Skipping.")
        return
    
    # 准备上下文
    context = prepare_context(global_context)
    course_name = context.get('course', {}).get('name', '未命名')
    
    # 输出文件 — 优先使用归档命名
    from scripts.docx_engine import archive_filename
    arch_name = archive_filename(context, '教学大纲')
    if arch_name:
        filename = arch_name
    else:
        filename = f"2025-2026-2_教学大纲_{course_name}.docx"
    out_path = output_dir / filename
    
    try:
        render_docx(
            template_path=src_path,
            output_path=out_path,
            fill_fn=_fill_syllabus,
            context=context,
        )
        print(f"    ✨ Saved: {filename}")
        
    except Exception as e:
        print(f"    ❌ Failed: {e}")
        import traceback
        traceback.print_exc()
