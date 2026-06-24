# How To: Groupby Groups Datetimeindex Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby groups datetimeindex tz

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

### Step 1: Assign dates = value

```python
dates = ['2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00', '2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'label': ['a', 'a', 'a', 'b', 'b', 'b'], 'datetime': dates, 'value1': np.arange(6, dtype='int64'), 'value2': [1, 2] * 3})
```

### Step 3: Assign unknown = unknown.apply(...)

```python
df['datetime'] = df['datetime'].apply(lambda d: Timestamp(d, tz='US/Pacific'))
```

### Step 4: Assign exp_idx1 = DatetimeIndex(...)

```python
exp_idx1 = DatetimeIndex(['2011-07-19 07:00:00', '2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00', '2011-07-19 09:00:00'], tz='US/Pacific', name='datetime')
```

### Step 5: Assign exp_idx2 = Index(...)

```python
exp_idx2 = Index(['a', 'b'] * 3, name='label')
```

### Step 6: Assign exp_idx = MultiIndex.from_arrays(...)

```python
exp_idx = MultiIndex.from_arrays([exp_idx1, exp_idx2])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value1': [0, 3, 1, 4, 2, 5], 'value2': [1, 2, 2, 1, 1, 2]}, index=exp_idx, columns=['value1', 'value2'])
```

### Step 8: Assign result = df.groupby.sum(...)

```python
result = df.groupby(['datetime', 'label']).sum()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign didx = DatetimeIndex(...)

```python
didx = DatetimeIndex(dates, tz='Asia/Tokyo')
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame({'value1': np.arange(6, dtype='int64'), 'value2': [1, 2, 3, 1, 2, 3]}, index=didx)
```

### Step 12: Assign exp_idx = DatetimeIndex(...)

```python
exp_idx = DatetimeIndex(['2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00'], tz='Asia/Tokyo')
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value1': [3, 5, 7], 'value2': [2, 4, 6]}, index=exp_idx, columns=['value1', 'value2'])
```

### Step 14: Assign result = df.groupby.sum(...)

```python
result = df.groupby(level=0).sum()
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dates = ['2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00', '2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00']
df = DataFrame({'label': ['a', 'a', 'a', 'b', 'b', 'b'], 'datetime': dates, 'value1': np.arange(6, dtype='int64'), 'value2': [1, 2] * 3})
df['datetime'] = df['datetime'].apply(lambda d: Timestamp(d, tz='US/Pacific'))
exp_idx1 = DatetimeIndex(['2011-07-19 07:00:00', '2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00', '2011-07-19 09:00:00'], tz='US/Pacific', name='datetime')
exp_idx2 = Index(['a', 'b'] * 3, name='label')
exp_idx = MultiIndex.from_arrays([exp_idx1, exp_idx2])
expected = DataFrame({'value1': [0, 3, 1, 4, 2, 5], 'value2': [1, 2, 2, 1, 1, 2]}, index=exp_idx, columns=['value1', 'value2'])
result = df.groupby(['datetime', 'label']).sum()
tm.assert_frame_equal(result, expected)
didx = DatetimeIndex(dates, tz='Asia/Tokyo')
df = DataFrame({'value1': np.arange(6, dtype='int64'), 'value2': [1, 2, 3, 1, 2, 3]}, index=didx)
exp_idx = DatetimeIndex(['2011-07-19 07:00:00', '2011-07-19 08:00:00', '2011-07-19 09:00:00'], tz='Asia/Tokyo')
expected = DataFrame({'value1': [3, 5, 7], 'value2': [2, 4, 6]}, index=exp_idx, columns=['value1', 'value2'])
result = df.groupby(level=0).sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timegrouper.py:546 | Complexity: Advanced | Last updated: 2026-06-02*