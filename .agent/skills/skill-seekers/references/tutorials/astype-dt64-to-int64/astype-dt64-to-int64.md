# How To: Astype Dt64 To Int64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype dt64 to int64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array(['NaT', '2016-01-02', '2016-01-03'], dtype='M8[ns]')
```

### Step 2: Assign arr = SparseArray(...)

```python
arr = SparseArray(values)
```

### Step 3: Assign result = arr.astype(...)

```python
result = arr.astype('int64')
```

### Step 4: Assign expected = values.astype(...)

```python
expected = values.astype('int64')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign dtype_int64 = SparseDtype(...)

```python
dtype_int64 = SparseDtype('int64', np.iinfo(np.int64).min)
```

### Step 7: Assign result2 = arr.astype(...)

```python
result2 = arr.astype(dtype_int64)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result2.to_numpy(), expected)
```

### Step 9: Assign dtype = SparseDtype(...)

```python
dtype = SparseDtype('datetime64[ns]', values[1])
```

### Step 10: Assign arr3 = SparseArray(...)

```python
arr3 = SparseArray(values, dtype=dtype)
```

### Step 11: Assign result3 = arr3.astype(...)

```python
result3 = arr3.astype('int64')
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result3, expected)
```


## Complete Example

```python
# Workflow
values = np.array(['NaT', '2016-01-02', '2016-01-03'], dtype='M8[ns]')
arr = SparseArray(values)
result = arr.astype('int64')
expected = values.astype('int64')
tm.assert_numpy_array_equal(result, expected)
dtype_int64 = SparseDtype('int64', np.iinfo(np.int64).min)
result2 = arr.astype(dtype_int64)
tm.assert_numpy_array_equal(result2.to_numpy(), expected)
dtype = SparseDtype('datetime64[ns]', values[1])
arr3 = SparseArray(values, dtype=dtype)
result3 = arr3.astype('int64')
tm.assert_numpy_array_equal(result3, expected)
```

## Next Steps


---

*Source: test_astype.py:114 | Complexity: Advanced | Last updated: 2026-06-02*