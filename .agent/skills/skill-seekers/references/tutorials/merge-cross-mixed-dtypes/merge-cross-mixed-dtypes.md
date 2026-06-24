# How To: Merge Cross Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge cross mixed dtypes

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame(['a', 'b', 'c'], columns=['A'])
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame(range(2), columns=['B'])
```

### Step 3: Assign result = merge(...)

```python
result = merge(left, right, how='cross')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['a', 'a', 'b', 'b', 'c', 'c'], 'B': [0, 1, 0, 1, 0, 1]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame(['a', 'b', 'c'], columns=['A'])
right = DataFrame(range(2), columns=['B'])
result = merge(left, right, how='cross')
expected = DataFrame({'A': ['a', 'a', 'b', 'b', 'c', 'c'], 'B': [0, 1, 0, 1, 0, 1]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_cross.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*