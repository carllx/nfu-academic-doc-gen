# How To: Invert Operator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invert operator

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
arr = SparseArray([False, True, False, True], fill_value=False, dtype=np.bool_)
```

### Step 2: Assign exp = SparseArray(...)

```python
exp = SparseArray(np.invert([False, True, False, True]), fill_value=True, dtype=np.bool_)
```

### Step 3: Assign res = value

```python
res = ~arr
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(exp, res)
```

### Step 5: Assign arr = SparseArray(...)

```python
arr = SparseArray([0, 1, 0, 2, 3, 0], fill_value=0, dtype=np.int32)
```

### Step 6: Assign res = value

```python
res = ~arr
```

### Step 7: Assign exp = SparseArray(...)

```python
exp = SparseArray([-1, -2, -1, -3, -4, -1], fill_value=-1, dtype=np.int32)
```

### Step 8: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(exp, res)
```


## Complete Example

```python
# Workflow
arr = SparseArray([False, True, False, True], fill_value=False, dtype=np.bool_)
exp = SparseArray(np.invert([False, True, False, True]), fill_value=True, dtype=np.bool_)
res = ~arr
tm.assert_sp_array_equal(exp, res)
arr = SparseArray([0, 1, 0, 2, 3, 0], fill_value=0, dtype=np.int32)
res = ~arr
exp = SparseArray([-1, -2, -1, -3, -4, -1], fill_value=-1, dtype=np.int32)
tm.assert_sp_array_equal(exp, res)
```

## Next Steps


---

*Source: test_unary.py:68 | Complexity: Advanced | Last updated: 2026-06-02*