# How To: Drop Nonunique

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop nonunique

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['x-a', 'x', 'a', 1.5], ['x-a', 'x', 'a', 1.2], ['z-c', 'z', 'c', 3.1], ['x-a', 'x', 'a', 4.1], ['x-b', 'x', 'b', 5.1], ['x-b', 'x', 'b', 4.1], ['x-b', 'x', 'b', 2.2], ['y-a', 'y', 'a', 1.2], ['z-b', 'z', 'b', 2.1]], columns=['var1', 'var2', 'var3', 'var4'])
```

### Step 2: Assign grp_size = df.groupby.size(...)

```python
grp_size = df.groupby('var1').size()
```

### Step 3: Assign drop_idx = value

```python
drop_idx = grp_size.loc[grp_size == 1]
```

### Step 4: Assign idf = df.set_index(...)

```python
idf = df.set_index(['var1', 'var2', 'var3'])
```

### Step 5: Assign result = idf.drop.reset_index(...)

```python
result = idf.drop(drop_idx.index, level=0).reset_index()
```

### Step 6: Assign expected = value

```python
expected = df[-df.var1.isin(drop_idx.index)]
```

### Step 7: Assign result.index = value

```python
result.index = expected.index
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([['x-a', 'x', 'a', 1.5], ['x-a', 'x', 'a', 1.2], ['z-c', 'z', 'c', 3.1], ['x-a', 'x', 'a', 4.1], ['x-b', 'x', 'b', 5.1], ['x-b', 'x', 'b', 4.1], ['x-b', 'x', 'b', 2.2], ['y-a', 'y', 'a', 1.2], ['z-b', 'z', 'b', 2.1]], columns=['var1', 'var2', 'var3', 'var4'])
grp_size = df.groupby('var1').size()
drop_idx = grp_size.loc[grp_size == 1]
idf = df.set_index(['var1', 'var2', 'var3'])
result = idf.drop(drop_idx.index, level=0).reset_index()
expected = df[-df.var1.isin(drop_idx.index)]
result.index = expected.index
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:353 | Complexity: Advanced | Last updated: 2026-06-02*