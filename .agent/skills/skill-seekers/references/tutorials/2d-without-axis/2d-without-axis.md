# How To: 2D Without Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2d without axis

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
i, j = np.ogrid[:4, :4]
```

**Verification:**
```python
assert_array_equal(arr_view, expected)
```

### Step 2: Assign arr = value

```python
arr = 10 * i + j
```

### Step 3: Assign shape = value

```python
shape = (2, 3)
```

### Step 4: Assign arr_view = sliding_window_view(...)

```python
arr_view = sliding_window_view(arr, shape)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([[[[0, 1, 2], [10, 11, 12]], [[1, 2, 3], [11, 12, 13]]], [[[10, 11, 12], [20, 21, 22]], [[11, 12, 13], [21, 22, 23]]], [[[20, 21, 22], [30, 31, 32]], [[21, 22, 23], [31, 32, 33]]]])
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(arr_view, expected)
```


## Complete Example

```python
# Workflow
i, j = np.ogrid[:4, :4]
arr = 10 * i + j
shape = (2, 3)
arr_view = sliding_window_view(arr, shape)
expected = np.array([[[[0, 1, 2], [10, 11, 12]], [[1, 2, 3], [11, 12, 13]]], [[[10, 11, 12], [20, 21, 22]], [[11, 12, 13], [21, 22, 23]]], [[[20, 21, 22], [30, 31, 32]], [[21, 22, 23], [31, 32, 33]]]])
assert_array_equal(arr_view, expected)
```

## Next Steps


---

*Source: test_stride_tricks.py:453 | Complexity: Intermediate | Last updated: 2026-06-02*