# How To: Neg Operator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test neg operator

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = SparseArray(...)

```python
arr = SparseArray([-1, -2, np.nan, 3], fill_value=np.nan, dtype=np.int8)
```

### Step 2: Assign res = value

```python
res = -arr
```

### Step 3: Assign exp = SparseArray(...)

```python
exp = SparseArray([1, 2, np.nan, -3], fill_value=np.nan, dtype=np.int8)
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(exp, res)
```

### Step 5: Assign arr = SparseArray(...)

```python
arr = SparseArray([-1, -2, 1, 3], fill_value=-1, dtype=np.int8)
```

### Step 6: Assign res = value

```python
res = -arr
```

### Step 7: Assign exp = SparseArray(...)

```python
exp = SparseArray([1, 2, -1, -3], fill_value=1, dtype=np.int8)
```

### Step 8: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(exp, res)
```


## Complete Example

```python
# Workflow
arr = SparseArray([-1, -2, np.nan, 3], fill_value=np.nan, dtype=np.int8)
res = -arr
exp = SparseArray([1, 2, np.nan, -3], fill_value=np.nan, dtype=np.int8)
tm.assert_sp_array_equal(exp, res)
arr = SparseArray([-1, -2, 1, 3], fill_value=-1, dtype=np.int8)
res = -arr
exp = SparseArray([1, 2, -1, -3], fill_value=1, dtype=np.int8)
tm.assert_sp_array_equal(exp, res)
```

## Next Steps


---

*Source: test_unary.py:43 | Complexity: Advanced | Last updated: 2026-06-02*