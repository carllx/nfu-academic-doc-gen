# Handover: 课程数据自审指南

> **目标读者**：在 `/Users/yamlam/Downloads/2025-2026-2 课程/` 工作区操作的 Agent
> **核心目标**：确保所有 `course.yaml` 与教务材料项目的 Schema/模板/生成器保持同步

## 1. 架构关系

```
教务材料/                          ← 项目定义层 (SSOT)
├── 00_Data_Context/
│   ├── Spec_Global.md             ← 全局规范 (Schema 2.2)
│   └── course.yaml                ← demo 数据 (Schema 参考基准)
├── 01~06_*_Generator/
│   ├── Spec_*.md                  ← 各文档的编写规范
│   └── Template_*.docx            ← 格式模板
└── scripts/
    ├── generate.py                ← 主生成入口
    └── gen_*_xml.py               ← 各文档生成器

2025-2026-2 课程/                  ← 课程数据层
├── 信息可视化/course.yaml
├── 交互产品开发/course.yaml
└── [新课程]/course.yaml           ← 必须遵守 Schema 2.2
```

**关键约束**：课程数据层的 `course.yaml` 被项目定义层的生成器消费。Schema 不兼容 = 生成失败。

## 2. 自审清单

对每门课程的 `course.yaml` 执行以下检查：

### 2.1 必填字段完整性

```yaml
# 顶层结构 — 以下字段缺一不可
course:
  name: ""           # 课程全称
  code: ""           # 课程代码
  semester: ""       # 格式: "2025-2026-2"
  nature: ""         # 五选一: 专业必修课/专业选修课/公共必修课/公共选修课/实践课程
  credits: 0.0
  department: ""     # 开课单位, 如 "设计学院"
  major: ""          # 专业名
  classes: []        # 至少一个班级
  hours:
    total: 0
    theory: 0
    practice: 0

teacher:
  name: ""
  title: ""          # 职称
  department: ""     # 所属系
  team: ""           # 课程团队 (可选)

objectives:          # 三类均必填，每项: {index, desc, mappings: [{requirement, point, support_level}]}
  knowledge: []      # 新版使用 mappings[] 数组；旧版扁平 requirement/point/support_level 仍兼容
  ability: []        # ❗ desc 禁用动词：了解/熟悉/理解/掌握（OBE 规范）
  quality: []
student_analysis: "" # 可选：学情分析文本（教案首页用）

calendar: []         # 每周: {week, topic, content, hours_theory, hours_practice}
textbooks: []        # 每本: {title, author, publisher, year, type}
exams: {}            # 即使考查课也必须有最小结构
semester_config:
  start_date: ""     # 格式: "2026-02-17"
```

### 2.2 数据一致性校验

| 校验项 | 公式 | 严重级别 |
|--------|------|----------|
| 学时总量 | `hours.theory + hours.practice == hours.total` | ❌ 致命 |
| 日历学时 | `∑(calendar[].hours_theory) == hours.theory` | ❌ 致命 |
| 日历学时 | `∑(calendar[].hours_practice) == hours.practice` | ❌ 致命 |
| 平时分项总和 | `attendance_ratio + Σ(normal_items[].ratio) == normal_score_ratio` | ❌ 致命 |
| 周次连续 | `calendar[].week` 应为连续整数 1,2,3…N | ⚠️ 警告 |
| nature 合法 | 必须是上述5种之一 | ❌ 致命 |
| schedule_time 格式 | 匹配 `周[一-日]\d+-\d+节` | ⚠️ 警告 |
| **OBE 行为动词** | `objectives.*.desc` 不含禁用动词（了解/熟悉/理解/掌握） | ⚠️ 警告 |
| **目标覆盖度** | 汇总全周次 `supported_objectives`，所有 objectives 条目至少被 1 周引用 | ⚠️ 警告 |

### 2.3 多班级特殊字段

**仅在以下场景需要**：

| 场景 | 需要的字段 | 示例 |
|------|-----------|------|
| 不同班级在不同周次上课 | `classes[].week_range` | `"10-18"` |
| 同一班级不同周次节次不同 | `classes[].schedule_segments` | 见下方 |

```yaml
# 分段排课示例 (游戏班: 10-13周1-5节, 14-18周2-5节)
classes:
  - name: 24数字媒体艺术游戏班
    schedule_time: 周五1-5节
    classroom: 温泉校区 3实208
    week_range: "10-18"
    schedule_segments:
      - weeks: "10-13"
        period: "1-5节"
      - weeks: "14-18"
        period: "2-5节"
```

## 3. 审查执行步骤

```bash
# Step 1: 读取规范 (了解最新 Schema)
cat /Users/yamlam/Downloads/教务材料/00_Data_Context/Spec_Global.md

# Step 2: 对每门课程运行数据审计
cd /Users/yamlam/Downloads/教务材料
python scripts/audit_course_data.py --course 课程目录名

# Step 3: 试运行生成器 (验证兼容性)
python scripts/generate.py --course 课程目录名

# Step 4: 检查输出中的警告
#   - ⚠️ Compliance Warning → objectives 与 course_matrix 不匹配
#   - ⚠️ semester_config.start_date 未设置 → 缺少日期配置
#   - ❌ Failed → 致命错误, 需修复 course.yaml
```

## 4. 已知陷阱

| 陷阱 | 说明 | 预防 |
|------|------|------|
| `schedule_time` 写错 | 曾填"周六"但实际无周六课，导致进度表星期几错误 | **必须与真实排课系统核对** |
| `nature` 不规范 | "必修" vs "专业必修课"，影响考核方式自动推导(必修→考试) | 使用完整5类名称 |
| `hours` 不匹配 | theory+practice ≠ total，进度表学时校验失败 | 修改后立即验算 |
| 缺少 `exams` | 考核材料生成器依赖此字段，缺失则崩溃 | 即使考查课也填最小结构 |
| `calendar` 缺 `hours_theory/practice` | 进度表课时子列为空 | 每周条目必填两个学时字段 |
| `objectives.point` 与人培方案不匹配 | 观测点编号仅位移一位即不合规（如 5.1 vs 5.2） | **须运行 `audit_course_data.py`**，脚本自动加载 `graduation_requirements.yaml` + `training_plan_2025.yaml` 交叉校验 |
| 课程名与人培方案矩阵不一致 | 矩阵中为「交互产品综合创作」但实际开课为「交互产品开发」 | 记录对应关系，不可擅自改名 |
| **OBE 行为动词违规** | desc 以「掌握/理解/了解」开头，禁用但很难发现因无自动校验 | 写完 desc 后手动自查首动词，推荐用 Bloom 分类中可测量动词 |
| **supported_objectives 孤岛** | 目标定义了但从未被任何周次引用，教案中完全无体现 | 新增目标后立即检查全周次引用覆盖度 |

## 5. 新课程快速接入

推荐流程：
1. **复制模板**：从现有课程（如交互产品开发）复制 `course.yaml`
2. **替换数据**：逐字段替换为新课程的实际信息
3. **运行审计**：`python scripts/audit_course_data.py --course 新课程名`
4. **试生成**：`python scripts/generate.py --course 新课程名`
5. **Word 检查**：打开输出 `.docx` 目视确认格式和内容

## 6. 参考文档索引

| 文档 | 路径 | 用途 |
|------|------|------|
| 全局规范 | `教务材料/00_Data_Context/Spec_Global.md` | Schema 定义、模板规范、防御性规则 |
| 进度表规范 | `教务材料/02_Schedule_Generator/Spec_Schedule.md` | 分段排课、偏移映射详解 |
| Demo 数据 | `教务材料/00_Data_Context/course.yaml` | Schema 参考基准 |
| 生成器引擎 | `教务材料/docs/Handover_Universal_Docx_Engine.md` | docx_engine 技术细节 |
