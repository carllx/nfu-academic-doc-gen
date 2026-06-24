# How To: Make Block No Pandas Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test make block no pandas array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.internals`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.internals`
- `pandas.core.internals.blocks`

**Setup Required:**
```python
# Fixtures: block_maker
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.arrays.NumpyExtensionArray(...)

```python
arr = pd.arrays.NumpyExtensionArray(np.array([1, 2]))
```

**Verification:**
```python
assert result.dtype.kind in ['i', 'u']
```

### Step 2: Assign result = block_maker(...)

```python
result = block_maker(arr, BlockPlacement(slice(len(arr))), ndim=arr.ndim)
```

**Verification:**
```python
assert result.is_extension is False
```

### Step 3: Assign result = block_maker(...)

```python
result = block_maker(arr, slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim)
```

**Verification:**
```python
assert result.dtype.kind in ['i', 'u']
```

### Step 4: Assign result = block_maker(...)

```python
result = block_maker(arr.to_numpy(), slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim)
```

**Verification:**
```python
assert result.is_extension is False
```


## Complete Example

```python
# Setup
# Fixtures: block_maker

# Workflow
arr = pd.arrays.NumpyExtensionArray(np.array([1, 2]))
result = block_maker(arr, BlockPlacement(slice(len(arr))), ndim=arr.ndim)
assert result.dtype.kind in ['i', 'u']
if block_maker is make_block:
    assert result.is_extension is False
    result = block_maker(arr, slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim)
    assert result.dtype.kind in ['i', 'u']
    assert result.is_extension is False
    result = block_maker(arr.to_numpy(), slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim)
    assert result.dtype.kind in ['i', 'u']
    assert result.is_extension is False
```

## Next Steps


---

*Source: test_internals.py:1399 | Complexity: Intermediate | Last updated: 2026-06-02*