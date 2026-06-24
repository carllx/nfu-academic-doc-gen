# How To: Iter Refcount

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test iter refcount

## Prerequisites

**Required Modules:**
- `inspect`
- `subprocess`
- `sys`
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core.umath`
- `numpy`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign a = arange(...)

```python
a = arange(6)
```

**Verification:**
```python
assert_(not it.iterationneedsapi)
```

### Step 2: Assign dt = np.dtype.newbyteorder(...)

```python
dt = np.dtype('f4').newbyteorder()
```

**Verification:**
```python
assert_(sys.getrefcount(a) > rc_a)
```

### Step 3: Assign rc_a = sys.getrefcount(...)

```python
rc_a = sys.getrefcount(a)
```

**Verification:**
```python
assert_(sys.getrefcount(dt) > rc_dt)
```

### Step 4: Assign rc_dt = sys.getrefcount(...)

```python
rc_dt = sys.getrefcount(dt)
```

**Verification:**
```python
assert_equal(sys.getrefcount(a), rc_a)
```

### Step 5: Assign it = None

```python
it = None
```

**Verification:**
```python
assert_equal(sys.getrefcount(dt), rc_dt)
```

### Step 6: Call assert_equal()

```python
assert_equal(sys.getrefcount(a), rc_a)
```

**Verification:**
```python
assert_(sys.getrefcount(a) > rc2_a)
```

### Step 7: Call assert_equal()

```python
assert_equal(sys.getrefcount(dt), rc_dt)
```

**Verification:**
```python
assert_(sys.getrefcount(dt) > rc2_dt)
```

### Step 8: Assign a = arange(...)

```python
a = arange(6, dtype='f4')
```

**Verification:**
```python
assert_equal(sys.getrefcount(a), rc2_a)
```

### Step 9: Assign dt = np.dtype(...)

```python
dt = np.dtype('f4')
```

**Verification:**
```python
assert_equal(sys.getrefcount(dt), rc2_dt)
```

### Step 10: Assign rc_a = sys.getrefcount(...)

```python
rc_a = sys.getrefcount(a)
```

**Verification:**
```python
assert_equal(sys.getrefcount(a), rc_a)
```

### Step 11: Assign rc_dt = sys.getrefcount(...)

```python
rc_dt = sys.getrefcount(dt)
```

**Verification:**
```python
assert_equal(sys.getrefcount(dt), rc_dt)
```

### Step 12: Assign it = nditer(...)

```python
it = nditer(a, [], [['readwrite']], op_dtypes=[dt])
```

### Step 13: Assign rc2_a = sys.getrefcount(...)

```python
rc2_a = sys.getrefcount(a)
```

### Step 14: Assign rc2_dt = sys.getrefcount(...)

```python
rc2_dt = sys.getrefcount(dt)
```

### Step 15: Assign it2 = it.copy(...)

```python
it2 = it.copy()
```

### Step 16: Call assert_()

```python
assert_(sys.getrefcount(a) > rc2_a)
```

### Step 17: Assign it = None

```python
it = None
```

### Step 18: Call assert_equal()

```python
assert_equal(sys.getrefcount(a), rc2_a)
```

### Step 19: Call assert_equal()

```python
assert_equal(sys.getrefcount(dt), rc2_dt)
```

### Step 20: Assign it2 = None

```python
it2 = None
```

### Step 21: Call assert_equal()

```python
assert_equal(sys.getrefcount(a), rc_a)
```

### Step 22: Call assert_equal()

```python
assert_equal(sys.getrefcount(dt), rc_dt)
```

### Step 23: Call assert_()

```python
assert_(not it.iterationneedsapi)
```

### Step 24: Call assert_()

```python
assert_(sys.getrefcount(a) > rc_a)
```

### Step 25: Call assert_()

```python
assert_(sys.getrefcount(dt) > rc_dt)
```

### Step 26: Call assert_()

```python
assert_(sys.getrefcount(dt) > rc2_dt)
```


## Complete Example

```python
# Workflow
a = arange(6)
dt = np.dtype('f4').newbyteorder()
rc_a = sys.getrefcount(a)
rc_dt = sys.getrefcount(dt)
with nditer(a, [], [['readwrite', 'updateifcopy']], casting='unsafe', op_dtypes=[dt]) as it:
    assert_(not it.iterationneedsapi)
    assert_(sys.getrefcount(a) > rc_a)
    assert_(sys.getrefcount(dt) > rc_dt)
it = None
assert_equal(sys.getrefcount(a), rc_a)
assert_equal(sys.getrefcount(dt), rc_dt)
a = arange(6, dtype='f4')
dt = np.dtype('f4')
rc_a = sys.getrefcount(a)
rc_dt = sys.getrefcount(dt)
it = nditer(a, [], [['readwrite']], op_dtypes=[dt])
rc2_a = sys.getrefcount(a)
rc2_dt = sys.getrefcount(dt)
it2 = it.copy()
assert_(sys.getrefcount(a) > rc2_a)
if sys.version_info < (3, 13):
    assert_(sys.getrefcount(dt) > rc2_dt)
it = None
assert_equal(sys.getrefcount(a), rc2_a)
assert_equal(sys.getrefcount(dt), rc2_dt)
it2 = None
assert_equal(sys.getrefcount(a), rc_a)
assert_equal(sys.getrefcount(dt), rc_dt)
```

## Next Steps


---

*Source: test_nditer.py:48 | Complexity: Advanced | Last updated: 2026-06-02*