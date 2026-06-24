# How To: Mean Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mean empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: arr1d, skipna
```

## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = arr1d[:0]
```

**Verification:**
```python
assert arr.mean(skipna=skipna) is NaT
```

### Step 2: Assign arr2d = arr.reshape(...)

```python
arr2d = arr.reshape(0, 3)
```

**Verification:**
```python
assert result is NaT
```

### Step 3: Assign result = arr2d.mean(...)

```python
result = arr2d.mean(axis=0, skipna=skipna)
```

### Step 4: Assign expected = DatetimeArray._from_sequence(...)

```python
expected = DatetimeArray._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
```

### Step 5: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected)
```

### Step 6: Assign result = arr2d.mean(...)

```python
result = arr2d.mean(axis=1, skipna=skipna)
```

### Step 7: Assign expected = arr

```python
expected = arr
```

### Step 8: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected)
```

### Step 9: Assign result = arr2d.mean(...)

```python
result = arr2d.mean(axis=None, skipna=skipna)
```

**Verification:**
```python
assert result is NaT
```


## Complete Example

```python
# Setup
# Fixtures: arr1d, skipna

# Workflow
arr = arr1d[:0]
assert arr.mean(skipna=skipna) is NaT
arr2d = arr.reshape(0, 3)
result = arr2d.mean(axis=0, skipna=skipna)
expected = DatetimeArray._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
tm.assert_datetime_array_equal(result, expected)
result = arr2d.mean(axis=1, skipna=skipna)
expected = arr
tm.assert_datetime_array_equal(result, expected)
result = arr2d.mean(axis=None, skipna=skipna)
assert result is NaT
```

## Next Steps


---

*Source: test_reductions.py:168 | Complexity: Advanced | Last updated: 2026-06-02*