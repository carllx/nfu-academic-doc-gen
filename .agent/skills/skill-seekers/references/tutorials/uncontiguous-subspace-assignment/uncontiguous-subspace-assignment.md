# How To: Uncontiguous Subspace Assignment

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test uncontiguous subspace assignment

## Prerequisites

**Required Modules:**
- `functools`
- `inspect`
- `operator`
- `sys`
- `warnings`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.full(...)

```python
a = np.full((3, 4, 2), -1)
```

**Verification:**
```python
assert_equal(a, b)
```

### Step 2: Assign b = np.full(...)

```python
b = np.full((3, 4, 2), -1)
```

### Step 3: Assign unknown = value

```python
a[[0, 1]] = np.arange(2 * 4 * 2).reshape(2, 4, 2).T
```

### Step 4: Assign unknown = np.arange.reshape.T.copy(...)

```python
b[[0, 1]] = np.arange(2 * 4 * 2).reshape(2, 4, 2).T.copy()
```

### Step 5: Call assert_equal()

```python
assert_equal(a, b)
```


## Complete Example

```python
# Workflow
a = np.full((3, 4, 2), -1)
b = np.full((3, 4, 2), -1)
a[[0, 1]] = np.arange(2 * 4 * 2).reshape(2, 4, 2).T
b[[0, 1]] = np.arange(2 * 4 * 2).reshape(2, 4, 2).T.copy()
assert_equal(a, b)
```

## Next Steps


---

*Source: test_indexing.py:329 | Complexity: Intermediate | Last updated: 2026-06-02*