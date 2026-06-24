# How To: Diag Indices

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diag indices

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._index_tricks_impl`
- `numpy.testing`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign di = diag_indices(...)

```python
di = diag_indices(4)
```

**Verification:**
```python
assert_array_equal(a, np.array([[100, 2, 3, 4], [5, 100, 7, 8], [9, 10, 100, 12], [13, 14, 15, 100]]))
```

### Step 2: Assign a = np.array(...)

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
```

**Verification:**
```python
assert_array_equal(a, np.array([[[1, 0], [0, 0]], [[0, 0], [0, 1]]]))
```

### Step 3: Assign unknown = 100

```python
a[di] = 100
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(a, np.array([[100, 2, 3, 4], [5, 100, 7, 8], [9, 10, 100, 12], [13, 14, 15, 100]]))
```

### Step 5: Assign d3 = diag_indices(...)

```python
d3 = diag_indices(2, 3)
```

### Step 6: Assign a = np.zeros(...)

```python
a = np.zeros((2, 2, 2), int)
```

### Step 7: Assign unknown = 1

```python
a[d3] = 1
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(a, np.array([[[1, 0], [0, 0]], [[0, 0], [0, 1]]]))
```


## Complete Example

```python
# Workflow
di = diag_indices(4)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
a[di] = 100
assert_array_equal(a, np.array([[100, 2, 3, 4], [5, 100, 7, 8], [9, 10, 100, 12], [13, 14, 15, 100]]))
d3 = diag_indices(2, 3)
a = np.zeros((2, 2, 2), int)
a[d3] = 1
assert_array_equal(a, np.array([[[1, 0], [0, 0]], [[0, 0], [0, 1]]]))
```

## Next Steps


---

*Source: test_index_tricks.py:505 | Complexity: Advanced | Last updated: 2026-06-02*