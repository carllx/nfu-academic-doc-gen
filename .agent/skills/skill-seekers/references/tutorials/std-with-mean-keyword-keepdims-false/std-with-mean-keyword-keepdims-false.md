# How To: Std With Mean Keyword Keepdims False

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test std with mean keyword keepdims false

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
assert std.shape == (10, 5)
```

### Step 2: Assign A = value

```python
A = rng.randn(10, 20, 5) + 0.5
```

**Verification:**
```python
assert std_old.shape == mean_old.shape
```

### Step 3: Assign mean = np.mean(...)

```python
mean = np.mean(A, axis=1, keepdims=True)
```

**Verification:**
```python
assert_equal(std, std_old)
```

### Step 4: Assign std = np.std(...)

```python
std = np.std(A, axis=1, keepdims=False, mean=mean)
```

**Verification:**
```python
assert std.shape == (10, 5)
```

### Step 5: Assign std_old = np.std(...)

```python
std_old = np.std(A, axis=1, keepdims=False)
```

### Step 6: Assign mean_old = np.mean(...)

```python
mean_old = np.mean(A, axis=1, keepdims=False)
```

**Verification:**
```python
assert std_old.shape == mean_old.shape
```

### Step 7: Call assert_equal()

```python
assert_equal(std, std_old)
```


## Complete Example

```python
# Workflow
rng = np.random.RandomState(1234)
A = rng.randn(10, 20, 5) + 0.5
mean = np.mean(A, axis=1, keepdims=True)
std = np.std(A, axis=1, keepdims=False, mean=mean)
assert std.shape == (10, 5)
std_old = np.std(A, axis=1, keepdims=False)
mean_old = np.mean(A, axis=1, keepdims=False)
assert std_old.shape == mean_old.shape
assert_equal(std, std_old)
```

## Next Steps


---

*Source: test_numeric.py:446 | Complexity: Intermediate | Last updated: 2026-06-02*