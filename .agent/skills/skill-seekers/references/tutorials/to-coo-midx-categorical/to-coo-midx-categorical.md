# How To: To Coo Midx Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to coo midx categorical

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

### Step 1: Assign sp_sparse = pytest.importorskip(...)

```python
sp_sparse = pytest.importorskip('scipy.sparse')
```

**Verification:**
```python
assert (result != expected).nnz == 0
```

### Step 2: Assign midx = pd.MultiIndex.from_arrays(...)

```python
midx = pd.MultiIndex.from_arrays([pd.CategoricalIndex(list('ab'), name='x'), pd.CategoricalIndex([0, 1], name='y')])
```

### Step 3: Assign ser = pd.Series(...)

```python
ser = pd.Series(1, index=midx, dtype='Sparse[int]')
```

### Step 4: Assign result = value

```python
result = ser.sparse.to_coo(row_levels=['x'], column_levels=['y'])[0]
```

### Step 5: Assign expected = sp_sparse.coo_matrix(...)

```python
expected = sp_sparse.coo_matrix((np.array([1, 1]), (np.array([0, 1]), np.array([0, 1]))), shape=(2, 2))
```

**Verification:**
```python
assert (result != expected).nnz == 0
```


## Complete Example

```python
# Workflow
sp_sparse = pytest.importorskip('scipy.sparse')
midx = pd.MultiIndex.from_arrays([pd.CategoricalIndex(list('ab'), name='x'), pd.CategoricalIndex([0, 1], name='y')])
ser = pd.Series(1, index=midx, dtype='Sparse[int]')
result = ser.sparse.to_coo(row_levels=['x'], column_levels=['y'])[0]
expected = sp_sparse.coo_matrix((np.array([1, 1]), (np.array([0, 1]), np.array([0, 1]))), shape=(2, 2))
assert (result != expected).nnz == 0
```

## Next Steps


---

*Source: test_accessor.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*