# How To: Series To Numpy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series to numpy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='name')
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(ser, 'name'))
```

### Step 2: Assign ser_orig = ser.copy(...)

```python
ser_orig = ser.copy()
```

**Verification:**
```python
assert arr.flags.writeable is False
```

### Step 3: Assign arr = ser.to_numpy(...)

```python
arr = ser.to_numpy()
```

**Verification:**
```python
assert ser.values[0] == 0
```

### Step 4: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='name')
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 5: Assign arr = ser.to_numpy(...)

```python
arr = ser.to_numpy(copy=True)
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 6: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='name')
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(ser, 'name'))
```

### Step 7: Assign arr = ser.to_numpy(...)

```python
arr = ser.to_numpy(dtype='float64')
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(ser, 'name'))
```

### Step 9: Assign unknown = 0

```python
ser.iloc[0] = 0
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 10: Assign unknown = 0

```python
arr[0] = 0
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 11: Assign unknown = 0

```python
arr[0] = 0
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
ser = Series([1, 2, 3], name='name')
ser_orig = ser.copy()
arr = ser.to_numpy()
if using_copy_on_write:
    assert np.shares_memory(arr, get_array(ser, 'name'))
    assert arr.flags.writeable is False
    with pytest.raises(ValueError, match='read-only'):
        arr[0] = 0
    tm.assert_series_equal(ser, ser_orig)
    ser.iloc[0] = 0
    assert ser.values[0] == 0
else:
    assert arr.flags.writeable is True
    arr[0] = 0
    assert ser.iloc[0] == 0
ser = Series([1, 2, 3], name='name')
arr = ser.to_numpy(copy=True)
assert not np.shares_memory(arr, get_array(ser, 'name'))
assert arr.flags.writeable is True
ser = Series([1, 2, 3], name='name')
arr = ser.to_numpy(dtype='float64')
assert not np.shares_memory(arr, get_array(ser, 'name'))
assert arr.flags.writeable is True
```

## Next Steps


---

*Source: test_array.py:89 | Complexity: Advanced | Last updated: 2026-06-02*