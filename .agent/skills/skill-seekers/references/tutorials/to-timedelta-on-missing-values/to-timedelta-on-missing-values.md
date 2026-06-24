# How To: To Timedelta On Missing Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timedelta on missing values

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign timedelta_NaT = np.timedelta64(...)

```python
timedelta_NaT = np.timedelta64('NaT')
```

### Step 2: Assign actual = to_timedelta(...)

```python
actual = to_timedelta(Series(['00:00:01', np.nan]))
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([np.timedelta64(1000000000, 'ns'), timedelta_NaT], dtype=f'{tm.ENDIAN}m8[ns]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(actual, expected)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(['00:00:01', pd.NaT], dtype='m8[ns]')
```

### Step 6: Assign actual = to_timedelta(...)

```python
actual = to_timedelta(ser)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(actual, expected)
```


## Complete Example

```python
# Workflow
timedelta_NaT = np.timedelta64('NaT')
actual = to_timedelta(Series(['00:00:01', np.nan]))
expected = Series([np.timedelta64(1000000000, 'ns'), timedelta_NaT], dtype=f'{tm.ENDIAN}m8[ns]')
tm.assert_series_equal(actual, expected)
ser = Series(['00:00:01', pd.NaT], dtype='m8[ns]')
actual = to_timedelta(ser)
tm.assert_series_equal(actual, expected)
```

## Next Steps


---

*Source: test_to_timedelta.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*