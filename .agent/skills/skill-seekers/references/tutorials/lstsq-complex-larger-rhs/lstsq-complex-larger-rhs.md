# How To: Lstsq Complex Larger Rhs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lstsq complex larger rhs

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign size = 20

```python
size = 20
```

**Verification:**
```python
assert_array_almost_equal(u_lstsq, u)
```

### Step 2: Assign n_rhs = 70

```python
n_rhs = 70
```

### Step 3: Assign G = value

```python
G = np.random.randn(size, size) + 1j * np.random.randn(size, size)
```

### Step 4: Assign u = value

```python
u = np.random.randn(size, n_rhs) + 1j * np.random.randn(size, n_rhs)
```

### Step 5: Assign b = G.dot(...)

```python
b = G.dot(u)
```

### Step 6: Assign unknown = linalg.lstsq(...)

```python
u_lstsq, res, rank, sv = linalg.lstsq(G, b, rcond=None)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(u_lstsq, u)
```


## Complete Example

```python
# Workflow
size = 20
n_rhs = 70
G = np.random.randn(size, size) + 1j * np.random.randn(size, size)
u = np.random.randn(size, n_rhs) + 1j * np.random.randn(size, n_rhs)
b = G.dot(u)
u_lstsq, res, rank, sv = linalg.lstsq(G, b, rcond=None)
assert_array_almost_equal(u_lstsq, u)
```

## Next Steps


---

*Source: test_regression.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*