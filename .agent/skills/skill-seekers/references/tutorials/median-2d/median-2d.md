# How To: Median 2D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test median 2d

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
# Fixtures: arr1d
```

## Step-by-Step Guide

### Step 1: Assign arr = arr1d.reshape(...)

```python
arr = arr1d.reshape(1, -1)
```

**Verification:**
```python
assert arr.median() == arr1d.median()
```

### Step 2: Assign result = arr.median(...)

```python
result = arr.median(axis=0)
```

**Verification:**
```python
assert arr.median(skipna=False) is NaT
```

### Step 3: Assign expected = arr1d

```python
expected = arr1d
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 5: Assign result = arr.median(...)

```python
result = arr.median(axis=0, skipna=False)
```

### Step 6: Assign expected = arr1d

```python
expected = arr1d
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign result = arr.median(...)

```python
result = arr.median(axis=1)
```

### Step 9: Assign expected = type._from_sequence(...)

```python
expected = type(arr)._from_sequence([arr1d.median()], dtype=arr.dtype)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 11: Assign result = arr.median(...)

```python
result = arr.median(axis=1, skipna=False)
```

### Step 12: Assign expected = type._from_sequence(...)

```python
expected = type(arr)._from_sequence([NaT], dtype=arr.dtype)
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: arr1d

# Workflow
arr = arr1d.reshape(1, -1)
assert arr.median() == arr1d.median()
assert arr.median(skipna=False) is NaT
result = arr.median(axis=0)
expected = arr1d
tm.assert_equal(result, expected)
result = arr.median(axis=0, skipna=False)
expected = arr1d
tm.assert_equal(result, expected)
result = arr.median(axis=1)
expected = type(arr)._from_sequence([arr1d.median()], dtype=arr.dtype)
tm.assert_equal(result, expected)
result = arr.median(axis=1, skipna=False)
expected = type(arr)._from_sequence([NaT], dtype=arr.dtype)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:108 | Complexity: Advanced | Last updated: 2026-06-02*