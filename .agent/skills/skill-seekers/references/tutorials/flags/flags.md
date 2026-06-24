# How To: Flags

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flags

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

### Step 1: Assign x = np.array(...)

```python
x = np.array([[1, 2], [3, 4]], order='F')
```

**Verification:**
```python
assert_(p.from_param(x))
```

### Step 2: Assign p = ndpointer(...)

```python
p = ndpointer(flags='FORTRAN')
```

**Verification:**
```python
assert_raises(TypeError, p.from_param, x)
```

### Step 3: Call assert_()

```python
assert_(p.from_param(x))
```

**Verification:**
```python
assert_(p.from_param(x))
```

### Step 4: Assign p = ndpointer(...)

```python
p = ndpointer(flags='CONTIGUOUS')
```

**Verification:**
```python
assert_raises(TypeError, p.from_param, np.array([[1, 2], [3, 4]]))
```

### Step 5: Call assert_raises()

```python
assert_raises(TypeError, p.from_param, x)
```

### Step 6: Assign p = ndpointer(...)

```python
p = ndpointer(flags=x.flags.num)
```

### Step 7: Call assert_()

```python
assert_(p.from_param(x))
```

### Step 8: Call assert_raises()

```python
assert_raises(TypeError, p.from_param, np.array([[1, 2], [3, 4]]))
```


## Complete Example

```python
# Workflow
x = np.array([[1, 2], [3, 4]], order='F')
p = ndpointer(flags='FORTRAN')
assert_(p.from_param(x))
p = ndpointer(flags='CONTIGUOUS')
assert_raises(TypeError, p.from_param, x)
p = ndpointer(flags=x.flags.num)
assert_(p.from_param(x))
assert_raises(TypeError, p.from_param, np.array([[1, 2], [3, 4]]))
```

## Next Steps


---

*Source: test_ctypeslib.py:117 | Complexity: Advanced | Last updated: 2026-06-02*