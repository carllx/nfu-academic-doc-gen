# How To: Group By Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group by copy

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame.set_index(...)

```python
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Carl'], 'age': [20, 21, 20]}).set_index('name')
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grp_by_same_value, grp_by_copy)
```

### Step 5: Assign grp_by_same_value = df.groupby.apply(...)

```python
grp_by_same_value = df.groupby(['age'], group_keys=False).apply(lambda group: group)
```

### Step 6: Assign grp_by_copy = df.groupby.apply(...)

```python
grp_by_copy = df.groupby(['age'], group_keys=False).apply(lambda group: group.copy())
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Carl'], 'age': [20, 21, 20]}).set_index('name')
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grp_by_same_value = df.groupby(['age'], group_keys=False).apply(lambda group: group)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grp_by_copy = df.groupby(['age'], group_keys=False).apply(lambda group: group.copy())
tm.assert_frame_equal(grp_by_same_value, grp_by_copy)
```

## Next Steps


---

*Source: test_apply_mutate.py:7 | Complexity: Intermediate | Last updated: 2026-06-02*