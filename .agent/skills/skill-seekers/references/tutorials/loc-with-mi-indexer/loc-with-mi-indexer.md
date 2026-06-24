# How To: Loc With Mi Indexer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc with mi indexer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data=[['a', 1], ['a', 0], ['b', 1], ['c', 2]], index=MultiIndex.from_tuples([(0, 1), (1, 0), (1, 1), (1, 1)], names=['index', 'date']), columns=['author', 'price'])
```

### Step 2: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([(0, 1), (1, 1)], names=['index', 'date'])
```

### Step 3: Assign result = value

```python
result = df.loc[idx, :]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['a', 1], ['b', 1], ['c', 2]], index=MultiIndex.from_tuples([(0, 1), (1, 1), (1, 1)], names=['index', 'date']), columns=['author', 'price'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(data=[['a', 1], ['a', 0], ['b', 1], ['c', 2]], index=MultiIndex.from_tuples([(0, 1), (1, 0), (1, 1), (1, 1)], names=['index', 'date']), columns=['author', 'price'])
idx = MultiIndex.from_tuples([(0, 1), (1, 1)], names=['index', 'date'])
result = df.loc[idx, :]
expected = DataFrame([['a', 1], ['b', 1], ['c', 2]], index=MultiIndex.from_tuples([(0, 1), (1, 1), (1, 1)], names=['index', 'date']), columns=['author', 'price'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:670 | Complexity: Intermediate | Last updated: 2026-06-02*