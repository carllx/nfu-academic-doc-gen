# How To: Inner Join Indexer2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inner join indexer2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.join`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = np.array(...)

```python
idx = np.array([1, 1, 2, 5], dtype=np.int64)
```

### Step 2: Assign idx2 = np.array(...)

```python
idx2 = np.array([1, 2, 5, 7, 9], dtype=np.int64)
```

### Step 3: Assign unknown = libjoin.inner_join_indexer(...)

```python
res, lidx, ridx = libjoin.inner_join_indexer(idx2, idx)
```

### Step 4: Assign exp_res = np.array(...)

```python
exp_res = np.array([1, 1, 2, 5], dtype=np.int64)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(res, exp_res)
```

### Step 6: Assign exp_lidx = np.array(...)

```python
exp_lidx = np.array([0, 0, 1, 2], dtype=np.intp)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(lidx, exp_lidx)
```

### Step 8: Assign exp_ridx = np.array(...)

```python
exp_ridx = np.array([0, 1, 2, 3], dtype=np.intp)
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(ridx, exp_ridx)
```


## Complete Example

```python
# Workflow
idx = np.array([1, 1, 2, 5], dtype=np.int64)
idx2 = np.array([1, 2, 5, 7, 9], dtype=np.int64)
res, lidx, ridx = libjoin.inner_join_indexer(idx2, idx)
exp_res = np.array([1, 1, 2, 5], dtype=np.int64)
tm.assert_almost_equal(res, exp_res)
exp_lidx = np.array([0, 0, 1, 2], dtype=np.intp)
tm.assert_almost_equal(lidx, exp_lidx)
exp_ridx = np.array([0, 1, 2, 3], dtype=np.intp)
tm.assert_almost_equal(ridx, exp_ridx)
```

## Next Steps


---

*Source: test_join.py:377 | Complexity: Advanced | Last updated: 2026-06-02*