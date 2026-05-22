# 任务单：交互产品开发实验 ID 类型标准化 + 实验数量与模板适配

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-05-21
> **优先级**：P1（重要）
> **背景**：教务端在处理 MSG-024（信息可视化实验二元数据重构）后，准备对所有课程重新生成实验材料时，发现**交互产品开发**课程的实验数据存在两个问题导致生成器崩溃。

---

## 一、教务侧已完成 / 正在进行的工作

1. **排查完成**：确认崩溃原因为 `sorted()` 对混合类型 ID 抛出 `TypeError`
2. **代码修复中**：教务端正在修复 `gen_experiment_xml.py` 中的排序逻辑，使其兼容混合类型 ID（防御性编程）
3. **模板适配中**：教务端正在增强实验指导书生成器，使一览表能动态扩展行以支持 >4 个实验

> [!IMPORTANT]
> 教务端的代码修复属于**防御性兜底**，不能替代数据层的规范化。混合类型 ID 在跨模块引用、日历映射、教案关联等场景中存在隐性风险。

---

## 二、请课程侧执行的任务

### 任务 1：标准化交互产品开发实验 ID 类型 ⭐

**目的**：消除 `course.yaml` 中 `experiments[].id` 字段的类型不一致问题，避免生成器排序崩溃和跨模块引用歧义。

**当前状态**（`交互产品开发/course.yaml`）：

| 实验 | 当前 ID | Python 类型 | 问题 |
|------|:-------:|:-----------:|------|
| JTBD 深度访谈 AI 陪练 | `'A'` | `str` | ⚠️ 字符串 |
| Proto-Persona 用户画像制作 | `'B'` | `str` | ⚠️ 字符串 |
| 状态机映射与视觉体系 | `2` | `int` | 整数 |
| AI 原型与创意动效生成 | `3` | `int` | 整数 |
| 启发式评估验证闭环 | `4` | `int` | 整数 |

**建议方案**（二选一，请课程端自主决策）：

#### 方案 A：全部统一为整数 ID（推荐）

```yaml
# Before
- id: 'A'
  name: JTBD 深度访谈 AI 陪练
- id: 'B'
  name: Proto-Persona 用户画像制作
- id: 2
  name: 状态机映射与视觉体系 (States & System)

# After
- id: 1
  name: JTBD 深度访谈 AI 陪练
- id: 2
  name: Proto-Persona 用户画像制作
- id: 3
  name: 状态机映射与视觉体系 (States & System)
- id: 4
  name: AI 原型与创意动效生成 (AI Prototyping)
- id: 5
  name: 启发式评估验证闭环 (Heuristic Evaluation)
```

**优点**：与信息可视化课程保持一致的 ID 风格，排序天然正确。
**注意**：需同步更新所有引用旧 ID 的位置（`calendar` 中的 `exp_id`、教案 `lesson_plans` 中的实验关联等）。

#### 方案 B：全部统一为字符串 ID

```yaml
# After
- id: 'A'
- id: 'B'
- id: 'C'
- id: 'D'
- id: 'E'
```

**优点**：保留原有字母命名风格。
**缺点**：与信息可视化课程的 ID 风格不一致。

> [!IMPORTANT]
> 无论选择哪个方案，修改 ID 后**必须全量搜索**以下位置并同步更新：
> - `calendar[].exp_id`（教学日历中的实验 ID 引用）
> - `lesson_plans` 或 `teaching_plan` 中的实验关联引用
> - `practices/experiments/` 下的增量配置文件名（如有）
> - `experiment_planning.md` 中的 ID 引用

### 任务 2：确认 5 个实验在指导书中的呈现需求

**目的**：教务端的实验指导书模板（`Template_Exp_Guide.docx`）当前设计为 **4 个实验插槽**（实验一/二/三 + 综合项目）。交互产品开发有 **5 个实验**，超出模板容量。

请课程端确认以下问题之一：

- **选项 A**：5 个实验全部需要出现在指导书中 → 教务端将扩展模板以支持 5+ 实验
- **选项 B**：实验 A、B 是课内小练习，不需要纳入正式实验指导书 → 教务端可按 3 个主实验 + 综合项目的标准模板渲染
- **选项 C**：其他方案（请描述）

> [!IMPORTANT]
> 此决策影响模板结构设计。请在回复 MSG 时明确选择。

---

## 三、规范依据

- `AGENTS.md` §Agent 边界：跨区修改须通过 MSG 委托
- `AGENTS.md` §SSOT 原则：`course.yaml` 是课程数据的唯一真实来源
- `course_schema.py` `Experiment` 模型：`id` 字段目前无类型约束，建议课程端统一后教务端补充 Schema 校验

---

## 四、验证方法

ID 标准化完成后，可运行以下命令验证：

```bash
cd "/Users/yamlam/Downloads/2025-2026-2 课程/"
/opt/anaconda3/envs/mybase/bin/python -c "
import yaml
with open('交互产品开发/course.yaml') as f:
    data = yaml.safe_load(f)
exps = data.get('experiments', [])
types = set(type(e['id']).__name__ for e in exps)
print(f'实验数: {len(exps)}, ID 类型: {types}')
assert len(types) == 1, f'ID 类型不一致: {types}'
print('✅ ID 类型校验通过')
"
```

合格标准：`ID 类型: {'int'}` 或 `{'str'}`（单一类型即可）

---

## 五、上下文引用

- **影响范围**：仅限交互产品开发课程（信息可视化和实习指导无此问题）
- **目标文件**：`交互产品开发/course.yaml` → `experiments` 区块
- **关联 MSG**：MSG-024（信息可视化实验二元数据重构）— 触发本次全量排查的来源

---
*消息时间：2026-05-21 | 教务材料 Agent*
