# How To: Apply Fast Slow Identical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply fast slow identical

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 0, 1], 'b': range(3)})
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(fast_df, slow_df)
```

### Step 4: Assign fast_df = df.groupby.apply(...)

```python
fast_df = df.groupby('A', group_keys=False).apply(fast)
```

### Step 5: Assign slow_df = df.groupby.apply(...)

```python
slow_df = df.groupby('A', group_keys=False).apply(slow)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [0, 0, 1], 'b': range(3)})

def slow(group):
    return group

def fast(group):
    return group.copy()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    fast_df = df.groupby('A', group_keys=False).apply(fast)
with tm.assert_produces_warning(FutureWarning, match=msg):
    slow_df = df.groupby('A', group_keys=False).apply(slow)
tm.assert_frame_equal(fast_df, slow_df)
```

## Next Steps


---

*Source: test_apply.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*