# How To: Basic Ud

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic ud

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

### Step 1: Assign a = get_mat(...)

```python
a = get_mat(4)
```

**Verification:**
```python
assert_equal(np.flip(a, 0), b)
```

### Step 2: Assign b = value

```python
b = a[::-1, :]
```

**Verification:**
```python
assert_equal(np.flip(a, 0), b)
```

### Step 3: Call assert_equal()

```python
assert_equal(np.flip(a, 0), b)
```

### Step 4: Assign a = value

```python
a = [[0, 1, 2], [3, 4, 5]]
```

### Step 5: Assign b = value

```python
b = [[3, 4, 5], [0, 1, 2]]
```

### Step 6: Call assert_equal()

```python
assert_equal(np.flip(a, 0), b)
```


## Complete Example

```python
# Workflow
a = get_mat(4)
b = a[::-1, :]
assert_equal(np.flip(a, 0), b)
a = [[0, 1, 2], [3, 4, 5]]
b = [[3, 4, 5], [0, 1, 2]]
assert_equal(np.flip(a, 0), b)
```

## Next Steps


---

*Source: test_function_base.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*