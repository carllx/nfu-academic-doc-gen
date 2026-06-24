# How To: Density

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test density

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = array(...)

```python
x = array([1, 2, 3, 1, 2, 3, 1, 2, 3])
```

**Verification:**
```python
assert_array_almost_equal(H, answer, 3)
```

### Step 2: Assign y = array(...)

```python
y = array([1, 1, 1, 2, 2, 2, 3, 3, 3])
```

### Step 3: Assign unknown = histogram2d(...)

```python
H, xed, yed = histogram2d(x, y, [[1, 2, 3, 5], [1, 2, 3, 5]], density=True)
```

### Step 4: Assign answer = value

```python
answer = array([[1, 1, 0.5], [1, 1, 0.5], [0.5, 0.5, 0.25]]) / 9.0
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(H, answer, 3)
```


## Complete Example

```python
# Workflow
x = array([1, 2, 3, 1, 2, 3, 1, 2, 3])
y = array([1, 1, 1, 2, 2, 2, 3, 3, 3])
H, xed, yed = histogram2d(x, y, [[1, 2, 3, 5], [1, 2, 3, 5]], density=True)
answer = array([[1, 1, 0.5], [1, 1, 0.5], [0.5, 0.5, 0.25]]) / 9.0
assert_array_almost_equal(H, answer, 3)
```

## Next Steps


---

*Source: test_twodim_base.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*