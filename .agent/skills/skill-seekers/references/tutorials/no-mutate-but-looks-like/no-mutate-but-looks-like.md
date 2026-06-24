# How To: No Mutate But Looks Like

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no mutate but looks like

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'key': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'value': range(9)})
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, result2)
```

### Step 4: Assign result1 = df.groupby.apply(...)

```python
result1 = df.groupby('key', group_keys=True).apply(lambda x: x[:].key)
```

### Step 5: Assign result2 = df.groupby.apply(...)

```python
result2 = df.groupby('key', group_keys=True).apply(lambda x: x.key)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'key': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'value': range(9)})
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result1 = df.groupby('key', group_keys=True).apply(lambda x: x[:].key)
with tm.assert_produces_warning(FutureWarning, match=msg):
    result2 = df.groupby('key', group_keys=True).apply(lambda x: x.key)
tm.assert_series_equal(result1, result2)
```

## Next Steps


---

*Source: test_apply_mutate.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*