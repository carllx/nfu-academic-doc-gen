# How To: Tz Convert Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz convert nat

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = [NaT]
```

### Step 2: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(dates)
```

### Step 3: Assign idx = idx.tz_localize(...)

```python
idx = idx.tz_localize('US/Pacific')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Pacific'))
```

### Step 5: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Eastern'))
```

### Step 7: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('UTC')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='UTC'))
```

### Step 9: Assign dates = value

```python
dates = ['2010-12-01 00:00', '2010-12-02 00:00', NaT]
```

### Step 10: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(dates)
```

### Step 11: Assign idx = idx.tz_localize(...)

```python
idx = idx.tz_localize('US/Pacific')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Pacific'))
```

### Step 13: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 14: Assign expected = value

```python
expected = ['2010-12-01 03:00', '2010-12-02 03:00', NaT]
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
```

### Step 16: Assign idx = value

```python
idx = idx + offsets.Hour(5)
```

### Step 17: Assign expected = value

```python
expected = ['2010-12-01 08:00', '2010-12-02 08:00', NaT]
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
```

### Step 19: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Pacific')
```

### Step 20: Assign expected = value

```python
expected = ['2010-12-01 05:00', '2010-12-02 05:00', NaT]
```

### Step 21: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Pacific'))
```

### Step 22: Assign idx = value

```python
idx = idx + np.timedelta64(3, 'h')
```

### Step 23: Assign expected = value

```python
expected = ['2010-12-01 08:00', '2010-12-02 08:00', NaT]
```

### Step 24: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Pacific'))
```

### Step 25: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 26: Assign expected = value

```python
expected = ['2010-12-01 11:00', '2010-12-02 11:00', NaT]
```

### Step 27: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
```


## Complete Example

```python
# Workflow
dates = [NaT]
idx = DatetimeIndex(dates)
idx = idx.tz_localize('US/Pacific')
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Pacific'))
idx = idx.tz_convert('US/Eastern')
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Eastern'))
idx = idx.tz_convert('UTC')
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='UTC'))
dates = ['2010-12-01 00:00', '2010-12-02 00:00', NaT]
idx = DatetimeIndex(dates)
idx = idx.tz_localize('US/Pacific')
tm.assert_index_equal(idx, DatetimeIndex(dates, tz='US/Pacific'))
idx = idx.tz_convert('US/Eastern')
expected = ['2010-12-01 03:00', '2010-12-02 03:00', NaT]
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
idx = idx + offsets.Hour(5)
expected = ['2010-12-01 08:00', '2010-12-02 08:00', NaT]
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
idx = idx.tz_convert('US/Pacific')
expected = ['2010-12-01 05:00', '2010-12-02 05:00', NaT]
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Pacific'))
idx = idx + np.timedelta64(3, 'h')
expected = ['2010-12-01 08:00', '2010-12-02 08:00', NaT]
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Pacific'))
idx = idx.tz_convert('US/Eastern')
expected = ['2010-12-01 11:00', '2010-12-02 11:00', NaT]
tm.assert_index_equal(idx, DatetimeIndex(expected, tz='US/Eastern'))
```

## Next Steps


---

*Source: test_tz_convert.py:23 | Complexity: Advanced | Last updated: 2026-06-02*