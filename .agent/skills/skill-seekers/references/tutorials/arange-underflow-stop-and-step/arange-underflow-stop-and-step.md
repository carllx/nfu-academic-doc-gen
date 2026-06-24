# How To: Arange Underflow Stop And Step

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arange underflow stop and step

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

### Step 1: Assign finfo = np.finfo(...)

```python
finfo = np.finfo(np.float64)
```

**Verification:**
```python
assert_array_equal(ref, x)
```

### Step 2: Assign ref = np.arange(...)

```python
ref = np.arange(0, finfo.eps, 2 * finfo.eps)
```

**Verification:**
```python
assert_array_equal(ref, x)
```

### Step 3: Assign x = np.arange(...)

```python
x = np.arange(0, finfo.eps, finfo.max)
```

**Verification:**
```python
assert_array_equal(ref, x)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(ref, x)
```

**Verification:**
```python
assert_array_equal(ref, x)
```

### Step 5: Assign ref = np.arange(...)

```python
ref = np.arange(0, finfo.eps, -2 * finfo.eps)
```

### Step 6: Assign x = np.arange(...)

```python
x = np.arange(0, finfo.eps, -finfo.max)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(ref, x)
```

### Step 8: Assign ref = np.arange(...)

```python
ref = np.arange(0, -finfo.eps, -2 * finfo.eps)
```

### Step 9: Assign x = np.arange(...)

```python
x = np.arange(0, -finfo.eps, -finfo.max)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(ref, x)
```

### Step 11: Assign ref = np.arange(...)

```python
ref = np.arange(0, -finfo.eps, 2 * finfo.eps)
```

### Step 12: Assign x = np.arange(...)

```python
x = np.arange(0, -finfo.eps, finfo.max)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(ref, x)
```


## Complete Example

```python
# Workflow
finfo = np.finfo(np.float64)
ref = np.arange(0, finfo.eps, 2 * finfo.eps)
x = np.arange(0, finfo.eps, finfo.max)
assert_array_equal(ref, x)
ref = np.arange(0, finfo.eps, -2 * finfo.eps)
x = np.arange(0, finfo.eps, -finfo.max)
assert_array_equal(ref, x)
ref = np.arange(0, -finfo.eps, -2 * finfo.eps)
x = np.arange(0, -finfo.eps, -finfo.max)
assert_array_equal(ref, x)
ref = np.arange(0, -finfo.eps, 2 * finfo.eps)
x = np.arange(0, -finfo.eps, finfo.max)
assert_array_equal(ref, x)
```

## Next Steps


---

*Source: test_regression.py:243 | Complexity: Advanced | Last updated: 2026-06-02*