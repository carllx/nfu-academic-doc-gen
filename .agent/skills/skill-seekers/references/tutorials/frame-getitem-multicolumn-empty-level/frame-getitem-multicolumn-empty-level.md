# How To: Frame Getitem Multicolumn Empty Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame getitem multicolumn empty level

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['1', '2', '3'], 'b': ['2', '3', '4']})
```

### Step 2: Assign df.columns = value

```python
df.columns = [['level1 item1', 'level1 item2'], ['', 'level2 item2'], ['level3 item1', 'level3 item2']]
```

### Step 3: Assign result = value

```python
result = df['level1 item1']
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['1'], ['2'], ['3']], index=df.index, columns=['level3 item1'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': ['1', '2', '3'], 'b': ['2', '3', '4']})
df.columns = [['level1 item1', 'level1 item2'], ['', 'level2 item2'], ['level3 item1', 'level3 item2']]
result = df['level1 item1']
expected = DataFrame([['1'], ['2'], ['3']], index=df.index, columns=['level3 item1'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*