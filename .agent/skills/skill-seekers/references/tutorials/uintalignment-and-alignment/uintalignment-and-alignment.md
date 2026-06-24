# How To: Uintalignment And Alignment

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test uintalignment and alignment

## Prerequisites

**Required Modules:**
- `builtins`
- `collections.abc`
- `ctypes`
- `functools`
- `gc`
- `importlib`
- `inspect`
- `io`
- `itertools`
- `mmap`
- `operator`
- `os`
- `pathlib`
- `pickle`
- `re`
- `sys`
- `tempfile`
- `warnings`
- `weakref`
- `contextlib`
- `datetime`
- `decimal`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy._core.multiarray`
- `numpy._core.tests._locales`
- `numpy.exceptions`
- `numpy.lib`
- `numpy.lib.recfunctions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy._core._internal`
- `numpy.testing`
- `operator`
- `numpy._core._multiarray_tests`
- `numpy._core._multiarray_tests`
- `pickle`
- `numpy._core._multiarray_tests`
- `numpy._core.arrayprint`
- `numpy._core._multiarray_tests`
- `numpy._core._multiarray_tests`
- `numpy._core._multiarray_tests`
- `fractions`
- `fractions`
- `numpy._core`
- `numpy._core._multiarray_tests`
- `numpy._core._multiarray_tests`
- `_testbuffer`


## Step-by-Step Guide

### Step 1: Assign d1 = np.dtype(...)

```python
d1 = np.dtype('u1,c8', align=True)
```

**Verification:**
```python
assert_equal(np.zeros(1, dtype=d1)['f1'].flags['ALIGNED'], True)
```

### Step 2: Assign d2 = np.dtype(...)

```python
d2 = np.dtype('u4,c8', align=True)
```

**Verification:**
```python
assert_equal(np.zeros(1, dtype=d2)['f1'].flags['ALIGNED'], True)
```

### Step 3: Assign d3 = np.dtype(...)

```python
d3 = np.dtype({'names': ['a', 'b'], 'formats': ['u1', d1]}, align=True)
```

**Verification:**
```python
assert_equal(np.zeros(1, dtype='u1,c8')['f1'].flags['ALIGNED'], False)
```

### Step 4: Call assert_equal()

```python
assert_equal(np.zeros(1, dtype=d1)['f1'].flags['ALIGNED'], True)
```

**Verification:**
```python
assert_equal(d.alignment, alignment)
```

### Step 5: Call assert_equal()

```python
assert_equal(np.zeros(1, dtype=d2)['f1'].flags['ALIGNED'], True)
```

**Verification:**
```python
assert_equal(d.itemsize, size)
```

### Step 6: Call assert_equal()

```python
assert_equal(np.zeros(1, dtype='u1,c8')['f1'].flags['ALIGNED'], False)
```

### Step 7: Assign s = _multiarray_tests.get_struct_alignments(...)

```python
s = _multiarray_tests.get_struct_alignments()
```

### Step 8: Assign src = value

```python
src = np.zeros((2, 2), dtype=d1)['f1']
```

### Step 9: Call np.exp()

```python
np.exp(src)
```

### Step 10: Assign dst = np.zeros(...)

```python
dst = np.zeros((2, 2), dtype='c8')
```

### Step 11: Assign unknown = value

```python
dst[:, 1] = src[:, 1]
```

### Step 12: Call assert_equal()

```python
assert_equal(d.alignment, alignment)
```

### Step 13: Call assert_equal()

```python
assert_equal(d.itemsize, size)
```


## Complete Example

```python
# Workflow
d1 = np.dtype('u1,c8', align=True)
d2 = np.dtype('u4,c8', align=True)
d3 = np.dtype({'names': ['a', 'b'], 'formats': ['u1', d1]}, align=True)
assert_equal(np.zeros(1, dtype=d1)['f1'].flags['ALIGNED'], True)
assert_equal(np.zeros(1, dtype=d2)['f1'].flags['ALIGNED'], True)
assert_equal(np.zeros(1, dtype='u1,c8')['f1'].flags['ALIGNED'], False)
s = _multiarray_tests.get_struct_alignments()
for d, (alignment, size) in zip([d1, d2, d3], s):
    assert_equal(d.alignment, alignment)
    assert_equal(d.itemsize, size)
src = np.zeros((2, 2), dtype=d1)['f1']
np.exp(src)
dst = np.zeros((2, 2), dtype='c8')
dst[:, 1] = src[:, 1]
```

## Next Steps


---

*Source: test_multiarray.py:10451 | Complexity: Advanced | Last updated: 2026-06-02*