# How To: Nanfunctions Matrices General

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanfunctions matrices general

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign mat = np.matrix(...)

```python
mat = np.matrix(np.eye(3))
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 2: Assign res = f(...)

```python
res = f(mat, axis=0)
```

**Verification:**
```python
assert_(res.shape == (1, 3))
```

### Step 3: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 4: Call assert_()

```python
assert_(res.shape == (1, 3))
```

**Verification:**
```python
assert_(res.shape == (3, 1))
```

### Step 5: Assign res = f(...)

```python
res = f(mat, axis=1)
```

**Verification:**
```python
assert_(np.isscalar(res))
```

### Step 6: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 7: Call assert_()

```python
assert_(res.shape == (3, 1))
```

**Verification:**
```python
assert_(res.shape == (3, 3))
```

### Step 8: Assign res = f(...)

```python
res = f(mat)
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 9: Call assert_()

```python
assert_(np.isscalar(res))
```

**Verification:**
```python
assert_(res.shape == (3, 3))
```

### Step 10: Assign res = f(...)

```python
res = f(mat, axis=0)
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 11: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(res.shape == (1, 3 * 3))
```

### Step 12: Call assert_()

```python
assert_(res.shape == (3, 3))
```

### Step 13: Assign res = f(...)

```python
res = f(mat, axis=1)
```

### Step 14: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

### Step 15: Call assert_()

```python
assert_(res.shape == (3, 3))
```

### Step 16: Assign res = f(...)

```python
res = f(mat)
```

### Step 17: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

### Step 18: Call assert_()

```python
assert_(res.shape == (1, 3 * 3))
```


## Complete Example

```python
# Workflow
mat = np.matrix(np.eye(3))
for f in (np.nanargmin, np.nanargmax, np.nansum, np.nanprod, np.nanmean, np.nanvar, np.nanstd):
    res = f(mat, axis=0)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (1, 3))
    res = f(mat, axis=1)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (3, 1))
    res = f(mat)
    assert_(np.isscalar(res))
for f in (np.nancumsum, np.nancumprod):
    res = f(mat, axis=0)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (3, 3))
    res = f(mat, axis=1)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (3, 3))
    res = f(mat)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (1, 3 * 3))
```

## Next Steps


---

*Source: test_interaction.py:209 | Complexity: Advanced | Last updated: 2026-06-02*