# How To: Construct Dask Float Array Int Dtype Match Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construct dask float array int dtype match ndarray

## Prerequisites

**Required Modules:**
- `array`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.util.version`
- `sklearn`
- `dask.array`
- `xarray`


## Step-by-Step Guide

### Step 1: Assign dd = pytest.importorskip(...)

```python
dd = pytest.importorskip('dask.dataframe')
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([1, 2.5, 3])
```

### Step 3: Assign darr = dd.from_array(...)

```python
darr = dd.from_array(arr)
```

### Step 4: Assign res = Series(...)

```python
res = Series(darr)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(arr)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Assign msg = 'Trying to coerce float values to integers'

```python
msg = 'Trying to coerce float values to integers'
```

### Step 8: Assign msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'

```python
msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
```

### Step 9: Assign unknown = value

```python
arr[2] = np.nan
```

### Step 10: Call Series()

```python
Series(darr, dtype='i8')
```

### Step 11: Call Series()

```python
Series(darr, dtype='i8')
```

### Step 12: Call Series()

```python
Series(arr, dtype='i8')
```


## Complete Example

```python
# Workflow
dd = pytest.importorskip('dask.dataframe')
arr = np.array([1, 2.5, 3])
darr = dd.from_array(arr)
res = Series(darr)
expected = Series(arr)
tm.assert_series_equal(res, expected)
msg = 'Trying to coerce float values to integers'
with pytest.raises(ValueError, match=msg):
    Series(darr, dtype='i8')
msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
arr[2] = np.nan
with pytest.raises(IntCastingNaNError, match=msg):
    Series(darr, dtype='i8')
with pytest.raises(IntCastingNaNError, match=msg):
    Series(arr, dtype='i8')
```

## Next Steps


---

*Source: test_downstream.py:69 | Complexity: Advanced | Last updated: 2026-06-02*