# How To: Vector

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test vector

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign vals = unknown.astype(...)

```python
vals = (100 * arange(5)).astype('l')
```

**Verification:**
```python
assert_equal(diag(vals), b)
```

### Step 2: Assign b = zeros(...)

```python
b = zeros((5, 5))
```

**Verification:**
```python
assert_equal(diag(vals, k=2), b)
```

### Step 3: Call assert_equal()

```python
assert_equal(diag(vals), b)
```

**Verification:**
```python
assert_equal(diag(vals, k=-2), c)
```

### Step 4: Assign b = zeros(...)

```python
b = zeros((7, 7))
```

### Step 5: Assign c = b.copy(...)

```python
c = b.copy()
```

### Step 6: Call assert_equal()

```python
assert_equal(diag(vals, k=2), b)
```

### Step 7: Call assert_equal()

```python
assert_equal(diag(vals, k=-2), c)
```

### Step 8: Assign unknown = value

```python
b[k, k] = vals[k]
```

### Step 9: Assign unknown = value

```python
b[k, k + 2] = vals[k]
```

### Step 10: Assign unknown = value

```python
c[k + 2, k] = vals[k]
```


## Complete Example

```python
# Workflow
vals = (100 * arange(5)).astype('l')
b = zeros((5, 5))
for k in range(5):
    b[k, k] = vals[k]
assert_equal(diag(vals), b)
b = zeros((7, 7))
c = b.copy()
for k in range(5):
    b[k, k + 2] = vals[k]
    c[k + 2, k] = vals[k]
assert_equal(diag(vals, k=2), b)
assert_equal(diag(vals, k=-2), c)
```

## Next Steps


---

*Source: test_twodim_base.py:131 | Complexity: Advanced | Last updated: 2026-06-02*