# How To: Overlap

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overlap

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.arange.reshape(...)

```python
a = np.arange(9, dtype=int).reshape(3, 3)
```

**Verification:**
```python
assert_equal(c, d)
```

### Step 2: Assign b = np.arange.reshape(...)

```python
b = np.arange(9, dtype=int).reshape(3, 3)
```

**Verification:**
```python
assert_equal(c, d)
```

### Step 3: Assign d = np.dot(...)

```python
d = np.dot(a, b)
```

### Step 4: Assign c = np.einsum(...)

```python
c = np.einsum('ij,jk->ik', a, b)
```

### Step 5: Call assert_equal()

```python
assert_equal(c, d)
```

### Step 6: Assign c = np.einsum(...)

```python
c = np.einsum('ij,jk->ik', a, b, out=b)
```

### Step 7: Call assert_equal()

```python
assert_equal(c, d)
```


## Complete Example

```python
# Workflow
a = np.arange(9, dtype=int).reshape(3, 3)
b = np.arange(9, dtype=int).reshape(3, 3)
d = np.dot(a, b)
c = np.einsum('ij,jk->ik', a, b)
assert_equal(c, d)
c = np.einsum('ij,jk->ik', a, b, out=b)
assert_equal(c, d)
```

## Next Steps


---

*Source: test_einsum.py:1315 | Complexity: Intermediate | Last updated: 2026-06-02*