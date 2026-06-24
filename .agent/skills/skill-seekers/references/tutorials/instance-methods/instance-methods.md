# How To: Instance Methods

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test instance methods

## Prerequisites

**Required Modules:**
- `collections.abc`
- `numpy`
- `numpy`
- `numpy.linalg`
- `numpy.testing`
- `numpy.linalg`
- `numpy.linalg`


## Step-by-Step Guide

### Step 1: Assign a = matrix(...)

```python
a = matrix([1.0], dtype='f8')
```

**Verification:**
```python
assert_(type(b) is matrix, f'{attrib}')
```

### Step 2: Assign methodargs = value

```python
methodargs = {'astype': ('intc',), 'clip': (0.0, 1.0), 'compress': ([1],), 'repeat': (1,), 'reshape': (1,), 'swapaxes': (0, 0), 'dot': np.array([1.0])}
```

**Verification:**
```python
assert_(type(a.real) is matrix)
```

### Step 3: Assign excluded_methods = value

```python
excluded_methods = ['argmin', 'choose', 'dump', 'dumps', 'fill', 'getfield', 'getA', 'getA1', 'item', 'nonzero', 'put', 'putmask', 'resize', 'searchsorted', 'setflags', 'setfield', 'sort', 'partition', 'argpartition', 'to_device', 'take', 'tofile', 'tolist', 'tobytes', 'all', 'any', 'sum', 'argmax', 'argmin', 'min', 'max', 'mean', 'var', 'ptp', 'prod', 'std', 'ctypes', 'bitwise_count']
```

**Verification:**
```python
assert_(type(a.imag) is matrix)
```

### Step 4: Call assert_()

```python
assert_(type(a.real) is matrix)
```

**Verification:**
```python
assert_(type(c) is np.ndarray)
```

### Step 5: Call assert_()

```python
assert_(type(a.imag) is matrix)
```

**Verification:**
```python
assert_(type(d) is np.ndarray)
```

### Step 6: Assign unknown = matrix.nonzero(...)

```python
c, d = matrix([0.0]).nonzero()
```

### Step 7: Call assert_()

```python
assert_(type(c) is np.ndarray)
```

### Step 8: Call assert_()

```python
assert_(type(d) is np.ndarray)
```

### Step 9: Assign f = getattr(...)

```python
f = getattr(a, attrib)
```

### Step 10: Call a.astype()

```python
a.astype('f8')
```

### Step 11: Call a.fill()

```python
a.fill(1.0)
```

### Step 12: Assign args = methodargs.get(...)

```python
args = methodargs.get(attrib, ())
```

### Step 13: Assign b = f(...)

```python
b = f(*args)
```

### Step 14: Call assert_()

```python
assert_(type(b) is matrix, f'{attrib}')
```


## Complete Example

```python
# Workflow
a = matrix([1.0], dtype='f8')
methodargs = {'astype': ('intc',), 'clip': (0.0, 1.0), 'compress': ([1],), 'repeat': (1,), 'reshape': (1,), 'swapaxes': (0, 0), 'dot': np.array([1.0])}
excluded_methods = ['argmin', 'choose', 'dump', 'dumps', 'fill', 'getfield', 'getA', 'getA1', 'item', 'nonzero', 'put', 'putmask', 'resize', 'searchsorted', 'setflags', 'setfield', 'sort', 'partition', 'argpartition', 'to_device', 'take', 'tofile', 'tolist', 'tobytes', 'all', 'any', 'sum', 'argmax', 'argmin', 'min', 'max', 'mean', 'var', 'ptp', 'prod', 'std', 'ctypes', 'bitwise_count']
for attrib in dir(a):
    if attrib.startswith('_') or attrib in excluded_methods:
        continue
    f = getattr(a, attrib)
    if isinstance(f, collections.abc.Callable):
        a.astype('f8')
        a.fill(1.0)
        args = methodargs.get(attrib, ())
        b = f(*args)
        assert_(type(b) is matrix, f'{attrib}')
assert_(type(a.real) is matrix)
assert_(type(a.imag) is matrix)
c, d = matrix([0.0]).nonzero()
assert_(type(c) is np.ndarray)
assert_(type(d) is np.ndarray)
```

## Next Steps


---

*Source: test_defmatrix.py:276 | Complexity: Advanced | Last updated: 2026-06-02*