# How To: Apply Index Date Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply index date object

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = ['2011-05-16 00:00', '2011-05-16 01:00', '2011-05-16 02:00', '2011-05-16 03:00', '2011-05-17 02:00', '2011-05-17 03:00', '2011-05-17 04:00', '2011-05-17 05:00', '2011-05-18 02:00', '2011-05-18 03:00', '2011-05-18 04:00', '2011-05-18 05:00']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([row.split() for row in ts], columns=['date', 'time'])
```

### Step 3: Assign unknown = value

```python
df['value'] = [1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649]
```

### Step 4: Assign exp_idx = Index(...)

```python
exp_idx = Index(['2011-05-16', '2011-05-17', '2011-05-18'], name='date')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(['00:00', '02:00', '02:00'], index=exp_idx)
```

### Step 6: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = df.groupby.apply(...)

```python
result = df.groupby('date', group_keys=False).apply(lambda x: x['time'][x['value'].idxmax()])
```


## Complete Example

```python
# Workflow
ts = ['2011-05-16 00:00', '2011-05-16 01:00', '2011-05-16 02:00', '2011-05-16 03:00', '2011-05-17 02:00', '2011-05-17 03:00', '2011-05-17 04:00', '2011-05-17 05:00', '2011-05-18 02:00', '2011-05-18 03:00', '2011-05-18 04:00', '2011-05-18 05:00']
df = DataFrame([row.split() for row in ts], columns=['date', 'time'])
df['value'] = [1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649]
exp_idx = Index(['2011-05-16', '2011-05-17', '2011-05-18'], name='date')
expected = Series(['00:00', '02:00', '02:00'], index=exp_idx)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('date', group_keys=False).apply(lambda x: x['time'][x['value'].idxmax()])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:82 | Complexity: Advanced | Last updated: 2026-06-02*