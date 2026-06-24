# How To: Matrix Transpose Equals Swapaxes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test matrix transpose equals swapaxes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: shape
```

## Step-by-Step Guide

### Step 1: Assign num_of_axes = len(...)

```python
num_of_axes = len(shape)
```

**Verification:**
```python
assert_array_equal(tgt, ma_arr.mT)
```

### Step 2: Assign vec = np.arange(...)

```python
vec = np.arange(shape[-1])
```

### Step 3: Assign arr = np.broadcast_to(...)

```python
arr = np.broadcast_to(vec, shape)
```

### Step 4: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(42)
```

### Step 5: Assign mask = rng.choice(...)

```python
mask = rng.choice([0, 1], size=shape)
```

### Step 6: Assign ma_arr = masked_array(...)

```python
ma_arr = masked_array(data=arr, mask=mask)
```

### Step 7: Assign tgt = np.swapaxes(...)

```python
tgt = np.swapaxes(arr, num_of_axes - 2, num_of_axes - 1)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(tgt, ma_arr.mT)
```


## Complete Example

```python
# Setup
# Fixtures: shape

# Workflow
num_of_axes = len(shape)
vec = np.arange(shape[-1])
arr = np.broadcast_to(vec, shape)
rng = np.random.default_rng(42)
mask = rng.choice([0, 1], size=shape)
ma_arr = masked_array(data=arr, mask=mask)
tgt = np.swapaxes(arr, num_of_axes - 2, num_of_axes - 1)
assert_array_equal(tgt, ma_arr.mT)
```

## Next Steps


---

*Source: test_arrayobject.py:30 | Complexity: Advanced | Last updated: 2026-06-02*