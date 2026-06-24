# How To: Coerce Outside Ns Bounds

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test coerce outside ns bounds

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
# Fixtures: invalid_date, errors
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([invalid_date], dtype='object')
```

### Step 2: Assign kwargs = value

```python
kwargs = {'values': arr, 'errors': errors}
```

### Step 3: Assign msg = '^Out of bounds nanosecond timestamp: .*, at position 0$'

```python
msg = '^Out of bounds nanosecond timestamp: .*, at position 0$'
```

### Step 4: Assign unknown = tslib.array_to_datetime(...)

```python
result, _ = tslib.array_to_datetime(**kwargs)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([iNaT], dtype='M8[ns]')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Call tslib.array_to_datetime()

```python
tslib.array_to_datetime(**kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: invalid_date, errors

# Workflow
arr = np.array([invalid_date], dtype='object')
kwargs = {'values': arr, 'errors': errors}
if errors == 'raise':
    msg = '^Out of bounds nanosecond timestamp: .*, at position 0$'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        tslib.array_to_datetime(**kwargs)
else:
    result, _ = tslib.array_to_datetime(**kwargs)
    expected = np.array([iNaT], dtype='M8[ns]')
    tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_to_datetime.py:243 | Complexity: Intermediate | Last updated: 2026-06-02*