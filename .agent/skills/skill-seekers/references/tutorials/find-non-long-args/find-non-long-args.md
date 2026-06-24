# How To: Find Non Long Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test find non long args

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

### Step 1: Assign element = 'abcd'

```python
element = 'abcd'
```

**Verification:**
```python
assert result.dtype == np.dtype('intp')
```

### Step 2: Assign start = dtype(...)

```python
start = dtype(0)
```

**Verification:**
```python
assert result == 0
```

### Step 3: Assign end = dtype(...)

```python
end = dtype(len(element))
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([element])
```

### Step 5: Assign result = np._core.umath.find(...)

```python
result = np._core.umath.find(arr, 'a', start, end)
```

**Verification:**
```python
assert result.dtype == np.dtype('intp')
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
element = 'abcd'
start = dtype(0)
end = dtype(len(element))
arr = np.array([element])
result = np._core.umath.find(arr, 'a', start, end)
assert result.dtype == np.dtype('intp')
assert result == 0
```

## Next Steps


---

*Source: test_ufunc.py:3172 | Complexity: Intermediate | Last updated: 2026-06-02*