# How To: Astype Mixed Object To Dt64Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype mixed object to dt64tz

## Prerequisites

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-04 05:06:07', tz='US/Pacific')
```

### Step 2: Assign ts2 = ts.tz_convert(...)

```python
ts2 = ts.tz_convert('Asia/Tokyo')
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([ts, ts2], dtype=object)
```

### Step 4: Assign res = ser.astype(...)

```python
res = ser.astype('datetime64[ns, Europe/Brussels]')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([ts.tz_convert('Europe/Brussels'), ts2.tz_convert('Europe/Brussels')], dtype='datetime64[ns, Europe/Brussels]')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
ts = Timestamp('2016-01-04 05:06:07', tz='US/Pacific')
ts2 = ts.tz_convert('Asia/Tokyo')
ser = Series([ts, ts2], dtype=object)
res = ser.astype('datetime64[ns, Europe/Brussels]')
expected = Series([ts.tz_convert('Europe/Brussels'), ts2.tz_convert('Europe/Brussels')], dtype='datetime64[ns, Europe/Brussels]')
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_astype.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*