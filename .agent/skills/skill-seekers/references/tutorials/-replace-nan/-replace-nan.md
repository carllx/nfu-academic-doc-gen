# How To:  Replace Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that _replace_nan returns the original array if there are no
NaNs, not a copy.

## Prerequisites

**Required Modules:**
- `inspect`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.lib._nanfunctions_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: ' Test that _replace_nan returns the original array if there are no\n    NaNs, not a copy.\n    '

```python
' Test that _replace_nan returns the original array if there are no\n    NaNs, not a copy.\n    '
```

**Verification:**
```python
assert mask is None
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([0, 1], dtype=dtype)
```

**Verification:**
```python
assert result is arr
```

### Step 3: Assign unknown = _replace_nan(...)

```python
result, mask = _replace_nan(arr, 0)
```

**Verification:**
```python
assert (mask == False).all()
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([0, 1], dtype=dtype)
```

**Verification:**
```python
assert result is not arr
```

### Step 5: Assign unknown = _replace_nan(...)

```python
result, mask = _replace_nan(arr, 2)
```

**Verification:**
```python
assert_equal(result, arr)
```

### Step 6: Call assert_equal()

```python
assert_equal(result, arr)
```

**Verification:**
```python
assert_equal(mask_nan, np.array([False, False, True]))
```

### Step 7: Assign arr_nan = np.array(...)

```python
arr_nan = np.array([0, 1, np.nan], dtype=dtype)
```

**Verification:**
```python
assert result_nan is not arr_nan
```

### Step 8: Assign unknown = _replace_nan(...)

```python
result_nan, mask_nan = _replace_nan(arr_nan, 2)
```

**Verification:**
```python
assert_equal(result_nan, np.array([0, 1, 2]))
```

### Step 9: Call assert_equal()

```python
assert_equal(mask_nan, np.array([False, False, True]))
```

**Verification:**
```python
assert np.isnan(arr_nan[-1])
```

### Step 10: Call assert_equal()

```python
assert_equal(result_nan, np.array([0, 1, 2]))
```

**Verification:**
```python
assert np.isnan(arr_nan[-1])
```


## Complete Example

```python
# Workflow
' Test that _replace_nan returns the original array if there are no\n    NaNs, not a copy.\n    '
for dtype in [np.bool, np.int32, np.int64]:
    arr = np.array([0, 1], dtype=dtype)
    result, mask = _replace_nan(arr, 0)
    assert mask is None
    assert result is arr
for dtype in [np.float32, np.float64]:
    arr = np.array([0, 1], dtype=dtype)
    result, mask = _replace_nan(arr, 2)
    assert (mask == False).all()
    assert result is not arr
    assert_equal(result, arr)
    arr_nan = np.array([0, 1, np.nan], dtype=dtype)
    result_nan, mask_nan = _replace_nan(arr_nan, 2)
    assert_equal(mask_nan, np.array([False, False, True]))
    assert result_nan is not arr_nan
    assert_equal(result_nan, np.array([0, 1, 2]))
    assert np.isnan(arr_nan[-1])
```

## Next Steps


---

*Source: test_nanfunctions.py:1398 | Complexity: Advanced | Last updated: 2026-06-02*