# How To: Cumulative Include Initial

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cumulative include initial

## Prerequisites

**Required Modules:**
- `decimal`
- `math`
- `operator`
- `sys`
- `warnings`
- `fractions`
- `functools`
- `hypothesis`
- `hypothesis.strategies`
- `pytest`
- `hypothesis.extra.numpy`
- `numpy`
- `numpy.lib._function_base_impl`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `random`
- `gc`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(8).reshape((2, 2, 2))
```

**Verification:**
```python
assert_array_equal(np.cumulative_sum(arr, axis=1, include_initial=True), expected)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([[[0, 0], [0, 1], [2, 4]], [[0, 0], [4, 5], [10, 12]]])
```

**Verification:**
```python
assert_array_equal(np.cumulative_prod(arr, axis=2, include_initial=True), expected)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(np.cumulative_sum(arr, axis=1, include_initial=True), expected)
```

**Verification:**
```python
assert_array_equal(out, expected)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([[[1, 0, 0], [1, 2, 6]], [[1, 4, 20], [1, 6, 42]]])
```

**Verification:**
```python
assert_array_equal(np.cumulative_prod(np.array([2, 2]), include_initial=True), expected)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(np.cumulative_prod(arr, axis=2, include_initial=True), expected)
```

### Step 6: Assign out = np.zeros(...)

```python
out = np.zeros((3, 2), dtype=np.float64)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([[0, 0], [1, 2], [4, 6]], dtype=np.float64)
```

### Step 8: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(1, 5).reshape((2, 2))
```

### Step 9: Call np.cumulative_sum()

```python
np.cumulative_sum(arr, axis=0, out=out, include_initial=True)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(out, expected)
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([1, 2, 4])
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(np.cumulative_prod(np.array([2, 2]), include_initial=True), expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(8).reshape((2, 2, 2))
expected = np.array([[[0, 0], [0, 1], [2, 4]], [[0, 0], [4, 5], [10, 12]]])
assert_array_equal(np.cumulative_sum(arr, axis=1, include_initial=True), expected)
expected = np.array([[[1, 0, 0], [1, 2, 6]], [[1, 4, 20], [1, 6, 42]]])
assert_array_equal(np.cumulative_prod(arr, axis=2, include_initial=True), expected)
out = np.zeros((3, 2), dtype=np.float64)
expected = np.array([[0, 0], [1, 2], [4, 6]], dtype=np.float64)
arr = np.arange(1, 5).reshape((2, 2))
np.cumulative_sum(arr, axis=0, out=out, include_initial=True)
assert_array_equal(out, expected)
expected = np.array([1, 2, 4])
assert_array_equal(np.cumulative_prod(np.array([2, 2]), include_initial=True), expected)
```

## Next Steps


---

*Source: test_function_base.py:810 | Complexity: Advanced | Last updated: 2026-06-02*