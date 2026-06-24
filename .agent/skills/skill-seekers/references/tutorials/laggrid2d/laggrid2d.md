# How To: Laggrid2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laggrid2d

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
assert_(res.shape == (2, 3) * 2)
```

### Step 3: Assign tgt = np.einsum(...)

```python
tgt = np.einsum('i,j->ij', y1, y2)
```

### Step 4: Assign res = lag.laggrid2d(...)

```python
res = lag.laggrid2d(x1, x2, self.c2d)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 6: Assign z = np.ones(...)

```python
z = np.ones((2, 3))
```

### Step 7: Assign res = lag.laggrid2d(...)

```python
res = lag.laggrid2d(z, z, self.c2d)
```

### Step 8: Call assert_()

```python
assert_(res.shape == (2, 3) * 2)
```


## Complete Example

```python
# Workflow
x1, x2, x3 = self.x
y1, y2, y3 = self.y
tgt = np.einsum('i,j->ij', y1, y2)
res = lag.laggrid2d(x1, x2, self.c2d)
assert_almost_equal(res, tgt)
z = np.ones((2, 3))
res = lag.laggrid2d(z, z, self.c2d)
assert_(res.shape == (2, 3) * 2)
```

## Next Steps


---

*Source: test_laguerre.py:172 | Complexity: Advanced | Last updated: 2026-06-02*