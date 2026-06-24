# How To: Zeroresize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zeroresize

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `math`
- `platform`
- `sys`
- `warnings`
- `decimal`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core._rational_tests`
- `numpy._core.numerictypes`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `fractions`
- `numbers`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign A = np.array(...)

```python
A = np.array([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_array_equal(Ar, np.array([]))
```

### Step 2: Assign Ar = np.resize(...)

```python
Ar = np.resize(A, (0,))
```

**Verification:**
```python
assert_equal(A.dtype, Ar.dtype)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(Ar, np.array([]))
```

**Verification:**
```python
assert_equal(Ar.shape, (0, 2))
```

### Step 4: Call assert_equal()

```python
assert_equal(A.dtype, Ar.dtype)
```

**Verification:**
```python
assert_equal(Ar.shape, (2, 0))
```

### Step 5: Assign Ar = np.resize(...)

```python
Ar = np.resize(A, (0, 2))
```

### Step 6: Call assert_equal()

```python
assert_equal(Ar.shape, (0, 2))
```

### Step 7: Assign Ar = np.resize(...)

```python
Ar = np.resize(A, (2, 0))
```

### Step 8: Call assert_equal()

```python
assert_equal(Ar.shape, (2, 0))
```


## Complete Example

```python
# Workflow
A = np.array([[1, 2], [3, 4]])
Ar = np.resize(A, (0,))
assert_array_equal(Ar, np.array([]))
assert_equal(A.dtype, Ar.dtype)
Ar = np.resize(A, (0, 2))
assert_equal(Ar.shape, (0, 2))
Ar = np.resize(A, (2, 0))
assert_equal(Ar.shape, (2, 0))
```

## Next Steps


---

*Source: test_numeric.py:58 | Complexity: Advanced | Last updated: 2026-06-02*