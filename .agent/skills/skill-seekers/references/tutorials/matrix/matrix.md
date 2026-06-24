# How To: Matrix

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matrix

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: vals
```

## Step-by-Step Guide

### Step 1: Assign b = zeros(...)

```python
b = zeros((5,))
```

**Verification:**
```python
assert_equal(diag(vals), b)
```

### Step 2: Call assert_equal()

```python
assert_equal(diag(vals), b)
```

**Verification:**
```python
assert_equal(diag(vals, 2), b[:3])
```

### Step 3: Assign b = value

```python
b = b * 0
```

**Verification:**
```python
assert_equal(diag(vals, -2), b[:3])
```

### Step 4: Call assert_equal()

```python
assert_equal(diag(vals, 2), b[:3])
```

### Step 5: Call assert_equal()

```python
assert_equal(diag(vals, -2), b[:3])
```

### Step 6: Assign vals = unknown.astype(...)

```python
vals = (100 * get_mat(5) + 1).astype('l')
```

### Step 7: Assign unknown = value

```python
b[k] = vals[k, k]
```

### Step 8: Assign unknown = value

```python
b[k] = vals[k, k + 2]
```

### Step 9: Assign unknown = value

```python
b[k] = vals[k + 2, k]
```


## Complete Example

```python
# Setup
# Fixtures: vals

# Workflow
if vals is None:
    vals = (100 * get_mat(5) + 1).astype('l')
b = zeros((5,))
for k in range(5):
    b[k] = vals[k, k]
assert_equal(diag(vals), b)
b = b * 0
for k in range(3):
    b[k] = vals[k, k + 2]
assert_equal(diag(vals, 2), b[:3])
for k in range(3):
    b[k] = vals[k + 2, k]
assert_equal(diag(vals, -2), b[:3])
```

## Next Steps


---

*Source: test_twodim_base.py:145 | Complexity: Advanced | Last updated: 2026-06-02*