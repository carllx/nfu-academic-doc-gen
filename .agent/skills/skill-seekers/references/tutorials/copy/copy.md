# How To: Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test copy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: deep, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(np.arange(10), dtype='float64')
```

**Verification:**
```python
assert np.may_share_memory(ser.values, ser2.values)
```

### Step 2: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy()
```

**Verification:**
```python
assert not np.may_share_memory(ser.values, ser2.values)
```

### Step 3: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy(deep=deep)
```

**Verification:**
```python
assert np.isnan(ser2[0])
```

### Step 4: Assign unknown = value

```python
ser2[::2] = np.nan
```

**Verification:**
```python
assert not np.isnan(ser[0])
```


## Complete Example

```python
# Setup
# Fixtures: deep, using_copy_on_write, warn_copy_on_write

# Workflow
ser = Series(np.arange(10), dtype='float64')
if deep == 'default':
    ser2 = ser.copy()
else:
    ser2 = ser.copy(deep=deep)
if using_copy_on_write:
    if deep is None or deep is False:
        assert np.may_share_memory(ser.values, ser2.values)
    else:
        assert not np.may_share_memory(ser.values, ser2.values)
with tm.assert_cow_warning(warn_copy_on_write and deep is False):
    ser2[::2] = np.nan
if deep is not False or using_copy_on_write:
    assert np.isnan(ser2[0])
    assert not np.isnan(ser[0])
else:
    assert np.isnan(ser2[0])
    assert np.isnan(ser[0])
```

## Next Steps


---

*Source: test_copy.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*