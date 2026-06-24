# How To: Zero Poly Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Regression test for gh-16354.

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: '\n        Regression test for gh-16354.\n        '

```python
'\n        Regression test for gh-16354.\n        '
```

**Verification:**
```python
assert_equal(p.coeffs.dtype, np.int64)
```

### Step 2: Assign z = np.array(...)

```python
z = np.array([0, 0, 0])
```

**Verification:**
```python
assert_equal(p.coeffs.dtype, np.float32)
```

### Step 3: Assign p = np.poly1d(...)

```python
p = np.poly1d(z.astype(np.int64))
```

**Verification:**
```python
assert_equal(p.coeffs.dtype, np.complex64)
```

### Step 4: Call assert_equal()

```python
assert_equal(p.coeffs.dtype, np.int64)
```

### Step 5: Assign p = np.poly1d(...)

```python
p = np.poly1d(z.astype(np.float32))
```

### Step 6: Call assert_equal()

```python
assert_equal(p.coeffs.dtype, np.float32)
```

### Step 7: Assign p = np.poly1d(...)

```python
p = np.poly1d(z.astype(np.complex64))
```

### Step 8: Call assert_equal()

```python
assert_equal(p.coeffs.dtype, np.complex64)
```


## Complete Example

```python
# Workflow
'\n        Regression test for gh-16354.\n        '
z = np.array([0, 0, 0])
p = np.poly1d(z.astype(np.int64))
assert_equal(p.coeffs.dtype, np.int64)
p = np.poly1d(z.astype(np.float32))
assert_equal(p.coeffs.dtype, np.float32)
p = np.poly1d(z.astype(np.complex64))
assert_equal(p.coeffs.dtype, np.complex64)
```

## Next Steps


---

*Source: test_polynomial.py:273 | Complexity: Advanced | Last updated: 2026-06-02*