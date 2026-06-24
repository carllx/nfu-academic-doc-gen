# How To: Array Of Dt64 Nat With Td64Dtype Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array of dt64 nat with td64dtype raises

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
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign nat = np.datetime64(...)

```python
nat = np.datetime64('NaT', 'ns')
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([nat], dtype=object)
```

### Step 3: Assign msg = "Invalid type for timedelta scalar: <class 'numpy.datetime64'>"

```python
msg = "Invalid type for timedelta scalar: <class 'numpy.datetime64'>"
```

### Step 4: Assign arr = arr.reshape(...)

```python
arr = arr.reshape(1, 1)
```

### Step 5: Call frame_or_series()

```python
frame_or_series(arr, dtype='m8[ns]')
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
nat = np.datetime64('NaT', 'ns')
arr = np.array([nat], dtype=object)
if frame_or_series is DataFrame:
    arr = arr.reshape(1, 1)
msg = "Invalid type for timedelta scalar: <class 'numpy.datetime64'>"
with pytest.raises(TypeError, match=msg):
    frame_or_series(arr, dtype='m8[ns]')
```

## Next Steps


---

*Source: test_constructors.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*