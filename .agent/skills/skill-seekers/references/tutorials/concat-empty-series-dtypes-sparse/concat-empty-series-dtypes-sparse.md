# How To: Concat Empty Series Dtypes Sparse

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty series dtypes sparse

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = concat(...)

```python
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64').astype('Sparse')])
```

**Verification:**
```python
assert result.dtype == 'Sparse[float64]'
```

### Step 2: Assign result = concat(...)

```python
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64')])
```

**Verification:**
```python
assert result.dtype == expected
```

### Step 3: Assign expected = pd.SparseDtype(...)

```python
expected = pd.SparseDtype(np.float64)
```

**Verification:**
```python
assert result.dtype == expected
```

### Step 4: Assign result = concat(...)

```python
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='object')])
```

### Step 5: Assign expected = pd.SparseDtype(...)

```python
expected = pd.SparseDtype('object')
```

**Verification:**
```python
assert result.dtype == expected
```


## Complete Example

```python
# Workflow
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64').astype('Sparse')])
assert result.dtype == 'Sparse[float64]'
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64')])
expected = pd.SparseDtype(np.float64)
assert result.dtype == expected
result = concat([Series(dtype='float64').astype('Sparse'), Series(dtype='object')])
expected = pd.SparseDtype('object')
assert result.dtype == expected
```

## Next Steps


---

*Source: test_empty.py:198 | Complexity: Intermediate | Last updated: 2026-06-02*