# How To: Hasnans Isnans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hasnans isnans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_flat
```

## Step-by-Step Guide

### Step 1: Assign index = index_flat

```python
index = index_flat
```

**Verification:**
```python
assert idx.hasnans is False
```

### Step 2: Assign idx = index.copy(...)

```python
idx = index.copy(deep=True)
```

**Verification:**
```python
assert idx.hasnans is True
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([False] * len(idx), dtype=bool)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._isnan, expected)
```

**Verification:**
```python
assert idx.hasnans is False
```

### Step 5: Assign idx = index.copy(...)

```python
idx = index.copy(deep=True)
```

### Step 6: Assign values = value

```python
values = idx._values
```

### Step 7: Assign unknown = value

```python
values[1] = np.nan
```

### Step 8: Assign idx = type(...)

```python
idx = type(index)(values)
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([False] * len(idx), dtype=bool)
```

### Step 10: Assign unknown = True

```python
expected[1] = True
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._isnan, expected)
```

**Verification:**
```python
assert idx.hasnans is True
```


## Complete Example

```python
# Setup
# Fixtures: index_flat

# Workflow
index = index_flat
idx = index.copy(deep=True)
expected = np.array([False] * len(idx), dtype=bool)
tm.assert_numpy_array_equal(idx._isnan, expected)
assert idx.hasnans is False
idx = index.copy(deep=True)
values = idx._values
if len(index) == 0:
    return
elif is_integer_dtype(index.dtype):
    return
elif index.dtype == bool:
    return
values[1] = np.nan
idx = type(index)(values)
expected = np.array([False] * len(idx), dtype=bool)
expected[1] = True
tm.assert_numpy_array_equal(idx._isnan, expected)
assert idx.hasnans is True
```

## Next Steps


---

*Source: test_common.py:418 | Complexity: Advanced | Last updated: 2026-06-02*