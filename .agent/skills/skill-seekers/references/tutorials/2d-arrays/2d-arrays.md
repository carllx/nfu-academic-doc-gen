# How To: 2D Arrays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2D arrays

## Prerequisites

**Required Modules:**
- `functools`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.random`
- `numpy.random`
- `numpy.random`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([[1], [2], [3]])
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([[2], [3], [4]])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[1, 2], [2, 3], [3, 4]])
```

### Step 4: Assign actual = np.column_stack(...)

```python
actual = np.column_stack((a, b))
```

### Step 5: Call assert_equal()

```python
assert_equal(actual, expected)
```


## Complete Example

```python
# Workflow
a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
expected = np.array([[1, 2], [2, 3], [3, 4]])
actual = np.column_stack((a, b))
assert_equal(actual, expected)
```

## Next Steps


---

*Source: test_shape_base.py:513 | Complexity: Intermediate | Last updated: 2026-06-02*