# How To: Dt Accessor Ambiguous Freq Conversions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt accessor ambiguous freq conversions

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


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('2015-01-01', '2016-01-01', freq='min'), name='xxx')
```

### Step 2: Assign ser = ser.dt.tz_localize.dt.tz_convert(...)

```python
ser = ser.dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
```

### Step 3: Assign exp_values = date_range.tz_convert(...)

```python
exp_values = date_range('2015-01-01', '2016-01-01', freq='min', tz='UTC').tz_convert('America/Chicago')
```

### Step 4: Assign exp_values = exp_values._with_freq(...)

```python
exp_values = exp_values._with_freq(None)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(exp_values, name='xxx')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```


## Complete Example

```python
# Workflow
ser = Series(date_range('2015-01-01', '2016-01-01', freq='min'), name='xxx')
ser = ser.dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
exp_values = date_range('2015-01-01', '2016-01-01', freq='min', tz='UTC').tz_convert('America/Chicago')
exp_values = exp_values._with_freq(None)
expected = Series(exp_values, name='xxx')
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_dt_accessor.py:271 | Complexity: Intermediate | Last updated: 2026-06-02*