# How To: Polyint Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polyint axis

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `fractions`
- `functools`
- `pytest`
- `numpy`
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
tgt = np.vstack([poly.polyint(c) for c in c2d.T]).T
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 3: Assign res = poly.polyint(...)

```python
res = poly.polyint(c2d, axis=0)
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 4: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 5: Assign tgt = np.vstack(...)

```python
tgt = np.vstack([poly.polyint(c) for c in c2d])
```

### Step 6: Assign res = poly.polyint(...)

```python
res = poly.polyint(c2d, axis=1)
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 8: Assign tgt = np.vstack(...)

```python
tgt = np.vstack([poly.polyint(c, k=3) for c in c2d])
```

### Step 9: Assign res = poly.polyint(...)

```python
res = poly.polyint(c2d, k=3, axis=1)
```

### Step 10: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```


## Complete Example

```python
# Workflow
c2d = np.random.random((3, 4))
tgt = np.vstack([poly.polyint(c) for c in c2d.T]).T
res = poly.polyint(c2d, axis=0)
assert_almost_equal(res, tgt)
tgt = np.vstack([poly.polyint(c) for c in c2d])
res = poly.polyint(c2d, axis=1)
assert_almost_equal(res, tgt)
tgt = np.vstack([poly.polyint(c, k=3) for c in c2d])
res = poly.polyint(c2d, k=3, axis=1)
assert_almost_equal(res, tgt)
```

## Next Steps


---

*Source: test_polynomial.py:410 | Complexity: Advanced | Last updated: 2026-06-02*