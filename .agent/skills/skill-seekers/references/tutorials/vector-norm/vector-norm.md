# How To: Vector Norm

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test vector norm

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign x = np.arange.reshape(...)

```python
x = np.arange(9).reshape((3, 3))
```

**Verification:**
```python
assert_almost_equal(actual, np.float64(14.2828), double_decimal=3)
```

### Step 2: Assign actual = np.linalg.vector_norm(...)

```python
actual = np.linalg.vector_norm(x)
```

**Verification:**
```python
assert_almost_equal(actual, np.array([6.7082, 8.124, 9.6436]), double_decimal=3)
```

### Step 3: Call assert_almost_equal()

```python
assert_almost_equal(actual, np.float64(14.2828), double_decimal=3)
```

**Verification:**
```python
assert_equal(actual.shape, expected.shape)
```

### Step 4: Assign actual = np.linalg.vector_norm(...)

```python
actual = np.linalg.vector_norm(x, axis=0)
```

**Verification:**
```python
assert_almost_equal(actual, expected, double_decimal=3)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(actual, np.array([6.7082, 8.124, 9.6436]), double_decimal=3)
```

### Step 6: Assign actual = np.linalg.vector_norm(...)

```python
actual = np.linalg.vector_norm(x, keepdims=True)
```

### Step 7: Assign expected = np.full(...)

```python
expected = np.full((1, 1), 14.2828, dtype='float64')
```

### Step 8: Call assert_equal()

```python
assert_equal(actual.shape, expected.shape)
```

### Step 9: Call assert_almost_equal()

```python
assert_almost_equal(actual, expected, double_decimal=3)
```


## Complete Example

```python
# Workflow
x = np.arange(9).reshape((3, 3))
actual = np.linalg.vector_norm(x)
assert_almost_equal(actual, np.float64(14.2828), double_decimal=3)
actual = np.linalg.vector_norm(x, axis=0)
assert_almost_equal(actual, np.array([6.7082, 8.124, 9.6436]), double_decimal=3)
actual = np.linalg.vector_norm(x, keepdims=True)
expected = np.full((1, 1), 14.2828, dtype='float64')
assert_equal(actual.shape, expected.shape)
assert_almost_equal(actual, expected, double_decimal=3)
```

## Next Steps


---

*Source: test_linalg.py:2419 | Complexity: Advanced | Last updated: 2026-06-02*