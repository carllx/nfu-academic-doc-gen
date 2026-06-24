# How To: Nested Array Repr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nested array repr

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign a = np.empty(...)

```python
a = np.empty((2, 2), dtype=object)
```

**Verification:**
```python
assert_equal(repr(a), 'array([[array([[1., 0.],\n               [0., 1.]]), array([[1., 0., 0.],\n                                  [0., 1., 0.],\n                                  [0., 0., 1.]])],\n       [None, array([[1.],\n                     [1.],\n                     [1.]])]], dtype=object)')
```

### Step 2: Assign unknown = np.eye(...)

```python
a[0, 0] = np.eye(2)
```

### Step 3: Assign unknown = np.eye(...)

```python
a[0, 1] = np.eye(3)
```

### Step 4: Assign unknown = None

```python
a[1, 0] = None
```

### Step 5: Assign unknown = np.ones(...)

```python
a[1, 1] = np.ones((3, 1))
```

### Step 6: Call assert_equal()

```python
assert_equal(repr(a), 'array([[array([[1., 0.],\n               [0., 1.]]), array([[1., 0., 0.],\n                                  [0., 1., 0.],\n                                  [0., 0., 1.]])],\n       [None, array([[1.],\n                     [1.],\n                     [1.]])]], dtype=object)')
```


## Complete Example

```python
# Workflow
a = np.empty((2, 2), dtype=object)
a[0, 0] = np.eye(2)
a[0, 1] = np.eye(3)
a[1, 0] = None
a[1, 1] = np.ones((3, 1))
assert_equal(repr(a), 'array([[array([[1., 0.],\n               [0., 1.]]), array([[1., 0., 0.],\n                                  [0., 1., 0.],\n                                  [0., 0., 1.]])],\n       [None, array([[1.],\n                     [1.],\n                     [1.]])]], dtype=object)')
```

## Next Steps


---

*Source: test_arrayprint.py:518 | Complexity: Intermediate | Last updated: 2026-06-02*