# How To: Where Retain Fill Value

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where retain fill value

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign arr = SparseArray(...)

```python
arr = SparseArray([np.nan, 1.0], fill_value=0)
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False])
```

### Step 3: Assign res = arr._where(...)

```python
res = arr._where(~mask, 1)
```

### Step 4: Assign exp = SparseArray(...)

```python
exp = SparseArray([1, 1.0], fill_value=0)
```

### Step 5: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```

### Step 6: Assign ser = pd.Series(...)

```python
ser = pd.Series(arr)
```

### Step 7: Assign res = ser.where(...)

```python
res = ser.where(~mask, 1)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, pd.Series(exp))
```


## Complete Example

```python
# Workflow
arr = SparseArray([np.nan, 1.0], fill_value=0)
mask = np.array([True, False])
res = arr._where(~mask, 1)
exp = SparseArray([1, 1.0], fill_value=0)
tm.assert_sp_array_equal(res, exp)
ser = pd.Series(arr)
res = ser.where(~mask, 1)
tm.assert_series_equal(res, pd.Series(exp))
```

## Next Steps


---

*Source: test_indexing.py:290 | Complexity: Advanced | Last updated: 2026-06-02*