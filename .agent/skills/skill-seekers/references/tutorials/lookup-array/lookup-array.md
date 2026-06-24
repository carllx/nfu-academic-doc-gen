# How To: Lookup Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test lookup array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind=kind)
```

### Step 2: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, 0], dtype=np.int32)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 5: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
```

### Step 6: Assign exp = np.array(...)

```python
exp = np.array([-1, 0, -1, 1], dtype=np.int32)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 8: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([], dtype=np.int32), kind=kind)
```

### Step 9: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([-1, 0, 2, 4], dtype=np.int32))
```

### Step 10: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, -1, -1], dtype=np.int32)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 12: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind=kind)
```

### Step 13: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
```

### Step 14: Assign exp = np.array(...)

```python
exp = np.array([-1, 0, 2], dtype=np.int32)
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 16: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
```

### Step 17: Assign exp = np.array(...)

```python
exp = np.array([-1, 2, 1, 3], dtype=np.int32)
```

### Step 18: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 19: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind=kind)
```

### Step 20: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([2, 1, 3, 0], dtype=np.int32))
```

### Step 21: Assign exp = np.array(...)

```python
exp = np.array([1, -1, 2, 0], dtype=np.int32)
```

### Step 22: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```

### Step 23: Assign res = idx.lookup_array(...)

```python
res = idx.lookup_array(np.array([1, 4, 2, 5], dtype=np.int32))
```

### Step 24: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, 1, -1], dtype=np.int32)
```

### Step 25: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
exp = np.array([-1, -1, 0], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
exp = np.array([-1, 0, -1, 1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
idx = make_sparse_index(4, np.array([], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([-1, 0, 2, 4], dtype=np.int32))
exp = np.array([-1, -1, -1, -1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
exp = np.array([-1, 0, 2], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
exp = np.array([-1, 2, 1, 3], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([2, 1, 3, 0], dtype=np.int32))
exp = np.array([1, -1, 2, 0], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
res = idx.lookup_array(np.array([1, 4, 2, 5], dtype=np.int32))
exp = np.array([-1, -1, 1, -1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
```

## Next Steps


---

*Source: test_libsparse.py:302 | Complexity: Advanced | Last updated: 2026-06-02*