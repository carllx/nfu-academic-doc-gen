# How To: Lapack Endian

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lapack endian

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = array(...)

```python
a = array([[5.7998084, -2.1825367], [-2.1825367, 9.85910595]], dtype='>f8')
```

**Verification:**
```python
assert_array_equal(ap, bp)
```

### Step 2: Assign b = array(...)

```python
b = array(a, dtype='<f8')
```

### Step 3: Assign ap = linalg.cholesky(...)

```python
ap = linalg.cholesky(a)
```

### Step 4: Assign bp = linalg.cholesky(...)

```python
bp = linalg.cholesky(b)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(ap, bp)
```


## Complete Example

```python
# Workflow
a = array([[5.7998084, -2.1825367], [-2.1825367, 9.85910595]], dtype='>f8')
b = array(a, dtype='<f8')
ap = linalg.cholesky(a)
bp = linalg.cholesky(b)
assert_array_equal(ap, bp)
```

## Next Steps


---

*Source: test_regression.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*