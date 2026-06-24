# How To: Join Inner

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join inner

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`

**Setup Required:**
```python
# Fixtures: index_large
```

## Step-by-Step Guide

### Step 1: Assign other = Index(...)

```python
other = Index(2 ** 63 + np.array([7, 12, 25, 1, 2, 10], dtype='uint64'))
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 2: Assign other_mono = Index(...)

```python
other_mono = Index(2 ** 63 + np.array([1, 2, 7, 10, 12, 25], dtype='uint64'))
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 3: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other, how='inner', return_indexers=True)
```

### Step 4: Assign ind = res.argsort(...)

```python
ind = res.argsort()
```

### Step 5: Assign res = res.take(...)

```python
res = res.take(ind)
```

### Step 6: Assign lidx = lidx.take(...)

```python
lidx = lidx.take(ind)
```

### Step 7: Assign ridx = ridx.take(...)

```python
ridx = ridx.take(ind)
```

### Step 8: Assign eres = Index(...)

```python
eres = Index(2 ** 63 + np.array([10, 25], dtype='uint64'))
```

### Step 9: Assign elidx = np.array(...)

```python
elidx = np.array([1, 4], dtype=np.intp)
```

### Step 10: Assign eridx = np.array(...)

```python
eridx = np.array([5, 2], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, eridx)
```

### Step 14: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other_mono, how='inner', return_indexers=True)
```

### Step 15: Assign res2 = index_large.intersection(...)

```python
res2 = index_large.intersection(other_mono)
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, res2)
```

### Step 17: Assign elidx = np.array(...)

```python
elidx = np.array([1, 4], dtype=np.intp)
```

### Step 18: Assign eridx = np.array(...)

```python
eridx = np.array([3, 5], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

### Step 21: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, eridx)
```


## Complete Example

```python
# Setup
# Fixtures: index_large

# Workflow
other = Index(2 ** 63 + np.array([7, 12, 25, 1, 2, 10], dtype='uint64'))
other_mono = Index(2 ** 63 + np.array([1, 2, 7, 10, 12, 25], dtype='uint64'))
res, lidx, ridx = index_large.join(other, how='inner', return_indexers=True)
ind = res.argsort()
res = res.take(ind)
lidx = lidx.take(ind)
ridx = ridx.take(ind)
eres = Index(2 ** 63 + np.array([10, 25], dtype='uint64'))
elidx = np.array([1, 4], dtype=np.intp)
eridx = np.array([5, 2], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
res, lidx, ridx = index_large.join(other_mono, how='inner', return_indexers=True)
res2 = index_large.intersection(other_mono)
tm.assert_index_equal(res, res2)
elidx = np.array([1, 4], dtype=np.intp)
eridx = np.array([3, 5], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
```

## Next Steps


---

*Source: test_join.py:200 | Complexity: Advanced | Last updated: 2026-06-02*