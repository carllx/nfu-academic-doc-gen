# How To: Groupby With Origin

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby with origin

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign freq = '1399min'

```python
freq = '1399min'
```

### Step 2: Assign unknown = value

```python
start, end = ('1/1/2000 00:00:00', '1/31/2000 00:00')
```

### Step 3: Assign middle = '1/15/2000 00:00:00'

```python
middle = '1/15/2000 00:00:00'
```

### Step 4: Assign rng = date_range(...)

```python
rng = date_range(start, end, freq='1231min')
```

### Step 5: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 6: Assign ts2 = value

```python
ts2 = ts[middle:end]
```

### Step 7: Assign simple_grouper = pd.Grouper(...)

```python
simple_grouper = pd.Grouper(freq=freq)
```

### Step 8: Assign count_ts = ts.groupby.agg(...)

```python
count_ts = ts.groupby(simple_grouper).agg('count')
```

### Step 9: Assign count_ts = value

```python
count_ts = count_ts[middle:end]
```

### Step 10: Assign count_ts2 = ts2.groupby.agg(...)

```python
count_ts2 = ts2.groupby(simple_grouper).agg('count')
```

### Step 11: Assign origin = Timestamp(...)

```python
origin = Timestamp(0)
```

### Step 12: Assign adjusted_grouper = pd.Grouper(...)

```python
adjusted_grouper = pd.Grouper(freq=freq, origin=origin)
```

### Step 13: Assign adjusted_count_ts = ts.groupby.agg(...)

```python
adjusted_count_ts = ts.groupby(adjusted_grouper).agg('count')
```

### Step 14: Assign adjusted_count_ts = value

```python
adjusted_count_ts = adjusted_count_ts[middle:end]
```

### Step 15: Assign adjusted_count_ts2 = ts2.groupby.agg(...)

```python
adjusted_count_ts2 = ts2.groupby(adjusted_grouper).agg('count')
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(adjusted_count_ts, adjusted_count_ts2)
```

### Step 17: Assign origin_future = value

```python
origin_future = Timestamp(0) + pd.Timedelta('1399min') * 30000
```

### Step 18: Assign adjusted_grouper2 = pd.Grouper(...)

```python
adjusted_grouper2 = pd.Grouper(freq=freq, origin=origin_future)
```

### Step 19: Assign adjusted2_count_ts = ts.groupby.agg(...)

```python
adjusted2_count_ts = ts.groupby(adjusted_grouper2).agg('count')
```

### Step 20: Assign adjusted2_count_ts = value

```python
adjusted2_count_ts = adjusted2_count_ts[middle:end]
```

### Step 21: Assign adjusted2_count_ts2 = ts2.groupby.agg(...)

```python
adjusted2_count_ts2 = ts2.groupby(adjusted_grouper2).agg('count')
```

### Step 22: Call tm.assert_series_equal()

```python
tm.assert_series_equal(adjusted2_count_ts, adjusted2_count_ts2)
```

### Step 23: Call tm.assert_series_equal()

```python
tm.assert_series_equal(adjusted_count_ts, adjusted2_count_ts2)
```

### Step 24: Call tm.assert_index_equal()

```python
tm.assert_index_equal(count_ts.index, count_ts2.index)
```


## Complete Example

```python
# Workflow
freq = '1399min'
start, end = ('1/1/2000 00:00:00', '1/31/2000 00:00')
middle = '1/15/2000 00:00:00'
rng = date_range(start, end, freq='1231min')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
ts2 = ts[middle:end]
simple_grouper = pd.Grouper(freq=freq)
count_ts = ts.groupby(simple_grouper).agg('count')
count_ts = count_ts[middle:end]
count_ts2 = ts2.groupby(simple_grouper).agg('count')
with pytest.raises(AssertionError, match='Index are different'):
    tm.assert_index_equal(count_ts.index, count_ts2.index)
origin = Timestamp(0)
adjusted_grouper = pd.Grouper(freq=freq, origin=origin)
adjusted_count_ts = ts.groupby(adjusted_grouper).agg('count')
adjusted_count_ts = adjusted_count_ts[middle:end]
adjusted_count_ts2 = ts2.groupby(adjusted_grouper).agg('count')
tm.assert_series_equal(adjusted_count_ts, adjusted_count_ts2)
origin_future = Timestamp(0) + pd.Timedelta('1399min') * 30000
adjusted_grouper2 = pd.Grouper(freq=freq, origin=origin_future)
adjusted2_count_ts = ts.groupby(adjusted_grouper2).agg('count')
adjusted2_count_ts = adjusted2_count_ts[middle:end]
adjusted2_count_ts2 = ts2.groupby(adjusted_grouper2).agg('count')
tm.assert_series_equal(adjusted2_count_ts, adjusted2_count_ts2)
tm.assert_series_equal(adjusted_count_ts, adjusted2_count_ts2)
```

## Next Steps


---

*Source: test_resampler_grouper.py:147 | Complexity: Advanced | Last updated: 2026-06-02*