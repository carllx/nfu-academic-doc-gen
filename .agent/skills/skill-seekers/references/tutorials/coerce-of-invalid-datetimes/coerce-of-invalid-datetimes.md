# How To: Coerce Of Invalid Datetimes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test coerce of invalid datetimes

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: errors
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(['01-01-2013', 'not_a_date', '1'], dtype=object)
```

### Step 2: Assign kwargs = value

```python
kwargs = {'values': arr, 'errors': errors}
```

### Step 3: Assign unknown = tslib.array_to_datetime(...)

```python
result, _ = tslib.array_to_datetime(**kwargs)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, arr)
```

### Step 5: Assign unknown = tslib.array_to_datetime(...)

```python
result, _ = tslib.array_to_datetime(arr, errors='coerce')
```

### Step 6: Assign expected = value

```python
expected = ['2013-01-01T00:00:00.000000000', iNaT, iNaT]
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array(expected, dtype='M8[ns]'))
```


## Complete Example

```python
# Setup
# Fixtures: errors

# Workflow
arr = np.array(['01-01-2013', 'not_a_date', '1'], dtype=object)
kwargs = {'values': arr, 'errors': errors}
if errors == 'ignore':
    result, _ = tslib.array_to_datetime(**kwargs)
    tm.assert_numpy_array_equal(result, arr)
else:
    result, _ = tslib.array_to_datetime(arr, errors='coerce')
    expected = ['2013-01-01T00:00:00.000000000', iNaT, iNaT]
    tm.assert_numpy_array_equal(result, np.array(expected, dtype='M8[ns]'))
```

## Next Steps


---

*Source: test_array_to_datetime.py:270 | Complexity: Intermediate | Last updated: 2026-06-02*