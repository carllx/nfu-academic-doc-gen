# Architecture Decision Records (ADRs)

> [!NOTE]
> 本文档记录 TMA (教务材料) 项目在开发与迭代期间做出的**重要架构决策**。
> 与课程 Agent 的 ADR 保持同步（SSOT 映射见 `docs/Handover_From_CourseAgent_20260222.md` §4）。

---

## ADR 004: docxtpl 延迟加载兼容性与 init_docx 前置
**Date**: 2026-02-22
**Context**: `docxtpl >= 0.20` 将 `__init__` 改为延迟加载（`self.docx = None`），`init_docx()` 仅在 `render()` 内部由 `render_init()` 调用。`generate.py` 中 `fill_tables_programmatically()` 需要在 `render()` 前通过 `doc.tables` 访问底层 Document，导致 `AttributeError: 'NoneType' object has no attribute 'tables'`。
**Decision**:
1. 在所有需要在 `render()` 前操作 python-docx 底层对象（如 `doc.tables`、`doc.paragraphs`）的场景，必须先调用 `doc.init_docx()` 手动初始化。
2. 今后升级 pip 依赖时，须对 `docxtpl` 生成流水线执行全量冒烟测试（两门课程各跑一次），确认三类文档（大纲/进度表/教案）均成功生成。

## ADR 005: course.yaml 评分项命名与考核描述规范
**Date**: 2026-02-22
**Context**: 教务审查要求 `assessment_methods.normal_items.name` 字段必须标注测试类型（章节测试/命题测试），不允许带括号；`desc` 必须明确关联对应实验并注明考核要求。
**Decision**:
1. `normal_items.name` 的 SSOT 规范为：`章节测试N` 或 `命题测试N`（无括号，无实验名称内嵌）。
2. `normal_items.desc` 的必备结构为：`对应实验N「实验名称」。考核要求：……`，即先声明外键关联，再给出具体考核指标。
3. Schema 中以 WARNING 级别校验（不阻断），兼容旧数据迁移期。
4. 判定标准：**模板实际使用的字段 = 必填字段**（即使 Schema 类型标为 Optional）。

## ADR 006: 偏移映射与停课跳过的编码规范
**Date**: 2026-02-24  
**Context**: 审查并修复了两个隐性 Bug：(1) `gen_lessonplan_xml.py` 的 `excluded_weeks` 跳过逻辑中 `continue` 位于内层 `for cls` 循环，无法跳过外层 `for week`（ISSUE-008）；(2) `gen_schedule_xml.py` 的 `content_map` 使用简单 `offset + ci` 顺序映射，不跳过停课周，导致游戏班 W18 空行（ISSUE-009）。两个 Bug 均因数据条件未触发而长期隐藏。  
**Decision**:
1. **嵌套循环跳过须用标志变量**：`_skip = False; for inner: if cond: _skip = True; break; if _skip: continue`。
2. **偏移映射须感知中间空洞**：构建 `skip_weeks` 集合（`excluded_weeks` + `is_class_holiday()`），映射时跳过停课周，calendar 顺延。
3. **输出验证伴随代码修复**：涉及周次映射的修复必须附带 docx 输出读取验证，不得仅凭代码审阅。
4. **停课周行标注**：不在 `content_map` 中的停课周行显示"节假日停课"并学时归零。
