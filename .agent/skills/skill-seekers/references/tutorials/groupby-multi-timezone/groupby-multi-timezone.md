# How To: Groupby Multi Timezone

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby multi timezone

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.groupby.ops`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'value': range(5), 'date': ['2000-01-28 16:47:00', '2000-01-29 16:48:00', '2000-01-30 16:49:00', '2000-01-31 16:50:00', '2000-01-01 16:50:00'], 'tz': ['America/Chicago', 'America/Chicago', 'America/Los_Angeles', 'America/Chicago', 'America/New_York']})
```

### Step 2: Assign result = df.groupby.date.apply(...)

```python
result = df.groupby('tz', group_keys=False).date.apply(lambda x: pd.to_datetime(x).dt.tz_localize(x.name))
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([Timestamp('2000-01-28 16:47:00-0600', tz='America/Chicago'), Timestamp('2000-01-29 16:48:00-0600', tz='America/Chicago'), Timestamp('2000-01-30 16:49:00-0800', tz='America/Los_Angeles'), Timestamp('2000-01-31 16:50:00-0600', tz='America/Chicago'), Timestamp('2000-01-01 16:50:00-0500', tz='America/New_York')], name='date', dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign tz = 'America/Chicago'

```python
tz = 'America/Chicago'
```

### Step 6: Assign res_values = df.groupby.date.get_group(...)

```python
res_values = df.groupby('tz').date.get_group(tz)
```

### Step 7: Assign result = pd.to_datetime.dt.tz_localize(...)

```python
result = pd.to_datetime(res_values).dt.tz_localize(tz)
```

### Step 8: Assign exp_values = Series(...)

```python
exp_values = Series(['2000-01-28 16:47:00', '2000-01-29 16:48:00', '2000-01-31 16:50:00'], index=[0, 1, 3], name='date')
```

### Step 9: Assign expected = pd.to_datetime.dt.tz_localize(...)

```python
expected = pd.to_datetime(exp_values).dt.tz_localize(tz)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'value': range(5), 'date': ['2000-01-28 16:47:00', '2000-01-29 16:48:00', '2000-01-30 16:49:00', '2000-01-31 16:50:00', '2000-01-01 16:50:00'], 'tz': ['America/Chicago', 'America/Chicago', 'America/Los_Angeles', 'America/Chicago', 'America/New_York']})
result = df.groupby('tz', group_keys=False).date.apply(lambda x: pd.to_datetime(x).dt.tz_localize(x.name))
expected = Series([Timestamp('2000-01-28 16:47:00-0600', tz='America/Chicago'), Timestamp('2000-01-29 16:48:00-0600', tz='America/Chicago'), Timestamp('2000-01-30 16:49:00-0800', tz='America/Los_Angeles'), Timestamp('2000-01-31 16:50:00-0600', tz='America/Chicago'), Timestamp('2000-01-01 16:50:00-0500', tz='America/New_York')], name='date', dtype=object)
tm.assert_series_equal(result, expected)
tz = 'America/Chicago'
res_values = df.groupby('tz').date.get_group(tz)
result = pd.to_datetime(res_values).dt.tz_localize(tz)
exp_values = Series(['2000-01-28 16:47:00', '2000-01-29 16:48:00', '2000-01-31 16:50:00'], index=[0, 1, 3], name='date')
expected = pd.to_datetime(exp_values).dt.tz_localize(tz)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_timegrouper.py:618 | Complexity: Advanced | Last updated: 2026-06-02*