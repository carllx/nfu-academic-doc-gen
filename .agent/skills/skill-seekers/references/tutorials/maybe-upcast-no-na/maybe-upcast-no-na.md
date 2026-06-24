# How To: Maybe Upcast No Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe upcast no na

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

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype=any_real_numpy_dtype)
```

### Step 2: Assign result = _maybe_upcast(...)

```python
result = _maybe_upcast(arr, use_dtype_backend=True)
```

### Step 3: Assign expected_mask = np.array(...)

```python
expected_mask = np.array([False, False, False])
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign expected = IntegerArray(...)

```python
expected = IntegerArray(arr, mask=expected_mask)
```

### Step 6: Assign expected = FloatingArray(...)

```python
expected = FloatingArray(arr, mask=expected_mask)
```


## Complete Example

```python
# Setup
# Fixtures: any_real_numpy_dtype

# Workflow
arr = np.array([1, 2, 3], dtype=any_real_numpy_dtype)
result = _maybe_upcast(arr, use_dtype_backend=True)
expected_mask = np.array([False, False, False])
if issubclass(np.dtype(any_real_numpy_dtype).type, np.integer):
    expected = IntegerArray(arr, mask=expected_mask)
else:
    expected = FloatingArray(arr, mask=expected_mask)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_upcast.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*