# How To: Non Nano Dt64 Addsub Np Nat Scalars Unsupported Unit

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non nano dt64 addsub np nat scalars unsupported unit

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
ser = Series([12332, 23243, 33243], dtype='datetime64[s]')
```

### Step 2: Assign result = value

```python
result = ser - np.datetime64('nat', 'D')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([NaT] * 3, dtype='timedelta64[s]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = ser + np.timedelta64('nat', 'D')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([NaT] * 3, dtype='datetime64[s]')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([12332, 23243, 33243], dtype='datetime64[s]')
result = ser - np.datetime64('nat', 'D')
expected = Series([NaT] * 3, dtype='timedelta64[s]')
tm.assert_series_equal(result, expected)
result = ser + np.timedelta64('nat', 'D')
expected = Series([NaT] * 3, dtype='datetime64[s]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime64.py:2460 | Complexity: Intermediate | Last updated: 2026-06-02*