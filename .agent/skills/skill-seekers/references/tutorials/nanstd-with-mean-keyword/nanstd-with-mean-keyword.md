# How To: Nanstd With Mean Keyword

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanstd with mean keyword

## Prerequisites

**Required Modules:**
- `inspect`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.lib._nanfunctions_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(1234)
```

**Verification:**
```python
assert mean_out is mean
```

### Step 2: Assign A = value

```python
A = rng.randn(10, 20, 5) + 0.5
```

**Verification:**
```python
assert std_out is std
```

### Step 3: Assign unknown = value

```python
A[:, 5, :] = np.nan
```

**Verification:**
```python
assert std.shape == mean.shape
```

### Step 4: Assign mean_out = np.zeros(...)

```python
mean_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert std.shape == (10, 1, 5)
```

### Step 5: Assign std_out = np.zeros(...)

```python
std_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert std_old.shape == mean.shape
```

### Step 6: Assign mean = np.nanmean(...)

```python
mean = np.nanmean(A, out=mean_out, axis=1, keepdims=True)
```

**Verification:**
```python
assert_almost_equal(std, std_old)
```

### Step 7: Assign std = np.nanstd(...)

```python
std = np.nanstd(A, out=std_out, axis=1, keepdims=True, mean=mean)
```

**Verification:**
```python
assert std_out is std
```

### Step 8: Assign std_old = np.nanstd(...)

```python
std_old = np.nanstd(A, axis=1, keepdims=True)
```

**Verification:**
```python
assert std_old.shape == mean.shape
```

### Step 9: Call assert_almost_equal()

```python
assert_almost_equal(std, std_old)
```


## Complete Example

```python
# Workflow
rng = np.random.RandomState(1234)
A = rng.randn(10, 20, 5) + 0.5
A[:, 5, :] = np.nan
mean_out = np.zeros((10, 1, 5))
std_out = np.zeros((10, 1, 5))
mean = np.nanmean(A, out=mean_out, axis=1, keepdims=True)
assert mean_out is mean
std = np.nanstd(A, out=std_out, axis=1, keepdims=True, mean=mean)
assert std_out is std
assert std.shape == mean.shape
assert std.shape == (10, 1, 5)
std_old = np.nanstd(A, axis=1, keepdims=True)
assert std_old.shape == mean.shape
assert_almost_equal(std, std_old)
```

## Next Steps


---

*Source: test_nanfunctions.py:797 | Complexity: Advanced | Last updated: 2026-06-02*