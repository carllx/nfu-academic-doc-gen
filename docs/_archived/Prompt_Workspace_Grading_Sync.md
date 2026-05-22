# 同步指令：与教务材料项目教学大纲分值映射规则对齐

> **发起方**：教务材料项目 (2026-02-26)
> **目标**：确保本工作区（`2025-2026-2 课程`）中关于大纲的分数权重规则、验证脚本以及模板文件，与教务材料最新的分值动态化计算要求保持一致。

## 背景与漏洞复盘

教务材料项目刚刚完成了一次针对“教学大纲平时成绩分值超限”的 Bug 修复与复盘。
旧版大纲模板及其关联约束遗留了一个静态占位极值（每个实验 100 分，要求比例之和为 100），这在实际计算中引发了组件总和超过 `normal_score_ratio` 的严重越限问题。

**核心结论如下：**
1. 模板中的硬编码分值（如大纲模板中的「100分」）仅起排版提示作用，绝不可当作真实基准原样写入或要求源数据向其妥协。
2. 平时成绩的各个分项（考勤占比 `attendance_ratio` 与各项测试 `normal_items[].ratio`）之和，必须**严格等于**课程的平时总占比 `normal_score_ratio`（如 50分）。

## 你需要执行的任务

请仔细审查并更新本工作区（`/Users/yamlam/Downloads/2025-2026-2 课程`）下的相关文件，确保符合新规：

### 任务 1：更新课程新建模板 (`course.yaml.template`)
如果你的工程内维护着一份用于生成新课程的 YAML 模板或 Demo 数据（如 `.agent/skills/new-course/course.yaml.template` 等），请检查其中的 `assessment_methods` 结构：
```yaml
assessment_methods:
  normal_score_ratio: 50
  final_score_ratio: 50
  attendance_ratio: 10
  normal_items:
    - name: 章节测试1
      ratio: 10    # 注意这里的比例！
      desc: 对应实验1「...」。考核要求：...
    - name: 章节测试2
      ratio: 15
      desc: ...
    - name: 章节测试3
      ratio: 15
      desc: ...
```
**要求**：务必确认该模板在新建课程时，它的 `attendance_ratio`（例如 10）加上所有 `normal_items` 的 `ratio` 总和，**正好等于 `normal_score_ratio`（通常等于 50）**，而非 100。

### 任务 2：更新工作区规范与 Linter 逻辑
如果本工作区内置了任何独立于教务材料大仓的自审脚本（如 YAML 合规性检查、CI 脚本），请更改其验证断言：
- **旧断言（报废）**：`attendance_ratio + Σ(normal_items.ratio) == 100`
- **新断言（生效）**：`attendance_ratio + Σ(normal_items.ratio) == normal_score_ratio`
请确保在文档或规则中更新这条说明，以免未来新建课程时被错误引导。

### 任务 3：审核存量课程
「信息可视化设计」和「交互产品开发」这两门课的 `course.yaml` 已经由教务材料 Agent 更新完毕，目前的分配是 **考勤 10% + 章节测试 10%、15%、15% = 50%**。如果你的工作区还管理着其他的实体课程目录，请逐一检查它们的 `course.yaml` 并修复超额的 ratio 分配。

## 成功标准

- [ ] 工作区内的模板文件 (`*.template` 或 `demo.yaml`) 的默认比重相加等于 `normal_score_ratio`。
- [ ] 存量课程（如果存在第三方课程）的平时分值比例能够通过最新的 `course_schema.py` 严格校验。
- [ ] 本 Agent 工作区涉及文档已将此条动态换算规则归档，不会再次产出旧版静态极值（100分）的数据。
