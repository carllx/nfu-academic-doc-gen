# How To: Infer Homogeoneous Datetimes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer homogeoneous datetimes

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

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([dt, dt, dt], dtype=object)
```

### Step 3: Assign unknown = tslib.array_to_datetime(...)

```python
result, tz = tslib.array_to_datetime(arr, creso=creso_infer)
```

**Verification:**
```python
assert tz is None
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([dt, dt, dt], dtype='M8[us]')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt = datetime(2023, 10, 27, 18, 3, 5, 678000)
arr = np.array([dt, dt, dt], dtype=object)
result, tz = tslib.array_to_datetime(arr, creso=creso_infer)
assert tz is None
expected = np.array([dt, dt, dt], dtype='M8[us]')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_to_datetime.py:35 | Complexity: Intermediate | Last updated: 2026-06-02*