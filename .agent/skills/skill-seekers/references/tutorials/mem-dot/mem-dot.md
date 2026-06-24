# How To: Mem Dot

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mem dot

## Prerequisites

**Required Modules:**
- `copy`
- `gc`
- `pickle`
- `sys`
- `tempfile`
- `warnings`
- `io`
- `itertools`
- `os`
- `pytest`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.testing._private.utils`
- `math`
- `numpy`
- `hashlib`
- `numpy`
- `re`
- `numpy`
- `operator`


## Step-by-Step Guide

### Step 1: Assign x = np.random.randn(...)

```python
x = np.random.randn(0, 1)
```

**Verification:**
```python
assert_equal(_z, np.ones(10))
```

### Step 2: Assign y = np.random.randn(...)

```python
y = np.random.randn(10, 1)
```

**Verification:**
```python
assert_equal(_z, np.ones(10))
```

### Step 3: Assign _z = np.ones(...)

```python
_z = np.ones(10)
```

### Step 4: Assign _dummy = np.empty(...)

```python
_dummy = np.empty((0, 10))
```

### Step 5: Assign z = as_strided(...)

```python
z = as_strided(_z, _dummy.shape, _dummy.strides)
```

### Step 6: Call np.dot()

```python
np.dot(x, np.transpose(y), out=z)
```

### Step 7: Call assert_equal()

```python
assert_equal(_z, np.ones(10))
```

### Step 8: Call np._core.multiarray.dot()

```python
np._core.multiarray.dot(x, np.transpose(y), out=z)
```

### Step 9: Call assert_equal()

```python
assert_equal(_z, np.ones(10))
```


## Complete Example

```python
# Workflow
x = np.random.randn(0, 1)
y = np.random.randn(10, 1)
_z = np.ones(10)
_dummy = np.empty((0, 10))
z = as_strided(_z, _dummy.shape, _dummy.strides)
np.dot(x, np.transpose(y), out=z)
assert_equal(_z, np.ones(10))
np._core.multiarray.dot(x, np.transpose(y), out=z)
assert_equal(_z, np.ones(10))
```

## Next Steps


---

*Source: test_regression.py:204 | Complexity: Advanced | Last updated: 2026-06-02*