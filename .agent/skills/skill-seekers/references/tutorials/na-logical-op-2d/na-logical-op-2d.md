# How To: Na Logical Op 2D

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na logical op 2d

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.ops.array_ops`


## Step-by-Step Guide

### Step 1: Assign left = np.arange.reshape(...)

```python
left = np.arange(8).reshape(4, 2)
```

### Step 2: Assign right = left.astype(...)

```python
right = left.astype(object)
```

### Step 3: Assign unknown = value

```python
right[0, 0] = np.nan
```

### Step 4: Assign result = na_logical_op(...)

```python
result = na_logical_op(left, right, operator.or_)
```

### Step 5: Assign expected = right

```python
expected = right
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Call operator.or_()

```python
operator.or_(left, right)
```


## Complete Example

```python
# Workflow
left = np.arange(8).reshape(4, 2)
right = left.astype(object)
right[0, 0] = np.nan
with pytest.raises(TypeError, match='unsupported operand type'):
    operator.or_(left, right)
result = na_logical_op(left, right, operator.or_)
expected = right
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_array_ops.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*