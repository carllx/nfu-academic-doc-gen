# How To: Addition Negative Zero

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test addition negative zero

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `inspect`
- `itertools`
- `pickle`
- `sys`
- `warnings`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._operand_flag_tests`
- `numpy._core._rational_tests`
- `numpy._core._umath_tests`
- `numpy._core.umath`
- `numpy.linalg._umath_linalg`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy._core._struct_ufunc_tests`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert _check_neg_zero(arr + arr2)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array(neg_zero)
```

**Verification:**
```python
assert _check_neg_zero(arr)
```

### Step 3: Assign arr2 = np.array(...)

```python
arr2 = np.array(neg_zero)
```

**Verification:**
```python
assert _check_neg_zero(arr + arr2)
```

### Step 4: Assign neg_zero = dtype.type(...)

```python
neg_zero = dtype.type(complex(-0.0, -0.0))
```

### Step 5: Assign neg_zero = dtype.type(...)

```python
neg_zero = dtype.type(-0.0)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
dtype = np.dtype(dtype)
if dtype.kind == 'c':
    neg_zero = dtype.type(complex(-0.0, -0.0))
else:
    neg_zero = dtype.type(-0.0)
arr = np.array(neg_zero)
arr2 = np.array(neg_zero)
assert _check_neg_zero(arr + arr2)
arr += arr2
assert _check_neg_zero(arr)
```

## Next Steps


---

*Source: test_ufunc.py:3108 | Complexity: Intermediate | Last updated: 2026-06-02*