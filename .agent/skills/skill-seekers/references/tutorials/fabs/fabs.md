# How To: Fabs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fabs

## Prerequisites

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([1 + 0j], dtype=complex)
```

**Verification:**
```python
assert_array_equal(np.abs(x), np.real(x))
```

### Step 2: Call assert_array_equal()

```python
assert_array_equal(np.abs(x), np.real(x))
```

**Verification:**
```python
assert_array_equal(np.abs(x), np.real(x))
```

### Step 3: Assign x = np.array(...)

```python
x = np.array([complex(1, ncu.NZERO)], dtype=complex)
```

**Verification:**
```python
assert_array_equal(np.abs(x), np.real(x))
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(np.abs(x), np.real(x))
```

**Verification:**
```python
assert_array_equal(np.abs(x), np.real(x))
```

### Step 5: Assign x = np.array(...)

```python
x = np.array([complex(np.inf, ncu.NZERO)], dtype=complex)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(np.abs(x), np.real(x))
```

### Step 7: Assign x = np.array(...)

```python
x = np.array([complex(np.nan, ncu.NZERO)], dtype=complex)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(np.abs(x), np.real(x))
```


## Complete Example

```python
# Workflow
x = np.array([1 + 0j], dtype=complex)
assert_array_equal(np.abs(x), np.real(x))
x = np.array([complex(1, ncu.NZERO)], dtype=complex)
assert_array_equal(np.abs(x), np.real(x))
x = np.array([complex(np.inf, ncu.NZERO)], dtype=complex)
assert_array_equal(np.abs(x), np.real(x))
x = np.array([complex(np.nan, ncu.NZERO)], dtype=complex)
assert_array_equal(np.abs(x), np.real(x))
```

## Next Steps


---

*Source: test_umath_complex.py:427 | Complexity: Advanced | Last updated: 2026-06-02*