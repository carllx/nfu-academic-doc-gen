# How To: Vague Return Value

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that vague ndpointer return values do not promote to arrays 

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

### Step 1: ' Test that vague ndpointer return values do not promote to arrays '

```python
' Test that vague ndpointer return values do not promote to arrays '
```

**Verification:**
```python
assert_(isinstance(ret, ptr_type))
```

### Step 2: Assign arr = np.zeros(...)

```python
arr = np.zeros((2, 3))
```

### Step 3: Assign ptr_type = ndpointer(...)

```python
ptr_type = ndpointer(dtype=arr.dtype)
```

### Step 4: Assign c_forward_pointer.restype = ptr_type

```python
c_forward_pointer.restype = ptr_type
```

### Step 5: Assign c_forward_pointer.argtypes = value

```python
c_forward_pointer.argtypes = (ptr_type,)
```

### Step 6: Assign ret = c_forward_pointer(...)

```python
ret = c_forward_pointer(arr)
```

### Step 7: Call assert_()

```python
assert_(isinstance(ret, ptr_type))
```


## Complete Example

```python
# Workflow
' Test that vague ndpointer return values do not promote to arrays '
arr = np.zeros((2, 3))
ptr_type = ndpointer(dtype=arr.dtype)
c_forward_pointer.restype = ptr_type
c_forward_pointer.argtypes = (ptr_type,)
ret = c_forward_pointer(arr)
assert_(isinstance(ret, ptr_type))
```

## Next Steps


---

*Source: test_ctypeslib.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*