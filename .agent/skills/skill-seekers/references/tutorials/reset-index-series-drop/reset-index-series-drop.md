# How To: Reset Index Series Drop

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reset index series drop

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, index
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2], index=index)
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), get_array(ser2))
```

### Step 2: Assign ser_orig = ser.copy(...)

```python
ser_orig = ser.copy()
```

**Verification:**
```python
assert not ser._mgr._has_no_reference(0)
```

### Step 3: Assign ser2 = ser.reset_index(...)

```python
ser2 = ser.reset_index(drop=True)
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser), get_array(ser2))
```

### Step 4: Assign unknown = 100

```python
ser2.iloc[0] = 100
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), get_array(ser2))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, index

# Workflow
ser = Series([1, 2], index=index)
ser_orig = ser.copy()
ser2 = ser.reset_index(drop=True)
if using_copy_on_write:
    assert np.shares_memory(get_array(ser), get_array(ser2))
    assert not ser._mgr._has_no_reference(0)
else:
    assert not np.shares_memory(get_array(ser), get_array(ser2))
ser2.iloc[0] = 100
tm.assert_series_equal(ser, ser_orig)
```

## Next Steps


---

*Source: test_methods.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*