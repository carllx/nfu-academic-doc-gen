# How To: Cast

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numbers`
- `pytest`
- `numpy`
- `numpy.exceptions`
- `numpy.polynomial`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: Poly1, Poly2
```

## Step-by-Step Guide

### Step 1: Assign x = np.linspace(...)

```python
x = np.linspace(0, 1, 10)
```

**Verification:**
```python
assert_almost_equal(p2.domain, d2)
```

### Step 2: Assign coef = random(...)

```python
coef = random((3,))
```

**Verification:**
```python
assert_almost_equal(p2.window, w2)
```

### Step 3: Assign d1 = value

```python
d1 = Poly1.domain + random((2,)) * 0.25
```

**Verification:**
```python
assert_almost_equal(p2(x), p1(x))
```

### Step 4: Assign w1 = value

```python
w1 = Poly1.window + random((2,)) * 0.25
```

### Step 5: Assign p1 = Poly1(...)

```python
p1 = Poly1(coef, domain=d1, window=w1)
```

### Step 6: Assign d2 = value

```python
d2 = Poly2.domain + random((2,)) * 0.25
```

### Step 7: Assign w2 = value

```python
w2 = Poly2.window + random((2,)) * 0.25
```

### Step 8: Assign p2 = Poly2.cast(...)

```python
p2 = Poly2.cast(p1, domain=d2, window=w2)
```

### Step 9: Call assert_almost_equal()

```python
assert_almost_equal(p2.domain, d2)
```

### Step 10: Call assert_almost_equal()

```python
assert_almost_equal(p2.window, w2)
```

### Step 11: Call assert_almost_equal()

```python
assert_almost_equal(p2(x), p1(x))
```


## Complete Example

```python
# Setup
# Fixtures: Poly1, Poly2

# Workflow
x = np.linspace(0, 1, 10)
coef = random((3,))
d1 = Poly1.domain + random((2,)) * 0.25
w1 = Poly1.window + random((2,)) * 0.25
p1 = Poly1(coef, domain=d1, window=w1)
d2 = Poly2.domain + random((2,)) * 0.25
w2 = Poly2.window + random((2,)) * 0.25
p2 = Poly2.cast(p1, domain=d2, window=w2)
assert_almost_equal(p2.domain, d2)
assert_almost_equal(p2.window, w2)
assert_almost_equal(p2(x), p1(x))
```

## Next Steps


---

*Source: test_classes.py:79 | Complexity: Advanced | Last updated: 2026-06-02*