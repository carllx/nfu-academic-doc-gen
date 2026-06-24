# How To: Matmul Axes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matmul axes

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

### Step 1: Assign a = np.arange.reshape(...)

```python
a = np.arange(3 * 4 * 5).reshape(3, 4, 5)
```

**Verification:**
```python
assert c.shape == (3, 4, 4)
```

### Step 2: Assign c = np.matmul(...)

```python
c = np.matmul(a, a, axes=[(-2, -1), (-1, -2), (1, 2)])
```

**Verification:**
```python
assert d.shape == (4, 4, 3)
```

### Step 3: Assign d = np.matmul(...)

```python
d = np.matmul(a, a, axes=[(-2, -1), (-1, -2), (0, 1)])
```

**Verification:**
```python
assert_array_equal(e, c)
```

### Step 4: Assign e = np.swapaxes(...)

```python
e = np.swapaxes(d, 0, 2)
```

**Verification:**
```python
assert f.shape == (4, 5)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(e, c)
```

### Step 6: Assign f = np.matmul(...)

```python
f = np.matmul(a, np.arange(3), axes=[(1, 0), 0, 0])
```

**Verification:**
```python
assert f.shape == (4, 5)
```


## Complete Example

```python
# Workflow
a = np.arange(3 * 4 * 5).reshape(3, 4, 5)
c = np.matmul(a, a, axes=[(-2, -1), (-1, -2), (1, 2)])
assert c.shape == (3, 4, 4)
d = np.matmul(a, a, axes=[(-2, -1), (-1, -2), (0, 1)])
assert d.shape == (4, 4, 3)
e = np.swapaxes(d, 0, 2)
assert_array_equal(e, c)
f = np.matmul(a, np.arange(3), axes=[(1, 0), 0, 0])
assert f.shape == (4, 5)
```

## Next Steps


---

*Source: test_multiarray.py:7791 | Complexity: Intermediate | Last updated: 2026-06-02*