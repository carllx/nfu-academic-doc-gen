# How To: Legder Axis

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test legder axis

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.legendre`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign c2d = np.random.random(...)

```python
c2d = np.random.random((3, 4))
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 2: Assign tgt = value

```python
tgt = np.vstack([leg.legder(c) for c in c2d.T]).T
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 3: Assign res = leg.legder(...)

```python
res = leg.legder(c2d, axis=0)
```

### Step 4: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 5: Assign tgt = np.vstack(...)

```python
tgt = np.vstack([leg.legder(c) for c in c2d])
```

### Step 6: Assign res = leg.legder(...)

```python
res = leg.legder(c2d, axis=1)
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```


## Complete Example

```python
# Workflow
c2d = np.random.random((3, 4))
tgt = np.vstack([leg.legder(c) for c in c2d.T]).T
res = leg.legder(c2d, axis=0)
assert_almost_equal(res, tgt)
tgt = np.vstack([leg.legder(c) for c in c2d])
res = leg.legder(c2d, axis=1)
assert_almost_equal(res, tgt)
```

## Next Steps


---

*Source: test_legendre.py:337 | Complexity: Intermediate | Last updated: 2026-06-02*