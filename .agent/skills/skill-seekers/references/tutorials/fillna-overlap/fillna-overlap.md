# How To: Fillna Overlap

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna overlap

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign s = SparseArray(...)

```python
s = SparseArray([1, np.nan, np.nan, 3, np.nan])
```

### Step 2: Assign res = s.fillna(...)

```python
res = s.fillna(3)
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([1, 3, 3, 3, 3], dtype=np.float64)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.to_dense(), exp)
```

### Step 5: Assign s = SparseArray(...)

```python
s = SparseArray([1, np.nan, np.nan, 3, np.nan], fill_value=0)
```

### Step 6: Assign res = s.fillna(...)

```python
res = s.fillna(3)
```

### Step 7: Assign exp = SparseArray(...)

```python
exp = SparseArray([1, 3, 3, 3, 3], fill_value=0, dtype=np.float64)
```

### Step 8: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```


## Complete Example

```python
# Workflow
s = SparseArray([1, np.nan, np.nan, 3, np.nan])
res = s.fillna(3)
exp = np.array([1, 3, 3, 3, 3], dtype=np.float64)
tm.assert_numpy_array_equal(res.to_dense(), exp)
s = SparseArray([1, np.nan, np.nan, 3, np.nan], fill_value=0)
res = s.fillna(3)
exp = SparseArray([1, 3, 3, 3, 3], fill_value=0, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)
```

## Next Steps


---

*Source: test_array.py:206 | Complexity: Advanced | Last updated: 2026-06-02*