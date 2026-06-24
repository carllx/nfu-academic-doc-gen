# How To: Cross

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cross

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
assert_equal(actual, expected)
```

### Step 2: Assign actual = np.linalg.cross(...)

```python
actual = np.linalg.cross(x, x + 1)
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]])
```

### Step 4: Call assert_equal()

```python
assert_equal(actual, expected)
```

### Step 5: Assign u = value

```python
u = [1, 2, 3]
```

### Step 6: Assign v = value

```python
v = [4, 5, 6]
```

### Step 7: Assign actual = np.linalg.cross(...)

```python
actual = np.linalg.cross(u, v)
```

### Step 8: Assign expected = array(...)

```python
expected = array([-3, 6, -3])
```

### Step 9: Call assert_equal()

```python
assert_equal(actual, expected)
```

### Step 10: Assign x_2dim = value

```python
x_2dim = x[:, 1:]
```

### Step 11: Call np.linalg.cross()

```python
np.linalg.cross(x_2dim, x_2dim)
```


## Complete Example

```python
# Workflow
x = np.arange(9).reshape((3, 3))
actual = np.linalg.cross(x, x + 1)
expected = np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]])
assert_equal(actual, expected)
u = [1, 2, 3]
v = [4, 5, 6]
actual = np.linalg.cross(u, v)
expected = array([-3, 6, -3])
assert_equal(actual, expected)
with assert_raises_regex(ValueError, 'input arrays must be \\(arrays of\\) 3-dimensional vectors'):
    x_2dim = x[:, 1:]
    np.linalg.cross(x_2dim, x_2dim)
```

## Next Steps


---

*Source: test_linalg.py:2340 | Complexity: Advanced | Last updated: 2026-06-02*