# How To: Frame Describe Multikey

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame describe multikey

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tsframe, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby([lambda x: x.year, lambda x: x.month])
```

### Step 2: Assign result = grouped.describe(...)

```python
result = grouped.describe()
```

### Step 3: Assign desc_groups = value

```python
desc_groups = []
```

### Step 4: Assign expected = pd.concat(...)

```python
expected = pd.concat(desc_groups, axis=1)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 7: Assign result = groupedT.describe(...)

```python
result = groupedT.describe()
```

### Step 8: Assign expected = value

```python
expected = tsframe.describe().T
```

### Step 9: Assign expected.index = MultiIndex(...)

```python
expected.index = MultiIndex(levels=[[0, 1], expected.index], codes=[[0, 0, 1, 1], range(len(expected.index))])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign group = unknown.describe(...)

```python
group = grouped[col].describe()
```

### Step 12: Assign group_col = MultiIndex(...)

```python
group_col = MultiIndex(levels=[Index([col], dtype=tsframe.columns.dtype), group.columns], codes=[[0] * len(group.columns), range(len(group.columns))])
```

### Step 13: Assign group = DataFrame(...)

```python
group = DataFrame(group.values, columns=group_col, index=group.index)
```

### Step 14: Call desc_groups.append()

```python
desc_groups.append(group)
```

### Step 15: Assign groupedT = tsframe.groupby(...)

```python
groupedT = tsframe.groupby({'A': 0, 'B': 0, 'C': 1, 'D': 1}, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: tsframe, using_infer_string

# Workflow
grouped = tsframe.groupby([lambda x: x.year, lambda x: x.month])
result = grouped.describe()
desc_groups = []
for col in tsframe:
    group = grouped[col].describe()
    group_col = MultiIndex(levels=[Index([col], dtype=tsframe.columns.dtype), group.columns], codes=[[0] * len(group.columns), range(len(group.columns))])
    group = DataFrame(group.values, columns=group_col, index=group.index)
    desc_groups.append(group)
expected = pd.concat(desc_groups, axis=1)
tm.assert_frame_equal(result, expected)
if using_infer_string:
    return
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    groupedT = tsframe.groupby({'A': 0, 'B': 0, 'C': 1, 'D': 1}, axis=1)
result = groupedT.describe()
expected = tsframe.describe().T
expected.index = MultiIndex(levels=[[0, 1], expected.index], codes=[[0, 0, 1, 1], range(len(expected.index))])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:74 | Complexity: Advanced | Last updated: 2026-06-02*