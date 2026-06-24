# How To: Join Outer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join outer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(range(0, 20, 2), dtype=np.int64)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.int64
```

### Step 2: Assign other = Index(...)

```python
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.int64
```

### Step 3: Assign other_mono = Index(...)

```python
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)
```

### Step 4: Assign unknown = index.join(...)

```python
res, lidx, ridx = index.join(other, how='outer', return_indexers=True)
```

### Step 5: Assign noidx_res = index.join(...)

```python
noidx_res = index.join(other, how='outer')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, noidx_res)
```

### Step 7: Assign eres = Index(...)

```python
eres = Index([0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 25], dtype=np.int64)
```

### Step 8: Assign elidx = np.array(...)

```python
elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
```

### Step 9: Assign eridx = np.array(...)

```python
eridx = np.array([-1, 3, 4, -1, 5, -1, 0, -1, -1, 1, -1, -1, -1, 2], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.int64
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, eres)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, elidx)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, eridx)
```

### Step 13: Assign unknown = index.join(...)

```python
res, lidx, ridx = index.join(other_mono, how='outer', return_indexers=True)
```

### Step 14: Assign noidx_res = index.join(...)

```python
noidx_res = index.join(other_mono, how='outer')
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, noidx_res)
```

### Step 16: Assign elidx = np.array(...)

```python
elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
```

### Step 17: Assign eridx = np.array(...)

```python
eridx = np.array([-1, 0, 1, -1, 2, -1, 3, -1, -1, 4, -1, -1, -1, 5], dtype=np.intp)
```

**Verification:**
```python
assert isinstance(res, Index) and res.dtype == np.int64
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
# Workflow
index = Index(range(0, 20, 2), dtype=np.int64)
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)
res, lidx, ridx = index.join(other, how='outer', return_indexers=True)
noidx_res = index.join(other, how='outer')
tm.assert_index_equal(res, noidx_res)
eres = Index([0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 25], dtype=np.int64)
elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
eridx = np.array([-1, 3, 4, -1, 5, -1, 0, -1, -1, 1, -1, -1, -1, 2], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
res, lidx, ridx = index.join(other_mono, how='outer', return_indexers=True)
noidx_res = index.join(other_mono, how='outer')
tm.assert_index_equal(res, noidx_res)
elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
eridx = np.array([-1, 0, 1, -1, 2, -1, 3, -1, -1, 4, -1, -1, -1, 5], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
```

## Next Steps


---

*Source: test_join.py:156 | Complexity: Advanced | Last updated: 2026-06-02*