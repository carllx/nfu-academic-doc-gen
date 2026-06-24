# How To: Astype Overflowsafe Disallow Rounding

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype overflowsafe disallow rounding

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.np_datetime`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([-1500, 1500], dtype='M8[ns]')
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('M8[us]')
```

### Step 3: Assign msg = "Cannot losslessly cast '-1500 ns' to us"

```python
msg = "Cannot losslessly cast '-1500 ns' to us"
```

### Step 4: Assign result = astype_overflowsafe(...)

```python
result = astype_overflowsafe(arr, dtype, round_ok=True)
```

### Step 5: Assign expected = arr.astype(...)

```python
expected = arr.astype(dtype)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Call astype_overflowsafe()

```python
astype_overflowsafe(arr, dtype, round_ok=False)
```


## Complete Example

```python
# Workflow
arr = np.array([-1500, 1500], dtype='M8[ns]')
dtype = np.dtype('M8[us]')
msg = "Cannot losslessly cast '-1500 ns' to us"
with pytest.raises(ValueError, match=msg):
    astype_overflowsafe(arr, dtype, round_ok=False)
result = astype_overflowsafe(arr, dtype, round_ok=True)
expected = arr.astype(dtype)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_np_datetime.py:212 | Complexity: Intermediate | Last updated: 2026-06-02*