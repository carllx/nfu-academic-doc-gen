# How To: Downcast Conversion Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test downcast conversion nan

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
# Fixtures: float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = float_numpy_dtype

```python
dtype = float_numpy_dtype
```

### Step 2: Assign data = value

```python
data = [1.0, 2.0, np.nan]
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array(data, dtype=dtype)
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array(data, dtype=dtype)
```

### Step 5: Assign result = maybe_downcast_to_dtype(...)

```python
result = maybe_downcast_to_dtype(arr, 'infer')
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_numpy_dtype

# Workflow
dtype = float_numpy_dtype
data = [1.0, 2.0, np.nan]
expected = np.array(data, dtype=dtype)
arr = np.array(data, dtype=dtype)
result = maybe_downcast_to_dtype(arr, 'infer')
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_downcast.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*