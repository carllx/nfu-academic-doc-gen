# How To: Convert Numeric Uint64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert numeric uint64

## Prerequisites

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([2 ** 63], dtype=object)
```

### Step 2: Assign exp = np.array(...)

```python
exp = np.array([2 ** 63], dtype=np.uint64)
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([str(2 ** 63)], dtype=object)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([2 ** 63], dtype=np.uint64)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
```

### Step 7: Assign arr = np.array(...)

```python
arr = np.array([np.uint64(2 ** 63)], dtype=object)
```

### Step 8: Assign exp = np.array(...)

```python
exp = np.array([2 ** 63], dtype=np.uint64)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
```


## Complete Example

```python
# Workflow
arr = np.array([2 ** 63], dtype=object)
exp = np.array([2 ** 63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
arr = np.array([str(2 ** 63)], dtype=object)
exp = np.array([2 ** 63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
arr = np.array([np.uint64(2 ** 63)], dtype=object)
exp = np.array([2 ** 63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
```

## Next Steps


---

*Source: test_inference.py:625 | Complexity: Advanced | Last updated: 2026-06-02*