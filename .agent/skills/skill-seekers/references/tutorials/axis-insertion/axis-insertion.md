# How To: Axis Insertion

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test axis insertion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.random`
- `numpy.random`
- `numpy.random`

**Setup Required:**
```python
# Fixtures: cls
```

## Step-by-Step Guide

### Step 1: Assign a2d = np.arange.reshape(...)

```python
a2d = np.arange(6 * 3).reshape((6, 3))
```

**Verification:**
```python
assert_equal(x.ndim, 1)
```

### Step 2: Assign actual = apply_along_axis(...)

```python
actual = apply_along_axis(f1to2, 0, a2d)
```

**Verification:**
```python
assert_equal(type(actual), type(expected))
```

### Step 3: Assign expected = np.stack.view(...)

```python
expected = np.stack([f1to2(a2d[:, i]) for i in range(a2d.shape[1])], axis=-1).view(cls)
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 4: Call assert_equal()

```python
assert_equal(type(actual), type(expected))
```

**Verification:**
```python
assert_equal(type(actual), type(expected))
```

### Step 5: Call assert_equal()

```python
assert_equal(actual, expected)
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 6: Assign actual = apply_along_axis(...)

```python
actual = apply_along_axis(f1to2, 1, a2d)
```

**Verification:**
```python
assert_equal(type(actual), type(expected))
```

### Step 7: Assign expected = np.stack.view(...)

```python
expected = np.stack([f1to2(a2d[i, :]) for i in range(a2d.shape[0])], axis=0).view(cls)
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 8: Call assert_equal()

```python
assert_equal(type(actual), type(expected))
```

### Step 9: Call assert_equal()

```python
assert_equal(actual, expected)
```

### Step 10: Assign a3d = np.arange.reshape(...)

```python
a3d = np.arange(6 * 5 * 3).reshape((6, 5, 3))
```

### Step 11: Assign actual = apply_along_axis(...)

```python
actual = apply_along_axis(f1to2, 1, a3d)
```

### Step 12: Assign expected = np.stack.view(...)

```python
expected = np.stack([np.stack([f1to2(a3d[i, :, j]) for i in range(a3d.shape[0])], axis=0) for j in range(a3d.shape[2])], axis=-1).view(cls)
```

### Step 13: Call assert_equal()

```python
assert_equal(type(actual), type(expected))
```

### Step 14: Call assert_equal()

```python
assert_equal(actual, expected)
```

### Step 15: """produces an asymmetric non-square matrix from x"""

```python
"""produces an asymmetric non-square matrix from x"""
```

### Step 16: Call assert_equal()

```python
assert_equal(x.ndim, 1)
```


## Complete Example

```python
# Setup
# Fixtures: cls

# Workflow
def f1to2(x):
    """produces an asymmetric non-square matrix from x"""
    assert_equal(x.ndim, 1)
    return (x[::-1] * x[1:, None]).view(cls)
a2d = np.arange(6 * 3).reshape((6, 3))
actual = apply_along_axis(f1to2, 0, a2d)
expected = np.stack([f1to2(a2d[:, i]) for i in range(a2d.shape[1])], axis=-1).view(cls)
assert_equal(type(actual), type(expected))
assert_equal(actual, expected)
actual = apply_along_axis(f1to2, 1, a2d)
expected = np.stack([f1to2(a2d[i, :]) for i in range(a2d.shape[0])], axis=0).view(cls)
assert_equal(type(actual), type(expected))
assert_equal(actual, expected)
a3d = np.arange(6 * 5 * 3).reshape((6, 5, 3))
actual = apply_along_axis(f1to2, 1, a3d)
expected = np.stack([np.stack([f1to2(a3d[i, :, j]) for i in range(a3d.shape[0])], axis=0) for j in range(a3d.shape[2])], axis=-1).view(cls)
assert_equal(type(actual), type(expected))
assert_equal(actual, expected)
```

## Next Steps


---

*Source: test_shape_base.py:203 | Complexity: Advanced | Last updated: 2026-06-02*