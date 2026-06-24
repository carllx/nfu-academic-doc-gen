# How To: Getitem Setitem Datetime Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem setitem datetime tz

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: tz_source
```

## Step-by-Step Guide

### Step 1: Assign N = 50

```python
N = 50
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range('1/1/1990', periods=N, freq='h', tz=tzget('US/Eastern'))
```

### Step 3: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(N), index=rng)
```

### Step 4: Assign result = ts.copy(...)

```python
result = ts.copy()
```

### Step 5: Assign unknown = 0

```python
result['1990-01-01 09:00:00+00:00'] = 0
```

### Step 6: Assign unknown = value

```python
result['1990-01-01 09:00:00+00:00'] = ts.iloc[4]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts)
```

### Step 8: Assign result = ts.copy(...)

```python
result = ts.copy()
```

### Step 9: Assign unknown = 0

```python
result['1990-01-01 03:00:00-06:00'] = 0
```

### Step 10: Assign unknown = value

```python
result['1990-01-01 03:00:00-06:00'] = ts.iloc[4]
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts)
```

### Step 12: Assign result = ts.copy(...)

```python
result = ts.copy()
```

### Step 13: Assign unknown = 0

```python
result[datetime(1990, 1, 1, 9, tzinfo=tzget('UTC'))] = 0
```

### Step 14: Assign unknown = value

```python
result[datetime(1990, 1, 1, 9, tzinfo=tzget('UTC'))] = ts.iloc[4]
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts)
```

### Step 16: Assign result = ts.copy(...)

```python
result = ts.copy()
```

### Step 17: Assign dt = Timestamp.tz_localize(...)

```python
dt = Timestamp(1990, 1, 1, 3).tz_localize(tzget('US/Central'))
```

### Step 18: Assign dt = dt.to_pydatetime(...)

```python
dt = dt.to_pydatetime()
```

### Step 19: Assign unknown = 0

```python
result[dt] = 0
```

### Step 20: Assign unknown = value

```python
result[dt] = ts.iloc[4]
```

### Step 21: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts)
```

### Step 22: Assign tzget = value

```python
tzget = pytz.timezone
```

### Step 23: Assign tzget = value

```python
tzget = lambda x: tzutc() if x == 'UTC' else gettz(x)
```


## Complete Example

```python
# Setup
# Fixtures: tz_source

# Workflow
if tz_source == 'pytz':
    tzget = pytz.timezone
else:
    tzget = lambda x: tzutc() if x == 'UTC' else gettz(x)
N = 50
rng = date_range('1/1/1990', periods=N, freq='h', tz=tzget('US/Eastern'))
ts = Series(np.random.default_rng(2).standard_normal(N), index=rng)
result = ts.copy()
result['1990-01-01 09:00:00+00:00'] = 0
result['1990-01-01 09:00:00+00:00'] = ts.iloc[4]
tm.assert_series_equal(result, ts)
result = ts.copy()
result['1990-01-01 03:00:00-06:00'] = 0
result['1990-01-01 03:00:00-06:00'] = ts.iloc[4]
tm.assert_series_equal(result, ts)
result = ts.copy()
result[datetime(1990, 1, 1, 9, tzinfo=tzget('UTC'))] = 0
result[datetime(1990, 1, 1, 9, tzinfo=tzget('UTC'))] = ts.iloc[4]
tm.assert_series_equal(result, ts)
result = ts.copy()
dt = Timestamp(1990, 1, 1, 3).tz_localize(tzget('US/Central'))
dt = dt.to_pydatetime()
result[dt] = 0
result[dt] = ts.iloc[4]
tm.assert_series_equal(result, ts)
```

## Next Steps


---

*Source: test_datetime.py:70 | Complexity: Advanced | Last updated: 2026-06-02*