# How To: Copy Tzaware

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test copy tzaware

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: deep, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign expected = Series(...)

```python
expected = Series([Timestamp('2012/01/01', tz='UTC')])
```

**Verification:**
```python
assert np.may_share_memory(ser.values, ser2.values)
```

### Step 2: Assign expected2 = Series(...)

```python
expected2 = Series([Timestamp('1999/01/01', tz='UTC')])
```

**Verification:**
```python
assert not np.may_share_memory(ser.values, ser2.values)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([Timestamp('2012/01/01', tz='UTC')])
```

### Step 4: Assign unknown = Timestamp(...)

```python
ser2[0] = Timestamp('1999/01/01', tz='UTC')
```

### Step 5: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy()
```

### Step 6: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy(deep=deep)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser2, expected2)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser2, expected2)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected2)
```

**Verification:**
```python
assert np.may_share_memory(ser.values, ser2.values)
```


## Complete Example

```python
# Setup
# Fixtures: deep, using_copy_on_write

# Workflow
expected = Series([Timestamp('2012/01/01', tz='UTC')])
expected2 = Series([Timestamp('1999/01/01', tz='UTC')])
ser = Series([Timestamp('2012/01/01', tz='UTC')])
if deep == 'default':
    ser2 = ser.copy()
else:
    ser2 = ser.copy(deep=deep)
if using_copy_on_write:
    if deep is None or deep is False:
        assert np.may_share_memory(ser.values, ser2.values)
    else:
        assert not np.may_share_memory(ser.values, ser2.values)
ser2[0] = Timestamp('1999/01/01', tz='UTC')
if deep is not False or using_copy_on_write:
    tm.assert_series_equal(ser2, expected2)
    tm.assert_series_equal(ser, expected)
else:
    tm.assert_series_equal(ser2, expected2)
    tm.assert_series_equal(ser, expected2)
```

## Next Steps


---

*Source: test_copy.py:44 | Complexity: Advanced | Last updated: 2026-06-02*