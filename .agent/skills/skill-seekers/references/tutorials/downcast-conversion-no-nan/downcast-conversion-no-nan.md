# How To: Downcast Conversion No Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test downcast conversion no nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_real_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_real_numpy_dtype

```python
dtype = any_real_numpy_dtype
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([1, 2])
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([1.0, 2.0], dtype=dtype)
```

### Step 4: Assign result = maybe_downcast_to_dtype(...)

```python
result = maybe_downcast_to_dtype(arr, 'infer')
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: any_real_numpy_dtype

# Workflow
dtype = any_real_numpy_dtype
expected = np.array([1, 2])
arr = np.array([1.0, 2.0], dtype=dtype)
result = maybe_downcast_to_dtype(arr, 'infer')
tm.assert_almost_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_downcast.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*