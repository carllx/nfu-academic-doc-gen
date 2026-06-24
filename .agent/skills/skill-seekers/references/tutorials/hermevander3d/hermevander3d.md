# How To: Hermevander3D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hermevander3d

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.hermite_e`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
x1, x2, x3 = self.x
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 2: Assign c = np.random.random(...)

```python
c = np.random.random((2, 3, 4))
```

**Verification:**
```python
assert_(van.shape == (1, 5, 24))
```

### Step 3: Assign van = herme.hermevander3d(...)

```python
van = herme.hermevander3d(x1, x2, x3, [1, 2, 3])
```

### Step 4: Assign tgt = herme.hermeval3d(...)

```python
tgt = herme.hermeval3d(x1, x2, x3, c)
```

### Step 5: Assign res = np.dot(...)

```python
res = np.dot(van, c.flat)
```

### Step 6: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 7: Assign van = herme.hermevander3d(...)

```python
van = herme.hermevander3d([x1], [x2], [x3], [1, 2, 3])
```

### Step 8: Call assert_()

```python
assert_(van.shape == (1, 5, 24))
```


## Complete Example

```python
# Workflow
x1, x2, x3 = self.x
c = np.random.random((2, 3, 4))
van = herme.hermevander3d(x1, x2, x3, [1, 2, 3])
tgt = herme.hermeval3d(x1, x2, x3, c)
res = np.dot(van, c.flat)
assert_almost_equal(res, tgt)
van = herme.hermevander3d([x1], [x2], [x3], [1, 2, 3])
assert_(van.shape == (1, 5, 24))
```

## Next Steps


---

*Source: test_hermite_e.py:381 | Complexity: Advanced | Last updated: 2026-06-02*