# How To: From Obscure Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from obscure array

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: dtype, array_likes
```

## Step-by-Step Guide

### Step 1: Assign unknown = array_likes

```python
arr, data = array_likes
```

### Step 2: Assign cls = value

```python
cls = {'M8[ns]': DatetimeArray, 'm8[ns]': TimedeltaArray}[dtype]
```

### Step 3: Assign depr_msg = value

```python
depr_msg = f'{cls.__name__}.__init__ is deprecated'
```

### Step 4: Assign result = cls._from_sequence(...)

```python
result = cls._from_sequence(data, dtype=dtype)
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign idx_cls = value

```python
idx_cls = {'M8[ns]': DatetimeIndex, 'm8[ns]': TimedeltaIndex}[dtype]
```

### Step 7: Assign result = idx_cls(...)

```python
result = idx_cls(arr)
```

### Step 8: Assign expected = idx_cls(...)

```python
expected = idx_cls(data)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign expected = cls(...)

```python
expected = cls(arr)
```

### Step 11: Assign func = value

```python
func = {'M8[ns]': pd.to_datetime, 'm8[ns]': pd.to_timedelta}[dtype]
```

### Step 12: Assign result = value

```python
result = func(arr).array
```

### Step 13: Assign expected = value

```python
expected = func(data).array
```

### Step 14: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, array_likes

# Workflow
arr, data = array_likes
cls = {'M8[ns]': DatetimeArray, 'm8[ns]': TimedeltaArray}[dtype]
depr_msg = f'{cls.__name__}.__init__ is deprecated'
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    expected = cls(arr)
result = cls._from_sequence(data, dtype=dtype)
tm.assert_extension_array_equal(result, expected)
if not isinstance(data, memoryview):
    func = {'M8[ns]': pd.to_datetime, 'm8[ns]': pd.to_timedelta}[dtype]
    result = func(arr).array
    expected = func(data).array
    tm.assert_equal(result, expected)
idx_cls = {'M8[ns]': DatetimeIndex, 'm8[ns]': TimedeltaIndex}[dtype]
result = idx_cls(arr)
expected = idx_cls(data)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_downstream.py:306 | Complexity: Advanced | Last updated: 2026-06-02*