# How To: Testaverage4

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testAverage4

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign x = np.array.reshape(...)

```python
x = np.array([2, 3, 4]).reshape(3, 1)
```

**Verification:**
```python
assert_equal(actual, desired)
```

### Step 2: Assign b = np.ma.array(...)

```python
b = np.ma.array(x, mask=[[False], [False], [True]])
```

### Step 3: Assign w = np.array.reshape(...)

```python
w = np.array([4, 5, 6]).reshape(3, 1)
```

### Step 4: Assign actual = average(...)

```python
actual = average(b, weights=w, axis=1, keepdims=True)
```

### Step 5: Assign desired = masked_array(...)

```python
desired = masked_array([[2.0], [3.0], [4.0]], [[False], [False], [True]])
```

### Step 6: Call assert_equal()

```python
assert_equal(actual, desired)
```


## Complete Example

```python
# Workflow
x = np.array([2, 3, 4]).reshape(3, 1)
b = np.ma.array(x, mask=[[False], [False], [True]])
w = np.array([4, 5, 6]).reshape(3, 1)
actual = average(b, weights=w, axis=1, keepdims=True)
desired = masked_array([[2.0], [3.0], [4.0]], [[False], [False], [True]])
assert_equal(actual, desired)
```

## Next Steps


---

*Source: test_extras.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*