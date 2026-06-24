# How To: Equal Subclass No Override

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test equal subclass no override

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: op, dt1, dt2
```

## Step-by-Step Guide

### Step 1: Assign numpy_arr = np.zeros(...)

```python
numpy_arr = np.zeros(5, dtype=dt1)
```

**Verification:**
```python
assert type(op(numpy_arr, my_arr)) is MyArr
```

### Step 2: Assign my_arr = np.zeros.view(...)

```python
my_arr = np.zeros(5, dtype=dt2).view(MyArr)
```

**Verification:**
```python
assert type(op(my_arr, numpy_arr)) is MyArr
```

### Step 3: Assign called_wrap = 0

```python
called_wrap = 0
```

**Verification:**
```python
assert MyArr.called_wrap == 2
```


## Complete Example

```python
# Setup
# Fixtures: op, dt1, dt2

# Workflow
class MyArr(np.ndarray):
    called_wrap = 0

    def __array_wrap__(self, new, context=None, return_scalar=False):
        type(self).called_wrap += 1
        return super().__array_wrap__(new, context, return_scalar)
numpy_arr = np.zeros(5, dtype=dt1)
my_arr = np.zeros(5, dtype=dt2).view(MyArr)
assert type(op(numpy_arr, my_arr)) is MyArr
assert type(op(my_arr, numpy_arr)) is MyArr
assert MyArr.called_wrap == 2
```

## Next Steps


---

*Source: test_multiarray.py:10312 | Complexity: Beginner | Last updated: 2026-06-02*