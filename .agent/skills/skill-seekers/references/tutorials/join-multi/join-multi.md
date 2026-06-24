# How To: Join Multi

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join multi

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_product(...)

```python
midx = MultiIndex.from_product([np.arange(4), np.arange(4)], names=['a', 'b'])
```

**Verification:**
```python
assert lidx is None
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([1, 2, 5], name='b')
```

**Verification:**
```python
assert lidx is None
```

### Step 3: Assign unknown = midx.join(...)

```python
jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
```

### Step 4: Assign exp_idx = MultiIndex.from_product(...)

```python
exp_idx = MultiIndex.from_product([np.arange(4), [1, 2]], names=['a', 'b'])
```

### Step 5: Assign exp_lidx = np.array(...)

```python
exp_lidx = np.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=np.intp)
```

### Step 6: Assign exp_ridx = np.array(...)

```python
exp_ridx = np.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=np.intp)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jidx, exp_idx)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, exp_lidx)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

### Step 10: Assign unknown = idx.join(...)

```python
jidx, ridx, lidx = idx.join(midx, how='inner', return_indexers=True)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jidx, exp_idx)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, exp_lidx)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

### Step 14: Assign unknown = midx.join(...)

```python
jidx, lidx, ridx = midx.join(idx, how='left', return_indexers=True)
```

### Step 15: Assign exp_ridx = np.array(...)

```python
exp_ridx = np.array([-1, 0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1], dtype=np.intp)
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jidx, midx)
```

**Verification:**
```python
assert lidx is None
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

### Step 18: Assign unknown = idx.join(...)

```python
jidx, ridx, lidx = idx.join(midx, how='right', return_indexers=True)
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jidx, midx)
```

**Verification:**
```python
assert lidx is None
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, exp_ridx)
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_product([np.arange(4), np.arange(4)], names=['a', 'b'])
idx = Index([1, 2, 5], name='b')
jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
exp_idx = MultiIndex.from_product([np.arange(4), [1, 2]], names=['a', 'b'])
exp_lidx = np.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=np.intp)
exp_ridx = np.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=np.intp)
tm.assert_index_equal(jidx, exp_idx)
tm.assert_numpy_array_equal(lidx, exp_lidx)
tm.assert_numpy_array_equal(ridx, exp_ridx)
jidx, ridx, lidx = idx.join(midx, how='inner', return_indexers=True)
tm.assert_index_equal(jidx, exp_idx)
tm.assert_numpy_array_equal(lidx, exp_lidx)
tm.assert_numpy_array_equal(ridx, exp_ridx)
jidx, lidx, ridx = midx.join(idx, how='left', return_indexers=True)
exp_ridx = np.array([-1, 0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1], dtype=np.intp)
tm.assert_index_equal(jidx, midx)
assert lidx is None
tm.assert_numpy_array_equal(ridx, exp_ridx)
jidx, ridx, lidx = idx.join(midx, how='right', return_indexers=True)
tm.assert_index_equal(jidx, midx)
assert lidx is None
tm.assert_numpy_array_equal(ridx, exp_ridx)
```

## Next Steps


---

*Source: test_join.py:61 | Complexity: Advanced | Last updated: 2026-06-02*