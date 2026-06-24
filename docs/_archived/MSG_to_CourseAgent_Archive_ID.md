# 任务单：课程端新增 `teacher.archive_id` 归档序号字段

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-27
> **优先级**：P2 常规
> **背景**：教务端新增了云盘归档命名规范（`Spec_Global.md §8`），需要课程端在 `course.yaml` 中提供教师归档序号字段，以支持自动化归档命名。

---

## 一、教务侧已完成的工作

1. **Schema 变更**：`course_schema.py` 的 `TeacherInfo` 新增可选字段 `archive_id: Optional[int]`（缺失时 fallback 为 `None`，不影响现有数据）
2. **Data Dictionary 同步**：`Data_Dictionary.md` §3 已新增字段说明
3. **规范文档**：`Spec_Global.md` 新增 §8「云盘归档命名规范」，定义了四类教务文档的归档命名公式
4. **工作流更新**：`mailbox_out.md` 新增「步骤 5：归档输出」

## 二、请课程侧执行的任务

### 任务 1：在两门课程的 `course.yaml` 中添加 `teacher.archive_id` 字段

**目的**：提供归档序号，使教务端可按规范自动重命名输出文档。

**修改位置**：`teacher` 节点下新增 `archive_id` 字段

```yaml
# Before
teacher:
  name: 林昕
  title: 无
  office: A101
  department: 数字媒体艺术
  team: 无

# After
teacher:
  name: 林昕
  title: 无
  office: A101
  department: 数字媒体艺术
  team: 无
  archive_id: 55    # 2025-2026-2 学期归档序号（每学期更换）
```

**适用文件**：
- `/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course.yaml`
- `/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course.yaml`

> [!IMPORTANT]
> `archive_id` 为 **每学期由系部汇总表分配的序号**，2025-2026-2 学期林昕的序号为 **55**。下一学期开课时须更新为新序号。

---

## 三、规范依据

- [Spec_Global.md §8 云盘归档命名规范](file:///Users/yamlam/Downloads/教务材料/00_Data_Context/Spec_Global.md)
- [Data_Dictionary.md §3 教师信息](file:///Users/yamlam/Downloads/教务材料/docs/Data_Dictionary.md)
- [course_schema.py TeacherInfo](file:///Users/yamlam/Downloads/教务材料/scripts/course_schema.py)

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python scripts/audit_course_data.py --root "/Users/yamlam/Downloads/2025-2026-2 课程"
```

合格标准：无新增 `[CRITICAL]` 或 `[WARN]` 错误。`archive_id` 为可选字段，Schema 不会因缺失报错，但填写后可支持归档命名自动化。

---
*消息时间：2026-02-27 | 教务材料 Agent*
