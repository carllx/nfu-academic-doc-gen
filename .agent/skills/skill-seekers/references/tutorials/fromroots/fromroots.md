# How To: Fromroots

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fromroots

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
# Fixtures: Poly
```

## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = Poly.domain + random((2,)) * 0.25
```

**Verification:**
```python
assert_equal(p1.degree(), len(r))
```

### Step 2: Assign w = value

```python
w = Poly.window + random((2,)) * 0.25
```

**Verification:**
```python
assert_equal(p1.domain, d)
```

### Step 3: Assign r = random(...)

```python
r = random((5,))
```

**Verification:**
```python
assert_equal(p1.window, w)
```

### Step 4: Assign p1 = Poly.fromroots(...)

```python
p1 = Poly.fromroots(r, domain=d, window=w)
```

**Verification:**
```python
assert_almost_equal(p1(r), 0)
```

### Step 5: Call assert_equal()

```python
assert_equal(p1.degree(), len(r))
```

**Verification:**
```python
assert_almost_equal(p2.coef[-1], 1)
```

### Step 6: Call assert_equal()

```python
assert_equal(p1.domain, d)
```

### Step 7: Call assert_equal()

```python
assert_equal(p1.window, w)
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(p1(r), 0)
```

### Step 9: Assign pdom = value

```python
pdom = Polynomial.domain
```

### Step 10: Assign pwin = value

```python
pwin = Polynomial.window
```

### Step 11: Assign p2 = Polynomial.cast(...)

```python
p2 = Polynomial.cast(p1, domain=pdom, window=pwin)
```

### Step 12: Call assert_almost_equal()

```python
assert_almost_equal(p2.coef[-1], 1)
```


## Complete Example

```python
# Setup
# Fixtures: Poly

# Workflow
d = Poly.domain + random((2,)) * 0.25
w = Poly.window + random((2,)) * 0.25
r = random((5,))
p1 = Poly.fromroots(r, domain=d, window=w)
assert_equal(p1.degree(), len(r))
assert_equal(p1.domain, d)
assert_equal(p1.window, w)
assert_almost_equal(p1(r), 0)
pdom = Polynomial.domain
pwin = Polynomial.window
p2 = Polynomial.cast(p1, domain=pdom, window=pwin)
assert_almost_equal(p2.coef[-1], 1)
```

## Next Steps


---

*Source: test_classes.py:120 | Complexity: Advanced | Last updated: 2026-06-02*