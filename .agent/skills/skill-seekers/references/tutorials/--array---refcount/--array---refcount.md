# How To:   Array   Refcount

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test   array   refcount

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core._rational_tests`
- `numpy.lib`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype(np.int32)
```

**Verification:**
```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 2: Assign old_refcount = sys.getrefcount(...)

```python
old_refcount = sys.getrefcount(dt)
```

**Verification:**
```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 3: Call np.array()

```python
np.array(MyArray(dt))
```

**Verification:**
```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 4: Call assert_equal()

```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

**Verification:**
```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 5: Call np.array()

```python
np.array(MyArray(dt), dtype=dt)
```

**Verification:**
```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 6: Call assert_equal()

```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

**Verification:**
```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 7: Call np.array()

```python
np.array(MyArray(dt), copy=None)
```

**Verification:**
```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 8: Call assert_equal()

```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 9: Call np.array()

```python
np.array(MyArray(dt), dtype=dt, copy=None)
```

### Step 10: Call assert_equal()

```python
assert_equal(old_refcount, sys.getrefcount(dt))
```

### Step 11: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype(np.int16)
```

### Step 12: Assign old_refcount2 = sys.getrefcount(...)

```python
old_refcount2 = sys.getrefcount(dt2)
```

### Step 13: Call np.array()

```python
np.array(MyArray(dt), dtype=dt2)
```

### Step 14: Call assert_equal()

```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 15: Call np.array()

```python
np.array(MyArray(dt), dtype=dt2, copy=None)
```

### Step 16: Call assert_equal()

```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 17: Call assert_equal()

```python
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

### Step 18: Call np.array()

```python
np.array(MyArray(dt), dtype=dt2, copy=False)
```

### Step 19: Assign self.val = np.array(...)

```python
self.val = np.array(-1, dtype=dtype)
```


## Complete Example

```python
# Workflow
class MyArray:

    def __init__(self, dtype):
        self.val = np.array(-1, dtype=dtype)

    def __array__(self, dtype=None, copy=None):
        return self.val.__array__(dtype=dtype, copy=copy)
dt = np.dtype(np.int32)
old_refcount = sys.getrefcount(dt)
np.array(MyArray(dt))
assert_equal(old_refcount, sys.getrefcount(dt))
np.array(MyArray(dt), dtype=dt)
assert_equal(old_refcount, sys.getrefcount(dt))
np.array(MyArray(dt), copy=None)
assert_equal(old_refcount, sys.getrefcount(dt))
np.array(MyArray(dt), dtype=dt, copy=None)
assert_equal(old_refcount, sys.getrefcount(dt))
dt2 = np.dtype(np.int16)
old_refcount2 = sys.getrefcount(dt2)
np.array(MyArray(dt), dtype=dt2)
assert_equal(old_refcount2, sys.getrefcount(dt2))
np.array(MyArray(dt), dtype=dt2, copy=None)
assert_equal(old_refcount2, sys.getrefcount(dt2))
with pytest.raises(ValueError):
    np.array(MyArray(dt), dtype=dt2, copy=False)
assert_equal(old_refcount2, sys.getrefcount(dt2))
```

## Next Steps


---

*Source: test_api.py:162 | Complexity: Advanced | Last updated: 2026-06-02*