# How To: Infer Homogeoneous Dt64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer homogeoneous dt64

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz.tz`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.np_datetime`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2023, 10, 27, 18, 3, 5, 678000)
```

**Verification:**
```python
assert tz is None
```

### Step 2: Assign dt64 = np.datetime64(...)

```python
dt64 = np.datetime64(dt, 'ms')
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([None, dt64, dt64, dt64], dtype=object)
```

### Step 4: Assign unknown = tslib.array_to_datetime(...)

```python
result, tz = tslib.array_to_datetime(arr, creso=creso_infer)
```

**Verification:**
```python
assert tz is None
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([np.datetime64('NaT'), dt64, dt64, dt64], dtype='M8[ms]')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt = datetime(2023, 10, 27, 18, 3, 5, 678000)
dt64 = np.datetime64(dt, 'ms')
arr = np.array([None, dt64, dt64, dt64], dtype=object)
result, tz = tslib.array_to_datetime(arr, creso=creso_infer)
assert tz is None
expected = np.array([np.datetime64('NaT'), dt64, dt64, dt64], dtype='M8[ms]')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_to_datetime.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*