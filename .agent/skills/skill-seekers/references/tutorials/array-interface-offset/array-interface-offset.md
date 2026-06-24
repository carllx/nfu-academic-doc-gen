# How To: Array Interface Offset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array interface offset

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

**Verification:**
```python
assert_equal(arr1, arr[1:])
```

### Step 2: Assign interface = dict(...)

```python
interface = dict(arr.__array_interface__)
```

### Step 3: Assign unknown = memoryview(...)

```python
interface['data'] = memoryview(arr)
```

### Step 4: Assign unknown = value

```python
interface['shape'] = (2,)
```

### Step 5: Assign unknown = 4

```python
interface['offset'] = 4
```

### Step 6: Assign arr1 = np.asarray(...)

```python
arr1 = np.asarray(DummyArray())
```

### Step 7: Call assert_equal()

```python
assert_equal(arr1, arr[1:])
```

### Step 8: Assign __array_interface__ = interface

```python
__array_interface__ = interface
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='int32')
interface = dict(arr.__array_interface__)
interface['data'] = memoryview(arr)
interface['shape'] = (2,)
interface['offset'] = 4

class DummyArray:
    __array_interface__ = interface
arr1 = np.asarray(DummyArray())
assert_equal(arr1, arr[1:])
```

## Next Steps


---

*Source: test_multiarray.py:9247 | Complexity: Advanced | Last updated: 2026-06-02*