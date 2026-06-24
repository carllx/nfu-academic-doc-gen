# How To: Method Args

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test method args

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

### Step 1: Assign funcs1 = value

```python
funcs1 = ['argmax', 'argmin', 'sum', 'any', 'all', 'cumsum', 'cumprod', 'prod', 'std', 'var', 'mean', 'round', 'min', 'max', 'argsort', 'sort']
```

**Verification:**
```python
assert_((res1 == res2).all(), func)
```

### Step 2: Assign funcs2 = value

```python
funcs2 = ['compress', 'take', 'repeat']
```

**Verification:**
```python
assert_(abs(res1 - res2).max() < 1e-08, func)
```

### Step 3: Assign arr = np.random.rand(...)

```python
arr = np.random.rand(8, 7)
```

**Verification:**
```python
assert_(abs(res1 - res2).max() < 1e-08, func)
```

### Step 4: Assign arr2 = arr.copy(...)

```python
arr2 = arr.copy()
```

### Step 5: Assign res1 = getattr(...)

```python
res1 = getattr(arr, func)()
```

### Step 6: Assign res2 = getattr(...)

```python
res2 = getattr(np, func)(arr2)
```

### Step 7: Assign arr1 = np.random.rand(...)

```python
arr1 = np.random.rand(8, 7)
```

### Step 8: Assign arr2 = np.random.rand(...)

```python
arr2 = np.random.rand(8, 7)
```

### Step 9: Assign res1 = None

```python
res1 = None
```

### Step 10: Assign res2 = getattr(...)

```python
res2 = getattr(np, func)(arr1, arr2)
```

### Step 11: Call assert_()

```python
assert_(abs(res1 - res2).max() < 1e-08, func)
```

### Step 12: Assign res1 = arr

```python
res1 = arr
```

### Step 13: Call assert_()

```python
assert_((res1 == res2).all(), func)
```

### Step 14: Call assert_()

```python
assert_(abs(res1 - res2).max() < 1e-08, func)
```

### Step 15: Assign arr1 = arr1.ravel(...)

```python
arr1 = arr1.ravel()
```

### Step 16: Assign res1 = getattr(...)

```python
res1 = getattr(arr2, func)(arr1)
```

### Step 17: Assign arr2 = unknown.astype.ravel(...)

```python
arr2 = (15 * arr2).astype(int).ravel()
```

### Step 18: Assign res1 = getattr(...)

```python
res1 = getattr(arr1, func)(arr2)
```


## Complete Example

```python
# Workflow
funcs1 = ['argmax', 'argmin', 'sum', 'any', 'all', 'cumsum', 'cumprod', 'prod', 'std', 'var', 'mean', 'round', 'min', 'max', 'argsort', 'sort']
funcs2 = ['compress', 'take', 'repeat']
for func in funcs1:
    arr = np.random.rand(8, 7)
    arr2 = arr.copy()
    res1 = getattr(arr, func)()
    res2 = getattr(np, func)(arr2)
    if res1 is None:
        res1 = arr
    if res1.dtype.kind in 'uib':
        assert_((res1 == res2).all(), func)
    else:
        assert_(abs(res1 - res2).max() < 1e-08, func)
for func in funcs2:
    arr1 = np.random.rand(8, 7)
    arr2 = np.random.rand(8, 7)
    res1 = None
    if func == 'compress':
        arr1 = arr1.ravel()
        res1 = getattr(arr2, func)(arr1)
    else:
        arr2 = (15 * arr2).astype(int).ravel()
    if res1 is None:
        res1 = getattr(arr1, func)(arr2)
    res2 = getattr(np, func)(arr1, arr2)
    assert_(abs(res1 - res2).max() < 1e-08, func)
```

## Next Steps


---

*Source: test_regression.py:525 | Complexity: Advanced | Last updated: 2026-06-02*