# How To: Series Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series values

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
# Fixtures: using_copy_on_write, method
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

### Step 3: Assign arr = method(...)

```python
arr = method(ser)
```

**Verification:**
```python
assert ser.values[0] == 0
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 5: Assign unknown = 0

```python
ser.iloc[0] = 0
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 6: Assign unknown = 0

```python
arr[0] = 0
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 7: Assign unknown = 0

```python
arr[0] = 0
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, method

# Workflow
ser = Series([1, 2, 3], name='name')
ser_orig = ser.copy()
arr = method(ser)
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
```

## Next Steps


---

*Source: test_array.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*