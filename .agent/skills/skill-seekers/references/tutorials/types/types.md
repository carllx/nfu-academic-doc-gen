# How To: Types

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `os`
- `subprocess`
- `sys`
- `textwrap`
- `threading`
- `traceback`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy.exceptions`
- `numpy.linalg`
- `numpy.linalg._linalg`
- `numpy.testing`
- `numpy.linalg.lapack_lite`
- `resource`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([[1, 0.5], [0.5, 1]], dtype=dtype)
```

**Verification:**
```python
assert_equal(w.dtype, dtype)
```

### Step 2: Assign unknown = np.linalg.eig(...)

```python
w, v = np.linalg.eig(x)
```

**Verification:**
```python
assert_equal(v.dtype, dtype)
```

### Step 3: Call assert_equal()

```python
assert_equal(w.dtype, dtype)
```

**Verification:**
```python
assert_equal(w.dtype, get_complex_dtype(dtype))
```

### Step 4: Call assert_equal()

```python
assert_equal(v.dtype, dtype)
```

**Verification:**
```python
assert_equal(v.dtype, get_complex_dtype(dtype))
```

### Step 5: Assign x = np.array(...)

```python
x = np.array([[1, 0.5], [-1, 1]], dtype=dtype)
```

### Step 6: Assign unknown = np.linalg.eig(...)

```python
w, v = np.linalg.eig(x)
```

### Step 7: Call assert_equal()

```python
assert_equal(w.dtype, get_complex_dtype(dtype))
```

### Step 8: Call assert_equal()

```python
assert_equal(v.dtype, get_complex_dtype(dtype))
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
x = np.array([[1, 0.5], [0.5, 1]], dtype=dtype)
w, v = np.linalg.eig(x)
assert_equal(w.dtype, dtype)
assert_equal(v.dtype, dtype)
x = np.array([[1, 0.5], [-1, 1]], dtype=dtype)
w, v = np.linalg.eig(x)
assert_equal(w.dtype, get_complex_dtype(dtype))
assert_equal(v.dtype, get_complex_dtype(dtype))
```

## Next Steps


---

*Source: test_linalg.py:643 | Complexity: Advanced | Last updated: 2026-06-02*