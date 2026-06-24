# How To: From Spmatrix

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from spmatrix

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
# Fixtures: format, labels, dtype
```

## Step-by-Step Guide

### Step 1: Assign sp_sparse = pytest.importorskip(...)

```python
sp_sparse = pytest.importorskip('scipy.sparse')
```

### Step 2: Assign sp_dtype = SparseDtype(...)

```python
sp_dtype = SparseDtype(dtype, np.array(0, dtype=dtype).item())
```

### Step 3: Assign mat = sp_sparse.eye(...)

```python
mat = sp_sparse.eye(10, format=format, dtype=dtype)
```

### Step 4: Assign result = pd.DataFrame.sparse.from_spmatrix(...)

```python
result = pd.DataFrame.sparse.from_spmatrix(mat, index=labels, columns=labels)
```

### Step 5: Assign expected = pd.DataFrame.astype(...)

```python
expected = pd.DataFrame(np.eye(10, dtype=dtype), index=labels, columns=labels).astype(sp_dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: format, labels, dtype

# Workflow
sp_sparse = pytest.importorskip('scipy.sparse')
sp_dtype = SparseDtype(dtype, np.array(0, dtype=dtype).item())
mat = sp_sparse.eye(10, format=format, dtype=dtype)
result = pd.DataFrame.sparse.from_spmatrix(mat, index=labels, columns=labels)
expected = pd.DataFrame(np.eye(10, dtype=dtype), index=labels, columns=labels).astype(sp_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_accessor.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*