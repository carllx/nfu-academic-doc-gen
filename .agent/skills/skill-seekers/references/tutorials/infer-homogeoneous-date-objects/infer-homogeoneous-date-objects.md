# How To: Infer Homogeoneous Date Objects

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer homogeoneous date objects

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

### Step 2: Assign dt2 = dt.date(...)

```python
dt2 = dt.date()
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([None, dt2, dt2, dt2], dtype=object)
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
expected = np.array([np.datetime64('NaT'), dt2, dt2, dt2], dtype='M8[s]')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt = datetime(2023, 10, 27, 18, 3, 5, 678000)
dt2 = dt.date()
arr = np.array([None, dt2, dt2, dt2], dtype=object)
result, tz = tslib.array_to_datetime(arr, creso=creso_infer)
assert tz is None
expected = np.array([np.datetime64('NaT'), dt2, dt2, dt2], dtype='M8[s]')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_to_datetime.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*