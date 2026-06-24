# How To: 2D With Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2d with axis

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._rational_tests`
- `numpy.lib._stride_tricks_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
i, j = np.ogrid[:3, :4]
```

**Verification:**
```python
assert_array_equal(arr_view, expected)
```

### Step 2: Assign arr = value

```python
arr = 10 * i + j
```

### Step 3: Assign arr_view = sliding_window_view(...)

```python
arr_view = sliding_window_view(arr, 3, 0)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([[[0, 10, 20], [1, 11, 21], [2, 12, 22], [3, 13, 23]]])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(arr_view, expected)
```


## Complete Example

```python
# Workflow
i, j = np.ogrid[:3, :4]
arr = 10 * i + j
arr_view = sliding_window_view(arr, 3, 0)
expected = np.array([[[0, 10, 20], [1, 11, 21], [2, 12, 22], [3, 13, 23]]])
assert_array_equal(arr_view, expected)
```

## Next Steps


---

*Source: test_stride_tricks.py:431 | Complexity: Intermediate | Last updated: 2026-06-02*