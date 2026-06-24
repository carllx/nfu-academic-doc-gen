# How To: Check Large Integers

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check large integers

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`


## Step-by-Step Guide

### Step 1: Assign uint64_max = value

```python
uint64_max = 2 ** 64 - 1
```

**Verification:**
```python
assert_array_equal(test, expected)
```

### Step 2: Assign arr = np.full(...)

```python
arr = np.full(5, uint64_max, dtype=np.uint64)
```

**Verification:**
```python
assert_array_equal(test, expected)
```

### Step 3: Assign test = np.pad(...)

```python
test = np.pad(arr, 1, mode='constant', constant_values=arr.min())
```

### Step 4: Assign expected = np.full(...)

```python
expected = np.full(7, uint64_max, dtype=np.uint64)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(test, expected)
```

### Step 6: Assign int64_max = value

```python
int64_max = 2 ** 63 - 1
```

### Step 7: Assign arr = np.full(...)

```python
arr = np.full(5, int64_max, dtype=np.int64)
```

### Step 8: Assign test = np.pad(...)

```python
test = np.pad(arr, 1, mode='constant', constant_values=arr.min())
```

### Step 9: Assign expected = np.full(...)

```python
expected = np.full(7, int64_max, dtype=np.int64)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(test, expected)
```


## Complete Example

```python
# Workflow
uint64_max = 2 ** 64 - 1
arr = np.full(5, uint64_max, dtype=np.uint64)
test = np.pad(arr, 1, mode='constant', constant_values=arr.min())
expected = np.full(7, uint64_max, dtype=np.uint64)
assert_array_equal(test, expected)
int64_max = 2 ** 63 - 1
arr = np.full(5, int64_max, dtype=np.int64)
test = np.pad(arr, 1, mode='constant', constant_values=arr.min())
expected = np.full(7, int64_max, dtype=np.int64)
assert_array_equal(test, expected)
```

## Next Steps


---

*Source: test_arraypad.py:641 | Complexity: Advanced | Last updated: 2026-06-02*