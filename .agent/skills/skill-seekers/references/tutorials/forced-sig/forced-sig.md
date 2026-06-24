# How To: Forced Sig

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test forced sig

## Prerequisites

**Required Modules:**
- `ctypes`
- `inspect`
- `itertools`
- `pickle`
- `sys`
- `warnings`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._operand_flag_tests`
- `numpy._core._rational_tests`
- `numpy._core._umath_tests`
- `numpy._core.umath`
- `numpy.linalg._umath_linalg`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy._core._struct_ufunc_tests`


## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = 0.5 * np.arange(3, dtype='f8')
```

**Verification:**
```python
assert_equal(np.add(a, 0.5), [0.5, 1, 1.5])
```

### Step 2: Call assert_equal()

```python
assert_equal(np.add(a, 0.5), [0.5, 1, 1.5])
```

**Verification:**
```python
assert_equal(np.add(a, 0.5, sig='ii->i', casting='unsafe'), [0, 0, 1])
```

### Step 3: Call assert_equal()

```python
assert_equal(np.add(a, 0.5, sig='ii->i', casting='unsafe'), [0, 0, 1])
```

**Verification:**
```python
assert_equal(np.add(a, 0.5, sig=('i4', 'i4', 'i4'), casting='unsafe'), [0, 0, 1])
```

### Step 4: Call assert_equal()

```python
assert_equal(np.add(a, 0.5, sig=('i4', 'i4', 'i4'), casting='unsafe'), [0, 0, 1])
```

**Verification:**
```python
assert_equal(b, [0.5, 1, 1.5])
```

### Step 5: Assign b = np.zeros(...)

```python
b = np.zeros((3,), dtype='f8')
```

**Verification:**
```python
assert_equal(b, [0, 0, 0])
```

### Step 6: Call np.add()

```python
np.add(a, 0.5, out=b)
```

**Verification:**
```python
assert_equal(b, [0, 0, 1])
```

### Step 7: Call assert_equal()

```python
assert_equal(b, [0.5, 1, 1.5])
```

**Verification:**
```python
assert_equal(b, [0, 0, 0])
```

### Step 8: Assign unknown = 0

```python
b[:] = 0
```

**Verification:**
```python
assert_equal(b, [0, 0, 1])
```

### Step 9: Call assert_equal()

```python
assert_equal(b, [0, 0, 0])
```

### Step 10: Call np.add()

```python
np.add(a, 0.5, sig='ii->i', out=b, casting='unsafe')
```

### Step 11: Call assert_equal()

```python
assert_equal(b, [0, 0, 1])
```

### Step 12: Assign unknown = 0

```python
b[:] = 0
```

### Step 13: Call assert_equal()

```python
assert_equal(b, [0, 0, 0])
```

### Step 14: Call np.add()

```python
np.add(a, 0.5, sig=('i4', 'i4', 'i4'), out=b, casting='unsafe')
```

### Step 15: Call assert_equal()

```python
assert_equal(b, [0, 0, 1])
```

### Step 16: Call np.add()

```python
np.add(a, 0.5, sig='i', casting='unsafe')
```

### Step 17: Call np.add()

```python
np.add(a, 0.5, sig=('i4',), casting='unsafe')
```

### Step 18: Call np.add()

```python
np.add(a, 0.5, sig='i', out=b, casting='unsafe')
```

### Step 19: Call np.add()

```python
np.add(a, 0.5, sig=('i4',), out=b, casting='unsafe')
```


## Complete Example

```python
# Workflow
a = 0.5 * np.arange(3, dtype='f8')
assert_equal(np.add(a, 0.5), [0.5, 1, 1.5])
with assert_raises(TypeError):
    np.add(a, 0.5, sig='i', casting='unsafe')
assert_equal(np.add(a, 0.5, sig='ii->i', casting='unsafe'), [0, 0, 1])
with assert_raises(TypeError):
    np.add(a, 0.5, sig=('i4',), casting='unsafe')
assert_equal(np.add(a, 0.5, sig=('i4', 'i4', 'i4'), casting='unsafe'), [0, 0, 1])
b = np.zeros((3,), dtype='f8')
np.add(a, 0.5, out=b)
assert_equal(b, [0.5, 1, 1.5])
b[:] = 0
with assert_raises(TypeError):
    np.add(a, 0.5, sig='i', out=b, casting='unsafe')
assert_equal(b, [0, 0, 0])
np.add(a, 0.5, sig='ii->i', out=b, casting='unsafe')
assert_equal(b, [0, 0, 1])
b[:] = 0
with assert_raises(TypeError):
    np.add(a, 0.5, sig=('i4',), out=b, casting='unsafe')
assert_equal(b, [0, 0, 0])
np.add(a, 0.5, sig=('i4', 'i4', 'i4'), out=b, casting='unsafe')
assert_equal(b, [0, 0, 1])
```

## Next Steps


---

*Source: test_ufunc.py:447 | Complexity: Advanced | Last updated: 2026-06-02*