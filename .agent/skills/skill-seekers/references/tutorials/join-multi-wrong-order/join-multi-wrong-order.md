# How To: Join Multi Wrong Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join multi wrong order

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx1 = MultiIndex.from_product(...)

```python
midx1 = MultiIndex.from_product([[1, 2], [3, 4]], names=['a', 'b'])
```

**Verification:**
```python
assert lidx is None
```

### Step 2: Assign midx2 = MultiIndex.from_product(...)

```python
midx2 = MultiIndex.from_product([[1, 2], [3, 4]], names=['b', 'a'])
```

### Step 3: Assign unknown = midx1.join(...)

```python
join_idx, lidx, ridx = midx1.join(midx2, return_indexers=True)
```

### Step 4: Assign exp_ridx = np.array(...)

```python
exp_ridx = np.array([-1, -1, -1, -1], dtype=np.intp)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(midx1, join_idx)
```

**Verification:**
```python
assert lidx is None
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```


## Complete Example

```python
# Workflow
midx1 = MultiIndex.from_product([[1, 2], [3, 4]], names=['a', 'b'])
midx2 = MultiIndex.from_product([[1, 2], [3, 4]], names=['b', 'a'])
join_idx, lidx, ridx = midx1.join(midx2, return_indexers=True)
exp_ridx = np.array([-1, -1, -1, -1], dtype=np.intp)
tm.assert_index_equal(midx1, join_idx)
assert lidx is None
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

## Next Steps


---

*Source: test_join.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*