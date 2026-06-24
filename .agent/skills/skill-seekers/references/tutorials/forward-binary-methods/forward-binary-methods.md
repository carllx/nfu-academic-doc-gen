# How To: Forward Binary Methods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test forward binary methods

## Prerequisites

**Required Modules:**
- `numbers`
- `operator`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign array = np.array(...)

```python
array = np.array([-1, 0, 1, 2])
```

### Step 2: Assign array_like = ArrayLike(...)

```python
array_like = ArrayLike(array)
```

### Step 3: Assign expected = wrap_array_like(...)

```python
expected = wrap_array_like(op(array, 1))
```

### Step 4: Assign actual = op(...)

```python
actual = op(array_like, 1)
```

### Step 5: Assign err_msg = value

```python
err_msg = f'failed for operator {op}'
```

### Step 6: Call _assert_equal_type_and_value()

```python
_assert_equal_type_and_value(expected, actual, err_msg=err_msg)
```


## Complete Example

```python
# Workflow
array = np.array([-1, 0, 1, 2])
array_like = ArrayLike(array)
for op in _ALL_BINARY_OPERATORS:
    expected = wrap_array_like(op(array, 1))
    actual = op(array_like, 1)
    err_msg = f'failed for operator {op}'
    _assert_equal_type_and_value(expected, actual, err_msg=err_msg)
```

## Next Steps


---

*Source: test_mixins.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*