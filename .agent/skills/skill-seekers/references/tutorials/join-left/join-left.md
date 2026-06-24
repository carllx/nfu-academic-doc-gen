# How To: Join Left

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join left

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
assert lidx is None
```

### Step 3: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other, how='left', return_indexers=True)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 4: Assign eres = index_large

```python
eres = index_large
```

**Verification:**
```python
assert lidx is None
```

### Step 5: Assign eridx = np.array(...)

```python
eridx = np.array([-1, 5, -1, -1, 2], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

**Verification:**
```python
assert lidx is None
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, eridx)
```

### Step 8: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other_mono, how='left', return_indexers=True)
```

### Step 9: Assign eridx = np.array(...)

```python
eridx = np.array([-1, 3, -1, -1, 5], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.uint64
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

**Verification:**
```python
assert lidx is None
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, eridx)
```

### Step 12: Assign idx = Index(...)

```python
idx = Index(2 ** 63 + np.array([1, 1, 2, 5], dtype='uint64'))
```

### Step 13: Assign idx2 = Index(...)

```python
idx2 = Index(2 ** 63 + np.array([1, 2, 5, 7, 9], dtype='uint64'))
```

### Step 14: Assign unknown = idx2.join(...)

```python
res, lidx, ridx = idx2.join(idx, how='left', return_indexers=True)
```

### Step 15: Assign eres = Index(...)

```python
eres = Index(2 ** 63 + np.array([1, 1, 2, 5, 7, 9], dtype='uint64'))
```

### Step 16: Assign eridx = np.array(...)

```python
eridx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
```

### Step 17: Assign elidx = np.array(...)

```python
elidx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

### Step 19: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

### Step 20: Call tm.assert_numpy_array_equal()

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
res, lidx, ridx = index_large.join(other, how='left', return_indexers=True)
eres = index_large
eridx = np.array([-1, 5, -1, -1, 2], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)
res, lidx, ridx = index_large.join(other_mono, how='left', return_indexers=True)
eridx = np.array([-1, 3, -1, -1, 5], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)
idx = Index(2 ** 63 + np.array([1, 1, 2, 5], dtype='uint64'))
idx2 = Index(2 ** 63 + np.array([1, 2, 5, 7, 9], dtype='uint64'))
res, lidx, ridx = idx2.join(idx, how='left', return_indexers=True)
eres = Index(2 ** 63 + np.array([1, 1, 2, 5, 7, 9], dtype='uint64'))
eridx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
elidx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
```

## Next Steps


---

*Source: test_join.py:238 | Complexity: Advanced | Last updated: 2026-06-02*