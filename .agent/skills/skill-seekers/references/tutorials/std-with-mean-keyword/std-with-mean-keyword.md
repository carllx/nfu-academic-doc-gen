# How To: Std With Mean Keyword

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test std with mean keyword

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `math`
- `platform`
- `sys`
- `warnings`
- `decimal`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core._rational_tests`
- `numpy._core.numerictypes`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `fractions`
- `numbers`
- `itertools`


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

### Step 3: Assign mean_out = np.zeros(...)

```python
mean_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert std.shape == mean.shape
```

### Step 4: Assign std_out = np.zeros(...)

```python
std_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert std.shape == (10, 1, 5)
```

### Step 5: Assign mean = np.mean(...)

```python
mean = np.mean(A, out=mean_out, axis=1, keepdims=True)
```

**Verification:**
```python
assert std_old.shape == mean.shape
```

### Step 6: Assign std = np.std(...)

```python
std = np.std(A, out=std_out, axis=1, keepdims=True, mean=mean)
```

**Verification:**
```python
assert_almost_equal(std, std_old)
```

### Step 7: Assign std_old = np.std(...)

```python
std_old = np.std(A, axis=1, keepdims=True)
```

**Verification:**
```python
assert std_old.shape == mean.shape
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(std, std_old)
```


## Complete Example

```python
# Workflow
rng = np.random.RandomState(1234)
A = rng.randn(10, 20, 5) + 0.5
mean_out = np.zeros((10, 1, 5))
std_out = np.zeros((10, 1, 5))
mean = np.mean(A, out=mean_out, axis=1, keepdims=True)
assert mean_out is mean
std = np.std(A, out=std_out, axis=1, keepdims=True, mean=mean)
assert std_out is std
assert std.shape == mean.shape
assert std.shape == (10, 1, 5)
std_old = np.std(A, axis=1, keepdims=True)
assert std_old.shape == mean.shape
assert_almost_equal(std, std_old)
```

## Next Steps


---

*Source: test_numeric.py:376 | Complexity: Advanced | Last updated: 2026-06-02*