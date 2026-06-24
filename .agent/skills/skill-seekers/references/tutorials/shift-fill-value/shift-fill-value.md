# How To: Shift Fill Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test shift fill value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: fill_value
```

## Step-by-Step Guide

### Step 1: Assign sparse = SparseArray(...)

```python
sparse = SparseArray(np.array([1, 0, 0, 3, 0]), fill_value=8.0)
```

### Step 2: Assign res = sparse.shift(...)

```python
res = sparse.shift(1, fill_value=fill_value)
```

### Step 3: Assign exp = SparseArray(...)

```python
exp = SparseArray(np.array([fill_value, 1, 0, 0, 3]), fill_value=8.0)
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```

### Step 5: Assign fill_value = value

```python
fill_value = res.dtype.na_value
```


## Complete Example

```python
# Setup
# Fixtures: fill_value

# Workflow
sparse = SparseArray(np.array([1, 0, 0, 3, 0]), fill_value=8.0)
res = sparse.shift(1, fill_value=fill_value)
if isna(fill_value):
    fill_value = res.dtype.na_value
exp = SparseArray(np.array([fill_value, 1, 0, 0, 3]), fill_value=8.0)
tm.assert_sp_array_equal(res, exp)
```

## Next Steps


---

*Source: test_array.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*