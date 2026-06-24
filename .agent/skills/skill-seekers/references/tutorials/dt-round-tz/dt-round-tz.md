# How To: Dt Round Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt round tz

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
ser = Series(pd.to_datetime(['2012-01-01 13:00:00', '2012-01-01 12:01:00', '2012-01-01 08:00:00']), name='xxx')
```

### Step 2: Assign result = ser.dt.tz_localize.dt.tz_convert.dt.round(...)

```python
result = ser.dt.tz_localize('UTC').dt.tz_convert('US/Eastern').dt.round('D')
```

### Step 3: Assign exp_values = pd.to_datetime.tz_localize(...)

```python
exp_values = pd.to_datetime(['2012-01-01', '2012-01-01', '2012-01-01']).tz_localize('US/Eastern')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(exp_values, name='xxx')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(pd.to_datetime(['2012-01-01 13:00:00', '2012-01-01 12:01:00', '2012-01-01 08:00:00']), name='xxx')
result = ser.dt.tz_localize('UTC').dt.tz_convert('US/Eastern').dt.round('D')
exp_values = pd.to_datetime(['2012-01-01', '2012-01-01', '2012-01-01']).tz_localize('US/Eastern')
expected = Series(exp_values, name='xxx')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dt_accessor.py:326 | Complexity: Intermediate | Last updated: 2026-06-02*