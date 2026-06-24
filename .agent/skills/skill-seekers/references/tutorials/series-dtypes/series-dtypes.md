# How To: Series Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, data, expected_data, coerce_int, dtypes, min_periods, step
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(data, dtype=get_dtype(dtypes, coerce_int=coerce_int))
```

### Step 2: Assign rolled = ser.rolling(...)

```python
rolled = ser.rolling(2, min_periods=min_periods, step=step)
```

### Step 3: Assign msg = 'No numeric types to aggregate'

```python
msg = 'No numeric types to aggregate'
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(rolled, method)()
```

### Step 5: Assign expected = value

```python
expected = Series(expected_data, dtype='float64')[::step]
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Call getattr()

```python
getattr(rolled, method)()
```


## Complete Example

```python
# Setup
# Fixtures: method, data, expected_data, coerce_int, dtypes, min_periods, step

# Workflow
ser = Series(data, dtype=get_dtype(dtypes, coerce_int=coerce_int))
rolled = ser.rolling(2, min_periods=min_periods, step=step)
if dtypes in ('m8[ns]', 'M8[ns]', 'datetime64[ns, UTC]') and method != 'count':
    msg = 'No numeric types to aggregate'
    with pytest.raises(DataError, match=msg):
        getattr(rolled, method)()
else:
    result = getattr(rolled, method)()
    expected = Series(expected_data, dtype='float64')[::step]
    tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*