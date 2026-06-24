# How To: Legval3D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test legval3d

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.legendre`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
x1, x2, x3 = self.x
```

**Verification:**
```python
assert_raises(ValueError, leg.legval3d, x1, x2, x3[:2], self.c3d)
```

### Step 2: Assign unknown = value

```python
y1, y2, y3 = self.y
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 3: Call assert_raises()

```python
assert_raises(ValueError, leg.legval3d, x1, x2, x3[:2], self.c3d)
```

**Verification:**
```python
assert_(res.shape == (2, 3))
```

### Step 4: Assign tgt = value

```python
tgt = y1 * y2 * y3
```

### Step 5: Assign res = leg.legval3d(...)

```python
res = leg.legval3d(x1, x2, x3, self.c3d)
```

### Step 6: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 7: Assign z = np.ones(...)

```python
z = np.ones((2, 3))
```

### Step 8: Assign res = leg.legval3d(...)

```python
res = leg.legval3d(z, z, z, self.c3d)
```

### Step 9: Call assert_()

```python
assert_(res.shape == (2, 3))
```


## Complete Example

```python
# Workflow
x1, x2, x3 = self.x
y1, y2, y3 = self.y
assert_raises(ValueError, leg.legval3d, x1, x2, x3[:2], self.c3d)
tgt = y1 * y2 * y3
res = leg.legval3d(x1, x2, x3, self.c3d)
assert_almost_equal(res, tgt)
z = np.ones((2, 3))
res = leg.legval3d(z, z, z, self.c3d)
assert_(res.shape == (2, 3))
```

## Next Steps


---

*Source: test_legendre.py:159 | Complexity: Advanced | Last updated: 2026-06-02*