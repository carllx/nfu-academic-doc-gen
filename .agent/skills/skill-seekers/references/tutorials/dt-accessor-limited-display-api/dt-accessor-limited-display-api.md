# How To: Dt Accessor Limited Display Api

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt accessor limited display api

## Prerequisites

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

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
```

### Step 2: Assign results = get_dir(...)

```python
results = get_dir(ser)
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(date_range('2015-01-01', '2016-01-01', freq='min'), name='xxx')
```

### Step 5: Assign ser = ser.dt.tz_localize.dt.tz_convert(...)

```python
ser = ser.dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
```

### Step 6: Assign results = get_dir(...)

```python
results = get_dir(ser)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
```

### Step 8: Assign idx = period_range.astype(...)

```python
idx = period_range('20130101', periods=5, freq='D', name='xxx').astype(object)
```

### Step 9: Assign results = get_dir(...)

```python
results = get_dir(ser)
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(results, sorted(set(ok_for_period + ok_for_period_methods)))
```

### Step 11: Assign ser = Series(...)

```python
ser = Series(idx)
```


## Complete Example

```python
# Workflow
ser = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
results = get_dir(ser)
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
ser = Series(date_range('2015-01-01', '2016-01-01', freq='min'), name='xxx')
ser = ser.dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
results = get_dir(ser)
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
idx = period_range('20130101', periods=5, freq='D', name='xxx').astype(object)
with tm.assert_produces_warning(FutureWarning, match='Dtype inference'):
    ser = Series(idx)
results = get_dir(ser)
tm.assert_almost_equal(results, sorted(set(ok_for_period + ok_for_period_methods)))
```

## Next Steps


---

*Source: test_dt_accessor.py:250 | Complexity: Advanced | Last updated: 2026-06-02*