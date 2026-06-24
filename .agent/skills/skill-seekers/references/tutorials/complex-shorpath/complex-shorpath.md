# How To: Complex Shorpath

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex shortest path

## Prerequisites

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core.function_base`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = value

```python
x = 1.2 + 3.4j
```

### Step 2: Assign y = value

```python
y = np.exp(1j * (np.pi - 0.1)) * x
```

### Step 3: Assign z = np.geomspace(...)

```python
z = np.geomspace(x, y, 5)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([1.2 + 3.4j, -1.47384 + 3.2905616j, -3.33577588 + 1.36842949j, -3.36011056 - 1.30753855j, -1.53343861 - 3.26321406j])
```

### Step 5: Call np.testing.assert_array_almost_equal()

```python
np.testing.assert_array_almost_equal(z, expected)
```


## Complete Example

```python
# Workflow
x = 1.2 + 3.4j
y = np.exp(1j * (np.pi - 0.1)) * x
z = np.geomspace(x, y, 5)
expected = np.array([1.2 + 3.4j, -1.47384 + 3.2905616j, -3.33577588 + 1.36842949j, -3.36011056 - 1.30753855j, -1.53343861 - 3.26321406j])
np.testing.assert_array_almost_equal(z, expected)
```

## Next Steps


---

*Source: test_function_base.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*