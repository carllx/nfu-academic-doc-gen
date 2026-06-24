# How To: Maybe Upcast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe upcast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: any_real_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(any_real_numpy_dtype)
```

### Step 2: Assign na_value = value

```python
na_value = na_values[dtype]
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([1, 2, na_value], dtype=dtype)
```

### Step 4: Assign result = _maybe_upcast(...)

```python
result = _maybe_upcast(arr, use_dtype_backend=True)
```

### Step 5: Assign expected_mask = np.array(...)

```python
expected_mask = np.array([False, False, True])
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 7: Assign expected = IntegerArray(...)

```python
expected = IntegerArray(arr, mask=expected_mask)
```

### Step 8: Assign expected = FloatingArray(...)

```python
expected = FloatingArray(arr, mask=expected_mask)
```


## Complete Example

```python
# Setup
# Fixtures: any_real_numpy_dtype

# Workflow
dtype = np.dtype(any_real_numpy_dtype)
na_value = na_values[dtype]
arr = np.array([1, 2, na_value], dtype=dtype)
result = _maybe_upcast(arr, use_dtype_backend=True)
expected_mask = np.array([False, False, True])
if issubclass(dtype.type, np.integer):
    expected = IntegerArray(arr, mask=expected_mask)
else:
    expected = FloatingArray(arr, mask=expected_mask)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_upcast.py:21 | Complexity: Advanced | Last updated: 2026-06-02*