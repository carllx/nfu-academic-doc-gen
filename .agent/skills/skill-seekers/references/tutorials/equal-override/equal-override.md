# How To: Equal Override

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equal override

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

### Step 1: Assign array = np.array(...)

```python
array = np.array([(0, 1), (2, 3)], dtype='i4,i4')
```

**Verification:**
```python
assert_equal(my_always_equal == array, 'eq')
```

### Step 2: Assign __array_priority__ = 10000

```python
__array_priority__ = 10000
```

**Verification:**
```python
assert_equal(array == my_always_equal, 'eq')
```

### Step 3: Assign __array_ufunc__ = None

```python
__array_ufunc__ = None
```

**Verification:**
```python
assert_equal(my_always_equal != array, 'ne')
```

### Step 4: Assign my_always_equal = my_always_equal_cls(...)

```python
my_always_equal = my_always_equal_cls()
```

**Verification:**
```python
assert_equal(array != my_always_equal, 'ne')
```

### Step 5: Call assert_equal()

```python
assert_equal(my_always_equal == array, 'eq')
```

### Step 6: Call assert_equal()

```python
assert_equal(array == my_always_equal, 'eq')
```

### Step 7: Call assert_equal()

```python
assert_equal(my_always_equal != array, 'ne')
```

### Step 8: Call assert_equal()

```python
assert_equal(array != my_always_equal, 'ne')
```


## Complete Example

```python
# Workflow
class MyAlwaysEqual:

    def __eq__(self, other):
        return 'eq'

    def __ne__(self, other):
        return 'ne'

class MyAlwaysEqualOld(MyAlwaysEqual):
    __array_priority__ = 10000

class MyAlwaysEqualNew(MyAlwaysEqual):
    __array_ufunc__ = None
array = np.array([(0, 1), (2, 3)], dtype='i4,i4')
for my_always_equal_cls in (MyAlwaysEqualOld, MyAlwaysEqualNew):
    my_always_equal = my_always_equal_cls()
    assert_equal(my_always_equal == array, 'eq')
    assert_equal(array == my_always_equal, 'eq')
    assert_equal(my_always_equal != array, 'ne')
    assert_equal(array != my_always_equal, 'ne')
```

## Next Steps


---

*Source: test_multiarray.py:10280 | Complexity: Advanced | Last updated: 2026-06-02*