# How To: Return

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that return values are coerced to arrays 

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: dt
```

## Step-by-Step Guide

### Step 1: ' Test that return values are coerced to arrays '

```python
' Test that return values are coerced to arrays '
```

**Verification:**
```python
assert_equal(arr2.dtype, arr.dtype)
```

### Step 2: Assign arr = np.zeros(...)

```python
arr = np.zeros((2, 3), dt)
```

**Verification:**
```python
assert_equal(arr2.shape, arr.shape)
```

### Step 3: Assign ptr_type = ndpointer(...)

```python
ptr_type = ndpointer(shape=arr.shape, dtype=arr.dtype)
```

**Verification:**
```python
assert_equal(arr2.__array_interface__['data'], arr.__array_interface__['data'])
```

### Step 4: Assign c_forward_pointer.restype = ptr_type

```python
c_forward_pointer.restype = ptr_type
```

### Step 5: Assign c_forward_pointer.argtypes = value

```python
c_forward_pointer.argtypes = (ptr_type,)
```

### Step 6: Assign arr2 = c_forward_pointer(...)

```python
arr2 = c_forward_pointer(arr)
```

### Step 7: Call assert_equal()

```python
assert_equal(arr2.dtype, arr.dtype)
```

### Step 8: Call assert_equal()

```python
assert_equal(arr2.shape, arr.shape)
```

### Step 9: Call assert_equal()

```python
assert_equal(arr2.__array_interface__['data'], arr.__array_interface__['data'])
```


## Complete Example

```python
# Setup
# Fixtures: dt

# Workflow
' Test that return values are coerced to arrays '
arr = np.zeros((2, 3), dt)
ptr_type = ndpointer(shape=arr.shape, dtype=arr.dtype)
c_forward_pointer.restype = ptr_type
c_forward_pointer.argtypes = (ptr_type,)
arr2 = c_forward_pointer(arr)
assert_equal(arr2.dtype, arr.dtype)
assert_equal(arr2.shape, arr.shape)
assert_equal(arr2.__array_interface__['data'], arr.__array_interface__['data'])
```

## Next Steps


---

*Source: test_ctypeslib.py:165 | Complexity: Advanced | Last updated: 2026-06-02*