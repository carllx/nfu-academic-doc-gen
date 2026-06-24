# How To: 3D Fill Nonna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 3d fill nonna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: dtype_fill_out_dtype
```

## Step-by-Step Guide

### Step 1: Assign unknown = dtype_fill_out_dtype

```python
dtype, fill_value, out_dtype = dtype_fill_out_dtype
```

**Verification:**
```python
assert (result[[0, 1, 2], :, :] == data[[2, 1, 0], :, :]).all()
```

### Step 2: Assign data = np.random.default_rng.integers.astype(...)

```python
data = np.random.default_rng(2).integers(0, 2, (5, 4, 3)).astype(dtype)
```

**Verification:**
```python
assert (result[3, :, :] == fill_value).all()
```

### Step 3: Assign indexer = value

```python
indexer = [2, 1, 0, -1]
```

**Verification:**
```python
assert result.dtype == out_dtype
```

### Step 4: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
```

**Verification:**
```python
assert (result[:, [0, 1, 2], :] == data[:, [2, 1, 0], :]).all()
```

### Step 5: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
```

**Verification:**
```python
assert (result[:, 3, :] == fill_value).all()
```

### Step 6: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=2, fill_value=fill_value)
```

**Verification:**
```python
assert result.dtype == out_dtype
```

### Step 7: Assign indexer = value

```python
indexer = [2, 1, 0, 1]
```

**Verification:**
```python
assert (result[:, :, [0, 1, 2]] == data[:, :, [2, 1, 0]]).all()
```

### Step 8: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
```

**Verification:**
```python
assert (result[:, :, 3] == fill_value).all()
```

### Step 9: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
```

**Verification:**
```python
assert result.dtype == out_dtype
```

### Step 10: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, axis=2, fill_value=fill_value)
```

**Verification:**
```python
assert (result[[0, 1, 2, 3], :, :] == data[indexer, :, :]).all()
```


## Complete Example

```python
# Setup
# Fixtures: dtype_fill_out_dtype

# Workflow
dtype, fill_value, out_dtype = dtype_fill_out_dtype
data = np.random.default_rng(2).integers(0, 2, (5, 4, 3)).astype(dtype)
indexer = [2, 1, 0, -1]
result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
assert (result[[0, 1, 2], :, :] == data[[2, 1, 0], :, :]).all()
assert (result[3, :, :] == fill_value).all()
assert result.dtype == out_dtype
result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
assert (result[:, [0, 1, 2], :] == data[:, [2, 1, 0], :]).all()
assert (result[:, 3, :] == fill_value).all()
assert result.dtype == out_dtype
result = algos.take_nd(data, indexer, axis=2, fill_value=fill_value)
assert (result[:, :, [0, 1, 2]] == data[:, :, [2, 1, 0]]).all()
assert (result[:, :, 3] == fill_value).all()
assert result.dtype == out_dtype
indexer = [2, 1, 0, 1]
result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
assert (result[[0, 1, 2, 3], :, :] == data[indexer, :, :]).all()
assert result.dtype == dtype
result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
assert (result[:, [0, 1, 2, 3], :] == data[:, indexer, :]).all()
assert result.dtype == dtype
result = algos.take_nd(data, indexer, axis=2, fill_value=fill_value)
assert (result[:, :, [0, 1, 2, 3]] == data[:, :, indexer]).all()
assert result.dtype == dtype
```

## Next Steps


---

*Source: test_take.py:83 | Complexity: Advanced | Last updated: 2026-06-02*