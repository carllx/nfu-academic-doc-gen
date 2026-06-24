# How To: Dti Tz Localize

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz localize

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: prefix
```

## Step-by-Step Guide

### Step 1: Assign tzstr = value

```python
tzstr = prefix + 'US/Eastern'
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range(start='1/1/2005', end='1/1/2005 0:00:30.256', freq='ms')
```

### Step 3: Assign dti2 = dti.tz_localize(...)

```python
dti2 = dti.tz_localize(tzstr)
```

### Step 4: Assign dti_utc = date_range(...)

```python
dti_utc = date_range(start='1/1/2005 05:00', end='1/1/2005 5:00:30.256', freq='ms', tz='utc')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti2.values, dti_utc.values)
```

### Step 6: Assign dti3 = dti2.tz_convert(...)

```python
dti3 = dti2.tz_convert(prefix + 'US/Pacific')
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti3.values, dti_utc.values)
```

### Step 8: Assign dti = date_range(...)

```python
dti = date_range(start='11/6/2011 1:59', end='11/6/2011 2:00', freq='ms')
```

### Step 9: Assign dti = date_range(...)

```python
dti = date_range(start='3/13/2011 1:59', end='3/13/2011 2:00', freq='ms')
```

### Step 10: Call dti.tz_localize()

```python
dti.tz_localize(tzstr)
```

### Step 11: Call dti.tz_localize()

```python
dti.tz_localize(tzstr)
```


## Complete Example

```python
# Setup
# Fixtures: prefix

# Workflow
tzstr = prefix + 'US/Eastern'
dti = date_range(start='1/1/2005', end='1/1/2005 0:00:30.256', freq='ms')
dti2 = dti.tz_localize(tzstr)
dti_utc = date_range(start='1/1/2005 05:00', end='1/1/2005 5:00:30.256', freq='ms', tz='utc')
tm.assert_numpy_array_equal(dti2.values, dti_utc.values)
dti3 = dti2.tz_convert(prefix + 'US/Pacific')
tm.assert_numpy_array_equal(dti3.values, dti_utc.values)
dti = date_range(start='11/6/2011 1:59', end='11/6/2011 2:00', freq='ms')
with pytest.raises(pytz.AmbiguousTimeError, match='Cannot infer dst time'):
    dti.tz_localize(tzstr)
dti = date_range(start='3/13/2011 1:59', end='3/13/2011 2:00', freq='ms')
with pytest.raises(pytz.NonExistentTimeError, match='2011-03-13 02:00:00'):
    dti.tz_localize(tzstr)
```

## Next Steps


---

*Source: test_tz_localize.py:162 | Complexity: Advanced | Last updated: 2026-06-02*