# How To: 32878 Int Itemsize

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 32878 int itemsize

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `os`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.astype(...)

```python
arr = np.arange(5).astype('i4')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(arr)
```

### Step 3: Assign val = np.int64(...)

```python
val = np.int64(np.iinfo(np.int64).max)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([val, 1, 2, 3, 4], dtype=np.int64)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 6: Assign unknown = val

```python
ser[0] = val
```


## Complete Example

```python
# Workflow
arr = np.arange(5).astype('i4')
ser = Series(arr)
val = np.int64(np.iinfo(np.int64).max)
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    ser[0] = val
expected = Series([val, 1, 2, 3, 4], dtype=np.int64)
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_setitem.py:1663 | Complexity: Intermediate | Last updated: 2026-06-02*