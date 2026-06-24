# How To: Fieldless Void

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fieldless void

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([])
```

**Verification:**
```python
assert_equal(mx.dtype, x.dtype)
```

### Step 2: Assign x = np.empty(...)

```python
x = np.empty(4, dt)
```

**Verification:**
```python
assert_equal(mx.shape, x.shape)
```

### Step 3: Assign mx = np.ma.array(...)

```python
mx = np.ma.array(x)
```

**Verification:**
```python
assert_equal(mx.dtype, x.dtype)
```

### Step 4: Call assert_equal()

```python
assert_equal(mx.dtype, x.dtype)
```

**Verification:**
```python
assert_equal(mx.shape, x.shape)
```

### Step 5: Call assert_equal()

```python
assert_equal(mx.shape, x.shape)
```

### Step 6: Assign mx = np.ma.array(...)

```python
mx = np.ma.array(x, mask=x)
```

### Step 7: Call assert_equal()

```python
assert_equal(mx.dtype, x.dtype)
```

### Step 8: Call assert_equal()

```python
assert_equal(mx.shape, x.shape)
```


## Complete Example

```python
# Workflow
dt = np.dtype([])
x = np.empty(4, dt)
mx = np.ma.array(x)
assert_equal(mx.dtype, x.dtype)
assert_equal(mx.shape, x.shape)
mx = np.ma.array(x, mask=x)
assert_equal(mx.dtype, x.dtype)
assert_equal(mx.shape, x.shape)
```

## Next Steps


---

*Source: test_core.py:5860 | Complexity: Advanced | Last updated: 2026-06-02*