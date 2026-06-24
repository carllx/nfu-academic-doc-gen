# How To: Block Internal

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test block internal

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind='block')
```

**Verification:**
```python
assert isinstance(idx, BlockIndex)
```

### Step 2: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blocs, np.array([2], dtype=np.int32))
```

**Verification:**
```python
assert idx.npoints == 2
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blengths, np.array([2], dtype=np.int32))
```

**Verification:**
```python
assert isinstance(idx, BlockIndex)
```

### Step 4: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([], dtype=np.int32), kind='block')
```

**Verification:**
```python
assert idx.npoints == 0
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blocs, np.array([], dtype=np.int32))
```

**Verification:**
```python
assert isinstance(idx, BlockIndex)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blengths, np.array([], dtype=np.int32))
```

**Verification:**
```python
assert idx.npoints == 4
```

### Step 7: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind='block')
```

**Verification:**
```python
assert isinstance(idx, BlockIndex)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blocs, np.array([0], dtype=np.int32))
```

**Verification:**
```python
assert idx.npoints == 3
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blengths, np.array([4], dtype=np.int32))
```

### Step 10: Assign idx = make_sparse_index(...)

```python
idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind='block')
```

**Verification:**
```python
assert isinstance(idx, BlockIndex)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blocs, np.array([0, 2], dtype=np.int32))
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.blengths, np.array([1, 2], dtype=np.int32))
```


## Complete Example

```python
# Workflow
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind='block')
assert isinstance(idx, BlockIndex)
assert idx.npoints == 2
tm.assert_numpy_array_equal(idx.blocs, np.array([2], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([2], dtype=np.int32))
idx = make_sparse_index(4, np.array([], dtype=np.int32), kind='block')
assert isinstance(idx, BlockIndex)
assert idx.npoints == 0
tm.assert_numpy_array_equal(idx.blocs, np.array([], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([], dtype=np.int32))
idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind='block')
assert isinstance(idx, BlockIndex)
assert idx.npoints == 4
tm.assert_numpy_array_equal(idx.blocs, np.array([0], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([4], dtype=np.int32))
idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind='block')
assert isinstance(idx, BlockIndex)
assert idx.npoints == 3
tm.assert_numpy_array_equal(idx.blocs, np.array([0, 2], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([1, 2], dtype=np.int32))
```

## Next Steps


---

*Source: test_libsparse.py:360 | Complexity: Advanced | Last updated: 2026-06-02*