# How To: Concat Datetime Timezone

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat datetime timezone

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = date_range(...)

```python
idx1 = date_range('2011-01-01', periods=3, freq='h', tz='Europe/Paris')
```

### Step 2: Assign idx2 = date_range(...)

```python
idx2 = date_range(start=idx1[0], end=idx1[-1], freq='h')
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 2, 3]}, index=idx1)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'b': [1, 2, 3]}, index=idx2)
```

### Step 5: Assign result = concat(...)

```python
result = concat([df1, df2], axis=1)
```

### Step 6: Assign exp_idx = DatetimeIndex(...)

```python
exp_idx = DatetimeIndex(['2011-01-01 00:00:00+01:00', '2011-01-01 01:00:00+01:00', '2011-01-01 02:00:00+01:00'], dtype='M8[ns, Europe/Paris]', freq='h')
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1], [2, 2], [3, 3]], index=exp_idx, columns=['a', 'b'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign idx3 = date_range(...)

```python
idx3 = date_range('2011-01-01', periods=3, freq='h', tz='Asia/Tokyo')
```

### Step 10: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'b': [1, 2, 3]}, index=idx3)
```

### Step 11: Assign result = concat(...)

```python
result = concat([df1, df3], axis=1)
```

### Step 12: Assign exp_idx = DatetimeIndex.as_unit(...)

```python
exp_idx = DatetimeIndex(['2010-12-31 15:00:00+00:00', '2010-12-31 16:00:00+00:00', '2010-12-31 17:00:00+00:00', '2010-12-31 23:00:00+00:00', '2011-01-01 00:00:00+00:00', '2011-01-01 01:00:00+00:00']).as_unit('ns')
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan, 1], [np.nan, 2], [np.nan, 3], [1, np.nan], [2, np.nan], [3, np.nan]], index=exp_idx, columns=['a', 'b'])
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign result = concat(...)

```python
result = concat([df1.resample('h').mean(), df2.resample('h').mean()], sort=True)
```

### Step 16: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3] + [np.nan] * 3, 'b': [np.nan] * 3 + [1, 2, 3]}, index=idx1.append(idx1))
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx1 = date_range('2011-01-01', periods=3, freq='h', tz='Europe/Paris')
idx2 = date_range(start=idx1[0], end=idx1[-1], freq='h')
df1 = DataFrame({'a': [1, 2, 3]}, index=idx1)
df2 = DataFrame({'b': [1, 2, 3]}, index=idx2)
result = concat([df1, df2], axis=1)
exp_idx = DatetimeIndex(['2011-01-01 00:00:00+01:00', '2011-01-01 01:00:00+01:00', '2011-01-01 02:00:00+01:00'], dtype='M8[ns, Europe/Paris]', freq='h')
expected = DataFrame([[1, 1], [2, 2], [3, 3]], index=exp_idx, columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
idx3 = date_range('2011-01-01', periods=3, freq='h', tz='Asia/Tokyo')
df3 = DataFrame({'b': [1, 2, 3]}, index=idx3)
result = concat([df1, df3], axis=1)
exp_idx = DatetimeIndex(['2010-12-31 15:00:00+00:00', '2010-12-31 16:00:00+00:00', '2010-12-31 17:00:00+00:00', '2010-12-31 23:00:00+00:00', '2011-01-01 00:00:00+00:00', '2011-01-01 01:00:00+00:00']).as_unit('ns')
expected = DataFrame([[np.nan, 1], [np.nan, 2], [np.nan, 3], [1, np.nan], [2, np.nan], [3, np.nan]], index=exp_idx, columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
result = concat([df1.resample('h').mean(), df2.resample('h').mean()], sort=True)
expected = DataFrame({'a': [1, 2, 3] + [np.nan] * 3, 'b': [np.nan] * 3 + [1, 2, 3]}, index=idx1.append(idx1))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:47 | Complexity: Advanced | Last updated: 2026-06-02*