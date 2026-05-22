# Handover: 教学大纲生成器 — 全流程重建需求

> **日期**: 2026-02-22  
> **状态**: ❌ 当前输出不合格，需要全流程重新架构

---

## 一、核心问题

**输出的 docx 格式与官方模板（`Syllabus.docx`）不一致。** 具体表现：

1. **评分表合并单元格丢失** — 原始模板中 R1-R4 的 C0（"课程过程性考核"）、C1（"平时成绩"）、C2（"1.考勤"）、C4（"100"）是纵向合并的一个大单元格，但输出中每行都是独立单元格并重复文字
2. **课程目标表** — 原始模板中 R1-R3 C0（"知识目标"）也是纵向合并，输出中同样被拆散
3. **字体/间距/边框等细节格式** — 从占位到模板到输出的过程中逐步劣化

**根因**: `docxtpl`（Jinja2 模板引擎）在渲染时**不保留 Word 垂直合并（vMerge）元素**。任何带有 `{{ }}` 变量的合并单元格区域，在渲染后都会丢失合并属性。

---

## 二、期望的工作流

```
Syllabus.docx (占位文件，包含所有格式)
    ↓ 替换 XXXX → Jinja2 变量
Template_Syllabus.docx (模板文件)
    ↓ docxtpl.render() + fill_tables_programmatically()
Output.docx (最终输出，格式与 Syllabus.docx 完全一致)
```

**约束**:
- 输出必须在**表格结构、合并方式、字体、边框**上与 `Syllabus.docx` 完全一致
- 唯一的差异应是 `XXXX` 被替换为实际数据

---

## 三、Syllabus.docx 完整结构清单

### 3.1 段落 (共 48 段)

| 段落 | 内容 | 变量 | 方式 |
|------|------|------|------|
| P4 | XXXX | `course.introduction.content_rt` | Jinja |
| P7 | XXXX | `course.introduction.design_rt` | Jinja |
| P13-P25 | 第1章 XXXX / 知识点 / 教学要求 / 重难点 / 思政 / 教学方法 / 学时 | `calendar[]` 各字段 | **编程填充** (fill_chapter_content) |
| P29 | XXXX | textbook for loop | Jinja |
| P33 | XXXX | reference for loop | Jinja |
| P37 | XXXX | `course.resources_url` | Jinja |

### 3.2 Table 0 — 课程信息 (9 行 4 列)

| 行 | 列 | 内容/占位 | 变量 | 合并 |
|----|-----|----------|------|------|
| R0 | C0-3 | "课程信息" | — | gridSpan=4 |
| R1 | C1 | `{{ course.code }}` | 已有 | — |
| R1 | C3 | `{{ course.name }}` | 已有 | — |
| R2 | C1 | (空) | `course.department` | — |
| R2 | C3 | "2025-2026学年第二学期" | `course.semester` | — |
| R3 | C1 | XXXX | `course.grade` | — |
| R3 | C3 | "数字媒体艺术" | `course.major` | — |
| R4 | C1 | `{{ course.credits }}` | 已有 | — |
| R4 | C3 | `{{ course.hours.total }}` | 已有 | — |
| R5 | C1-3 | ☐ 必修 ☐ 选修 ... | `course.nature_rt` | **gridSpan=3** |
| R6 | C1-3 | XXXX | `course.prerequisites` | **gridSpan=3** |
| R7 | C1-3 | "无" | — | gridSpan=3 |
| R8 | C0-3 | 签名栏 | — | gridSpan=4 |

### 3.3 Table 1 — 课程目标 (10 行 4 列)

| 行 | C0 | C1 | C2 | C3 | 合并 |
|----|----|----|----|----|------|
| R0 | "课程目标" (gridSpan=2) | — | "对应毕业要求" | "对应观测点" | — |
| R1-R3 | **"知识目标" (vMerge)** | 1-3. XXXX | XXXX | XXXX | **C0 纵向合并** |
| R4-R6 | **"能力目标" (vMerge)** | 1-3. XXXX | XXXX | XXXX | **C0 纵向合并** |
| R7-R9 | **"素质目标" (vMerge)** | 1-3. XXXX | XXXX | XXXX | **C0 纵向合并** |

### 3.4 Table 2 — 评分体系 (9 行 5 列) ⚠️ 关键难点

| 行 | C0 | C1 | C2 | C3 | C4 | 合并方式 |
|----|----|----|----|----|-----|---------|
| R0 | "评分构成与占比" (gridSpan=3) | — | — | "考核要求" | "分值" | — |
| R1-R4 | **"课程过程性考核" (vMerge 4行)** | **"平时成绩（XXXX%）" (vMerge 4行)** | **"1.考勤（10%）" (vMerge 4行)** | (1)-(4)各一条 | **"100" (vMerge 4行)** | **C0,C1,C2,C4 全部纵向合并** |
| R5-R7 | **vMerge续** | **vMerge续** | XXXX（XXXX%） | XXXX | "100" | 仍在同一 vMerge 组内 |
| R8 | "课程期末考核" | "课程考核成绩（XXXX%）" | "考查" | 考查说明+XXXX | "100" | 独立行 |

> [!CAUTION]
> **R1-R7 的 C0、C1 是一个 7 行纵向合并的大单元格。** 在 Word XML 中，只有 R1 的 `<w:tc>` 包含 `<w:vMerge w:val="restart"/>`（合并起始），R2-R7 的对应 `<w:tc>` 包含 `<w:vMerge/>`（合并延续，不含文字）。docxtpl 渲染后，这些 vMerge 属性被破坏，导致每行都变成独立单元格并重复显示文字。

---

## 四、已知的技术限制

| 限制 | 说明 | 影响 |
|------|------|------|
| docxtpl 破坏 vMerge | 含 `{{ }}` 变量的合并区域在渲染后丢失合并 | 评分表、课程目标表 |
| python-docx 不能用于 docxtpl 输出 | SKILL.md 明确规定: 不能将 docxtpl 渲染输出再用 python-docx 打开修改 | 评分表编程填充 |
| XML 中 XXXX 可能被拆分到多个 `<w:r>` | 占位符跨 run 时简单文本替换不可靠 | 所有表格变量替换 |

---

## 五、推荐的重建方案

### 方案 A: XML 直接操作（推荐）

放弃 `docxtpl`，完全使用 XML 操作：
1. 复制 `Syllabus.docx` ZIP
2. 解析 `word/document.xml`
3. 用 lxml 精确替换每个 `XXXX` 为实际数据
4. 重新打包为 ZIP

**优点**: 100% 保留原始格式（合并、边框、字体全部不变）  
**缺点**: 需要处理跨 run 的 XXXX 替换

### 方案 B: 混合方案

对于**不涉及合并单元格**的区域使用 `docxtpl`，对于**合并区域**使用 XML 后处理修复 vMerge。

### 方案 C: 分区渲染

将模板拆分为多个区域，分别处理：
- 段落区域 → docxtpl Jinja 渲染（安全）
- 表格区域 → 全部使用 python-docx 编程填充

---

## 六、验证标准

每次修改后，必须通过以下自动化验证：

```python
# 1. 表格一致性
assert len(output.tables) == len(syllabus.tables) == 3
assert [len(t.rows) for t in output.tables] == [9, 10, 9]

# 2. 评分表合并检查 (通过 XML vMerge)
# R1-R7 C0 必须是 vMerge 合并的

# 3. 视觉对比
# 将 Syllabus.docx 和 Output.docx 都转换为 PDF/图片，像素级对比
```

---

## 七、当前文件状态

| 文件 | 状态 | 说明 |
|------|------|------|
| `Syllabus.docx` | ✅ 正确 | 官方模板 + XXXX 占位符，格式完整 |
| `Template_Syllabus.docx` | ⚠️ 部分正确 | 从 Syllabus.docx ZIP 复制，XXXX→Jinja 替换完成，但渲染后合并丢失 |
| `generate.py` | ⚠️ 逻辑正确但输出格式错误 | `fill_chapter_content` 和评分表替换逻辑已有，但 vMerge 问题未解决 |
| `course_schema.py` | ✅ 已更新 | CalendarWeek 新增 5 个 Optional 字段 |
| `course.yaml` (两门) | ✅ 已更新 | 包含新字段数据 |

---

## 八、交接清单

- [ ] 选定重建方案 (A/B/C)
- [ ] 重写 `gen_syllabus()` 核心渲染逻辑
- [ ] 逐段/逐表验证 Syllabus.docx ↔ Output.docx 一致性
- [ ] 自动化验证脚本（表结构 + vMerge + 视觉对比）
- [ ] 两门课程 (交互产品开发 + 信息可视化) 输出验收
