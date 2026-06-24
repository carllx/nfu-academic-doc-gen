# How To: Coerce Outside Ns Bounds One Valid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test coerce outside ns bounds one valid

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

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(['1/1/1000', '1/1/2000'], dtype=object)
```

### Step 2: Assign unknown = tslib.array_to_datetime(...)

```python
result, _ = tslib.array_to_datetime(arr, errors='coerce')
```

### Step 3: Assign expected = value

```python
expected = [iNaT, '2000-01-01T00:00:00.000000000']
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array(expected, dtype='M8[ns]')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.array(['1/1/1000', '1/1/2000'], dtype=object)
result, _ = tslib.array_to_datetime(arr, errors='coerce')
expected = [iNaT, '2000-01-01T00:00:00.000000000']
expected = np.array(expected, dtype='M8[ns]')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_to_datetime.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*