# How To: Left Outer Join Bug

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test left outer join bug

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.join`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = np.array(...)

```python
left = np.array([0, 1, 0, 1, 1, 2, 3, 1, 0, 2, 1, 2, 0, 1, 1, 2, 3, 2, 3, 2, 1, 1, 3, 0, 3, 2, 3, 0, 0, 2, 3, 2, 0, 3, 1, 3, 0, 1, 3, 0, 0, 1, 0, 3, 1, 0, 1, 0, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 1, 2, 0, 0, 3, 1, 3, 2, 2, 0, 1, 3, 0, 2, 3, 2, 3, 3, 2, 3, 3, 1, 3, 2, 0, 0, 3, 1, 1, 1, 0, 2, 3, 3, 1, 2, 0, 3, 1, 2, 0, 2], dtype=np.intp)
```

### Step 2: Assign right = np.array(...)

```python
right = np.array([3, 1], dtype=np.intp)
```

### Step 3: Assign max_groups = 4

```python
max_groups = 4
```

### Step 4: Assign unknown = libjoin.left_outer_join(...)

```python
lidx, ridx = libjoin.left_outer_join(left, right, max_groups, sort=False)
```

### Step 5: Assign exp_lidx = np.arange(...)

```python
exp_lidx = np.arange(len(left), dtype=np.intp)
```

### Step 6: Assign exp_ridx = value

```python
exp_ridx = -np.ones(len(left), dtype=np.intp)
```

### Step 7: Assign unknown = 1

```python
exp_ridx[left == 1] = 1
```

### Step 8: Assign unknown = 0

```python
exp_ridx[left == 3] = 0
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, exp_lidx)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```


## Complete Example

```python
# Workflow
left = np.array([0, 1, 0, 1, 1, 2, 3, 1, 0, 2, 1, 2, 0, 1, 1, 2, 3, 2, 3, 2, 1, 1, 3, 0, 3, 2, 3, 0, 0, 2, 3, 2, 0, 3, 1, 3, 0, 1, 3, 0, 0, 1, 0, 3, 1, 0, 1, 0, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 1, 2, 0, 0, 3, 1, 3, 2, 2, 0, 1, 3, 0, 2, 3, 2, 3, 3, 2, 3, 3, 1, 3, 2, 0, 0, 3, 1, 1, 1, 0, 2, 3, 3, 1, 2, 0, 3, 1, 2, 0, 2], dtype=np.intp)
right = np.array([3, 1], dtype=np.intp)
max_groups = 4
lidx, ridx = libjoin.left_outer_join(left, right, max_groups, sort=False)
exp_lidx = np.arange(len(left), dtype=np.intp)
exp_ridx = -np.ones(len(left), dtype=np.intp)
exp_ridx[left == 1] = 1
exp_ridx[left == 3] = 0
tm.assert_numpy_array_equal(lidx, exp_lidx)
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

## Next Steps


---

*Source: test_join.py:155 | Complexity: Advanced | Last updated: 2026-06-02*