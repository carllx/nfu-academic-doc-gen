# How To: Blas64 Dot

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test blas64 dot

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

### Step 1: Assign n = value

```python
n = 2 ** 32
```

**Verification:**
```python
assert_equal(c[0, -1], 1)
```

### Step 2: Assign a = np.zeros(...)

```python
a = np.zeros([1, n], dtype=np.float32)
```

### Step 3: Assign b = np.ones(...)

```python
b = np.ones([1, 1], dtype=np.float32)
```

### Step 4: Assign unknown = 1

```python
a[0, -1] = 1
```

### Step 5: Assign c = np.dot(...)

```python
c = np.dot(b, a)
```

### Step 6: Call assert_equal()

```python
assert_equal(c[0, -1], 1)
```


## Complete Example

```python
# Workflow
n = 2 ** 32
a = np.zeros([1, n], dtype=np.float32)
b = np.ones([1, 1], dtype=np.float32)
a[0, -1] = 1
c = np.dot(b, a)
assert_equal(c[0, -1], 1)
```

## Next Steps


---

*Source: test_linalg.py:2276 | Complexity: Intermediate | Last updated: 2026-06-02*