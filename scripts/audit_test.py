import os
import sys
import zipfile
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET

# 确保能导入 generate.py
script_dir = Path("/Users/yamlam/Downloads/教务材料/scripts")
sys.path.append(str(script_dir))
import generate

def run_audit():
    # 1. 设置工作区
    course_name = "TestCourse"
    target_dir = Path("/Users/yamlam/Documents/nfu - 教务/2025-2026-2") / course_name
    
    # 运行 generate.py
    print("🚀 开始运行生成脚本...")
    try:
        generate.generate_documents(
            course_dir_name=str(target_dir), 
            base_dir=script_dir.parent, 
            output_pdf=False
        )
    except Exception as e:
        print(f"❌ 生成失败: {e}")
        return

    # 2. 验证生成文件
    output_dir = target_dir / "Output"
    docx_file = output_dir / "排版测试课_实验指导书.docx" # 注意名称根据生成逻辑确认，如果有前缀可能是 排版测试课_Template_Exp_Guide.docx，其实这里我们只要找 *指导书*.docx
    
    guide_docx = None
    for f in output_dir.glob("*.docx"):
        if "指导书" in f.name:
            guide_docx = f
            break
            
    if not guide_docx:
        print("❌ 未找到实验指导书 DOCX。目录内容:")
        for f in output_dir.glob("*"): print(f.name)
        return
        
    print(f"✅ 找到实验指导书: {guide_docx.name}")
    
    # 3. 解压并解析 document.xml
    print("🚀 开始解压并分析 document.xml...")
    xml_content = None
    with zipfile.ZipFile(guide_docx, 'r') as docx_zip:
        xml_content = docx_zip.read('word/document.xml')
        
    root = ET.fromstring(xml_content)
    # 定义 Word 命名空间
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    # 获取所有的文本以做粗略检查
    all_texts = []
    for t in root.findall('.//w:t', ns):
        if t.text:
            all_texts.append(t.text)
            
    full_doc_text = "".join(all_texts)
    
    # 检查 1: 一览表的表格数据行数是否被裁切为 3 行
    # 在文档中找到包含"项目名称"或"序号"表头的表格
    tables = root.findall('.//w:tbl', ns)
    overview_table = None
    for tbl in tables:
        first_row_texts = "".join([t.text for t in tbl.findall('.//w:tr[1]//w:t', ns) if t.text])
        if '序号' in first_row_texts and '项目名称' in first_row_texts:
            overview_table = tbl
            break
            
    if overview_table is not None:
        # 去掉表头和合计行，计算数据行数
        rows = overview_table.findall('.//w:tr', ns)
        data_rows = len(rows) - 2
        print(f"🔍 检查1 (一览表行数): 找到 {data_rows} 行数据")
        if data_rows == 3:
            print("  ✅ 断言通过：一览表已精准裁切为 3 行")
        else:
            print(f"  ❌ 断言失败：一览表行数为 {data_rows}，预期为 3")
    else:
        print("  ❌ 断言失败：未找到一览表")
        
    # 检查 2: 目录区是否成功删除了多余的“实验四”等占位段落
    # 找目录里是否还有"实验四"或者"综合项目"
    # 我们知道课程只有 3 个实验，没有综合项目(在这个例子里实验3是综合性)
    print("🔍 检查2 (目录占位删除):")
    if '实验四' in full_doc_text:
        print("  ❌ 断言失败：目录或正文中仍然残余“实验四”")
    else:
        print("  ✅ 断言通过：已成功清理“实验四”")
        
    if '综合项目' in full_doc_text:
        print("  ⚠️ 存在“综合项目”字样，检查是否是正常数据，还是残余的目录占位。")
    
    # 检查 3: 漏网的冗余 XXXX
    print("🔍 检查3 (冗余 XXXX):")
    xxxx_count = full_doc_text.count("XXXX")
    if xxxx_count > 0:
        print(f"  ❌ 断言失败：文档中还有 {xxxx_count} 个漏网的“XXXX”未被替换或清理")
        # 寻找附近文本上下文
        for p in root.findall('.//w:p', ns):
            p_text = "".join([t.text for t in p.findall('.//w:t', ns) if t.text])
            if "XXXX" in p_text:
                print(f"      遗漏上下文: {p_text}")
    else:
        print("  ✅ 断言通过：文档中无遗漏的“XXXX”")

if __name__ == "__main__":
    run_audit()
