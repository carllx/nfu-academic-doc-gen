# How To: Laggrid3D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laggrid3d

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.laguerre`
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

### Step 2: Assign unknown = value

```python
y1, y2, y3 = self.y
```

**Verification:**
```python
assert_(res.shape == (2, 3) * 3)
```

### Step 3: Assign tgt = np.einsum(...)

```python
tgt = np.einsum('i,j,k->ijk', y1, y2, y3)
```

### Step 4: Assign res = lag.laggrid3d(...)

```python
res = lag.laggrid3d(x1, x2, x3, self.c3d)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 6: Assign z = np.ones(...)

```python
z = np.ones((2, 3))
```

### Step 7: Assign res = lag.laggrid3d(...)

```python
res = lag.laggrid3d(z, z, z, self.c3d)
```

### Step 8: Call assert_()

```python
assert_(res.shape == (2, 3) * 3)
```


## Complete Example

```python
# Workflow
x1, x2, x3 = self.x
y1, y2, y3 = self.y
tgt = np.einsum('i,j,k->ijk', y1, y2, y3)
res = lag.laggrid3d(x1, x2, x3, self.c3d)
assert_almost_equal(res, tgt)
z = np.ones((2, 3))
res = lag.laggrid3d(z, z, z, self.c3d)
assert_(res.shape == (2, 3) * 3)
```

## Next Steps


---

*Source: test_laguerre.py:186 | Complexity: Advanced | Last updated: 2026-06-02*