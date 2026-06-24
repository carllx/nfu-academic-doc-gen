# How To: Struct Array Pointer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test struct array pointer

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

### Step 1: Assign Struct3 = value

```python
Struct3 = 3 * Struct
```

**Verification:**
```python
assert_equal(x.dtype, expected.dtype)
```

### Step 2: Assign c_array = unknown(...)

```python
c_array = (2 * Struct3)(Struct3(Struct(a=1), Struct(a=2), Struct(a=3)), Struct3(Struct(a=4), Struct(a=5), Struct(a=6)))
```

**Verification:**
```python
assert_equal(x, expected)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[(1,), (2,), (3,)], [(4,), (5,), (6,)]], dtype=[('a', np.int16)])
```

### Step 4: Call check()

```python
check(as_array(c_array))
```

### Step 5: Call check()

```python
check(as_array(pointer(c_array), shape=()))
```

### Step 6: Call check()

```python
check(as_array(pointer(c_array[0]), shape=(2,)))
```

### Step 7: Call check()

```python
check(as_array(pointer(c_array[0][0]), shape=(2, 3)))
```

### Step 8: Assign _fields_ = value

```python
_fields_ = [('a', c_int16)]
```

### Step 9: Call assert_equal()

```python
assert_equal(x.dtype, expected.dtype)
```

### Step 10: Call assert_equal()

```python
assert_equal(x, expected)
```


## Complete Example

```python
# Workflow
from ctypes import Structure, c_int16, pointer

class Struct(Structure):
    _fields_ = [('a', c_int16)]
Struct3 = 3 * Struct
c_array = (2 * Struct3)(Struct3(Struct(a=1), Struct(a=2), Struct(a=3)), Struct3(Struct(a=4), Struct(a=5), Struct(a=6)))
expected = np.array([[(1,), (2,), (3,)], [(4,), (5,), (6,)]], dtype=[('a', np.int16)])

def check(x):
    assert_equal(x.dtype, expected.dtype)
    assert_equal(x, expected)
check(as_array(c_array))
check(as_array(pointer(c_array), shape=()))
check(as_array(pointer(c_array[0]), shape=(2,)))
check(as_array(pointer(c_array[0][0]), shape=(2, 3)))
```

## Next Steps


---

*Source: test_ctypeslib.py:229 | Complexity: Advanced | Last updated: 2026-06-02*