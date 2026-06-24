# How To: Quantile Array Multiple Levels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile array multiple levels

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
df = DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'c': ['a', 'a', 'a'], 'd': ['a', 'a', 'b']})
```

### Step 2: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(['c', 'd']).quantile([0.25, 0.75])
```

### Step 3: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples([('a', 'a', 0.25), ('a', 'a', 0.75), ('a', 'b', 0.25), ('a', 'b', 0.75)], names=['c', 'd', None])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0.25, 0.75, 2.0, 2.0], 'B': [3.25, 3.75, 5.0, 5.0]}, index=index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'c': ['a', 'a', 'a'], 'd': ['a', 'a', 'b']})
result = df.groupby(['c', 'd']).quantile([0.25, 0.75])
index = pd.MultiIndex.from_tuples([('a', 'a', 0.25), ('a', 'a', 0.75), ('a', 'b', 0.25), ('a', 'b', 0.75)], names=['c', 'd', None])
expected = DataFrame({'A': [0.25, 0.75, 2.0, 2.0], 'B': [3.25, 3.75, 5.0, 5.0]}, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*