# How To: Polyder

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polyder

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

### Step 1: Call assert_raises()

```python
assert_raises(TypeError, poly.polyder, [0], 0.5)
```

**Verification:**
```python
assert_raises(TypeError, poly.polyder, [0], 0.5)
```

### Step 2: Call assert_raises()

```python
assert_raises(ValueError, poly.polyder, [0], -1)
```

**Verification:**
```python
assert_raises(ValueError, poly.polyder, [0], -1)
```

### Step 3: Assign tgt = value

```python
tgt = [0] * i + [1]
```

**Verification:**
```python
assert_equal(trim(res), trim(tgt))
```

### Step 4: Assign res = poly.polyder(...)

```python
res = poly.polyder(tgt, m=0)
```

**Verification:**
```python
assert_almost_equal(trim(res), trim(tgt))
```

### Step 5: Call assert_equal()

```python
assert_equal(trim(res), trim(tgt))
```

**Verification:**
```python
assert_almost_equal(trim(res), trim(tgt))
```

### Step 6: Assign tgt = value

```python
tgt = [0] * i + [1]
```

### Step 7: Assign res = poly.polyder(...)

```python
res = poly.polyder(poly.polyint(tgt, m=j), m=j)
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(trim(res), trim(tgt))
```

### Step 9: Assign tgt = value

```python
tgt = [0] * i + [1]
```

### Step 10: Assign res = poly.polyder(...)

```python
res = poly.polyder(poly.polyint(tgt, m=j, scl=2), m=j, scl=0.5)
```

### Step 11: Call assert_almost_equal()

```python
assert_almost_equal(trim(res), trim(tgt))
```


## Complete Example

```python
# Workflow
assert_raises(TypeError, poly.polyder, [0], 0.5)
assert_raises(ValueError, poly.polyder, [0], -1)
for i in range(5):
    tgt = [0] * i + [1]
    res = poly.polyder(tgt, m=0)
    assert_equal(trim(res), trim(tgt))
for i in range(5):
    for j in range(2, 5):
        tgt = [0] * i + [1]
        res = poly.polyder(poly.polyint(tgt, m=j), m=j)
        assert_almost_equal(trim(res), trim(tgt))
for i in range(5):
    for j in range(2, 5):
        tgt = [0] * i + [1]
        res = poly.polyder(poly.polyint(tgt, m=j, scl=2), m=j, scl=0.5)
        assert_almost_equal(trim(res), trim(tgt))
```

## Next Steps


---

*Source: test_polynomial.py:429 | Complexity: Advanced | Last updated: 2026-06-02*