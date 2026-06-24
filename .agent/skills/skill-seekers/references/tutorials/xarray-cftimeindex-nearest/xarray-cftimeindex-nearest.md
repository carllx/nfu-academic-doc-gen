# How To: Xarray Cftimeindex Nearest

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xarray cftimeindex nearest

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

### Step 1: Assign cftime = pytest.importorskip(...)

```python
cftime = pytest.importorskip('cftime')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign xarray = pytest.importorskip(...)

```python
xarray = pytest.importorskip('xarray')
```

### Step 3: Assign times = xarray.cftime_range(...)

```python
times = xarray.cftime_range('0001', periods=2)
```

### Step 4: Assign key = cftime.DatetimeGregorian(...)

```python
key = cftime.DatetimeGregorian(2000, 1, 1)
```

### Step 5: Assign result = times.get_indexer(...)

```python
result = times.get_indexer([key], method='nearest')
```

### Step 6: Assign expected = 1

```python
expected = 1
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
cftime = pytest.importorskip('cftime')
xarray = pytest.importorskip('xarray')
times = xarray.cftime_range('0001', periods=2)
key = cftime.DatetimeGregorian(2000, 1, 1)
result = times.get_indexer([key], method='nearest')
expected = 1
assert result == expected
```

## Next Steps


---

*Source: test_downstream.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*