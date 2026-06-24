# How To: From Coo

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from coo

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign scipy_sparse = pytest.importorskip(...)

```python
scipy_sparse = pytest.importorskip('scipy.sparse')
```

### Step 2: Assign row = value

```python
row = [0, 3, 1, 0]
```

### Step 3: Assign col = value

```python
col = [0, 3, 1, 2]
```

### Step 4: Assign data = value

```python
data = [4, 5, 7, 9]
```

### Step 5: Assign sp_array = scipy_sparse.coo_matrix(...)

```python
sp_array = scipy_sparse.coo_matrix((data, (row, col)))
```

### Step 6: Assign result = pd.Series.sparse.from_coo(...)

```python
result = pd.Series.sparse.from_coo(sp_array)
```

### Step 7: Assign index = pd.MultiIndex.from_arrays(...)

```python
index = pd.MultiIndex.from_arrays([np.array([0, 0, 1, 3], dtype=np.int32), np.array([0, 2, 1, 3], dtype=np.int32)])
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series([4, 9, 7, 5], index=index, dtype='Sparse[int]')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
scipy_sparse = pytest.importorskip('scipy.sparse')
row = [0, 3, 1, 0]
col = [0, 3, 1, 2]
data = [4, 5, 7, 9]
sp_array = scipy_sparse.coo_matrix((data, (row, col)))
result = pd.Series.sparse.from_coo(sp_array)
index = pd.MultiIndex.from_arrays([np.array([0, 0, 1, 3], dtype=np.int32), np.array([0, 2, 1, 3], dtype=np.int32)])
expected = pd.Series([4, 9, 7, 5], index=index, dtype='Sparse[int]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_accessor.py:28 | Complexity: Advanced | Last updated: 2026-06-02*