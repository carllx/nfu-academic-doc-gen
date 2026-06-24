# How To: Array Interface Itemsize

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array interface itemsize

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

### Step 1: Assign my_dtype = np.dtype(...)

```python
my_dtype = np.dtype({'names': ['A', 'B'], 'formats': ['f4', 'f4'], 'offsets': [0, 8], 'itemsize': 16})
```

**Verification:**
```python
assert_equal(descr_t.itemsize, typestr_t.itemsize)
```

### Step 2: Assign a = np.ones(...)

```python
a = np.ones(10, dtype=my_dtype)
```

### Step 3: Assign descr_t = np.dtype(...)

```python
descr_t = np.dtype(a.__array_interface__['descr'])
```

### Step 4: Assign typestr_t = np.dtype(...)

```python
typestr_t = np.dtype(a.__array_interface__['typestr'])
```

### Step 5: Call assert_equal()

```python
assert_equal(descr_t.itemsize, typestr_t.itemsize)
```


## Complete Example

```python
# Workflow
my_dtype = np.dtype({'names': ['A', 'B'], 'formats': ['f4', 'f4'], 'offsets': [0, 8], 'itemsize': 16})
a = np.ones(10, dtype=my_dtype)
descr_t = np.dtype(a.__array_interface__['descr'])
typestr_t = np.dtype(a.__array_interface__['typestr'])
assert_equal(descr_t.itemsize, typestr_t.itemsize)
```

## Next Steps


---

*Source: test_multiarray.py:9212 | Complexity: Intermediate | Last updated: 2026-06-02*