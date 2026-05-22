# 任务单：迁移 archive_id 到班级级别

> **发件方**：教务材料 Agent（`/Users/yamlam/Downloads/教务材料/`）
> **收件方**：课程工作区 Agent（`/Users/yamlam/Downloads/2025-2026-2 课程/`）
> **创建时间**：2026-02-28
> **优先级**：P1 重要
> **背景**：归档命名功能已集成到所有生成器中，但发现 `archive_id`（云盘提交编号）实际为**班级级别**，而非教师级别。当前 `teacher.archive_id: 55` 是错误值，需迁移到 `classes[].archive_id` 并填入正确的班级序号。

---

## 一、教务侧已完成的工作

1. `course_schema.py` — `ClassInfo` 新增 `archive_id: Optional[int]` 字段
2. `docx_engine.py` — `archive_filename()` 改为从 `classes[].archive_id` 读取，向后兼容 `teacher.archive_id`
3. 5 个生成器（大纲/进度表/教案/实验/考核）已全部使用归档命名

---

## 二、请课程侧执行的任务

### 任务 1：在每个班级条目中添加 `archive_id` ⭐

**目的**：为每个班级填入系部汇总表分配的归档序号。

### 信息可视化 (`/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course.yaml`)

**Before:**
```yaml
teacher:
  archive_id: 55  # ← 删除此行

course:
  classes:
    - name: 24数字媒体艺术影视班
      schedule_time: ...
    - name: 24数字媒体艺术游戏班
      schedule_time: ...
```

**After:**
```yaml
teacher:
  # archive_id 已移至 classes 级别

course:
  classes:
    - name: 24数字媒体艺术影视班
      archive_id: 45
      schedule_time: ...
    - name: 24数字媒体艺术游戏班
      archive_id: 46
      schedule_time: ...
```

### 交互产品开发 (`/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course.yaml`)

**Before:**
```yaml
teacher:
  archive_id: 55  # ← 删除此行

course:
  classes:
    - name: 2023级数字媒体艺术影视班
      schedule_time: ...
```

**After:**
```yaml
teacher:
  # archive_id 已移至 classes 级别

course:
  classes:
    - name: 2023级数字媒体艺术影视班
      archive_id: 21
      schedule_time: ...
```

> [!IMPORTANT]
> `archive_id` 每学期由系部汇总表分配。不同课程、不同班级的序号各不相同。
> 同时**删除** `teacher.archive_id: 55`（错误旧值）以避免混淆。

---

## 三、规范依据

- `Spec_Global.md §8` — 云盘归档命名规范
- `course_schema.py` — `ClassInfo.archive_id` 字段定义（2026-02-28 新增）

## 四、验证方法

```bash
cd "/Users/yamlam/Downloads/教务材料"
/opt/anaconda3/envs/mybase/bin/python -m scripts.generate --course "信息可视化"
/opt/anaconda3/envs/mybase/bin/python -m scripts.generate --course "交互产品开发"
```

合格标准：
- 所有输出文件名以班级对应的 `archive_id` 开头（信息可视化影视=45、游戏=46，交互产品开发=21）
- 不再出现 `55` 作为序号

---
*消息时间：2026-02-28 | 教务材料 Agent*
