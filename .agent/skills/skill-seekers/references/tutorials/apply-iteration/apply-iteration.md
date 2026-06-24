# How To: Apply Iteration

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply iteration

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

### Step 1: Assign N = 1000

```python
N = 1000
```

### Step 2: Assign ind = date_range(...)

```python
ind = date_range(start='2000-01-01', freq='D', periods=N)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'open': 1, 'close': 2}, index=ind)
```

### Step 4: Assign tg = Grouper(...)

```python
tg = Grouper(freq='ME')
```

### Step 5: Assign unknown = tg._get_grouper(...)

```python
grouper, _ = tg._get_grouper(df)
```

### Step 6: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(grouper, group_keys=False)
```

### Step 7: Assign result = grouped.apply(...)

```python
result = grouped.apply(f)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, df.index)
```


## Complete Example

```python
# Workflow
N = 1000
ind = date_range(start='2000-01-01', freq='D', periods=N)
df = DataFrame({'open': 1, 'close': 2}, index=ind)
tg = Grouper(freq='ME')
grouper, _ = tg._get_grouper(df)
grouped = df.groupby(grouper, group_keys=False)

def f(df):
    return df['close'] / df['open']
result = grouped.apply(f)
tm.assert_index_equal(result.index, df.index)
```

## Next Steps


---

*Source: test_time_grouper.py:69 | Complexity: Advanced | Last updated: 2026-06-02*