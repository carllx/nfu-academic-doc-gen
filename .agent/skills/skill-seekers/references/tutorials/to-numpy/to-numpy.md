# How To: To Numpy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: arr, expected, zero_copy, index_or_series_or_array
```

## Step-by-Step Guide

### Step 1: Assign box = index_or_series_or_array

```python
box = index_or_series_or_array
```

**Verification:**
```python
assert not np.may_share_memory(result_cp1, result_cp2)
```

### Step 2: Assign result = thing.to_numpy(...)

```python
result = thing.to_numpy()
```

**Verification:**
```python
assert np.may_share_memory(result_nocopy1, result_nocopy2)
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign result = np.asarray(...)

```python
result = np.asarray(thing)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result_cp1 = np.array(...)

```python
result_cp1 = np.array(thing, copy=True)
```

### Step 7: Assign result_cp2 = np.array(...)

```python
result_cp2 = np.array(thing, copy=True)
```

**Verification:**
```python
assert not np.may_share_memory(result_cp1, result_cp2)
```

### Step 8: Assign thing = box(...)

```python
thing = box(arr)
```

### Step 9: Assign msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"

```python
msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"
```

### Step 10: Assign result_nocopy1 = np.array(...)

```python
result_nocopy1 = np.array(thing, copy=False)
```

### Step 11: Assign result_nocopy2 = np.array(...)

```python
result_nocopy2 = np.array(thing, copy=False)
```

**Verification:**
```python
assert np.may_share_memory(result_nocopy1, result_nocopy2)
```

### Step 12: Call np.array()

```python
np.array(thing, copy=False)
```


## Complete Example

```python
# Setup
# Fixtures: arr, expected, zero_copy, index_or_series_or_array

# Workflow
box = index_or_series_or_array
with tm.assert_produces_warning(None):
    thing = box(arr)
result = thing.to_numpy()
tm.assert_numpy_array_equal(result, expected)
result = np.asarray(thing)
tm.assert_numpy_array_equal(result, expected)
result_cp1 = np.array(thing, copy=True)
result_cp2 = np.array(thing, copy=True)
assert not np.may_share_memory(result_cp1, result_cp2)
if not np_version_gt2:
    return
if not zero_copy:
    msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"
    with tm.assert_produces_warning(FutureWarning, match=msg):
        np.array(thing, copy=False)
else:
    result_nocopy1 = np.array(thing, copy=False)
    result_nocopy2 = np.array(thing, copy=False)
    assert np.may_share_memory(result_nocopy1, result_nocopy2)
```

## Next Steps


---

*Source: test_conversion.py:357 | Complexity: Advanced | Last updated: 2026-06-02*