# How To: Series From Block Manager

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series from block manager

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
# Fixtures: using_copy_on_write, idx, dtype, fastpath
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], dtype='int64')
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
assert not ser2._mgr._has_no_reference(0)
```

### Step 3: Assign msg = "The 'fastpath' keyword in pd.Series is deprecated"

```python
msg = "The 'fastpath' keyword in pd.Series is deprecated"
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), get_array(ser2))
```

### Step 4: Assign unknown = 100

```python
ser2.iloc[0] = 100
```

### Step 5: Assign ser2 = Series(...)

```python
ser2 = Series(ser._mgr, dtype=dtype, fastpath=fastpath, index=idx)
```

**Verification:**
```python
assert not ser2._mgr._has_no_reference(0)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([100, 2, 3])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, idx, dtype, fastpath

# Workflow
ser = Series([1, 2, 3], dtype='int64')
ser_orig = ser.copy()
msg = "The 'fastpath' keyword in pd.Series is deprecated"
with tm.assert_produces_warning(DeprecationWarning, match=msg):
    ser2 = Series(ser._mgr, dtype=dtype, fastpath=fastpath, index=idx)
assert np.shares_memory(get_array(ser), get_array(ser2))
if using_copy_on_write:
    assert not ser2._mgr._has_no_reference(0)
ser2.iloc[0] = 100
if using_copy_on_write:
    tm.assert_series_equal(ser, ser_orig)
else:
    expected = Series([100, 2, 3])
    tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_constructors.py:163 | Complexity: Advanced | Last updated: 2026-06-02*