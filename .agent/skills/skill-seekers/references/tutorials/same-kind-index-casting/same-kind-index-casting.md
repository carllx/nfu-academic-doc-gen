# How To: Same Kind Index Casting

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test same kind index casting

## Prerequisites

**Required Modules:**
- `functools`
- `inspect`
- `operator`
- `sys`
- `warnings`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign index = np.arange(...)

```python
index = np.arange(5)
```

**Verification:**
```python
assert_array_equal(arr[index], arr[u_index])
```

### Step 2: Assign u_index = index.astype(...)

```python
u_index = index.astype(np.uintp)
```

**Verification:**
```python
assert_array_equal(arr, np.arange(10))
```

### Step 3: Assign arr = np.arange(...)

```python
arr = np.arange(10)
```

**Verification:**
```python
assert_array_equal(arr[index], arr[u_index])
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(arr[index], arr[u_index])
```

**Verification:**
```python
assert_array_equal(arr, np.arange(5)[:, None].repeat(2, axis=1))
```

### Step 5: Assign unknown = np.arange(...)

```python
arr[u_index] = np.arange(5)
```

**Verification:**
```python
assert_array_equal(arr[u_index, u_index], arr[index, index])
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(arr, np.arange(10))
```

### Step 7: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(10).reshape(5, 2)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(arr[index], arr[u_index])
```

### Step 9: Assign unknown = value

```python
arr[u_index] = np.arange(5)[:, None]
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(arr, np.arange(5)[:, None].repeat(2, axis=1))
```

### Step 11: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(25).reshape(5, 5)
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(arr[u_index, u_index], arr[index, index])
```


## Complete Example

```python
# Workflow
index = np.arange(5)
u_index = index.astype(np.uintp)
arr = np.arange(10)
assert_array_equal(arr[index], arr[u_index])
arr[u_index] = np.arange(5)
assert_array_equal(arr, np.arange(10))
arr = np.arange(10).reshape(5, 2)
assert_array_equal(arr[index], arr[u_index])
arr[u_index] = np.arange(5)[:, None]
assert_array_equal(arr, np.arange(5)[:, None].repeat(2, axis=1))
arr = np.arange(25).reshape(5, 5)
assert_array_equal(arr[u_index, u_index], arr[index, index])
```

## Next Steps


---

*Source: test_indexing.py:108 | Complexity: Advanced | Last updated: 2026-06-02*