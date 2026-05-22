---
trigger: glob
description: 当修改 course_schema.py 或 Spec 规范文件时，注入 Schema 校验的必填性判定、校验级别选择和迁移期兼容规范。
globs:
  - "scripts/course_schema.py"
  - "00_Data_Context/Spec_*.md"
---

# Schema 校验通用准则 (Schema Guard)

> [!NOTE]
> 本规则编纂 `course_schema.py` 中 Schema 校验的通用原则，指导字段必填性判定和校验级别选择。

## 1. 必填性判定标准

**核心原则**：模板实际使用 = 必填。

| 场景 | 判定 | 处理方式 |
|------|------|----------|
| 模板中存在 `{{ field }}` 占位符 | **Required** | Schema 中添加 default 值或 `root_validator` 兜底 |
| `generate.py` 中编程引用 | **Required** | 同上 |
| 仅文档/规范中提及 | Optional | 保持 Optional |
| 新增字段（迁移期） | Optional + WARNING | 旧数据不报错，新数据有提示 |

## 2. 校验级别选择

| 级别 | 机制 | 适用场景 |
|------|------|----------|
| **ERROR** | `raise ValueError` / Pydantic `validator` | 数据逻辑矛盾（如学时之和不等于总学时） |
| **WARNING** | `print("⚠️ [WARNING]...")` + 返回原值 | 命名规范、格式建议、外键关联检查 |
| **INFO** | `print("ℹ️ [INFO]...")` | 非强制建议（如周数不足 16 周） |

## 3. 迁移期兼容

- 新增 validator 时，默认使用 **WARNING** 级别。
- 待所有课程数据迁移完成后，可升级为 ERROR。
- 升级前须运行 `audit_course_data.py --root "/path/to/courses"` 确认零 WARNING。
- **迁移完成标志**：`/audit` 零 WARNING 且所有 `course.yaml` 已采用新格式。
- **迁移完成后必须执行清理**（ADR 014）：删除旧字段定义（Schema）、旧格式回退代码（生成器）、废弃文件（`_deprecated/`）。不设「观察期」，不做「保留性标注」。

## 4. SSOT 同步

- Schema 变更后须同步更新 `docs/Data_Dictionary.md`。
- 判定标准变更须记录到 `.agent/memory/ADR.md`。
- `textbooks[].toc` 变更后须同步验证 `reading_utils.resolve_chapter_titles()` 兼容性（新增教材的 `chapter` 键类型须与解析引擎的匹配策略一致：int 型用于传统编号，str 型用于无编号教材）。
