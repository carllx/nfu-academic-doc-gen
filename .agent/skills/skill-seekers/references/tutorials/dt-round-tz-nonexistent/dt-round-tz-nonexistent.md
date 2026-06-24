# How To: Dt Round Tz Nonexistent

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dt round tz nonexistent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`

**Setup Required:**
```python
# Fixtures: method, ts_str, freq
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([pd.Timestamp(ts_str, tz='America/Chicago')])
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(ser.dt, method)(freq, nonexistent='shift_forward')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([pd.Timestamp('2018-03-11 03:00:00', tz='America/Chicago')])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(ser.dt, method)(freq, nonexistent='NaT')
```

### Step 6: Assign expected = Series.dt.tz_localize(...)

```python
expected = Series([pd.NaT]).dt.tz_localize(result.dt.tz)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Call getattr()

```python
getattr(ser.dt, method)(freq, nonexistent='raise')
```


## Complete Example

```python
# Setup
# Fixtures: method, ts_str, freq

# Workflow
ser = Series([pd.Timestamp(ts_str, tz='America/Chicago')])
result = getattr(ser.dt, method)(freq, nonexistent='shift_forward')
expected = Series([pd.Timestamp('2018-03-11 03:00:00', tz='America/Chicago')])
tm.assert_series_equal(result, expected)
result = getattr(ser.dt, method)(freq, nonexistent='NaT')
expected = Series([pd.NaT]).dt.tz_localize(result.dt.tz)
tm.assert_series_equal(result, expected)
with pytest.raises(pytz.NonExistentTimeError, match='2018-03-11 02:00:00'):
    getattr(ser.dt, method)(freq, nonexistent='raise')
```

## Next Steps


---

*Source: test_dt_accessor.py:380 | Complexity: Advanced | Last updated: 2026-06-02*