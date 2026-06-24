# How To: Subarray From Array Construction

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subarray from array construction

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy._core._rational_tests`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2])
```

**Verification:**
```python
assert_array_equal(res, [[1, 1], [2, 2]])
```

### Step 2: Assign res = arr.astype(...)

```python
res = arr.astype('2i')
```

**Verification:**
```python
assert_array_equal(res, [[1, 1], [2, 2]])
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(res, [[1, 1], [2, 2]])
```

**Verification:**
```python
assert_array_equal(res, [[[1, 1], [2, 2]], [[1, 1], [2, 2]]])
```

### Step 4: Assign res = np.array(...)

```python
res = np.array(arr, dtype='(2,)i')
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(res, [[1, 1], [2, 2]])
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 6: Assign res = np.array(...)

```python
res = np.array([[(1,), (2,)], arr], dtype='2i')
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res, [[[1, 1], [2, 2]], [[1, 1], [2, 2]]])
```

### Step 8: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(5 * 2).reshape(5, 2)
```

### Step 9: Assign expected = np.broadcast_to(...)

```python
expected = np.broadcast_to(arr[:, :, np.newaxis, np.newaxis], (5, 2, 2, 2))
```

### Step 10: Assign res = arr.astype(...)

```python
res = arr.astype('(2,2)f')
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 12: Assign res = np.array(...)

```python
res = np.array(arr, dtype='(2,2)f')
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2])
res = arr.astype('2i')
assert_array_equal(res, [[1, 1], [2, 2]])
res = np.array(arr, dtype='(2,)i')
assert_array_equal(res, [[1, 1], [2, 2]])
res = np.array([[(1,), (2,)], arr], dtype='2i')
assert_array_equal(res, [[[1, 1], [2, 2]], [[1, 1], [2, 2]]])
arr = np.arange(5 * 2).reshape(5, 2)
expected = np.broadcast_to(arr[:, :, np.newaxis, np.newaxis], (5, 2, 2, 2))
res = arr.astype('(2,2)f')
assert_array_equal(res, expected)
res = np.array(arr, dtype='(2,2)f')
assert_array_equal(res, expected)
```

## Next Steps


---

*Source: test_array_coercion.py:859 | Complexity: Advanced | Last updated: 2026-06-02*