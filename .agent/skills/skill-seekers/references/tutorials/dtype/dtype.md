# How To: Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dtype

## Prerequisites

**Required Modules:**
- `sys`
- `sysconfig`
- `weakref`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.ctypeslib`
- `numpy.testing`
- `ctypes`
- `ctypes`
- `ctypes`
- `ctypes`
- `ctypes`


## Step-by-Step Guide

### Step 1: Assign dt = value

```python
dt = np.intc
```

**Verification:**
```python
assert_(p.from_param(np.array([1], dt)))
```

### Step 2: Assign p = ndpointer(...)

```python
p = ndpointer(dtype=dt)
```

**Verification:**
```python
assert_(p.from_param(np.array([1], dt)))
```

### Step 3: Call assert_()

```python
assert_(p.from_param(np.array([1], dt)))
```

**Verification:**
```python
assert_raises(TypeError, p.from_param, np.array([1], dt.newbyteorder('swap')))
```

### Step 4: Assign dt = '<i4'

```python
dt = '<i4'
```

**Verification:**
```python
assert_(p.from_param(np.zeros((10,), dt)))
```

### Step 5: Assign p = ndpointer(...)

```python
p = ndpointer(dtype=dt)
```

**Verification:**
```python
assert_(p.from_param(np.zeros((10,), dt)))
```

### Step 6: Call assert_()

```python
assert_(p.from_param(np.array([1], dt)))
```

**Verification:**
```python
assert_raises(TypeError, p.from_param, np.zeros((10,), dt2))
```

### Step 7: Assign dt = np.dtype(...)

```python
dt = np.dtype('>i4')
```

**Verification:**
```python
assert_(p.from_param(np.zeros((10,), dt2)))
```

### Step 8: Assign p = ndpointer(...)

```python
p = ndpointer(dtype=dt)
```

### Step 9: Call p.from_param()

```python
p.from_param(np.array([1], dt))
```

### Step 10: Call assert_raises()

```python
assert_raises(TypeError, p.from_param, np.array([1], dt.newbyteorder('swap')))
```

### Step 11: Assign dtnames = value

```python
dtnames = ['x', 'y']
```

### Step 12: Assign dtformats = value

```python
dtformats = [np.intc, np.float64]
```

### Step 13: Assign dtdescr = value

```python
dtdescr = {'names': dtnames, 'formats': dtformats}
```

### Step 14: Assign dt = np.dtype(...)

```python
dt = np.dtype(dtdescr)
```

### Step 15: Assign p = ndpointer(...)

```python
p = ndpointer(dtype=dt)
```

### Step 16: Call assert_()

```python
assert_(p.from_param(np.zeros((10,), dt)))
```

### Step 17: Assign samedt = np.dtype(...)

```python
samedt = np.dtype(dtdescr)
```

### Step 18: Assign p = ndpointer(...)

```python
p = ndpointer(dtype=samedt)
```

### Step 19: Call assert_()

```python
assert_(p.from_param(np.zeros((10,), dt)))
```

### Step 20: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype(dtdescr, align=True)
```

### Step 21: Call assert_raises()

```python
assert_raises(TypeError, p.from_param, np.zeros((10,), dt2))
```

### Step 22: Call assert_()

```python
assert_(p.from_param(np.zeros((10,), dt2)))
```


## Complete Example

```python
# Workflow
dt = np.intc
p = ndpointer(dtype=dt)
assert_(p.from_param(np.array([1], dt)))
dt = '<i4'
p = ndpointer(dtype=dt)
assert_(p.from_param(np.array([1], dt)))
dt = np.dtype('>i4')
p = ndpointer(dtype=dt)
p.from_param(np.array([1], dt))
assert_raises(TypeError, p.from_param, np.array([1], dt.newbyteorder('swap')))
dtnames = ['x', 'y']
dtformats = [np.intc, np.float64]
dtdescr = {'names': dtnames, 'formats': dtformats}
dt = np.dtype(dtdescr)
p = ndpointer(dtype=dt)
assert_(p.from_param(np.zeros((10,), dt)))
samedt = np.dtype(dtdescr)
p = ndpointer(dtype=samedt)
assert_(p.from_param(np.zeros((10,), dt)))
dt2 = np.dtype(dtdescr, align=True)
if dt.itemsize != dt2.itemsize:
    assert_raises(TypeError, p.from_param, np.zeros((10,), dt2))
else:
    assert_(p.from_param(np.zeros((10,), dt2)))
```

## Next Steps


---

*Source: test_ctypeslib.py:73 | Complexity: Advanced | Last updated: 2026-06-02*