# How To: Different Paths

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test different paths

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert res == arr.sum()
```

### Step 2: Assign arr = unknown.astype(...)

```python
arr = (np.arange(7) + 0.5).astype(dtype)
```

**Verification:**
```python
assert_array_equal(res, arr * arr)
```

### Step 3: Assign scalar = np.array(...)

```python
scalar = np.array(2, dtype=dtype)
```

**Verification:**
```python
assert_array_equal(res, arr * arr)
```

### Step 4: Assign res = np.einsum(...)

```python
res = np.einsum('i->', arr)
```

**Verification:**
```python
assert np.einsum('i,i->', arr, arr) == (arr * arr).sum()
```

### Step 5: Assign res = np.einsum(...)

```python
res = np.einsum('i,i->i', arr, arr)
```

**Verification:**
```python
assert_array_equal(res, arr * dtype.type(2))
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, arr * arr)
```

**Verification:**
```python
assert_array_equal(res, arr * dtype.type(2))
```

### Step 7: Assign res = np.einsum(...)

```python
res = np.einsum('i,i->i', arr.repeat(2)[::2], arr.repeat(2)[::2])
```

**Verification:**
```python
assert res == np.einsum('i->', scalar * arr)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(res, arr * arr)
```

**Verification:**
```python
assert res == np.einsum('i->', scalar * arr)
```

### Step 9: Assign out = np.ones(...)

```python
out = np.ones(7, dtype=dtype)
```

**Verification:**
```python
assert_array_equal(res, (arr * arr * arr).sum())
```

### Step 10: Assign res = np.einsum(...)

```python
res = np.einsum('i,->i', arr, dtype.type(2), out=out)
```

**Verification:**
```python
assert_array_equal(res, (arr * arr * arr * arr).sum())
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(res, arr * dtype.type(2))
```

### Step 12: Assign res = np.einsum(...)

```python
res = np.einsum(',i->i', scalar, arr)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(res, arr * dtype.type(2))
```

### Step 14: Assign res = np.einsum(...)

```python
res = np.einsum(',i->', scalar, arr)
```

**Verification:**
```python
assert res == np.einsum('i->', scalar * arr)
```

### Step 15: Assign res = np.einsum(...)

```python
res = np.einsum('i,->', arr, scalar)
```

**Verification:**
```python
assert res == np.einsum('i->', scalar * arr)
```

### Step 16: Assign arr = np.array(...)

```python
arr = np.array([0.5, 0.5, 0.25, 4.5, 3.0], dtype=dtype)
```

### Step 17: Assign res = np.einsum(...)

```python
res = np.einsum('i,i,i->', arr, arr, arr)
```

### Step 18: Call assert_array_equal()

```python
assert_array_equal(res, (arr * arr * arr).sum())
```

### Step 19: Assign res = np.einsum(...)

```python
res = np.einsum('i,i,i,i->', arr, arr, arr, arr)
```

### Step 20: Call assert_array_equal()

```python
assert_array_equal(res, (arr * arr * arr * arr).sum())
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
dtype = np.dtype(dtype)
arr = (np.arange(7) + 0.5).astype(dtype)
scalar = np.array(2, dtype=dtype)
res = np.einsum('i->', arr)
assert res == arr.sum()
res = np.einsum('i,i->i', arr, arr)
assert_array_equal(res, arr * arr)
res = np.einsum('i,i->i', arr.repeat(2)[::2], arr.repeat(2)[::2])
assert_array_equal(res, arr * arr)
assert np.einsum('i,i->', arr, arr) == (arr * arr).sum()
out = np.ones(7, dtype=dtype)
res = np.einsum('i,->i', arr, dtype.type(2), out=out)
assert_array_equal(res, arr * dtype.type(2))
res = np.einsum(',i->i', scalar, arr)
assert_array_equal(res, arr * dtype.type(2))
res = np.einsum(',i->', scalar, arr)
assert res == np.einsum('i->', scalar * arr)
res = np.einsum('i,->', arr, scalar)
assert res == np.einsum('i->', scalar * arr)
arr = np.array([0.5, 0.5, 0.25, 4.5, 3.0], dtype=dtype)
res = np.einsum('i,i,i->', arr, arr, arr)
assert_array_equal(res, (arr * arr * arr).sum())
res = np.einsum('i,i,i,i->', arr, arr, arr, arr)
assert_array_equal(res, (arr * arr * arr * arr).sum())
```

## Next Steps


---

*Source: test_einsum.py:906 | Complexity: Advanced | Last updated: 2026-06-02*