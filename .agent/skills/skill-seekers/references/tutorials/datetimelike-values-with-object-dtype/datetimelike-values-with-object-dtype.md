# How To: Datetimelike Values With Object Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetimelike values with object dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`

**Setup Required:**
```python
# Fixtures: kind, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign arr = np.arange.view.reshape(...)

```python
arr = np.arange(6, dtype='i8').view(dtype).reshape(3, 2)
```

**Verification:**
```python
assert obj._mgr.arrays[0].dtype == object
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(arr, dtype=object)
```

**Verification:**
```python
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
```

### Step 3: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(frame_or_series(arr), dtype=object)
```

**Verification:**
```python
assert obj._mgr.arrays[0].dtype == object
```

### Step 4: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(frame_or_series(arr), dtype=NumpyEADtype(object))
```

**Verification:**
```python
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
```

### Step 5: Assign dtype = 'M8[ns]'

```python
dtype = 'M8[ns]'
```

**Verification:**
```python
assert obj._mgr.arrays[0].dtype == object
```

### Step 6: Assign scalar_type = Timestamp

```python
scalar_type = Timestamp
```

**Verification:**
```python
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
```

### Step 7: Assign dtype = 'm8[ns]'

```python
dtype = 'm8[ns]'
```

**Verification:**
```python
assert obj._mgr.arrays[0].dtype == object
```

### Step 8: Assign scalar_type = Timedelta

```python
scalar_type = Timedelta
```

**Verification:**
```python
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
```

### Step 9: Assign arr = value

```python
arr = arr[:, 0]
```

### Step 10: Assign sers = value

```python
sers = [Series(x) for x in arr]
```

### Step 11: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(sers, dtype=object)
```

**Verification:**
```python
assert obj._mgr.arrays[0].dtype == object
```


## Complete Example

```python
# Setup
# Fixtures: kind, frame_or_series

# Workflow
if kind == 'M':
    dtype = 'M8[ns]'
    scalar_type = Timestamp
else:
    dtype = 'm8[ns]'
    scalar_type = Timedelta
arr = np.arange(6, dtype='i8').view(dtype).reshape(3, 2)
if frame_or_series is Series:
    arr = arr[:, 0]
obj = frame_or_series(arr, dtype=object)
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
obj = frame_or_series(frame_or_series(arr), dtype=object)
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
obj = frame_or_series(frame_or_series(arr), dtype=NumpyEADtype(object))
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
if frame_or_series is DataFrame:
    sers = [Series(x) for x in arr]
    obj = frame_or_series(sers, dtype=object)
    assert obj._mgr.arrays[0].dtype == object
    assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)
```

## Next Steps


---

*Source: test_constructors.py:169 | Complexity: Advanced | Last updated: 2026-06-02*