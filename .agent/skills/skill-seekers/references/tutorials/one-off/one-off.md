# How To: One Off

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test one off

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._rational_tests`
- `numpy.lib._stride_tricks_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([[1, 2, 3]])
```

**Verification:**
```python
assert_array_equal(bx0, bx)
```

### Step 2: Assign y = np.array(...)

```python
y = np.array([[1], [2], [3]])
```

**Verification:**
```python
assert_array_equal(by0, by)
```

### Step 3: Assign unknown = broadcast_arrays(...)

```python
bx, by = broadcast_arrays(x, y)
```

### Step 4: Assign bx0 = np.array(...)

```python
bx0 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
```

### Step 5: Assign by0 = value

```python
by0 = bx0.T
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(bx0, bx)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(by0, by)
```


## Complete Example

```python
# Workflow
x = np.array([[1, 2, 3]])
y = np.array([[1], [2], [3]])
bx, by = broadcast_arrays(x, y)
bx0 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
by0 = bx0.T
assert_array_equal(bx0, bx)
assert_array_equal(by0, by)
```

## Next Steps


---

*Source: test_stride_tricks.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*