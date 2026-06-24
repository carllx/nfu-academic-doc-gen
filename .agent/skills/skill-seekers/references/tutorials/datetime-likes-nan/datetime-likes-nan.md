# How To: Datetime Likes Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetime likes nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = klass.__name__ + '[ns]'
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([1, 2, np.nan])
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([1, 2, klass('NaT')], dtype)
```

### Step 4: Assign res = maybe_downcast_to_dtype(...)

```python
res = maybe_downcast_to_dtype(arr, dtype)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
dtype = klass.__name__ + '[ns]'
arr = np.array([1, 2, np.nan])
exp = np.array([1, 2, klass('NaT')], dtype)
res = maybe_downcast_to_dtype(arr, dtype)
tm.assert_numpy_array_equal(res, exp)
```

## Next Steps


---

*Source: test_downcast.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*