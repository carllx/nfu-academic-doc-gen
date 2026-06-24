# How To: 3D Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 3D array

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core.shape_base`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`


## Step-by-Step Guide

### Step 1: Assign a = array(...)

```python
a = array([[1, 2], [1, 2]])
```

**Verification:**
```python
assert_array_equal(res, desired)
```

### Step 2: Assign b = array(...)

```python
b = array([[2, 3], [2, 3]])
```

### Step 3: Assign a = array(...)

```python
a = array([a, a])
```

### Step 4: Assign b = array(...)

```python
b = array([b, b])
```

### Step 5: Assign res = value

```python
res = [atleast_2d(a), atleast_2d(b)]
```

### Step 6: Assign desired = value

```python
desired = [a, b]
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res, desired)
```


## Complete Example

```python
# Workflow
a = array([[1, 2], [1, 2]])
b = array([[2, 3], [2, 3]])
a = array([a, a])
b = array([b, b])
res = [atleast_2d(a), atleast_2d(b)]
desired = [a, b]
assert_array_equal(res, desired)
```

## Next Steps


---

*Source: test_shape_base.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*