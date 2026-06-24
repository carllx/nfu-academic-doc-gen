# How To: Astype Mask Ordering

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype mask ordering

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: Assign descr = np.dtype(...)

```python
descr = np.dtype([('v', int, 3), ('x', [('y', float)])])
```

**Verification:**
```python
assert x_a.dtype.names == np.dtype(descr).names
```

### Step 2: Assign x = array(...)

```python
x = array([[([1, 2, 3], (1.0,)), ([1, 2, 3], (2.0,))], [([1, 2, 3], (3.0,)), ([1, 2, 3], (4.0,))]], dtype=descr)
```

**Verification:**
```python
assert x_a.mask.dtype.names == np.dtype(descr).names
```

### Step 3: Assign unknown = value

```python
x[0]['v'][0] = np.ma.masked
```

**Verification:**
```python
assert_equal(x, x_a)
```

### Step 4: Assign x_a = x.astype(...)

```python
x_a = x.astype(descr)
```

**Verification:**
```python
assert_(x is x.astype(x.dtype, copy=False))
```

### Step 5: Call assert_equal()

```python
assert_equal(x, x_a)
```

**Verification:**
```python
assert_equal(type(x.astype(x.dtype, subok=False)), np.ndarray)
```

### Step 6: Call assert_()

```python
assert_(x is x.astype(x.dtype, copy=False))
```

**Verification:**
```python
assert_(x_f.flags.f_contiguous)
```

### Step 7: Call assert_equal()

```python
assert_equal(type(x.astype(x.dtype, subok=False)), np.ndarray)
```

**Verification:**
```python
assert_(x_f.mask.flags.f_contiguous)
```

### Step 8: Assign x_f = x.astype(...)

```python
x_f = x.astype(x.dtype, order='F')
```

**Verification:**
```python
assert x_a2.dtype.names == np.dtype(descr).names
```

### Step 9: Call assert_()

```python
assert_(x_f.flags.f_contiguous)
```

**Verification:**
```python
assert x_a2.mask.dtype.names == np.dtype(descr).names
```

### Step 10: Call assert_()

```python
assert_(x_f.mask.flags.f_contiguous)
```

**Verification:**
```python
assert_equal(x, x_a2)
```

### Step 11: Assign x_a2 = np.array(...)

```python
x_a2 = np.array(x, dtype=descr, subok=True)
```

**Verification:**
```python
assert_(x is np.array(x, dtype=descr, copy=None, subok=True))
```

### Step 12: Call assert_equal()

```python
assert_equal(x, x_a2)
```

**Verification:**
```python
assert_(x_f2.flags.f_contiguous)
```

### Step 13: Call assert_()

```python
assert_(x is np.array(x, dtype=descr, copy=None, subok=True))
```

**Verification:**
```python
assert_(x_f2.mask.flags.f_contiguous)
```

### Step 14: Assign x_f2 = np.array(...)

```python
x_f2 = np.array(x, dtype=x.dtype, order='F', subok=True)
```

### Step 15: Call assert_()

```python
assert_(x_f2.flags.f_contiguous)
```

### Step 16: Call assert_()

```python
assert_(x_f2.mask.flags.f_contiguous)
```


## Complete Example

```python
# Workflow
descr = np.dtype([('v', int, 3), ('x', [('y', float)])])
x = array([[([1, 2, 3], (1.0,)), ([1, 2, 3], (2.0,))], [([1, 2, 3], (3.0,)), ([1, 2, 3], (4.0,))]], dtype=descr)
x[0]['v'][0] = np.ma.masked
x_a = x.astype(descr)
assert x_a.dtype.names == np.dtype(descr).names
assert x_a.mask.dtype.names == np.dtype(descr).names
assert_equal(x, x_a)
assert_(x is x.astype(x.dtype, copy=False))
assert_equal(type(x.astype(x.dtype, subok=False)), np.ndarray)
x_f = x.astype(x.dtype, order='F')
assert_(x_f.flags.f_contiguous)
assert_(x_f.mask.flags.f_contiguous)
x_a2 = np.array(x, dtype=descr, subok=True)
assert x_a2.dtype.names == np.dtype(descr).names
assert x_a2.mask.dtype.names == np.dtype(descr).names
assert_equal(x, x_a2)
assert_(x is np.array(x, dtype=descr, copy=None, subok=True))
x_f2 = np.array(x, dtype=x.dtype, order='F', subok=True)
assert_(x_f2.flags.f_contiguous)
assert_(x_f2.mask.flags.f_contiguous)
```

## Next Steps


---

*Source: test_core.py:5809 | Complexity: Advanced | Last updated: 2026-06-02*