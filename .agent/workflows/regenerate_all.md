---
description: 重新生成 2025-2026-2 学期所有课程的全部教务文档（大纲/进度表/教案/实验/考核）
---

# 重新生成所有教务文档

> 适用于修改了生成器代码、模板或 course.yaml 后，需要全量刷新输出文档的场景。
> 默认同时输出 DOCX + PDF。如需仅输出 DOCX，可在命令末尾加 `--no-pdf`。

## 前置条件

- `course.yaml` 数据已就绪且通过 `audit_course_data.py` 审计
- 模板文件 (`Template_*.docx`) 在各生成器目录下可用
- LibreOffice 已安装（PDF 转换需要，`/opt/homebrew/bin/soffice`）

## 步骤

// turbo-all

1. 生成信息可视化全部文档

```bash
cd /Users/yamlam/Downloads/教务材料 && /opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 信息可视化
```

2. 生成交互产品开发全部文档

```bash
cd /Users/yamlam/Downloads/教务材料 && /opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 交互产品开发
```

3. 确认输出文件（DOCX + PDF）

```bash
echo "=== 信息可视化 ===" && find "/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/Output/" -name "*.docx" -o -name "*.pdf" | sort && echo "---" && echo "=== 交互产品开发 ===" && find "/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/Output/" -name "*.docx" -o -name "*.pdf" | sort
```

## 验证

生成完成后，检查终端输出中是否有 ❌ 或 ⚠️ 提示。重点关注：

- 教材子项序号是否使用 `(1)` `(2)` 格式（单项无序号）
- 学时总和是否合规
- 所有模板占位符是否被替换
- PDF 转换是否全部成功（查看 📊 汇总行）
- 随机抽查 PDF 文件排版是否与 DOCX 一致

