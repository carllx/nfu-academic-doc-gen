# How To: Series From Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series from array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, idx, dtype, fastpath, arr
```

## Step-by-Step Guide

### Step 1: Assign msg = "The 'fastpath' keyword in pd.Series is deprecated"

```python
msg = "The 'fastpath' keyword in pd.Series is deprecated"
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser), data)
```

### Step 2: Assign ser_orig = ser.copy(...)

```python
ser_orig = ser.copy()
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), data)
```

### Step 3: Assign data = getattr(...)

```python
data = getattr(arr, '_data', arr)
```

### Step 4: Assign unknown = 100

```python
arr[0] = 100
```

### Step 5: Assign fastpath = False

```python
fastpath = False
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(arr, dtype=dtype, index=idx, fastpath=fastpath)
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser), data)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([100, 2, 3], dtype=dtype if dtype is not None else arr.dtype)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, idx, dtype, fastpath, arr

# Workflow
if idx is None or dtype is not None:
    fastpath = False
msg = "The 'fastpath' keyword in pd.Series is deprecated"
with tm.assert_produces_warning(DeprecationWarning, match=msg):
    ser = Series(arr, dtype=dtype, index=idx, fastpath=fastpath)
ser_orig = ser.copy()
data = getattr(arr, '_data', arr)
if using_copy_on_write:
    assert not np.shares_memory(get_array(ser), data)
else:
    assert np.shares_memory(get_array(ser), data)
arr[0] = 100
if using_copy_on_write:
    tm.assert_series_equal(ser, ser_orig)
else:
    expected = Series([100, 2, 3], dtype=dtype if dtype is not None else arr.dtype)
    tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_constructors.py:102 | Complexity: Advanced | Last updated: 2026-06-02*