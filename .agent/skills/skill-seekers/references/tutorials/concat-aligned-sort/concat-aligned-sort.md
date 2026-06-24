# How To: Concat Aligned Sort

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat aligned sort

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'c': [1, 2], 'b': [3, 4], 'a': [5, 6]}, columns=['c', 'b', 'a'])
```

### Step 2: Assign result = pd.concat(...)

```python
result = pd.concat([df, df], sort=True, ignore_index=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [5, 6, 5, 6], 'b': [3, 4, 3, 4], 'c': [1, 2, 1, 2]}, columns=['a', 'b', 'c'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat([df, df[['c', 'b']]], join='inner', sort=True, ignore_index=True)
```

### Step 6: Assign expected = value

```python
expected = expected[['b', 'c']]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'c': [1, 2], 'b': [3, 4], 'a': [5, 6]}, columns=['c', 'b', 'a'])
result = pd.concat([df, df], sort=True, ignore_index=True)
expected = DataFrame({'a': [5, 6, 5, 6], 'b': [3, 4, 3, 4], 'c': [1, 2, 1, 2]}, columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
result = pd.concat([df, df[['c', 'b']]], join='inner', sort=True, ignore_index=True)
expected = expected[['b', 'c']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*