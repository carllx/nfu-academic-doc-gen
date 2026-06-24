# How To: Series From Coo

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series from coo

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: dtype, dense_index
```

## Step-by-Step Guide

### Step 1: Assign sp_sparse = pytest.importorskip(...)

```python
sp_sparse = pytest.importorskip('scipy.sparse')
```

### Step 2: Assign A = sp_sparse.eye(...)

```python
A = sp_sparse.eye(3, format='coo', dtype=dtype)
```

### Step 3: Assign result = pd.Series.sparse.from_coo(...)

```python
result = pd.Series.sparse.from_coo(A, dense_index=dense_index)
```

### Step 4: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples([np.array([0, 0], dtype=np.int32), np.array([1, 1], dtype=np.int32), np.array([2, 2], dtype=np.int32)])
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series(SparseArray(np.array([1, 1, 1], dtype=dtype)), index=index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign expected = expected.reindex(...)

```python
expected = expected.reindex(pd.MultiIndex.from_product(index.levels))
```


## Complete Example

```python
# Setup
# Fixtures: dtype, dense_index

# Workflow
sp_sparse = pytest.importorskip('scipy.sparse')
A = sp_sparse.eye(3, format='coo', dtype=dtype)
result = pd.Series.sparse.from_coo(A, dense_index=dense_index)
index = pd.MultiIndex.from_tuples([np.array([0, 0], dtype=np.int32), np.array([1, 1], dtype=np.int32), np.array([2, 2], dtype=np.int32)])
expected = pd.Series(SparseArray(np.array([1, 1, 1], dtype=dtype)), index=index)
if dense_index:
    expected = expected.reindex(pd.MultiIndex.from_product(index.levels))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_accessor.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*