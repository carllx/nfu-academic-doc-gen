# How To: Nullable Integer To Datetime

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nullable integer to datetime

## Prerequisites

**Required Modules:**
- `calendar`
- `collections`
- `datetime`
- `decimal`
- `locale`
- `dateutil.parser`
- `dateutil.tz.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools`
- `pandas.core.tools.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, None, 2 ** 61, None])
```

### Step 2: Assign ser = ser.astype(...)

```python
ser = ser.astype('Int64')
```

### Step 3: Assign ser_copy = ser.copy(...)

```python
ser_copy = ser.copy()
```

### Step 4: Assign res = to_datetime(...)

```python
res = to_datetime(ser, unit='ns')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.datetime64('1970-01-01 00:00:00.000000001'), np.datetime64('1970-01-01 00:00:00.000000002'), np.datetime64('NaT'), np.datetime64('2043-01-25 23:56:49.213693952'), np.datetime64('NaT')])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_copy)
```


## Complete Example

```python
# Workflow
ser = Series([1, 2, None, 2 ** 61, None])
ser = ser.astype('Int64')
ser_copy = ser.copy()
res = to_datetime(ser, unit='ns')
expected = Series([np.datetime64('1970-01-01 00:00:00.000000001'), np.datetime64('1970-01-01 00:00:00.000000002'), np.datetime64('NaT'), np.datetime64('2043-01-25 23:56:49.213693952'), np.datetime64('NaT')])
tm.assert_series_equal(res, expected)
tm.assert_series_equal(ser, ser_copy)
```

## Next Steps


---

*Source: test_to_datetime.py:3572 | Complexity: Intermediate | Last updated: 2026-06-02*