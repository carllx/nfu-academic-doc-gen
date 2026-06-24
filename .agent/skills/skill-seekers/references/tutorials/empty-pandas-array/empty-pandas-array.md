# How To: Empty Pandas Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty pandas array

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = NumpyExtensionArray(...)

```python
arr = NumpyExtensionArray(np.array([1, 2]))
```

**Verification:**
```python
assert isinstance(result, NumpyExtensionArray)
```

### Step 2: Assign dtype = value

```python
dtype = arr.dtype
```

**Verification:**
```python
assert result.dtype == dtype
```

### Step 3: Assign shape = value

```python
shape = (3, 9)
```

**Verification:**
```python
assert result.shape == shape
```

### Step 4: Assign result = NumpyExtensionArray._empty(...)

```python
result = NumpyExtensionArray._empty(shape, dtype=dtype)
```

**Verification:**
```python
assert isinstance(result, NumpyExtensionArray)
```


## Complete Example

```python
# Workflow
arr = NumpyExtensionArray(np.array([1, 2]))
dtype = arr.dtype
shape = (3, 9)
result = NumpyExtensionArray._empty(shape, dtype=dtype)
assert isinstance(result, NumpyExtensionArray)
assert result.dtype == dtype
assert result.shape == shape
```

## Next Steps


---

*Source: test_ndarray_backed.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*