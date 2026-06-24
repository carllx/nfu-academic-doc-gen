# How To: Sort Index Reorder On Ops

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index reorder on ops

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((8, 2)), index=MultiIndex.from_product([['a', 'b'], ['big', 'small'], ['red', 'blu']], names=['letter', 'size', 'color']), columns=['near', 'far'])
```

### Step 2: Assign df = df.sort_index(...)

```python
df = df.sort_index()
```

### Step 3: Assign result = df.groupby.apply.sort_index(...)

```python
result = df.groupby(level=['letter', 'size']).apply(my_func).sort_index()
```

### Step 4: Assign expected = MultiIndex.from_product(...)

```python
expected = MultiIndex.from_product([['a', 'b'], ['big', 'small'], ['newa', 'newz']], names=['letter', 'size', None])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected)
```

### Step 6: Assign group.index = value

```python
group.index = ['newz', 'newa']
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((8, 2)), index=MultiIndex.from_product([['a', 'b'], ['big', 'small'], ['red', 'blu']], names=['letter', 'size', 'color']), columns=['near', 'far'])
df = df.sort_index()

def my_func(group):
    group.index = ['newz', 'newa']
    return group
result = df.groupby(level=['letter', 'size']).apply(my_func).sort_index()
expected = MultiIndex.from_product([['a', 'b'], ['big', 'small'], ['newa', 'newz']], names=['letter', 'size', None])
tm.assert_index_equal(result.index, expected)
```

## Next Steps


---

*Source: test_sort_index.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*