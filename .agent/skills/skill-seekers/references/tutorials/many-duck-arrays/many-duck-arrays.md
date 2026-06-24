# How To: Many Duck Arrays

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test many duck arrays

## Prerequisites

**Required Modules:**
- `inspect`
- `os`
- `pickle`
- `sys`
- `tempfile`
- `io`
- `unittest`
- `pytest`
- `numpy`
- `numpy._core.overrides`
- `numpy.testing`
- `numpy.testing.overrides`


## Step-by-Step Guide

### Step 1: Assign a = A(...)

```python
a = A()
```

**Verification:**
```python
assert_equal(_get_implementing_args([1]), [])
```

### Step 2: Assign b = B(...)

```python
b = B()
```

**Verification:**
```python
assert_equal(_get_implementing_args([a]), [a])
```

### Step 3: Assign c = C(...)

```python
c = C()
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, 1]), [a])
```

### Step 4: Assign d = D(...)

```python
d = D()
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, a, a]), [a])
```

### Step 5: Call assert_equal()

```python
assert_equal(_get_implementing_args([1]), [])
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, d, a]), [a, d])
```

### Step 6: Call assert_equal()

```python
assert_equal(_get_implementing_args([a]), [a])
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, b]), [b, a])
```

### Step 7: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, 1]), [a])
```

**Verification:**
```python
assert_equal(_get_implementing_args([b, a]), [b, a])
```

### Step 8: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, a, a]), [a])
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, b, c]), [b, c, a])
```

### Step 9: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, d, a]), [a, d])
```

**Verification:**
```python
assert_equal(_get_implementing_args([a, c, b]), [c, b, a])
```

### Step 10: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, b]), [b, a])
```

### Step 11: Call assert_equal()

```python
assert_equal(_get_implementing_args([b, a]), [b, a])
```

### Step 12: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, b, c]), [b, c, a])
```

### Step 13: Call assert_equal()

```python
assert_equal(_get_implementing_args([a, c, b]), [c, b, a])
```

### Step 14: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```

### Step 15: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```

### Step 16: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```

### Step 17: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```


## Complete Example

```python
# Workflow
class A:
    __array_function__ = _return_not_implemented

class B(A):
    __array_function__ = _return_not_implemented

class C(A):
    __array_function__ = _return_not_implemented

class D:
    __array_function__ = _return_not_implemented
a = A()
b = B()
c = C()
d = D()
assert_equal(_get_implementing_args([1]), [])
assert_equal(_get_implementing_args([a]), [a])
assert_equal(_get_implementing_args([a, 1]), [a])
assert_equal(_get_implementing_args([a, a, a]), [a])
assert_equal(_get_implementing_args([a, d, a]), [a, d])
assert_equal(_get_implementing_args([a, b]), [b, a])
assert_equal(_get_implementing_args([b, a]), [b, a])
assert_equal(_get_implementing_args([a, b, c]), [b, c, a])
assert_equal(_get_implementing_args([a, c, b]), [c, b, a])
```

## Next Steps


---

*Source: test_overrides.py:108 | Complexity: Advanced | Last updated: 2026-06-02*