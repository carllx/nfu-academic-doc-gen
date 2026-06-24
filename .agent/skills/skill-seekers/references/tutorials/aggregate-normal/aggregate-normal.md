# How To: Aggregate Normal

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check TimeGrouper's aggregation is identical as normal groupby.

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
# Fixtures: resample_method
```

## Step-by-Step Guide

### Step 1: "Check TimeGrouper's aggregation is identical as normal groupby."

```python
"Check TimeGrouper's aggregation is identical as normal groupby."
```

### Step 2: Assign data = np.random.default_rng.standard_normal(...)

```python
data = np.random.default_rng(2).standard_normal((20, 4))
```

### Step 3: Assign normal_df = DataFrame(...)

```python
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
```

### Step 4: Assign unknown = value

```python
normal_df['key'] = [1, 2, 3, 4, 5] * 4
```

### Step 5: Assign dt_df = DataFrame(...)

```python
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
```

### Step 6: Assign unknown = Index(...)

```python
dt_df['key'] = Index([datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4, dtype='M8[ns]')
```

### Step 7: Assign normal_grouped = normal_df.groupby(...)

```python
normal_grouped = normal_df.groupby('key')
```

### Step 8: Assign dt_grouped = dt_df.groupby(...)

```python
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
```

### Step 9: Assign expected = getattr(...)

```python
expected = getattr(normal_grouped, resample_method)()
```

### Step 10: Assign dt_result = getattr(...)

```python
dt_result = getattr(dt_grouped, resample_method)()
```

### Step 11: Assign expected.index = date_range(...)

```python
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key')
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(expected, dt_result)
```


## Complete Example

```python
# Setup
# Fixtures: resample_method

# Workflow
"Check TimeGrouper's aggregation is identical as normal groupby."
data = np.random.default_rng(2).standard_normal((20, 4))
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
normal_df['key'] = [1, 2, 3, 4, 5] * 4
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
dt_df['key'] = Index([datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4, dtype='M8[ns]')
normal_grouped = normal_df.groupby('key')
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
expected = getattr(normal_grouped, resample_method)()
dt_result = getattr(dt_grouped, resample_method)()
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key')
tm.assert_equal(expected, dt_result)
```

## Next Steps


---

*Source: test_time_grouper.py:132 | Complexity: Advanced | Last updated: 2026-06-02*