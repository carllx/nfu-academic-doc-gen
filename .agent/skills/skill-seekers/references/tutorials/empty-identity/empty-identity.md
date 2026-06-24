# How To: Empty Identity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Empty input should put an identity matrix in u or vh 

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

### Step 1: ' Empty input should put an identity matrix in u or vh '

```python
' Empty input should put an identity matrix in u or vh '
```

**Verification:**
```python
assert_equal(u.shape, (4, 4))
```

### Step 2: Assign x = np.empty(...)

```python
x = np.empty((4, 0))
```

**Verification:**
```python
assert_equal(vh.shape, (0, 0))
```

### Step 3: Assign unknown = linalg.svd(...)

```python
u, s, vh = linalg.svd(x, compute_uv=True, hermitian=self.hermitian)
```

**Verification:**
```python
assert_equal(u, np.eye(4))
```

### Step 4: Call assert_equal()

```python
assert_equal(u.shape, (4, 4))
```

**Verification:**
```python
assert_equal(u.shape, (0, 0))
```

### Step 5: Call assert_equal()

```python
assert_equal(vh.shape, (0, 0))
```

**Verification:**
```python
assert_equal(vh.shape, (4, 4))
```

### Step 6: Call assert_equal()

```python
assert_equal(u, np.eye(4))
```

**Verification:**
```python
assert_equal(vh, np.eye(4))
```

### Step 7: Assign x = np.empty(...)

```python
x = np.empty((0, 4))
```

### Step 8: Assign unknown = linalg.svd(...)

```python
u, s, vh = linalg.svd(x, compute_uv=True, hermitian=self.hermitian)
```

### Step 9: Call assert_equal()

```python
assert_equal(u.shape, (0, 0))
```

### Step 10: Call assert_equal()

```python
assert_equal(vh.shape, (4, 4))
```

### Step 11: Call assert_equal()

```python
assert_equal(vh, np.eye(4))
```


## Complete Example

```python
# Workflow
' Empty input should put an identity matrix in u or vh '
x = np.empty((4, 0))
u, s, vh = linalg.svd(x, compute_uv=True, hermitian=self.hermitian)
assert_equal(u.shape, (4, 4))
assert_equal(vh.shape, (0, 0))
assert_equal(u, np.eye(4))
x = np.empty((0, 4))
u, s, vh = linalg.svd(x, compute_uv=True, hermitian=self.hermitian)
assert_equal(u.shape, (0, 0))
assert_equal(vh.shape, (4, 4))
assert_equal(vh, np.eye(4))
```

## Next Steps


---

*Source: test_linalg.py:704 | Complexity: Advanced | Last updated: 2026-06-02*