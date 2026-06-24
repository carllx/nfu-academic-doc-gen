# How To: Reduceat Empty

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Reduceat should work with empty arrays

## Prerequisites

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`


## Step-by-Step Guide

### Step 1: 'Reduceat should work with empty arrays'

```python
'Reduceat should work with empty arrays'
```

**Verification:**
```python
assert_equal(result.dtype, x.dtype)
```

### Step 2: Assign indices = np.array(...)

```python
indices = np.array([], 'i4')
```

**Verification:**
```python
assert_equal(result.shape, (0,))
```

### Step 3: Assign x = np.array(...)

```python
x = np.array([], 'f8')
```

**Verification:**
```python
assert_equal(result.dtype, x.dtype)
```

### Step 4: Assign result = np.add.reduceat(...)

```python
result = np.add.reduceat(x, indices)
```

**Verification:**
```python
assert_equal(result.shape, (0, 2))
```

### Step 5: Call assert_equal()

```python
assert_equal(result.dtype, x.dtype)
```

**Verification:**
```python
assert_equal(result.dtype, x.dtype)
```

### Step 6: Call assert_equal()

```python
assert_equal(result.shape, (0,))
```

**Verification:**
```python
assert_equal(result.shape, (5, 0))
```

### Step 7: Assign x = np.ones(...)

```python
x = np.ones((5, 2))
```

### Step 8: Assign result = np.add.reduceat(...)

```python
result = np.add.reduceat(x, [], axis=0)
```

### Step 9: Call assert_equal()

```python
assert_equal(result.dtype, x.dtype)
```

### Step 10: Call assert_equal()

```python
assert_equal(result.shape, (0, 2))
```

### Step 11: Assign result = np.add.reduceat(...)

```python
result = np.add.reduceat(x, [], axis=1)
```

### Step 12: Call assert_equal()

```python
assert_equal(result.dtype, x.dtype)
```

### Step 13: Call assert_equal()

```python
assert_equal(result.shape, (5, 0))
```


## Complete Example

```python
# Workflow
'Reduceat should work with empty arrays'
indices = np.array([], 'i4')
x = np.array([], 'f8')
result = np.add.reduceat(x, indices)
assert_equal(result.dtype, x.dtype)
assert_equal(result.shape, (0,))
x = np.ones((5, 2))
result = np.add.reduceat(x, [], axis=0)
assert_equal(result.dtype, x.dtype)
assert_equal(result.shape, (0, 2))
result = np.add.reduceat(x, [], axis=1)
assert_equal(result.dtype, x.dtype)
assert_equal(result.shape, (5, 0))
```

## Next Steps


---

*Source: test_umath.py:4735 | Complexity: Advanced | Last updated: 2026-06-02*