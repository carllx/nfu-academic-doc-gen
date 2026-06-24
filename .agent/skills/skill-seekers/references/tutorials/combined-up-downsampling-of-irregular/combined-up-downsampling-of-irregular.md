# How To: Combined Up Downsampling Of Irregular

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combined up downsampling of irregular

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2012', periods=100, freq='s')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.arange(len(rng)), index=rng)
```

### Step 3: Assign ts2 = value

```python
ts2 = ts.iloc[[0, 1, 2, 3, 5, 7, 11, 15, 16, 25, 30]]
```

### Step 4: Assign result = ts2.resample.mean.ffill(...)

```python
result = ts2.resample('2s').mean().ffill()
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0.5, 2.5, 5.0, 7.0, 7.0, 11.0, 11.0, 15.0, 16.0, 16.0, 16.0, 16.0, 25.0, 25.0, 25.0, 30.0], index=pd.DatetimeIndex(['2012-01-01 00:00:00', '2012-01-01 00:00:02', '2012-01-01 00:00:04', '2012-01-01 00:00:06', '2012-01-01 00:00:08', '2012-01-01 00:00:10', '2012-01-01 00:00:12', '2012-01-01 00:00:14', '2012-01-01 00:00:16', '2012-01-01 00:00:18', '2012-01-01 00:00:20', '2012-01-01 00:00:22', '2012-01-01 00:00:24', '2012-01-01 00:00:26', '2012-01-01 00:00:28', '2012-01-01 00:00:30'], dtype='datetime64[ns]', freq='2s'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2012', periods=100, freq='s')
ts = Series(np.arange(len(rng)), index=rng)
ts2 = ts.iloc[[0, 1, 2, 3, 5, 7, 11, 15, 16, 25, 30]]
result = ts2.resample('2s').mean().ffill()
expected = Series([0.5, 2.5, 5.0, 7.0, 7.0, 11.0, 11.0, 15.0, 16.0, 16.0, 16.0, 16.0, 25.0, 25.0, 25.0, 30.0], index=pd.DatetimeIndex(['2012-01-01 00:00:00', '2012-01-01 00:00:02', '2012-01-01 00:00:04', '2012-01-01 00:00:06', '2012-01-01 00:00:08', '2012-01-01 00:00:10', '2012-01-01 00:00:12', '2012-01-01 00:00:14', '2012-01-01 00:00:16', '2012-01-01 00:00:18', '2012-01-01 00:00:20', '2012-01-01 00:00:22', '2012-01-01 00:00:24', '2012-01-01 00:00:26', '2012-01-01 00:00:28', '2012-01-01 00:00:30'], dtype='datetime64[ns]', freq='2s'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*