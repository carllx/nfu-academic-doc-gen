# How To: Inner Join Indexer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inner join indexer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.join`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([0, 3, 5, 7, 9], dtype=np.int64)
```

### Step 3: Assign unknown = libjoin.inner_join_indexer(...)

```python
index, ares, bres = libjoin.inner_join_indexer(a, b)
```

### Step 4: Assign index_exp = np.array(...)

```python
index_exp = np.array([3, 5], dtype=np.int64)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(index, index_exp)
```

### Step 6: Assign aexp = np.array(...)

```python
aexp = np.array([2, 4], dtype=np.intp)
```

### Step 7: Assign bexp = np.array(...)

```python
bexp = np.array([1, 2], dtype=np.intp)
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(ares, aexp)
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(bres, bexp)
```

### Step 10: Assign a = np.array(...)

```python
a = np.array([5], dtype=np.int64)
```

### Step 11: Assign b = np.array(...)

```python
b = np.array([5], dtype=np.int64)
```

### Step 12: Assign unknown = libjoin.inner_join_indexer(...)

```python
index, ares, bres = libjoin.inner_join_indexer(a, b)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(index, np.array([5], dtype=np.int64))
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ares, np.array([0], dtype=np.intp))
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(bres, np.array([0], dtype=np.intp))
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
b = np.array([0, 3, 5, 7, 9], dtype=np.int64)
index, ares, bres = libjoin.inner_join_indexer(a, b)
index_exp = np.array([3, 5], dtype=np.int64)
tm.assert_almost_equal(index, index_exp)
aexp = np.array([2, 4], dtype=np.intp)
bexp = np.array([1, 2], dtype=np.intp)
tm.assert_almost_equal(ares, aexp)
tm.assert_almost_equal(bres, bexp)
a = np.array([5], dtype=np.int64)
b = np.array([5], dtype=np.int64)
index, ares, bres = libjoin.inner_join_indexer(a, b)
tm.assert_numpy_array_equal(index, np.array([5], dtype=np.int64))
tm.assert_numpy_array_equal(ares, np.array([0], dtype=np.intp))
tm.assert_numpy_array_equal(bres, np.array([0], dtype=np.intp))
```

## Next Steps


---

*Source: test_join.py:277 | Complexity: Advanced | Last updated: 2026-06-02*