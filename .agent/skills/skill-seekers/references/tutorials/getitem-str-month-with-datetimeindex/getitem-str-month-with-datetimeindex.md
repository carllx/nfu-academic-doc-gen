# How To: Getitem Str Month With Datetimeindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem str month with datetimeindex

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='2013-05-31 00:00', end='2013-05-31 23:00', freq='h')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(range(len(idx)), index=idx)
```

### Step 3: Assign expected = value

```python
expected = ts['2013-05']
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, ts)
```

### Step 5: Assign idx = date_range(...)

```python
idx = date_range(start='2013-05-31 00:00', end='2013-05-31 23:59', freq='s')
```

### Step 6: Assign ts = Series(...)

```python
ts = Series(range(len(idx)), index=idx)
```

### Step 7: Assign expected = value

```python
expected = ts['2013-05']
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, ts)
```


## Complete Example

```python
# Workflow
idx = date_range(start='2013-05-31 00:00', end='2013-05-31 23:00', freq='h')
ts = Series(range(len(idx)), index=idx)
expected = ts['2013-05']
tm.assert_series_equal(expected, ts)
idx = date_range(start='2013-05-31 00:00', end='2013-05-31 23:59', freq='s')
ts = Series(range(len(idx)), index=idx)
expected = ts['2013-05']
tm.assert_series_equal(expected, ts)
```

## Next Steps


---

*Source: test_datetime.py:453 | Complexity: Advanced | Last updated: 2026-06-02*