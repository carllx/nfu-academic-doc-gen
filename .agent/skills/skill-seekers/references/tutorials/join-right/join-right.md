# How To: Join Right

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join right

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
assert isinstance(other, Index) and other.dtype == np.uint64
```

### Step 2: Assign other_mono = Index(...)

```python
other_mono = Index(2 ** 63 + np.array([1, 2, 7, 10, 12, 25], dtype='uint64'))
```

**Verification:**
```python
assert ridx is None
```

### Step 3: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other, how='right', return_indexers=True)
```

**Verification:**
```python
assert isinstance(other, Index) and other.dtype == np.uint64
```

### Step 4: Assign eres = other

```python
eres = other
```

**Verification:**
```python
assert ridx is None
```

### Step 5: Assign elidx = np.array(...)

```python
elidx = np.array([-1, -1, 4, -1, -1, 1], dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

**Verification:**
```python
assert isinstance(other, Index) and other.dtype == np.uint64
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

**Verification:**
```python
assert ridx is None
```

### Step 8: Assign unknown = index_large.join(...)

```python
res, lidx, ridx = index_large.join(other_mono, how='right', return_indexers=True)
```

### Step 9: Assign eres = other_mono

```python
eres = other_mono
```

### Step 10: Assign elidx = np.array(...)

```python
elidx = np.array([-1, -1, -1, 1, -1, 4], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(other, Index) and other.dtype == np.uint64
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

**Verification:**
```python
assert ridx is None
```

### Step 13: Assign idx = Index(...)

```python
idx = Index(2 ** 63 + np.array([1, 1, 2, 5], dtype='uint64'))
```

### Step 14: Assign idx2 = Index(...)

```python
idx2 = Index(2 ** 63 + np.array([1, 2, 5, 7, 9], dtype='uint64'))
```

### Step 15: Assign unknown = idx.join(...)

```python
res, lidx, ridx = idx.join(idx2, how='right', return_indexers=True)
```

### Step 16: Assign eres = Index(...)

```python
eres = Index(2 ** 63 + np.array([1, 1, 2, 5, 7, 9], dtype='uint64'))
```

### Step 17: Assign elidx = np.array(...)

```python
elidx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
```

### Step 18: Assign eridx = np.array(...)

```python
eridx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
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
res, lidx, ridx = index_large.join(other, how='right', return_indexers=True)
eres = other
elidx = np.array([-1, -1, 4, -1, -1, 1], dtype=np.intp)
tm.assert_numpy_array_equal(lidx, elidx)
assert isinstance(other, Index) and other.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert ridx is None
res, lidx, ridx = index_large.join(other_mono, how='right', return_indexers=True)
eres = other_mono
elidx = np.array([-1, -1, -1, 1, -1, 4], dtype=np.intp)
assert isinstance(other, Index) and other.dtype == np.uint64
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_index_equal(res, eres)
assert ridx is None
idx = Index(2 ** 63 + np.array([1, 1, 2, 5], dtype='uint64'))
idx2 = Index(2 ** 63 + np.array([1, 2, 5, 7, 9], dtype='uint64'))
res, lidx, ridx = idx.join(idx2, how='right', return_indexers=True)
eres = Index(2 ** 63 + np.array([1, 1, 2, 5, 7, 9], dtype='uint64'))
elidx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
eridx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
```

## Next Steps


---

*Source: test_join.py:275 | Complexity: Advanced | Last updated: 2026-06-02*