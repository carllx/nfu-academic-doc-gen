# How To: Integers To Negative Integer Power

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integers to negative integer power

## Prerequisites

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign exp = value

```python
exp = [np.array(-1, dt)[()] for dt in 'bhilq']
```

**Verification:**
```python
assert_raises(ValueError, operator.pow, i1, i2)
```

### Step 2: Assign base = value

```python
base = [np.array(1, dt)[()] for dt in 'bhilqBHILQ']
```

**Verification:**
```python
assert_(res.dtype.type is np.float64)
```

### Step 3: Assign base = value

```python
base = [np.array(-1, dt)[()] for dt in 'bhilq']
```

**Verification:**
```python
assert_almost_equal(res, 1.0)
```

### Step 4: Assign base = value

```python
base = [np.array(2, dt)[()] for dt in 'bhilqBHILQ']
```

**Verification:**
```python
assert_raises(ValueError, operator.pow, i1, i2)
```

### Step 5: Call assert_raises()

```python
assert_raises(ValueError, operator.pow, i1, i2)
```

**Verification:**
```python
assert_(res.dtype.type is np.float64)
```

### Step 6: Assign res = operator.pow(...)

```python
res = operator.pow(i1, i2)
```

**Verification:**
```python
assert_almost_equal(res, -1.0)
```

### Step 7: Call assert_()

```python
assert_(res.dtype.type is np.float64)
```

**Verification:**
```python
assert_raises(ValueError, operator.pow, i1, i2)
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(res, 1.0)
```

**Verification:**
```python
assert_(res.dtype.type is np.float64)
```

### Step 9: Call assert_raises()

```python
assert_raises(ValueError, operator.pow, i1, i2)
```

**Verification:**
```python
assert_almost_equal(res, 0.5)
```

### Step 10: Assign res = operator.pow(...)

```python
res = operator.pow(i1, i2)
```

### Step 11: Call assert_()

```python
assert_(res.dtype.type is np.float64)
```

### Step 12: Call assert_almost_equal()

```python
assert_almost_equal(res, -1.0)
```

### Step 13: Call assert_raises()

```python
assert_raises(ValueError, operator.pow, i1, i2)
```

### Step 14: Assign res = operator.pow(...)

```python
res = operator.pow(i1, i2)
```

### Step 15: Call assert_()

```python
assert_(res.dtype.type is np.float64)
```

### Step 16: Call assert_almost_equal()

```python
assert_almost_equal(res, 0.5)
```


## Complete Example

```python
# Workflow
exp = [np.array(-1, dt)[()] for dt in 'bhilq']
base = [np.array(1, dt)[()] for dt in 'bhilqBHILQ']
for i1, i2 in itertools.product(base, exp):
    if i1.dtype != np.uint64:
        assert_raises(ValueError, operator.pow, i1, i2)
    else:
        res = operator.pow(i1, i2)
        assert_(res.dtype.type is np.float64)
        assert_almost_equal(res, 1.0)
base = [np.array(-1, dt)[()] for dt in 'bhilq']
for i1, i2 in itertools.product(base, exp):
    if i1.dtype != np.uint64:
        assert_raises(ValueError, operator.pow, i1, i2)
    else:
        res = operator.pow(i1, i2)
        assert_(res.dtype.type is np.float64)
        assert_almost_equal(res, -1.0)
base = [np.array(2, dt)[()] for dt in 'bhilqBHILQ']
for i1, i2 in itertools.product(base, exp):
    if i1.dtype != np.uint64:
        assert_raises(ValueError, operator.pow, i1, i2)
    else:
        res = operator.pow(i1, i2)
        assert_(res.dtype.type is np.float64)
        assert_almost_equal(res, 0.5)
```

## Next Steps


---

*Source: test_scalarmath.py:223 | Complexity: Advanced | Last updated: 2026-06-02*