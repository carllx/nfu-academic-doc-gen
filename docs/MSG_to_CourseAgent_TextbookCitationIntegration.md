# 任务单：教材章节引用标准化 — 课程端整合与新机会探索

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-05-16
> **优先级**：P1 重要
> **背景**：教务材料端完成了教材章节引用标准化 Phase 2 全链路改造（2a→2e），涉及 Schema 升级、解析引擎开发、数据回填和三生成器渲染集成。本报告将教务端的变更摘要、对课程端的直接影响、以及由此衍生的新机会完整传达给课程端 Agent，以便后续整合探索。

---

## 一、教务侧已完成的工作

### 1.1 Schema 升级 (Phase 2a)

在 `course_schema.py` 中新增：
- `TextbookChapter` 模型：`{chapter: int|str, title: str, title_en?: str}`
- `Textbook.toc` 字段：`Optional[List[TextbookChapter]]`

**影响**：课程端的 `course.yaml` 中 `textbooks[]` 现在支持 `toc` 子字段。

### 1.2 TOC 数据注入 (Phase 2a)

已完成 8 本教材的目录结构录入（共 108 个章节条目）：

| 课程 | 教材 | 章节数 |
|------|------|:------:|
| 信息可视化 | 信息可视化设计（郝亚维） | 5 |
| 信息可视化 | Visualization Analysis & Design (Munzner) | 15 |
| 交互产品开发 | 交互设计：超越人机交互（原书第5版） | 16 |
| 交互产品开发 | Interaction Design 6th Ed. (Rogers) | 16 |
| 交互产品开发 | 精益 UX (Lean UX) | 19 |
| 交互产品开发 | 交互设计精髓 (About Face 4) | 21 |
| 交互产品开发 | Refactoring UI | 9 |
| 交互产品开发 | 数字媒体交互设计（慕课版） | 6 |

**数据源**：各教材的 `knowledge/textbook/*/index.md` 中的目录翻译。

### 1.3 解析引擎开发 (Phase 2b)

新增 `scripts/utils/reading_utils.py :: resolve_chapter_titles()` 函数：

```python
resolve_chapter_titles(
    readings: list,      # 自由文本引用列表
    textbooks: list,     # 教材列表（含 toc）
    fmt: str = 'full'    # 'full'（大纲/教案）或 'short'（进度表）
) -> list               # 解析后的标准化引用
```

**支持的 readings 格式**（6 种解析模式）：
1. `《书名》第一、二章` — 中文枚举
2. `《书名》第1-3章` — 阿拉伯数字范围
3. `Munzner Ch5/Ch6` — 作者姓氏 + ChX
4. `《交互设计精髓》Ch1-3` — 书名 + 英文范围
5. `《数字媒体交互设计》项目2` — 项目编号
6. `《Refactoring UI》Hierarchy is Everything` — 字符串 section group

### 1.4 readings 回填 (Phase 2c)

**交互产品开发 `course.yaml`** 的 15 周 `readings` 字段从主题描述格式回填为精确章节引用：

| Before（不可解析） | After（可解析） |
|---------------------|-----------------|
| `《交互设计：超越人机交互》交互定义与可用性目标篇` | `《交互设计：超越人机交互》第1、2章` |
| `《交互设计精髓》目标导向设计导论篇` | `《交互设计精髓》Ch1-2` |
| `《精益UX》定性调研与假设生成篇` | `《精益 UX》Ch1-4` |
| `《Refactoring UI》视觉层级与色彩篇` | `《Refactoring UI》Hierarchy is Everything` + `Working with Color` |

解析率：18/19 = 95%（仅 W15 "全书综合复习" 保留原文，属预期行为）。

### 1.5 三生成器渲染集成 (Phase 2d)

| 生成器 | 格式 | 效果 |
|--------|------|------|
| 大纲 `gen_syllabus_xml.py` | full | 知识点后追加 `参考教材：《书名》第X章 标题` |
| 教案 `gen_lessonplan_xml.py` | full | R7 课前阅读自动展开章节标题 |
| 进度表 `gen_schedule_xml.py` | short | 列4 末尾追加 `（《书名》§1-2）` |

### 1.6 文档与规则同步 (Phase 2e + 机制审查)

已同步更新：
- `Spec_Syllabus.md` §5 — 参考教材引用行规范
- `Spec_LessonPlan.md` R7 — resolve 增强说明
- `Spec_Schedule.md` 列4 — 引用摘要说明
- `Data_Dictionary.md` §6.2 — 解析链路文档
- `rule_data_mapping.md` §3 — readings 编写格式约定
- `rule_schema_guard.md` §4 — toc SSOT 链路
- `/new_course` 工作流 — 步骤 8.5 TOC 配置检查

---

## 二、课程端受影响的文件

以下文件已被教务端直接修改（属于数据清洗性质的例外操作，详见 AGENTS.md 边界问题复盘）：

### 2.1 `信息可视化/course.yaml`
- **变更**：`textbooks[].toc` 字段注入（2 本教材，20 个章节）
- **无 readings 回填**：信息可视化的 readings 已是精确章节引用格式，无需回填

### 2.2 `交互产品开发/course.yaml`
- **变更 1**：`textbooks[].toc` 字段注入（6 本教材，88 个章节）
- **变更 2**：15 周 `readings` 字段格式回填（主题描述 → 精确章节引用）

> [!IMPORTANT]
> 课程端 Agent 应**审阅并确认**这些变更的语义正确性，尤其是 readings 的章节→教学内容映射关系。教务端基于 topic/content 语义对照完成了映射，但课程端对教学设计的理解更深入。

---

## 三、课程端可探索的新机会

以下是由 Phase 2 基础设施解锁的新能力，课程端可按价值优先级自行决定是否跟进。

### 3.1 📖 教学脚本与 TOC 交叉索引 ⭐

**机会描述**：现在 `course.yaml` 中有了完整的教材 TOC 结构数据，可以自动校验教学脚本（`weeks/W*/src/M*.md`）中引用的教材章节是否存在于 TOC 中。

**价值**：
- 防止脚本中引用不存在的章节
- 构建"哪些章节被哪些周次引用"的覆盖率报告
- 发现教材中未被任何教学周引用的章节（可能的教学盲区）

**实现路径**：编写一个审计脚本，扫描 `weeks/*/src/*.md` 中的教材引用并与 `course.yaml` 的 TOC 比对。

### 3.2 📊 readings 覆盖率可视化

**机会描述**：通过 `resolve_chapter_titles()` 引擎，可以反向统计：
- 每本教材被引用的章节覆盖率
- 哪些章节从未被任何周次引用
- readings 引用的时序分布（是否均匀分布在学期中）

**价值**：辅助教学设计调整，确保教材内容的合理覆盖。

### 3.3 🔗 knowledge/textbook 与 toc 的双向校验

**机会描述**：`knowledge/textbook/*/index.md` 是 TOC 数据的原始来源。可以建立自动校验机制，确保 `course.yaml` 中的 `toc` 数据与 `index.md` 保持同步。

**实现路径**：当 `index.md` 有更新时，自动检测 `course.yaml` 中的 TOC 是否过时。

### 3.4 📝 教案课前阅读的学生友好化

**机会描述**：resolve 引擎现在输出完整的中文章节标题。课程端可进一步扩展，为每个 reading 条目生成"阅读指引"文本，告诉学生"为什么读这一章"以及"重点关注什么"。

**数据源**：`weeks/W*/src/M*.md` 中的教学目标 + `toc[].title` 的语义匹配。

### 3.5 🎯 实习指导课程的 TOC 扩展

**机会描述**：当前 TOC 数据仅覆盖信息可视化和交互产品开发两门课。若实习指导等其他课程也有教材引用需求，可直接沿用已有架构。

---

## 四、请课程端确认/执行的任务

### 任务 1：审阅 readings 回填的语义正确性 ⭐
**目的**：确认教务端基于 topic/content 语义推导的章节映射是否符合教学设计意图。

**重点审阅**：
- 交互产品开发 W3 `readings: ["《精益 UX》Ch1-4"]` — 是否应为 Ch5-8（用户调研相关）?
- 交互产品开发 W10 `readings: ["《交互设计精髓》Ch11"]` — Ch11（编排与心流）vs Ch17（整合视觉设计）?

**方法**：
```bash
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python -c "
import yaml, sys
sys.path.insert(0, '.')
from scripts.utils.reading_utils import resolve_chapter_titles
with open('/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course.yaml', 'r') as f:
    data = yaml.safe_load(f)
for w in data['calendar']:
    readings = w.get('readings', [])
    if readings:
        resolved = resolve_chapter_titles(readings, data['textbooks'])
        print(f'W{w[\"week\"]:>2} [{w[\"topic\"]}]')
        for r in resolved:
            print(f'     → {r}')
"
```

### 任务 2：探索机会优先级排序
**目的**：根据课程端当前的开发优先级，对 §三 中的 5 个新机会进行优先级排序。

建议优先级参考：
- **3.1 交叉索引** — 如果当前正在进行教学脚本审计（如 W03/W04 审计），此机会价值最高
- **3.2 覆盖率** — 学期末教学复盘时价值最高
- **3.3 双向校验** — 如果 `index.md` 会频繁更新，此机会是防腐层

---

## 五、规范依据

| 规范 | 引用条目 |
|------|----------|
| `rule_data_mapping.md` §3 | readings 编写格式约定 |
| `rule_schema_guard.md` §4 | toc SSOT 链路 |
| `Data_Dictionary.md` §6.2 | 教材引用解析链路 |
| `Spec_Syllabus.md` §5 | 参考教材引用行规范 |
| `Spec_LessonPlan.md` R7 | resolve 增强说明 |
| `Spec_Schedule.md` 列4 | 引用摘要说明 |
| `/new_course` 步骤 8.5 | TOC 配置检查清单 |

## 六、验证方法

```bash
# 确认两门课的 Schema 校验通过
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python -c "
import yaml
from scripts.course_schema import CourseSchema
for name in ['信息可视化', '交互产品开发']:
    with open(f'/Users/yamlam/Downloads/2025-2026-2 课程/{name}/course.yaml') as f:
        CourseSchema(**yaml.safe_load(f))
    print(f'✅ {name} Schema 校验通过')
"
```

```bash
# 确认全量生成零错误
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 信息可视化 --no-pdf 2>&1 | tail -3
/opt/anaconda3/envs/mybase/bin/python scripts/generate.py --course 交互产品开发 --no-pdf 2>&1 | tail -3
```

合格标准：两门课均输出 `✅ All documents generated` 且无 ❌ / ⚠️ 错误。

---
*消息时间：2026-05-16 | 教务材料 Agent*
