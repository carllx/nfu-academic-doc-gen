# How To: 32878 Complex Itemsize

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 32878 complex itemsize

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
arr = np.arange(5).astype('c8')
```

**Verification:**
```python
assert ser[0] == val
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(arr)
```

### Step 3: Assign val = value

```python
val = np.finfo(np.float64).max
```

### Step 4: Assign val = val.astype(...)

```python
val = val.astype('c16')
```

**Verification:**
```python
assert ser[0] == val
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([val, 1, 2, 3, 4], dtype='c16')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 7: Assign unknown = val

```python
ser[0] = val
```


## Complete Example

```python
# Workflow
arr = np.arange(5).astype('c8')
ser = Series(arr)
val = np.finfo(np.float64).max
val = val.astype('c16')
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    ser[0] = val
assert ser[0] == val
expected = Series([val, 1, 2, 3, 4], dtype='c16')
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_setitem.py:1674 | Complexity: Intermediate | Last updated: 2026-06-02*