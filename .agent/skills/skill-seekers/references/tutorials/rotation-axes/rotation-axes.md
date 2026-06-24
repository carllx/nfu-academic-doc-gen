# How To: Rotation Axes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rotation axes

## Prerequisites

**Required Modules:**
- `decimal`
- `math`
- `operator`
- `sys`
- `warnings`
- `fractions`
- `functools`
- `hypothesis`
- `hypothesis.strategies`
- `pytest`
- `hypothesis.extra.numpy`
- `numpy`
- `numpy.lib._function_base_impl`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `random`
- `gc`


## Step-by-Step Guide

### Step 1: Assign a = np.arange.reshape(...)

```python
a = np.arange(8).reshape((2, 2, 2))
```

**Verification:**
```python
assert_equal(rot90(a, axes=(0, 1)), a_rot90_01)
```

### Step 2: Assign a_rot90_01 = value

```python
a_rot90_01 = [[[2, 3], [6, 7]], [[0, 1], [4, 5]]]
```

**Verification:**
```python
assert_equal(rot90(a, axes=(1, 0)), a_rot90_10)
```

### Step 3: Assign a_rot90_12 = value

```python
a_rot90_12 = [[[1, 3], [0, 2]], [[5, 7], [4, 6]]]
```

**Verification:**
```python
assert_equal(rot90(a, axes=(1, 2)), a_rot90_12)
```

### Step 4: Assign a_rot90_20 = value

```python
a_rot90_20 = [[[4, 0], [6, 2]], [[5, 1], [7, 3]]]
```

**Verification:**
```python
assert_equal(rot90(a, k=k, axes=(2, 0)), rot90(a_rot90_20, k=k - 1, axes=(2, 0)))
```

### Step 5: Assign a_rot90_10 = value

```python
a_rot90_10 = [[[4, 5], [0, 1]], [[6, 7], [2, 3]]]
```

### Step 6: Call assert_equal()

```python
assert_equal(rot90(a, axes=(0, 1)), a_rot90_01)
```

### Step 7: Call assert_equal()

```python
assert_equal(rot90(a, axes=(1, 0)), a_rot90_10)
```

### Step 8: Call assert_equal()

```python
assert_equal(rot90(a, axes=(1, 2)), a_rot90_12)
```

### Step 9: Call assert_equal()

```python
assert_equal(rot90(a, k=k, axes=(2, 0)), rot90(a_rot90_20, k=k - 1, axes=(2, 0)))
```


## Complete Example

```python
# Workflow
a = np.arange(8).reshape((2, 2, 2))
a_rot90_01 = [[[2, 3], [6, 7]], [[0, 1], [4, 5]]]
a_rot90_12 = [[[1, 3], [0, 2]], [[5, 7], [4, 6]]]
a_rot90_20 = [[[4, 0], [6, 2]], [[5, 1], [7, 3]]]
a_rot90_10 = [[[4, 5], [0, 1]], [[6, 7], [2, 3]]]
assert_equal(rot90(a, axes=(0, 1)), a_rot90_01)
assert_equal(rot90(a, axes=(1, 0)), a_rot90_10)
assert_equal(rot90(a, axes=(1, 2)), a_rot90_12)
for k in range(1, 5):
    assert_equal(rot90(a, k=k, axes=(2, 0)), rot90(a_rot90_20, k=k - 1, axes=(2, 0)))
```

## Next Steps


---

*Source: test_function_base.py:124 | Complexity: Advanced | Last updated: 2026-06-02*