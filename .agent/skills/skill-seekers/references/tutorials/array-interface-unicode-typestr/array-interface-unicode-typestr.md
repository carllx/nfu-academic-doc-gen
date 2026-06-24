# How To: Array Interface Unicode Typestr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array interface unicode typestr

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

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='int32')
```

### Step 2: Assign interface = dict(...)

```python
interface = dict(arr.__array_interface__)
```

### Step 3: Assign unknown = '✓'

```python
interface['typestr'] = '✓'
```

### Step 4: Assign __array_interface__ = interface

```python
__array_interface__ = interface
```

### Step 5: Call np.asarray()

```python
np.asarray(DummyArray())
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='int32')
interface = dict(arr.__array_interface__)
interface['typestr'] = '✓'

class DummyArray:
    __array_interface__ = interface
with pytest.raises(TypeError):
    np.asarray(DummyArray())
```

## Next Steps


---

*Source: test_multiarray.py:9260 | Complexity: Intermediate | Last updated: 2026-06-02*