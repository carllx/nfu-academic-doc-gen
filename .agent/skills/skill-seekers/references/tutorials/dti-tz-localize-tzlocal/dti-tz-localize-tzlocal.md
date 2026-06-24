# How To: Dti Tz Localize Tzlocal

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz localize tzlocal

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

### Step 1: Assign offset = dateutil.tz.tzlocal.utcoffset(...)

```python
offset = dateutil.tz.tzlocal().utcoffset(datetime(2011, 1, 1))
```

### Step 2: Assign offset = int(...)

```python
offset = int(offset.total_seconds() * 1000000000)
```

### Step 3: Assign dti = date_range(...)

```python
dti = date_range(start='2001-01-01', end='2001-03-01')
```

### Step 4: Assign dti2 = dti.tz_localize(...)

```python
dti2 = dti.tz_localize(dateutil.tz.tzlocal())
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti2.asi8 + offset, dti.asi8)
```

### Step 6: Assign dti = date_range(...)

```python
dti = date_range(start='2001-01-01', end='2001-03-01', tz=dateutil.tz.tzlocal())
```

### Step 7: Assign dti2 = dti.tz_localize(...)

```python
dti2 = dti.tz_localize(None)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti2.asi8 - offset, dti.asi8)
```


## Complete Example

```python
# Workflow
offset = dateutil.tz.tzlocal().utcoffset(datetime(2011, 1, 1))
offset = int(offset.total_seconds() * 1000000000)
dti = date_range(start='2001-01-01', end='2001-03-01')
dti2 = dti.tz_localize(dateutil.tz.tzlocal())
tm.assert_numpy_array_equal(dti2.asi8 + offset, dti.asi8)
dti = date_range(start='2001-01-01', end='2001-03-01', tz=dateutil.tz.tzlocal())
dti2 = dti.tz_localize(None)
tm.assert_numpy_array_equal(dti2.asi8 - offset, dti.asi8)
```

## Next Steps


---

*Source: test_tz_localize.py:235 | Complexity: Advanced | Last updated: 2026-06-02*