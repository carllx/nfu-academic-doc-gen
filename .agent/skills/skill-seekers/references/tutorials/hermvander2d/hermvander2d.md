# How To: Hermvander2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hermvander2d

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
assert_almost_equal(res, tgt)
```

### Step 2: Assign c = np.random.random(...)

```python
c = np.random.random((2, 3))
```

**Verification:**
```python
assert_(van.shape == (1, 5, 6))
```

### Step 3: Assign van = herm.hermvander2d(...)

```python
van = herm.hermvander2d(x1, x2, [1, 2])
```

### Step 4: Assign tgt = herm.hermval2d(...)

```python
tgt = herm.hermval2d(x1, x2, c)
```

### Step 5: Assign res = np.dot(...)

```python
res = np.dot(van, c.flat)
```

### Step 6: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 7: Assign van = herm.hermvander2d(...)

```python
van = herm.hermvander2d([x1], [x2], [1, 2])
```

### Step 8: Call assert_()

```python
assert_(van.shape == (1, 5, 6))
```


## Complete Example

```python
# Workflow
x1, x2, x3 = self.x
c = np.random.random((2, 3))
van = herm.hermvander2d(x1, x2, [1, 2])
tgt = herm.hermval2d(x1, x2, c)
res = np.dot(van, c.flat)
assert_almost_equal(res, tgt)
van = herm.hermvander2d([x1], [x2], [1, 2])
assert_(van.shape == (1, 5, 6))
```

## Next Steps


---

*Source: test_hermite.py:367 | Complexity: Advanced | Last updated: 2026-06-02*