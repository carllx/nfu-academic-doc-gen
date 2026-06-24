# How To: Addition Reduce Negative Zero

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test addition reduce negative zero

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
# Fixtures: dtype, use_initial
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert _check_neg_zero(res)
```

### Step 2: Assign kwargs = value

```python
kwargs = {}
```

**Verification:**
```python
assert not np.signbit(res.real)
```

### Step 3: Assign neg_zero = dtype.type(...)

```python
neg_zero = dtype.type(complex(-0.0, -0.0))
```

**Verification:**
```python
assert not np.signbit(res.imag)
```

### Step 4: Assign neg_zero = dtype.type(...)

```python
neg_zero = dtype.type(-0.0)
```

### Step 5: Assign unknown = neg_zero

```python
kwargs['initial'] = neg_zero
```

### Step 6: Call pytest.xfail()

```python
pytest.xfail('-0. propagation in sum currently requires initial')
```

### Step 7: Assign arr = np.array(...)

```python
arr = np.array([neg_zero] * i, dtype=dtype)
```

### Step 8: Assign res = np.sum(...)

```python
res = np.sum(arr, **kwargs)
```

**Verification:**
```python
assert _check_neg_zero(res)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, use_initial

# Workflow
dtype = np.dtype(dtype)
if dtype.kind == 'c':
    neg_zero = dtype.type(complex(-0.0, -0.0))
else:
    neg_zero = dtype.type(-0.0)
kwargs = {}
if use_initial:
    kwargs['initial'] = neg_zero
else:
    pytest.xfail('-0. propagation in sum currently requires initial')
for i in range(150):
    arr = np.array([neg_zero] * i, dtype=dtype)
    res = np.sum(arr, **kwargs)
    if i > 0 or use_initial:
        assert _check_neg_zero(res)
    else:
        assert not np.signbit(res.real)
        assert not np.signbit(res.imag)
```

## Next Steps


---

*Source: test_ufunc.py:3126 | Complexity: Advanced | Last updated: 2026-06-02*