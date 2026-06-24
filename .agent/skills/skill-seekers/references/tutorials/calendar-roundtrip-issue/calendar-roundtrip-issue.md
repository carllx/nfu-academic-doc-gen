# How To: Calendar Roundtrip Issue

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test calendar roundtrip issue

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `hashlib`
- `tempfile`
- `time`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign weekmask_egypt = 'Sun Mon Tue Wed Thu'

```python
weekmask_egypt = 'Sun Mon Tue Wed Thu'
```

### Step 2: Assign holidays = value

```python
holidays = ['2012-05-01', dt.datetime(2013, 5, 1), np.datetime64('2014-05-01')]
```

### Step 3: Assign bday_egypt = pd.offsets.CustomBusinessDay(...)

```python
bday_egypt = pd.offsets.CustomBusinessDay(holidays=holidays, weekmask=weekmask_egypt)
```

### Step 4: Assign mydt = dt.datetime(...)

```python
mydt = dt.datetime(2013, 4, 30)
```

### Step 5: Assign dts = date_range(...)

```python
dts = date_range(mydt, periods=5, freq=bday_egypt)
```

### Step 6: Assign s = Series.map(...)

```python
s = Series(dts.weekday, dts).map(Series('Mon Tue Wed Thu Fri Sat Sun'.split()))
```

### Step 7: Call store.put()

```python
store.put('fixed', s)
```

### Step 8: Assign result = store.select(...)

```python
result = store.select('fixed')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s)
```

### Step 10: Call store.append()

```python
store.append('table', s)
```

### Step 11: Assign result = store.select(...)

```python
result = store.select('table')
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
weekmask_egypt = 'Sun Mon Tue Wed Thu'
holidays = ['2012-05-01', dt.datetime(2013, 5, 1), np.datetime64('2014-05-01')]
bday_egypt = pd.offsets.CustomBusinessDay(holidays=holidays, weekmask=weekmask_egypt)
mydt = dt.datetime(2013, 4, 30)
dts = date_range(mydt, periods=5, freq=bday_egypt)
s = Series(dts.weekday, dts).map(Series('Mon Tue Wed Thu Fri Sat Sun'.split()))
with ensure_clean_store(setup_path) as store:
    store.put('fixed', s)
    result = store.select('fixed')
    tm.assert_series_equal(result, s)
    store.append('table', s)
    result = store.select('table')
    tm.assert_series_equal(result, s)
```

## Next Steps


---

*Source: test_store.py:525 | Complexity: Advanced | Last updated: 2026-06-02*