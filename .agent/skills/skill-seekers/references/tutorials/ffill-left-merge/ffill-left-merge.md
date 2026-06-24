# How To: Ffill Left Merge

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ffill left merge

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3, 1, 2, 3], 'group': ['a', 'a', 'a', 'b', 'b', 'b']})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key': ['b', 'c', 'd'], 'rvalue': [1, 2, 3]})
```

### Step 3: Assign result = merge_ordered(...)

```python
result = merge_ordered(df1, df2, fill_method='ffill', left_by='group', how='left')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3, 1, 2, 3], 'group': ['a', 'a', 'a', 'b', 'b', 'b'], 'rvalue': [np.nan, 2.0, 2.0, np.nan, 2.0, 2.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3, 1, 2, 3], 'group': ['a', 'a', 'a', 'b', 'b', 'b']})
df2 = DataFrame({'key': ['b', 'c', 'd'], 'rvalue': [1, 2, 3]})
result = merge_ordered(df1, df2, fill_method='ffill', left_by='group', how='left')
expected = DataFrame({'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3, 1, 2, 3], 'group': ['a', 'a', 'a', 'b', 'b', 'b'], 'rvalue': [np.nan, 2.0, 2.0, np.nan, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_ordered.py:223 | Complexity: Intermediate | Last updated: 2026-06-02*