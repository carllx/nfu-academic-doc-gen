# How To: Crosstab Non Aligned

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab non aligned

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([0, 1, 1], index=['a', 'b', 'c'])
```

### Step 2: Assign b = Series(...)

```python
b = Series([3, 4, 3, 4, 3], index=['a', 'b', 'c', 'd', 'f'])
```

### Step 3: Assign c = np.array(...)

```python
c = np.array([3, 4, 3], dtype=np.int64)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 0], [1, 1]], index=Index([0, 1], name='row_0'), columns=Index([3, 4], name='col_0'))
```

### Step 5: Assign result = crosstab(...)

```python
result = crosstab(a, b)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = crosstab(...)

```python
result = crosstab(a, c)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Series([0, 1, 1], index=['a', 'b', 'c'])
b = Series([3, 4, 3, 4, 3], index=['a', 'b', 'c', 'd', 'f'])
c = np.array([3, 4, 3], dtype=np.int64)
expected = DataFrame([[1, 0], [1, 1]], index=Index([0, 1], name='row_0'), columns=Index([3, 4], name='col_0'))
result = crosstab(a, b)
tm.assert_frame_equal(result, expected)
result = crosstab(a, c)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_crosstab.py:110 | Complexity: Advanced | Last updated: 2026-06-02*