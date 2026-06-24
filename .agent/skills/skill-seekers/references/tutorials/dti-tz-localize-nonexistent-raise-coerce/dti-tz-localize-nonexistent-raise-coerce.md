# How To: Dti Tz Localize Nonexistent Raise Coerce

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz localize nonexistent raise coerce

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign times = value

```python
times = ['2015-03-08 01:00', '2015-03-08 02:00', '2015-03-08 03:00']
```

### Step 2: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(times)
```

### Step 3: Assign tz = 'US/Eastern'

```python
tz = 'US/Eastern'
```

### Step 4: Assign result = index.tz_localize(...)

```python
result = index.tz_localize(tz=tz, nonexistent='NaT')
```

### Step 5: Assign test_times = value

```python
test_times = ['2015-03-08 01:00-05:00', 'NaT', '2015-03-08 03:00-04:00']
```

### Step 6: Assign dti = to_datetime(...)

```python
dti = to_datetime(test_times, utc=True)
```

### Step 7: Assign expected = dti.tz_convert(...)

```python
expected = dti.tz_convert('US/Eastern')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Call index.tz_localize()

```python
index.tz_localize(tz=tz)
```

### Step 10: Call index.tz_localize()

```python
index.tz_localize(tz=tz, nonexistent='raise')
```


## Complete Example

```python
# Workflow
times = ['2015-03-08 01:00', '2015-03-08 02:00', '2015-03-08 03:00']
index = DatetimeIndex(times)
tz = 'US/Eastern'
with pytest.raises(pytz.NonExistentTimeError, match='|'.join(times)):
    index.tz_localize(tz=tz)
with pytest.raises(pytz.NonExistentTimeError, match='|'.join(times)):
    index.tz_localize(tz=tz, nonexistent='raise')
result = index.tz_localize(tz=tz, nonexistent='NaT')
test_times = ['2015-03-08 01:00-05:00', 'NaT', '2015-03-08 03:00-04:00']
dti = to_datetime(test_times, utc=True)
expected = dti.tz_convert('US/Eastern')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_tz_localize.py:74 | Complexity: Advanced | Last updated: 2026-06-02*