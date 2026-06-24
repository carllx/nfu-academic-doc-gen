# How To: Median Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test median empty

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
# Fixtures: skipna, tz
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype('M8[ns]')
```

**Verification:**
```python
assert result is NaT
```

### Step 2: Assign arr = DatetimeArray._from_sequence(...)

```python
arr = DatetimeArray._from_sequence([], dtype=dtype)
```

### Step 3: Assign result = arr.median(...)

```python
result = arr.median(skipna=skipna)
```

**Verification:**
```python
assert result is NaT
```

### Step 4: Assign arr = arr.reshape(...)

```python
arr = arr.reshape(0, 3)
```

### Step 5: Assign result = arr.median(...)

```python
result = arr.median(axis=0, skipna=skipna)
```

### Step 6: Assign expected = type._from_sequence(...)

```python
expected = type(arr)._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign result = arr.median(...)

```python
result = arr.median(axis=1, skipna=skipna)
```

### Step 9: Assign expected = type._from_sequence(...)

```python
expected = type(arr)._from_sequence([], dtype=arr.dtype)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: skipna, tz

# Workflow
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype('M8[ns]')
arr = DatetimeArray._from_sequence([], dtype=dtype)
result = arr.median(skipna=skipna)
assert result is NaT
arr = arr.reshape(0, 3)
result = arr.median(axis=0, skipna=skipna)
expected = type(arr)._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
tm.assert_equal(result, expected)
result = arr.median(axis=1, skipna=skipna)
expected = type(arr)._from_sequence([], dtype=arr.dtype)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:69 | Complexity: Advanced | Last updated: 2026-06-02*