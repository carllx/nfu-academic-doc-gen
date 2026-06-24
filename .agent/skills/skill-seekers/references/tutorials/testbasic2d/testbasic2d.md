# How To: Testbasic2D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test testBasic2d

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: s
```

## Step-by-Step Guide

### Step 1: Assign unknown = self._create_data(...)

```python
x, y, _, m1, _, xm, ym, _, _, xf, s = self._create_data()
```

**Verification:**
```python
assert_(not isMaskedArray(x))
```

### Step 2: Assign x.shape = s

```python
x.shape = s
```

**Verification:**
```python
assert_(isMaskedArray(xm))
```

### Step 3: Assign y.shape = s

```python
y.shape = s
```

**Verification:**
```python
assert_equal(shape(xm), s)
```

### Step 4: Assign xm.shape = s

```python
xm.shape = s
```

**Verification:**
```python
assert_equal(xm.shape, s)
```

### Step 5: Assign ym.shape = s

```python
ym.shape = s
```

**Verification:**
```python
assert_equal(xm.size, reduce(lambda x, y: x * y, s))
```

### Step 6: Assign xf.shape = s

```python
xf.shape = s
```

**Verification:**
```python
assert_equal(count(xm), len(m1) - reduce(lambda x, y: x + y, m1))
```

### Step 7: Call assert_()

```python
assert_(not isMaskedArray(x))
```

**Verification:**
```python
assert_(eq(xm, xf))
```

### Step 8: Call assert_()

```python
assert_(isMaskedArray(xm))
```

**Verification:**
```python
assert_(eq(filled(xm, 1e+20), xf))
```

### Step 9: Call assert_equal()

```python
assert_equal(shape(xm), s)
```

**Verification:**
```python
assert_(eq(x, xm))
```

### Step 10: Call assert_equal()

```python
assert_equal(xm.shape, s)
```

### Step 11: Call assert_equal()

```python
assert_equal(xm.size, reduce(lambda x, y: x * y, s))
```

### Step 12: Call assert_equal()

```python
assert_equal(count(xm), len(m1) - reduce(lambda x, y: x + y, m1))
```

### Step 13: Call assert_()

```python
assert_(eq(xm, xf))
```

### Step 14: Call assert_()

```python
assert_(eq(filled(xm, 1e+20), xf))
```

### Step 15: Call assert_()

```python
assert_(eq(x, xm))
```


## Complete Example

```python
# Setup
# Fixtures: s

# Workflow
x, y, _, m1, _, xm, ym, _, _, xf, s = self._create_data()
x.shape = s
y.shape = s
xm.shape = s
ym.shape = s
xf.shape = s
assert_(not isMaskedArray(x))
assert_(isMaskedArray(xm))
assert_equal(shape(xm), s)
assert_equal(xm.shape, s)
assert_equal(xm.size, reduce(lambda x, y: x * y, s))
assert_equal(count(xm), len(m1) - reduce(lambda x, y: x + y, m1))
assert_(eq(xm, xf))
assert_(eq(filled(xm, 1e+20), xf))
assert_(eq(x, xm))
```

## Next Steps


---

*Source: test_old_ma.py:130 | Complexity: Advanced | Last updated: 2026-06-02*