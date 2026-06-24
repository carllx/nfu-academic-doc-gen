# How To: Xarray Coerce Unit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xarray coerce unit

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

### Step 1: Assign xr = pytest.importorskip(...)

```python
xr = pytest.importorskip('xarray')
```

### Step 2: Assign arr = xr.DataArray(...)

```python
arr = xr.DataArray([1, 2, 3])
```

### Step 3: Assign result = pd.to_datetime(...)

```python
result = pd.to_datetime(arr, unit='ns')
```

### Step 4: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['1970-01-01 00:00:00.000000001', '1970-01-01 00:00:00.000000002', '1970-01-01 00:00:00.000000003'], dtype='datetime64[ns]', freq=None)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
xr = pytest.importorskip('xarray')
arr = xr.DataArray([1, 2, 3])
result = pd.to_datetime(arr, unit='ns')
expected = DatetimeIndex(['1970-01-01 00:00:00.000000001', '1970-01-01 00:00:00.000000002', '1970-01-01 00:00:00.000000003'], dtype='datetime64[ns]', freq=None)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_downstream.py:355 | Complexity: Intermediate | Last updated: 2026-06-02*