# How To: Non Nano Dt64 Addsub Np Nat Scalars Unitless

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non nano dt64 addsub np nat scalars unitless

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.conversion`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1233242342344, 232432434324, 332434242344], dtype='datetime64[ms]')
```

### Step 2: Assign result = value

```python
result = ser - np.datetime64('nat')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([NaT] * 3, dtype='timedelta64[ns]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = ser + np.timedelta64('nat')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([NaT] * 3, dtype='datetime64[ns]')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([1233242342344, 232432434324, 332434242344], dtype='datetime64[ms]')
result = ser - np.datetime64('nat')
expected = Series([NaT] * 3, dtype='timedelta64[ns]')
tm.assert_series_equal(result, expected)
result = ser + np.timedelta64('nat')
expected = Series([NaT] * 3, dtype='datetime64[ns]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime64.py:2447 | Complexity: Intermediate | Last updated: 2026-06-02*