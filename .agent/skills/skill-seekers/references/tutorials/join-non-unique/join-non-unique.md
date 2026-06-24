# How To: Join Non Unique

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join non unique

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign left = Index(...)

```python
left = Index([4, 4, 3, 3])
```

### Step 2: Assign unknown = left.join(...)

```python
joined, lidx, ridx = left.join(left, return_indexers=True)
```

### Step 3: Assign exp_joined = Index(...)

```python
exp_joined = Index([4, 4, 4, 4, 3, 3, 3, 3])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined, exp_joined)
```

### Step 5: Assign exp_lidx = np.array(...)

```python
exp_lidx = np.array([0, 0, 1, 1, 2, 2, 3, 3], dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, exp_lidx)
```

### Step 7: Assign exp_ridx = np.array(...)

```python
exp_ridx = np.array([0, 1, 0, 1, 2, 3, 2, 3], dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```


## Complete Example

```python
# Workflow
left = Index([4, 4, 3, 3])
joined, lidx, ridx = left.join(left, return_indexers=True)
exp_joined = Index([4, 4, 4, 4, 3, 3, 3, 3])
tm.assert_index_equal(joined, exp_joined)
exp_lidx = np.array([0, 0, 1, 1, 2, 2, 3, 3], dtype=np.intp)
tm.assert_numpy_array_equal(lidx, exp_lidx)
exp_ridx = np.array([0, 1, 0, 1, 2, 3, 2, 3], dtype=np.intp)
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

## Next Steps


---

*Source: test_join.py:9 | Complexity: Advanced | Last updated: 2026-06-02*