# How To: Aggregate With Nat Size

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aggregate with nat size

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign n = 20

```python
n = 20
```

**Verification:**
```python
assert dt_result.index.name == 'key'
```

### Step 2: Assign data = np.random.default_rng.standard_normal.astype(...)

```python
data = np.random.default_rng(2).standard_normal((n, 4)).astype('int64')
```

### Step 3: Assign normal_df = DataFrame(...)

```python
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
```

### Step 4: Assign unknown = value

```python
normal_df['key'] = [1, 2, np.nan, 4, 5] * 4
```

### Step 5: Assign dt_df = DataFrame(...)

```python
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
```

### Step 6: Assign unknown = Index(...)

```python
dt_df['key'] = Index([datetime(2013, 1, 1), datetime(2013, 1, 2), pd.NaT, datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4, dtype='M8[ns]')
```

### Step 7: Assign normal_grouped = normal_df.groupby(...)

```python
normal_grouped = normal_df.groupby('key')
```

### Step 8: Assign dt_grouped = dt_df.groupby(...)

```python
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
```

### Step 9: Assign normal_result = normal_grouped.size(...)

```python
normal_result = normal_grouped.size()
```

### Step 10: Assign dt_result = dt_grouped.size(...)

```python
dt_result = dt_grouped.size()
```

### Step 11: Assign pad = Series(...)

```python
pad = Series([0], index=[3])
```

### Step 12: Assign expected = pd.concat(...)

```python
expected = pd.concat([normal_result, pad])
```

### Step 13: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 14: Assign expected.index = date_range._with_freq(...)

```python
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key', unit=dt_df['key']._values.unit)._with_freq(None)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, dt_result)
```

**Verification:**
```python
assert dt_result.index.name == 'key'
```


## Complete Example

```python
# Workflow
n = 20
data = np.random.default_rng(2).standard_normal((n, 4)).astype('int64')
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
normal_df['key'] = [1, 2, np.nan, 4, 5] * 4
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
dt_df['key'] = Index([datetime(2013, 1, 1), datetime(2013, 1, 2), pd.NaT, datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4, dtype='M8[ns]')
normal_grouped = normal_df.groupby('key')
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
normal_result = normal_grouped.size()
dt_result = dt_grouped.size()
pad = Series([0], index=[3])
expected = pd.concat([normal_result, pad])
expected = expected.sort_index()
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key', unit=dt_df['key']._values.unit)._with_freq(None)
tm.assert_series_equal(expected, dt_result)
assert dt_result.index.name == 'key'
```

## Next Steps


---

*Source: test_time_grouper.py:255 | Complexity: Advanced | Last updated: 2026-06-02*