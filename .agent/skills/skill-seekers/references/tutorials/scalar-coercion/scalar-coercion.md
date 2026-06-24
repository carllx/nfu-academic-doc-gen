# How To: Scalar Coercion

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar coercion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: scalar
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array.astype(...)

```python
arr = np.array(scalar, dtype=object).astype(scalar.dtype)
```

**Verification:**
```python
assert_array_equal(arr, arr1)
```

### Step 2: Assign arr1 = np.array.reshape(...)

```python
arr1 = np.array(scalar).reshape(1)
```

**Verification:**
```python
assert_array_equal(arr, arr2)
```

### Step 3: Assign arr2 = np.array(...)

```python
arr2 = np.array([scalar])
```

**Verification:**
```python
assert_array_equal(arr, arr3)
```

### Step 4: Assign arr3 = np.empty(...)

```python
arr3 = np.empty(1, dtype=scalar.dtype)
```

**Verification:**
```python
assert_array_equal(arr, arr4)
```

### Step 5: Assign unknown = scalar

```python
arr3[0] = scalar
```

### Step 6: Assign arr4 = np.empty(...)

```python
arr4 = np.empty(1, dtype=scalar.dtype)
```

### Step 7: Assign unknown = value

```python
arr4[:] = [scalar]
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(arr, arr1)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(arr, arr2)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(arr, arr3)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(arr, arr4)
```

### Step 12: Assign scalar = type(...)

```python
scalar = type(scalar)((scalar * 2) ** 0.5)
```


## Complete Example

```python
# Setup
# Fixtures: scalar

# Workflow
if isinstance(scalar, np.inexact):
    scalar = type(scalar)((scalar * 2) ** 0.5)
arr = np.array(scalar, dtype=object).astype(scalar.dtype)
arr1 = np.array(scalar).reshape(1)
arr2 = np.array([scalar])
arr3 = np.empty(1, dtype=scalar.dtype)
arr3[0] = scalar
arr4 = np.empty(1, dtype=scalar.dtype)
arr4[:] = [scalar]
assert_array_equal(arr, arr1)
assert_array_equal(arr, arr2)
assert_array_equal(arr, arr3)
assert_array_equal(arr, arr4)
```

## Next Steps


---

*Source: test_array_coercion.py:262 | Complexity: Advanced | Last updated: 2026-06-02*