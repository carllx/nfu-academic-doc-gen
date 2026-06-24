# How To: Npymath Real

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test npymath real

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

### Step 1: Assign funcs = value

```python
funcs = {npy_log10: np.log10, npy_cosh: np.cosh, npy_sinh: np.sinh, npy_tan: np.tan, npy_tanh: np.tanh}
```

**Verification:**
```python
assert_allclose(got, expected)
```

### Step 2: Assign vals = value

```python
vals = (1, np.inf, -np.inf, np.nan)
```

### Step 3: Assign types = value

```python
types = (np.float32, np.float64, np.longdouble)
```

### Step 4: Assign z = t(...)

```python
z = t(x)
```

### Step 5: Assign got = fun(...)

```python
got = fun(z)
```

### Step 6: Assign expected = npfun(...)

```python
expected = npfun(z)
```

### Step 7: Call assert_allclose()

```python
assert_allclose(got, expected)
```


## Complete Example

```python
# Workflow
from numpy._core._multiarray_tests import npy_cosh, npy_log10, npy_sinh, npy_tan, npy_tanh
funcs = {npy_log10: np.log10, npy_cosh: np.cosh, npy_sinh: np.sinh, npy_tan: np.tan, npy_tanh: np.tanh}
vals = (1, np.inf, -np.inf, np.nan)
types = (np.float32, np.float64, np.longdouble)
with np.errstate(all='ignore'):
    for fun, npfun in funcs.items():
        for x, t in itertools.product(vals, types):
            z = t(x)
            got = fun(z)
            expected = npfun(z)
            assert_allclose(got, expected)
```

## Next Steps


---

*Source: test_multiarray.py:10425 | Complexity: Intermediate | Last updated: 2026-06-02*