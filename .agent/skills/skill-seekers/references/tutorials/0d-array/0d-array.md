# How To: 0D Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 0D array

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
a = array(1)
```

**Verification:**
```python
assert_array_equal(res, desired)
```

### Step 2: Assign b = array(...)

```python
b = array(2)
```

### Step 3: Assign res = value

```python
res = [atleast_3d(a), atleast_3d(b)]
```

### Step 4: Assign desired = value

```python
desired = [array([[[1]]]), array([[[2]]])]
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(res, desired)
```


## Complete Example

```python
# Workflow
a = array(1)
b = array(2)
res = [atleast_3d(a), atleast_3d(b)]
desired = [array([[[1]]]), array([[[2]]])]
assert_array_equal(res, desired)
```

## Next Steps


---

*Source: test_shape_base.py:117 | Complexity: Intermediate | Last updated: 2026-06-02*