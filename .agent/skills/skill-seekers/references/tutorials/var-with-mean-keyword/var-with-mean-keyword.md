# How To: Var With Mean Keyword

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test var with mean keyword

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
assert var_out is var
```

### Step 3: Assign mean_out = np.zeros(...)

```python
mean_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert var.shape == mean.shape
```

### Step 4: Assign var_out = np.zeros(...)

```python
var_out = np.zeros((10, 1, 5))
```

**Verification:**
```python
assert var.shape == (10, 1, 5)
```

### Step 5: Assign mean = np.mean(...)

```python
mean = np.mean(A, out=mean_out, axis=1, keepdims=True)
```

**Verification:**
```python
assert var_old.shape == mean.shape
```

### Step 6: Assign var = np.var(...)

```python
var = np.var(A, out=var_out, axis=1, keepdims=True, mean=mean)
```

**Verification:**
```python
assert_almost_equal(var, var_old)
```

### Step 7: Assign var_old = np.var(...)

```python
var_old = np.var(A, axis=1, keepdims=True)
```

**Verification:**
```python
assert var_old.shape == mean.shape
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(var, var_old)
```


## Complete Example

```python
# Workflow
rng = np.random.RandomState(1234)
A = rng.randn(10, 20, 5) + 0.5
mean_out = np.zeros((10, 1, 5))
var_out = np.zeros((10, 1, 5))
mean = np.mean(A, out=mean_out, axis=1, keepdims=True)
assert mean_out is mean
var = np.var(A, out=var_out, axis=1, keepdims=True, mean=mean)
assert var_out is var
assert var.shape == mean.shape
assert var.shape == (10, 1, 5)
var_old = np.var(A, axis=1, keepdims=True)
assert var_old.shape == mean.shape
assert_almost_equal(var, var_old)
```

## Next Steps


---

*Source: test_numeric.py:411 | Complexity: Advanced | Last updated: 2026-06-02*