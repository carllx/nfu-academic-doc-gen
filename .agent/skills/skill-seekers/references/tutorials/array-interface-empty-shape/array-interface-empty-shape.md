# How To: Array Interface Empty Shape

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array interface empty shape

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
arr = np.array([1, 2, 3])
```

**Verification:**
```python
assert_equal(arr1, arr2)
```

### Step 2: Assign interface1 = dict(...)

```python
interface1 = dict(arr.__array_interface__)
```

**Verification:**
```python
assert_equal(arr1, arr3)
```

### Step 3: Assign unknown = value

```python
interface1['shape'] = ()
```

### Step 4: Assign interface2 = dict(...)

```python
interface2 = dict(interface1)
```

### Step 5: Assign unknown = unknown.tobytes(...)

```python
interface2['data'] = arr[0].tobytes()
```

### Step 6: Assign arr1 = np.asarray(...)

```python
arr1 = np.asarray(DummyArray1())
```

### Step 7: Assign arr2 = np.asarray(...)

```python
arr2 = np.asarray(DummyArray2())
```

### Step 8: Assign arr3 = unknown.reshape(...)

```python
arr3 = arr[:1].reshape(())
```

### Step 9: Call assert_equal()

```python
assert_equal(arr1, arr2)
```

### Step 10: Call assert_equal()

```python
assert_equal(arr1, arr3)
```

### Step 11: Assign __array_interface__ = interface1

```python
__array_interface__ = interface1
```

### Step 12: Assign __array_interface__ = interface2

```python
__array_interface__ = interface2
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3])
interface1 = dict(arr.__array_interface__)
interface1['shape'] = ()

class DummyArray1:
    __array_interface__ = interface1
interface2 = dict(interface1)
interface2['data'] = arr[0].tobytes()

class DummyArray2:
    __array_interface__ = interface2
arr1 = np.asarray(DummyArray1())
arr2 = np.asarray(DummyArray2())
arr3 = arr[:1].reshape(())
assert_equal(arr1, arr2)
assert_equal(arr1, arr3)
```

## Next Steps


---

*Source: test_multiarray.py:9222 | Complexity: Advanced | Last updated: 2026-06-02*