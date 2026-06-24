# How To: To Coo

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to coo

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
# Fixtures: colnames
```

## Step-by-Step Guide

### Step 1: Assign sp_sparse = pytest.importorskip(...)

```python
sp_sparse = pytest.importorskip('scipy.sparse')
```

**Verification:**
```python
assert (result != expected).nnz == 0
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({colnames[0]: [0, 1, 0], colnames[1]: [1, 0, 0]}, dtype='Sparse[int64, 0]')
```

### Step 3: Assign result = df.sparse.to_coo(...)

```python
result = df.sparse.to_coo()
```

### Step 4: Assign expected = sp_sparse.coo_matrix(...)

```python
expected = sp_sparse.coo_matrix(np.asarray(df))
```

**Verification:**
```python
assert (result != expected).nnz == 0
```


## Complete Example

```python
# Setup
# Fixtures: colnames

# Workflow
sp_sparse = pytest.importorskip('scipy.sparse')
df = pd.DataFrame({colnames[0]: [0, 1, 0], colnames[1]: [1, 0, 0]}, dtype='Sparse[int64, 0]')
result = df.sparse.to_coo()
expected = sp_sparse.coo_matrix(np.asarray(df))
assert (result != expected).nnz == 0
```

## Next Steps


---

*Source: test_accessor.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*