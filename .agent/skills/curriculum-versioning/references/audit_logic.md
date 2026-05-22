# 审计校验逻辑 (Audit Logic)

> 本文档说明 `audit_course_data.py` 如何根据 `schema_type` 分派人培交叉校验。

## 1. 人培数据四层架构

```
_archived/南方人培_源文件/      → PDF 原始文档（归档，不直接消费）
_archived/人培_XXXX_本科.md    → 人工可读的清洗 Markdown（参考用）
training_plans/graduation_requirements_{version}.yaml  → 观测点命名 SSOT（含 schema_type）
training_plans/training_plan_{version}.yaml            → 课程支撑矩阵 SSOT
```

**关键规则**：审计脚本**只消费 YAML 层**，不读取 PDF 或 Markdown。

## 2. 校验分派流程

```python
# 伪代码
version = course['training_plan_version']  # e.g. "2025"
grad_req = load(f'graduation_requirements_{version}.yaml')
schema_type = grad_req['schema_type']  # none / coarse / detailed

if schema_type == 'detailed':
    # 精确校验：逐条比对观测点名称
    validate_detailed(objectives, grad_req)
elif schema_type == 'coarse':
    # 粗略校验：仅校验大类编号（如 "2 专业知识"）
    validate_coarse(objectives, grad_req)
elif schema_type == 'none':
    # 跳过人培交叉校验
    print("[INFO] schema_type=none, 跳过人培交叉校验")
```

## 3. `detailed` 校验细节

- 逐条比对 `objectives[].mappings[].point` 与 `graduation_requirements` 中的观测点文本
- 编号索引仅位移一位即可导致教务不合规（如 5.1 vs 5.2）
- 使用精确字符串匹配，不做模糊匹配

## 4. `coarse` 校验细节

- 仅校验 `objectives[].mappings[].requirement` 中的大类编号
- 不检查观测点（因 2024 版人培未细分观测点）
- 课程名匹配使用 n-gram 模糊匹配（阈值 ≥ 0.5）

## 5. 覆盖度审计

独立于 `schema_type`，始终执行：

- 汇总 `calendar[].supported_objectives` 的所有引用
- 与 `objectives` 定义的全部条目做差集
- 未被引用的目标报告为「孤岛目标」（`[WARN]`）

## 6. 新增人培版本的接入流程

1. 获取新版人培原始文档 → 归档至 `_archived/南方人培_源文件/`
2. 清洗为 Markdown → 归档至 `_archived/`
3. 提取结构化 YAML：
   - `graduation_requirements_{new_version}.yaml`（标注 `schema_type`）
   - `training_plan_{new_version}.yaml`（课程支撑矩阵）
4. 在审计脚本中确认新版本能被正确加载
5. 在对应课程的 `course.yaml` 中更新 `training_plan_version`
6. 运行全量审计确认零错误
