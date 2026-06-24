# How To: 1D Fill Nonna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 1d fill nonna

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
assert (result[[0, 1, 2]] == data[[2, 1, 0]]).all()
```

### Step 2: Assign data = np.random.default_rng.integers.astype(...)

```python
data = np.random.default_rng(2).integers(0, 2, 4).astype(dtype)
```

**Verification:**
```python
assert result[3] == fill_value
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
result = algos.take_nd(data, indexer, fill_value=fill_value)
```

**Verification:**
```python
assert (result[[0, 1, 2, 3]] == data[indexer]).all()
```

### Step 5: Assign indexer = value

```python
indexer = [2, 1, 0, 1]
```

**Verification:**
```python
assert result.dtype == dtype
```

### Step 6: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(data, indexer, fill_value=fill_value)
```

**Verification:**
```python
assert (result[[0, 1, 2, 3]] == data[indexer]).all()
```


## Complete Example

```python
# Setup
# Fixtures: dtype_fill_out_dtype

# Workflow
dtype, fill_value, out_dtype = dtype_fill_out_dtype
data = np.random.default_rng(2).integers(0, 2, 4).astype(dtype)
indexer = [2, 1, 0, -1]
result = algos.take_nd(data, indexer, fill_value=fill_value)
assert (result[[0, 1, 2]] == data[[2, 1, 0]]).all()
assert result[3] == fill_value
assert result.dtype == out_dtype
indexer = [2, 1, 0, 1]
result = algos.take_nd(data, indexer, fill_value=fill_value)
assert (result[[0, 1, 2, 3]] == data[indexer]).all()
assert result.dtype == dtype
```

## Next Steps


---

*Source: test_take.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*