# How To: Svd Build

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test svd build

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = array(...)

```python
a = array([[0.0, 1.0], [1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
```

**Verification:**
```python
assert_array_almost_equal(b, np.zeros((2, 2)))
```

### Step 2: Assign unknown = value

```python
m, n = a.shape
```

### Step 3: Assign unknown = linalg.svd(...)

```python
u, s, vh = linalg.svd(a)
```

### Step 4: Assign b = dot(...)

```python
b = dot(transpose(u[:, n:]), a)
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(b, np.zeros((2, 2)))
```


## Complete Example

```python
# Workflow
a = array([[0.0, 1.0], [1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
m, n = a.shape
u, s, vh = linalg.svd(a)
b = dot(transpose(u[:, n:]), a)
assert_array_almost_equal(b, np.zeros((2, 2)))
```

## Next Steps


---

*Source: test_regression.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*