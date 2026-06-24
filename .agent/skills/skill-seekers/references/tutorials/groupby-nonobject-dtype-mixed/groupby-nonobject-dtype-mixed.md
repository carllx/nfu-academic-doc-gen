# How To: Groupby Nonobject Dtype Mixed

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby nonobject dtype mixed

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.array(np.random.default_rng(2).standard_normal(8), dtype='float32')})
```

### Step 2: Assign unknown = range(...)

```python
df['value'] = range(len(df))
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 4: Assign result = value

```python
result = applied.dtypes
```

### Step 5: Assign expected = value

```python
expected = df.dtypes
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign applied = df.groupby.apply(...)

```python
applied = df.groupby('A').apply(max_value)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.array(np.random.default_rng(2).standard_normal(8), dtype='float32')})
df['value'] = range(len(df))

def max_value(group):
    return group.loc[group['value'].idxmax()]
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    applied = df.groupby('A').apply(max_value)
result = applied.dtypes
expected = df.dtypes
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:148 | Complexity: Intermediate | Last updated: 2026-06-02*