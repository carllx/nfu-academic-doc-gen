# How To: Ndarray And Duck Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test ndarray and duck array

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
assert_equal(list(args), [other, array])
```

### Step 2: Assign other = Other(...)

```python
other = Other()
```

**Verification:**
```python
assert_equal(list(args), [array, other])
```

### Step 3: Assign args = _get_implementing_args(...)

```python
args = _get_implementing_args([other, array])
```

### Step 4: Call assert_equal()

```python
assert_equal(list(args), [other, array])
```

### Step 5: Assign args = _get_implementing_args(...)

```python
args = _get_implementing_args([array, other])
```

### Step 6: Call assert_equal()

```python
assert_equal(list(args), [array, other])
```

### Step 7: Assign __array_function__ = _return_not_implemented

```python
__array_function__ = _return_not_implemented
```


## Complete Example

```python
# Workflow
class Other:
    __array_function__ = _return_not_implemented
array = np.array(1)
other = Other()
args = _get_implementing_args([other, array])
assert_equal(list(args), [other, array])
args = _get_implementing_args([array, other])
assert_equal(list(args), [array, other])
```

## Next Steps


---

*Source: test_overrides.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*