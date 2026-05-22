"""
verify_syllabus.py — 教学大纲输出验证 (增强版)

验证项:
1. 表格数量和行数
2. vMerge 完整性 (通过 XML 检查)
3. XXXX 残留检查
4. 基本内容完整性
"""
import sys
import zipfile
from pathlib import Path
from lxml import etree

NSMAP = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def _qn(tag: str) -> str:
    prefix, local = tag.split(':')
    return f'{{{NSMAP[prefix]}}}{local}'


def verify(path: str):
    path = Path(path)
    if not path.exists():
        print(f"❌ 文件不存在: {path}")
        return False
    
    print(f"🔍 验证: {path.name}")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # 解压 XML
    with zipfile.ZipFile(path, 'r') as z:
        xml_content = z.read('word/document.xml')
    
    root = etree.fromstring(xml_content)
    
    # ─── 1. 表格数量 ────────────────────────────────────
    tables = list(root.iter(_qn('w:tbl')))
    print(f"\n📊 表格数量: {len(tables)}")
    if len(tables) != 3:
        errors.append(f"表格数量: 期望 3, 实际 {len(tables)}")
    else:
        print("   ✅ 表格数量正确 (3)")
    
    # ─── 2. 表格行数 ────────────────────────────────────
    expected_rows = [9, 10, 9]
    for ti, tbl in enumerate(tables):
        rows = tbl.findall(_qn('w:tr'))
        actual = len(rows)
        if ti < len(expected_rows):
            exp = expected_rows[ti]
            status = "✅" if actual == exp else "❌"
            print(f"   Table {ti}: {actual} 行 (期望 {exp}) {status}")
            if actual != exp:
                errors.append(f"Table {ti}: 期望 {exp} 行, 实际 {actual} 行")
    
    # ─── 3. vMerge 完整性 ────────────────────────────────
    print(f"\n🔗 vMerge 检查:")
    
    # Table 1 (课程目标): R1/R4/R7 C0 = restart, R2-3/R5-6/R8-9 C0 = continue
    if len(tables) > 1:
        t1 = tables[1]
        t1_rows = t1.findall(_qn('w:tr'))
        t1_ok = True
        
        restart_rows = [1, 4, 7]
        continue_rows = [2, 3, 5, 6, 8, 9]
        
        for ri in restart_rows:
            if ri < len(t1_rows):
                cells = t1_rows[ri].findall(_qn('w:tc'))
                if cells:
                    tcPr = cells[0].find(_qn('w:tcPr'))
                    vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                    if vm is not None:
                        val = vm.get(_qn('w:val'), 'continue')
                        if val != 'restart':
                            errors.append(f"Table 1 R{ri} C0: vMerge 应为 restart, 实际 {val}")
                            t1_ok = False
                    else:
                        errors.append(f"Table 1 R{ri} C0: 缺少 vMerge restart")
                        t1_ok = False
        
        for ri in continue_rows:
            if ri < len(t1_rows):
                cells = t1_rows[ri].findall(_qn('w:tc'))
                if cells:
                    tcPr = cells[0].find(_qn('w:tcPr'))
                    vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                    if vm is not None:
                        val = vm.get(_qn('w:val'), 'continue')
                        if val != 'continue':
                            errors.append(f"Table 1 R{ri} C0: vMerge 应为 continue, 实际 {val}")
                            t1_ok = False
                    else:
                        errors.append(f"Table 1 R{ri} C0: 缺少 vMerge continue")
                        t1_ok = False
        
        print(f"   Table 1 (课程目标) C0 vMerge: {'✅' if t1_ok else '❌'}")
    
    # Table 2 (评分表): R1-R7 C0/C1 vMerge, R1-R4 C2/C4 vMerge
    if len(tables) > 2:
        t2 = tables[2]
        t2_rows = t2.findall(_qn('w:tr'))
        t2_ok = True
        
        # C0: R1=restart, R2-R7=continue
        for ri in range(1, min(8, len(t2_rows))):
            cells = t2_rows[ri].findall(_qn('w:tc'))
            if cells:
                tcPr = cells[0].find(_qn('w:tcPr'))
                vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                expected_val = 'restart' if ri == 1 else 'continue'
                if vm is not None:
                    actual_val = vm.get(_qn('w:val'), 'continue')
                    if actual_val != expected_val:
                        errors.append(f"Table 2 R{ri} C0: vMerge 应为 {expected_val}, 实际 {actual_val}")
                        t2_ok = False
                else:
                    errors.append(f"Table 2 R{ri} C0: 缺少 vMerge")
                    t2_ok = False
        
        # C1: R1=restart, R2-R7=continue
        for ri in range(1, min(8, len(t2_rows))):
            cells = t2_rows[ri].findall(_qn('w:tc'))
            if len(cells) > 1:
                tcPr = cells[1].find(_qn('w:tcPr'))
                vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                expected_val = 'restart' if ri == 1 else 'continue'
                if vm is not None:
                    actual_val = vm.get(_qn('w:val'), 'continue')
                    if actual_val != expected_val:
                        errors.append(f"Table 2 R{ri} C1: vMerge 应为 {expected_val}, 实际 {actual_val}")
                        t2_ok = False
                else:
                    errors.append(f"Table 2 R{ri} C1: 缺少 vMerge")
                    t2_ok = False
        
        # C2 (考勤): R1=restart, R2-R4=continue
        for ri in range(1, min(5, len(t2_rows))):
            cells = t2_rows[ri].findall(_qn('w:tc'))
            if len(cells) > 2:
                tcPr = cells[2].find(_qn('w:tcPr'))
                vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                expected_val = 'restart' if ri == 1 else 'continue'
                if vm is not None:
                    actual_val = vm.get(_qn('w:val'), 'continue')
                    if actual_val != expected_val:
                        errors.append(f"Table 2 R{ri} C2: vMerge 应为 {expected_val}, 实际 {actual_val}")
                        t2_ok = False
                else:
                    errors.append(f"Table 2 R{ri} C2: 缺少 vMerge")
                    t2_ok = False
        
        # C4 (分值100): R1=restart, R2-R4=continue
        for ri in range(1, min(5, len(t2_rows))):
            cells = t2_rows[ri].findall(_qn('w:tc'))
            if len(cells) > 4:
                tcPr = cells[4].find(_qn('w:tcPr'))
                vm = tcPr.find(_qn('w:vMerge')) if tcPr is not None else None
                expected_val = 'restart' if ri == 1 else 'continue'
                if vm is not None:
                    actual_val = vm.get(_qn('w:val'), 'continue')
                    if actual_val != expected_val:
                        errors.append(f"Table 2 R{ri} C4: vMerge 应为 {expected_val}, 实际 {actual_val}")
                        t2_ok = False
                else:
                    errors.append(f"Table 2 R{ri} C4: 缺少 vMerge")
                    t2_ok = False
        
        print(f"   Table 2 (评分表) vMerge: {'✅' if t2_ok else '❌'}")
    
    # ─── 4. XXXX 残留检查 ────────────────────────────────
    print(f"\n🔍 XXXX 残留检查:")
    xxxx_count = 0
    for t in root.iter(_qn('w:t')):
        if t.text and 'XXXX' in t.text:
            xxxx_count += 1
    
    if xxxx_count == 0:
        print("   ✅ 无 XXXX 残留")
    else:
        print(f"   ⚠️ 发现 {xxxx_count} 处 XXXX 残留")
        warnings.append(f"发现 {xxxx_count} 处 XXXX 残留")
    
    # ─── 5. Jinja 标签残留检查 ────────────────────────────
    print(f"\n🔍 Jinja 标签残留检查:")
    jinja_count = 0
    for t in root.iter(_qn('w:t')):
        if t.text and '{{' in t.text:
            jinja_count += 1
    
    if jinja_count == 0:
        print("   ✅ 无 Jinja 标签残留")
    else:
        print(f"   ⚠️ 发现 {jinja_count} 处 Jinja 标签残留")
        warnings.append(f"发现 {jinja_count} 处 Jinja 标签残留")
    
    # ─── 6. 基本内容检查 ────────────────────────────────
    print(f"\n📋 内容完整性:")
    all_text = ' '.join(t.text for t in root.iter(_qn('w:t')) if t.text)
    
    checks = [
        ('课程信息', '课程信息'),
        ('课程目标', '课程目标'),
        ('评分构成', '评分构成'),
        ('课程内容和教学要求', '课程内容'),
        ('课程资料', '课程资料'),
    ]
    for label, keyword in checks:
        found = keyword in all_text
        print(f"   {label}: {'✅' if found else '❌'}")
        if not found:
            warnings.append(f"未找到 '{keyword}' 区域")
    
    # ─── 汇总 ────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    if errors:
        print(f"❌ {len(errors)} 个错误:")
        for e in errors:
            print(f"   - {e}")
    if warnings:
        print(f"⚠️ {len(warnings)} 个警告:")
        for w in warnings:
            print(f"   - {w}")
    
    if not errors and not warnings:
        print("✅ 所有验证通过!")
    elif not errors:
        print("⚠️ 验证通过 (有警告)")
    else:
        print("❌ 验证失败")
    
    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_syllabus.py <docx_path>")
        sys.exit(1)
    
    success = verify(sys.argv[1])
    sys.exit(0 if success else 1)
