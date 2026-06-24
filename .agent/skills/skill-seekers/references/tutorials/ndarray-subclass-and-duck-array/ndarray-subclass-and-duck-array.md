# How To: Ndarray Subclass And Duck Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test ndarray subclass and duck array

## Prerequisites

**Required Modules:**
- `inspect`
- `os`
- `pickle`
- `sys`
- `tempfile`
- `io`
- `unittest`
- `pytest`
- `numpy`
- `numpy._core.overrides`
- `numpy.testing`
- `numpy.testing.overrides`


## Step-by-Step Guide

### Step 1: Assign array = np.array(...)

```python
array = np.array(1)
```

**Verification:**
```python
assert_equal(_get_implementing_args([array, subarray, other]), [subarray, array, other])
```

### Step 2: Assign subarray = np.array.view(...)

```python
subarray = np.array(1).view(OverrideSub)
```

**Verification:**
```python
assert_equal(_get_implementing_args([array, other, subarray]), [subarray, array, other])
```

### Step 3: Assign other = Other(...)

```python
other = Other()
```

### Step 4: Call assert_equal()

```python
assert_equal(_get_implementing_args([array, subarray, other]), [subarray, array, other])
```

### Step 5: Call assert_equal()

```python
assert_equal(_get_implementing_args([array, other, subarray]), [subarray, array, other])
```

### Step 6: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```

### Step 7: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```


## Complete Example

```python
# Workflow
class OverrideSub(np.ndarray):
    __array_function__ = _return_not_implemented

class Other:
    __array_function__ = _return_not_implemented
array = np.array(1)
subarray = np.array(1).view(OverrideSub)
other = Other()
assert_equal(_get_implementing_args([array, subarray, other]), [subarray, array, other])
assert_equal(_get_implementing_args([array, other, subarray]), [subarray, array, other])
```

## Next Steps


---

*Source: test_overrides.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*