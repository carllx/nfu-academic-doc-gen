# How To: Outer Out Param

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test outer out param

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

### Step 1: Assign arr1 = np.ones(...)

```python
arr1 = np.ones((5,))
```

**Verification:**
```python
assert_equal(res1, out1)
```

### Step 2: Assign arr2 = np.ones(...)

```python
arr2 = np.ones((2,))
```

**Verification:**
```python
assert_equal(np.outer(arr2, arr3, out2), out2)
```

### Step 3: Assign arr3 = np.linspace(...)

```python
arr3 = np.linspace(-2, 2, 5)
```

### Step 4: Assign out1 = np.ndarray(...)

```python
out1 = np.ndarray(shape=(5, 5))
```

### Step 5: Assign out2 = np.ndarray(...)

```python
out2 = np.ndarray(shape=(2, 5))
```

### Step 6: Assign res1 = np.outer(...)

```python
res1 = np.outer(arr1, arr3, out1)
```

### Step 7: Call assert_equal()

```python
assert_equal(res1, out1)
```

### Step 8: Call assert_equal()

```python
assert_equal(np.outer(arr2, arr3, out2), out2)
```


## Complete Example

```python
# Workflow
arr1 = np.ones((5,))
arr2 = np.ones((2,))
arr3 = np.linspace(-2, 2, 5)
out1 = np.ndarray(shape=(5, 5))
out2 = np.ndarray(shape=(2, 5))
res1 = np.outer(arr1, arr3, out1)
assert_equal(res1, out1)
assert_equal(np.outer(arr2, arr3, out2), out2)
```

## Next Steps


---

*Source: test_numeric.py:4047 | Complexity: Advanced | Last updated: 2026-06-02*