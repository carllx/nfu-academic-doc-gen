# How To: Setting Fill Value Fillna Still Works

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setting fill value fillna still works

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

### Step 1: Assign arr = SparseArray(...)

```python
arr = SparseArray([1.0, np.nan, 1.0], fill_value=0.0)
```

### Step 2: Assign arr.fill_value = value

```python
arr.fill_value = np.nan
```

### Step 3: Assign result = arr.isna(...)

```python
result = arr.isna()
```

### Step 4: Assign result = np.asarray(...)

```python
result = np.asarray(result)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([False, True, False])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = SparseArray([1.0, np.nan, 1.0], fill_value=0.0)
arr.fill_value = np.nan
result = arr.isna()
result = np.asarray(result)
expected = np.array([False, True, False])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*