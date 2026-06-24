# How To: Hermval2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hermval2d

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.hermite`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
x1, x2, x3 = self.x
```

**Verification:**
```python
assert_raises(ValueError, herm.hermval2d, x1, x2[:2], self.c2d)
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
assert_raises(ValueError, herm.hermval2d, x1, x2[:2], self.c2d)
```

**Verification:**
```python
assert_(res.shape == (2, 3))
```

### Step 4: Assign tgt = value

```python
tgt = y1 * y2
```

### Step 5: Assign res = herm.hermval2d(...)

```python
res = herm.hermval2d(x1, x2, self.c2d)
```

### Step 6: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 7: Assign z = np.ones(...)

```python
z = np.ones((2, 3))
```

### Step 8: Assign res = herm.hermval2d(...)

```python
res = herm.hermval2d(z, z, self.c2d)
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
assert_raises(ValueError, herm.hermval2d, x1, x2[:2], self.c2d)
tgt = y1 * y2
res = herm.hermval2d(x1, x2, self.c2d)
assert_almost_equal(res, tgt)
z = np.ones((2, 3))
res = herm.hermval2d(z, z, self.c2d)
assert_(res.shape == (2, 3))
```

## Next Steps


---

*Source: test_hermite.py:141 | Complexity: Advanced | Last updated: 2026-06-02*