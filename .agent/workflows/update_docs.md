---
description: Update project documentation (README, Workflow, Architecture) to match code changes.
---

# Update Documentation Workflow

Use this workflow when the user asks to "update documentation", "sync docs with code", or when you have made significant changes to the codebase (especially `scripts/`) and need to ensure the documentation reflects the new reality.

## 1. Analyze Changes
First, understand what has changed in the codebase.
*   **Schema Changes**: Read `scripts/course_schema.py`. This is the Single Source of Truth for data structures.
*   **Script Changes**: Run `ls -R scripts/` and read the `__doc__` string or headers of any modified scripts.
*   **Directory Structure**: Run `ls -R` to see if new directories or files were added.

## 2. Update README.md
The `README.md` is the entry point. Ensure:
*   **Tree Structure**: The `目录结构` section should match the output of `ls -R` (simplified).
*   **Quick Start**: The commands in "Quick Start" must be copy-paste executable.
*   **Features**: New features (like "Schema 2.0" or "PDF parsing") should be listed.

## 3. Update docs/Architecture.md
*   **Design Philosophy**: Has the core philosophy (Domain Driven) changed?
*   **Generator Structure**: If new Generators (e.g., `07_New_Generator`) were added, update the "Directory Mapping" table.
*   **Data Flow**: If new data sources were introduced, update the Mermaid diagram.

## 4. Update docs/Data_Dictionary.md
*   **Crucial Step**: Compare this file against `scripts/course_schema.py`.
*   If `course_schema.py` added a field (e.g., `ClassInfo.classroom`), adding it here is optional but recommended.
*   **Disclaimer**: Ensure the "SSOT" warning ("Standard is `course_schema.py`") is prominent.
*   **Exams 必填性**: 确认 `exams` 字段的必填性标注与 Schema 一致（模板使用 = 必填）。
*   **normal_items 命名规范**: 确认 `normal_items` 的 `name`/`desc` 示例符合 ADR 005 规范。

## 5. Update docs/Workflow.md
*   **Step-by-Step**: Walk through the "User Workflow".
*   If a script name changed (e.g., `generate.py` -> `main.py`), update the command examples.
*   Remove "Todo" markers if features are now implemented.

## 6. Self-Correction
*   **Links**: Check that relative links (e.g., `[Overview](docs/Architecture.md)`) are valid.
*   **Consistency**: Ensure terminology is consistent (e.g., don't call it "Template" in one place and "Skeleton" in another).
