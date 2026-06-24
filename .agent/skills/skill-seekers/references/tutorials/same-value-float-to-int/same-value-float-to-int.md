# How To: Same Value Float To Int

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test same value float to int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `enum`
- `random`
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.lib.stride_tricks`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: from_dtype, to_dtype
```

## Step-by-Step Guide

### Step 1: Assign arr1 = np.arange(...)

```python
arr1 = np.arange(10, dtype=from_dtype)
```

**Verification:**
```python
assert_array_equal(arr1.astype(to_dtype, casting='same_value'), arr2)
```

### Step 2: Assign aligned = np.empty(...)

```python
aligned = np.empty(arr1.itemsize * arr1.size + 1, 'uint8')
```

**Verification:**
```python
assert_array_equal(unaligned.astype(to_dtype, casting='same_value'), arr2)
```

### Step 3: Assign unaligned = unknown.view(...)

```python
unaligned = aligned[1:].view(arr1.dtype)
```

### Step 4: Assign unknown = arr1

```python
unaligned[:] = arr1
```

### Step 5: Assign arr2 = np.arange(...)

```python
arr2 = np.arange(10, dtype=to_dtype)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(arr1.astype(to_dtype, casting='same_value'), arr2)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(unaligned.astype(to_dtype, casting='same_value'), arr2)
```

### Step 8: Assign arr1_66 = value

```python
arr1_66 = arr1 + 0.666
```

### Step 9: Assign unaligned_66 = value

```python
unaligned_66 = unaligned + 0.66
```

### Step 10: Call arr1_66.astype()

```python
arr1_66.astype(to_dtype, casting='same_value')
```

### Step 11: Call unaligned_66.astype()

```python
unaligned_66.astype(to_dtype, casting='same_value')
```


## Complete Example

```python
# Setup
# Fixtures: from_dtype, to_dtype

# Workflow
arr1 = np.arange(10, dtype=from_dtype)
aligned = np.empty(arr1.itemsize * arr1.size + 1, 'uint8')
unaligned = aligned[1:].view(arr1.dtype)
unaligned[:] = arr1
arr2 = np.arange(10, dtype=to_dtype)
assert_array_equal(arr1.astype(to_dtype, casting='same_value'), arr2)
assert_array_equal(unaligned.astype(to_dtype, casting='same_value'), arr2)
arr1_66 = arr1 + 0.666
unaligned_66 = unaligned + 0.66
with pytest.raises(ValueError):
    arr1_66.astype(to_dtype, casting='same_value')
with pytest.raises(ValueError):
    unaligned_66.astype(to_dtype, casting='same_value')
```

## Next Steps


---

*Source: test_casting_unittests.py:889 | Complexity: Advanced | Last updated: 2026-06-02*