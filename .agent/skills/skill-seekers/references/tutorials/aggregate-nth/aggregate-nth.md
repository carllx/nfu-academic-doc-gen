# How To: Aggregate Nth

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Check TimeGrouper's aggregation is identical as normal groupby.

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

### Step 6: Assign unknown = value

```python
dt_df['key'] = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4
```

### Step 7: Assign normal_grouped = normal_df.groupby(...)

```python
normal_grouped = normal_df.groupby('key')
```

### Step 8: Assign dt_grouped = dt_df.groupby(...)

```python
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
```

### Step 9: Assign expected = normal_grouped.nth(...)

```python
expected = normal_grouped.nth(3)
```

### Step 10: Assign expected.index = date_range(...)

```python
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key')
```

### Step 11: Assign dt_result = dt_grouped.nth(...)

```python
dt_result = dt_grouped.nth(3)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, dt_result)
```


## Complete Example

```python
# Workflow
"Check TimeGrouper's aggregation is identical as normal groupby."
data = np.random.default_rng(2).standard_normal((20, 4))
normal_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
normal_df['key'] = [1, 2, 3, 4, 5] * 4
dt_df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
dt_df['key'] = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4
normal_grouped = normal_df.groupby('key')
dt_grouped = dt_df.groupby(Grouper(key='key', freq='D'))
expected = normal_grouped.nth(3)
expected.index = date_range(start='2013-01-01', freq='D', periods=5, name='key')
dt_result = dt_grouped.nth(3)
tm.assert_frame_equal(expected, dt_result)
```

## Next Steps


---

*Source: test_time_grouper.py:162 | Complexity: Advanced | Last updated: 2026-06-02*