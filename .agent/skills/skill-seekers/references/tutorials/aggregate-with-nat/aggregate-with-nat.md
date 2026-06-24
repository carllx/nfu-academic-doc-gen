# How To: Aggregate With Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test aggregate with nat

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: func, fill_value
```

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

### Step 9: Assign normal_result = getattr(...)

```python
normal_result = getattr(normal_grouped, func)()
```

### Step 10: Assign dt_result = getattr(...)

```python
dt_result = getattr(dt_grouped, func)()
```

### Step 11: Assign pad = DataFrame(...)

```python
pad = DataFrame([[fill_value] * 4], index=[3], columns=['A', 'B', 'C', 'D'])
```

### Step 12: Assign expected = pd.concat(...)

```python
expected = pd.concat([normal_result, pad])
```

### Step 13: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 14: Assign dti = date_range(...)

```python
dti = date_range(start='2013-01-01', freq='D', periods=5, name='key', unit=dt_df['key']._values.unit)
```

### Step 15: Assign expected.index = dti._with_freq(...)

```python
expected.index = dti._with_freq(None)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, dt_result)
```

**Verification:**
```python
assert dt_result.index.name == 'key'
```


## Complete Example

```python
# Setup
# Fixtures: func, fill_value

# Workflow
n = 20
data = np.random.default_rng(2).standard_normal((n, 4)).astype('int64')
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
normal_df['key'] = [1, 2, np.nan, 4, 5] * 4
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
dt_df['key'] = Index([datetime(2013, 1, 1), datetime(2013, 1, 2), pd.NaT, datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4, dtype='M8[ns]')
normal_grouped = normal_df.groupby('key')
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
normal_result = getattr(normal_grouped, func)()
dt_result = getattr(dt_grouped, func)()
pad = DataFrame([[fill_value] * 4], index=[3], columns=['A', 'B', 'C', 'D'])
expected = pd.concat([normal_result, pad])
expected = expected.sort_index()
dti = date_range(start='2013-01-01', freq='D', periods=5, name='key', unit=dt_df['key']._values.unit)
expected.index = dti._with_freq(None)
tm.assert_frame_equal(expected, dt_result)
assert dt_result.index.name == 'key'
```

## Next Steps


---

*Source: test_time_grouper.py:211 | Complexity: Advanced | Last updated: 2026-06-02*