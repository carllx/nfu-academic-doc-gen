# How To: Iloc Setitem Ea Inplace

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test iloc setitem ea inplace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: frame_or_series, box, has_ref, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign arr = array(...)

```python
arr = array([1, 2, 3, 4])
```

**Verification:**
```python
assert obj.values is not values
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(arr.to_numpy('i8'))
```

**Verification:**
```python
assert np.shares_memory(obj.values, values)
```

### Step 3: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(np.array([3, 4, 3, 4], dtype='i8'))
```

**Verification:**
```python
assert obj.values is values
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(obj, expected)
```

**Verification:**
```python
assert np.shares_memory(obj[0].values, values)
```

### Step 5: Assign view = value

```python
view = obj[:]
```

### Step 6: Assign values = value

```python
values = obj.values
```

### Step 7: Assign values = value

```python
values = obj._mgr.arrays[0]
```

### Step 8: Assign unknown = box(...)

```python
obj.iloc[:2] = box(arr[2:])
```

### Step 9: Assign unknown = box(...)

```python
obj.iloc[:2, 0] = box(arr[2:])
```

**Verification:**
```python
assert np.shares_memory(obj[0].values, values)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, box, has_ref, using_copy_on_write

# Workflow
arr = array([1, 2, 3, 4])
obj = frame_or_series(arr.to_numpy('i8'))
if has_ref:
    view = obj[:]
if frame_or_series is Series:
    values = obj.values
else:
    values = obj._mgr.arrays[0]
if frame_or_series is Series:
    obj.iloc[:2] = box(arr[2:])
else:
    obj.iloc[:2, 0] = box(arr[2:])
expected = frame_or_series(np.array([3, 4, 3, 4], dtype='i8'))
tm.assert_equal(obj, expected)
if not has_ref:
    if frame_or_series is Series:
        if using_copy_on_write:
            assert obj.values is not values
            assert np.shares_memory(obj.values, values)
        else:
            assert obj.values is values
    else:
        assert np.shares_memory(obj[0].values, values)
```

## Next Steps


---

*Source: test_iloc.py:110 | Complexity: Advanced | Last updated: 2026-06-02*