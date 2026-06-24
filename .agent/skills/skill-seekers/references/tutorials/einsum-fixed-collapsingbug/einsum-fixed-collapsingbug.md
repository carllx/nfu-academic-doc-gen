# How To: Einsum Fixed Collapsingbug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test einsum fixed collapsingbug

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.random.normal(...)

```python
x = np.random.normal(0, 1, (5, 5, 5, 5))
```

**Verification:**
```python
assert_equal(y1, y2)
```

### Step 2: Assign y1 = np.zeros(...)

```python
y1 = np.zeros((5, 5))
```

### Step 3: Call np.einsum()

```python
np.einsum('aabb->ab', x, out=y1)
```

### Step 4: Assign idx = np.arange(...)

```python
idx = np.arange(5)
```

### Step 5: Assign y2 = value

```python
y2 = x[idx[:, None], idx[:, None], idx, idx]
```

### Step 6: Call assert_equal()

```python
assert_equal(y1, y2)
```


## Complete Example

```python
# Workflow
x = np.random.normal(0, 1, (5, 5, 5, 5))
y1 = np.zeros((5, 5))
np.einsum('aabb->ab', x, out=y1)
idx = np.arange(5)
y2 = x[idx[:, None], idx[:, None], idx, idx]
assert_equal(y1, y2)
```

## Next Steps


---

*Source: test_einsum.py:863 | Complexity: Intermediate | Last updated: 2026-06-02*