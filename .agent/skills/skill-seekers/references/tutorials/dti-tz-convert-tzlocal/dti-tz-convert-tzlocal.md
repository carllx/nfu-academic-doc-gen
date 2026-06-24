# How To: Dti Tz Convert Tzlocal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz convert tzlocal

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

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(start='2001-01-01', end='2001-03-01', tz='UTC')
```

### Step 2: Assign dti2 = dti.tz_convert(...)

```python
dti2 = dti.tz_convert(dateutil.tz.tzlocal())
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
```

### Step 4: Assign dti = date_range(...)

```python
dti = date_range(start='2001-01-01', end='2001-03-01', tz=dateutil.tz.tzlocal())
```

### Step 5: Assign dti2 = dti.tz_convert(...)

```python
dti2 = dti.tz_convert(None)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
```


## Complete Example

```python
# Workflow
dti = date_range(start='2001-01-01', end='2001-03-01', tz='UTC')
dti2 = dti.tz_convert(dateutil.tz.tzlocal())
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
dti = date_range(start='2001-01-01', end='2001-03-01', tz=dateutil.tz.tzlocal())
dti2 = dti.tz_convert(None)
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
```

## Next Steps


---

*Source: test_tz_convert.py:247 | Complexity: Intermediate | Last updated: 2026-06-02*