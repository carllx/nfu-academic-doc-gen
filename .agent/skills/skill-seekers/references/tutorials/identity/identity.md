# How To: Identity

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test identity

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
assert_equal(p.domain, d)
```

### Step 2: Assign w = value

```python
w = Poly.window + random((2,)) * 0.25
```

**Verification:**
```python
assert_equal(p.window, w)
```

### Step 3: Assign x = np.linspace(...)

```python
x = np.linspace(d[0], d[1], 11)
```

**Verification:**
```python
assert_almost_equal(p(x), x)
```

### Step 4: Assign p = Poly.identity(...)

```python
p = Poly.identity(domain=d, window=w)
```

### Step 5: Call assert_equal()

```python
assert_equal(p.domain, d)
```

### Step 6: Call assert_equal()

```python
assert_equal(p.window, w)
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(p(x), x)
```


## Complete Example

```python
# Setup
# Fixtures: Poly

# Workflow
d = Poly.domain + random((2,)) * 0.25
w = Poly.window + random((2,)) * 0.25
x = np.linspace(d[0], d[1], 11)
p = Poly.identity(domain=d, window=w)
assert_equal(p.domain, d)
assert_equal(p.window, w)
assert_almost_equal(p(x), x)
```

## Next Steps


---

*Source: test_classes.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*