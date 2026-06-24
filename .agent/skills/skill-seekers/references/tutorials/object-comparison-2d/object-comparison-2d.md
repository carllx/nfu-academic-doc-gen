# How To: Object Comparison 2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test object comparison 2d

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.ops.array_ops`


## Step-by-Step Guide

### Step 1: Assign left = np.arange.reshape.astype(...)

```python
left = np.arange(9).reshape(3, 3).astype(object)
```

### Step 2: Assign right = value

```python
right = left.T
```

### Step 3: Assign result = comparison_op(...)

```python
result = comparison_op(left, right, operator.eq)
```

### Step 4: Assign expected = np.eye.astype(...)

```python
expected = np.eye(3).astype(bool)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign right.flags.writeable = False

```python
right.flags.writeable = False
```

### Step 7: Assign result = comparison_op(...)

```python
result = comparison_op(left, right, operator.ne)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```


## Complete Example

```python
# Workflow
left = np.arange(9).reshape(3, 3).astype(object)
right = left.T
result = comparison_op(left, right, operator.eq)
expected = np.eye(3).astype(bool)
tm.assert_numpy_array_equal(result, expected)
right.flags.writeable = False
result = comparison_op(left, right, operator.ne)
tm.assert_numpy_array_equal(result, ~expected)
```

## Next Steps


---

*Source: test_array_ops.py:27 | Complexity: Advanced | Last updated: 2026-06-02*