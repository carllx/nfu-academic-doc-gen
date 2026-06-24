# How To: Multi Axis Dups

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi axis dups

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
df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
```

### Step 2: Assign z = unknown.copy(...)

```python
z = df[['A', 'C', 'A']].copy()
```

### Step 3: Assign expected = value

```python
expected = z.loc[['a', 'c', 'a']]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
```

### Step 5: Assign z = value

```python
z = df[['A', 'C', 'A']]
```

### Step 6: Assign result = value

```python
result = z.loc[['a', 'c', 'a']]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
z = df[['A', 'C', 'A']].copy()
expected = z.loc[['a', 'c', 'a']]
df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
z = df[['A', 'C', 'A']]
result = z.loc[['a', 'c', 'a']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:228 | Complexity: Intermediate | Last updated: 2026-06-02*