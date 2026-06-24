# How To: Merge Cross Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge cross series

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign ls = Series(...)

```python
ls = Series([1, 2, 3, 4], index=[1, 2, 3, 4], name='left')
```

### Step 2: Assign rs = Series(...)

```python
rs = Series([3, 4, 5, 6], index=[3, 4, 5, 6], name='right')
```

### Step 3: Assign res = merge(...)

```python
res = merge(ls, rs, how='cross')
```

### Step 4: Assign expected = merge(...)

```python
expected = merge(ls.to_frame(), rs.to_frame(), how='cross')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
ls = Series([1, 2, 3, 4], index=[1, 2, 3, 4], name='left')
rs = Series([3, 4, 5, 6], index=[3, 4, 5, 6], name='right')
res = merge(ls, rs, how='cross')
expected = merge(ls.to_frame(), rs.to_frame(), how='cross')
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_merge_cross.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*