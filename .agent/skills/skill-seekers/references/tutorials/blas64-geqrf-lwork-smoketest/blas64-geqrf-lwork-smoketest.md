# How To: Blas64 Geqrf Lwork Smoketest

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test blas64 geqrf lwork smoketest

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

### Step 1: Assign dtype = value

```python
dtype = np.float64
```

**Verification:**
```python
assert_equal(results['info'], 0)
```

### Step 2: Assign lapack_routine = value

```python
lapack_routine = np.linalg.lapack_lite.dgeqrf
```

**Verification:**
```python
assert_equal(results['m'], m)
```

### Step 3: Assign m = value

```python
m = 2 ** 32 + 1
```

**Verification:**
```python
assert_equal(results['n'], m)
```

### Step 4: Assign n = value

```python
n = 2 ** 32 + 1
```

**Verification:**
```python
assert_(2 ** 32 < lwork < 2 ** 42)
```

### Step 5: Assign lda = m

```python
lda = m
```

### Step 6: Assign a = np.zeros(...)

```python
a = np.zeros([1, 1], dtype=dtype)
```

### Step 7: Assign work = np.zeros(...)

```python
work = np.zeros([1], dtype=dtype)
```

### Step 8: Assign tau = np.zeros(...)

```python
tau = np.zeros([1], dtype=dtype)
```

### Step 9: Assign results = lapack_routine(...)

```python
results = lapack_routine(m, n, a, lda, tau, work, -1, 0)
```

### Step 10: Call assert_equal()

```python
assert_equal(results['info'], 0)
```

### Step 11: Call assert_equal()

```python
assert_equal(results['m'], m)
```

### Step 12: Call assert_equal()

```python
assert_equal(results['n'], m)
```

### Step 13: Assign lwork = int(...)

```python
lwork = int(work.item())
```

### Step 14: Call assert_()

```python
assert_(2 ** 32 < lwork < 2 ** 42)
```


## Complete Example

```python
# Workflow
dtype = np.float64
lapack_routine = np.linalg.lapack_lite.dgeqrf
m = 2 ** 32 + 1
n = 2 ** 32 + 1
lda = m
a = np.zeros([1, 1], dtype=dtype)
work = np.zeros([1], dtype=dtype)
tau = np.zeros([1], dtype=dtype)
results = lapack_routine(m, n, a, lda, tau, work, -1, 0)
assert_equal(results['info'], 0)
assert_equal(results['m'], m)
assert_equal(results['n'], m)
lwork = int(work.item())
assert_(2 ** 32 < lwork < 2 ** 42)
```

## Next Steps


---

*Source: test_linalg.py:2287 | Complexity: Advanced | Last updated: 2026-06-02*