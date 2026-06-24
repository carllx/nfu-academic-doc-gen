# How To: Endian Bool Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test endian bool indexing

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

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(10.0, dtype='>f8')
```

**Verification:**
```python
assert_array_almost_equal(xa, ya.nonzero())
```

### Step 2: Assign b = np.arange(...)

```python
b = np.arange(10.0, dtype='<f8')
```

**Verification:**
```python
assert_array_almost_equal(xb, yb.nonzero())
```

### Step 3: Assign xa = np.where(...)

```python
xa = np.where((a > 2) & (a < 6))
```

**Verification:**
```python
assert_(np.all(a[ya] > 0.5))
```

### Step 4: Assign xb = np.where(...)

```python
xb = np.where((b > 2) & (b < 6))
```

**Verification:**
```python
assert_(np.all(b[yb] > 0.5))
```

### Step 5: Assign ya = value

```python
ya = (a > 2) & (a < 6)
```

### Step 6: Assign yb = value

```python
yb = (b > 2) & (b < 6)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(xa, ya.nonzero())
```

### Step 8: Call assert_array_almost_equal()

```python
assert_array_almost_equal(xb, yb.nonzero())
```

### Step 9: Call assert_()

```python
assert_(np.all(a[ya] > 0.5))
```

### Step 10: Call assert_()

```python
assert_(np.all(b[yb] > 0.5))
```


## Complete Example

```python
# Workflow
a = np.arange(10.0, dtype='>f8')
b = np.arange(10.0, dtype='<f8')
xa = np.where((a > 2) & (a < 6))
xb = np.where((b > 2) & (b < 6))
ya = (a > 2) & (a < 6)
yb = (b > 2) & (b < 6)
assert_array_almost_equal(xa, ya.nonzero())
assert_array_almost_equal(xb, yb.nonzero())
assert_(np.all(a[ya] > 0.5))
assert_(np.all(b[yb] > 0.5))
```

## Next Steps


---

*Source: test_regression.py:165 | Complexity: Advanced | Last updated: 2026-06-02*