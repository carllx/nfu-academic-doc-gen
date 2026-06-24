# How To: Getitem Multilevel Index Tuple Not Sorted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem multilevel index tuple not sorted

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index_columns = list(...)

```python
index_columns = list('abc')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[0, 1, 0, 'x'], [0, 0, 1, 'y']], columns=index_columns + ['data'])
```

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index(index_columns)
```

### Step 4: Assign query_index = value

```python
query_index = df.index[:1]
```

### Step 5: Assign rs = value

```python
rs = df.loc[query_index, 'data']
```

### Step 6: Assign xp_idx = MultiIndex.from_tuples(...)

```python
xp_idx = MultiIndex.from_tuples([(0, 1, 0)], names=['a', 'b', 'c'])
```

### Step 7: Assign xp = Series(...)

```python
xp = Series(['x'], index=xp_idx, name='data')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, xp)
```


## Complete Example

```python
# Workflow
index_columns = list('abc')
df = DataFrame([[0, 1, 0, 'x'], [0, 0, 1, 'y']], columns=index_columns + ['data'])
df = df.set_index(index_columns)
query_index = df.index[:1]
rs = df.loc[query_index, 'data']
xp_idx = MultiIndex.from_tuples([(0, 1, 0)], names=['a', 'b', 'c'])
xp = Series(['x'], index=xp_idx, name='data')
tm.assert_series_equal(rs, xp)
```

## Next Steps


---

*Source: test_sorted.py:15 | Complexity: Advanced | Last updated: 2026-06-02*