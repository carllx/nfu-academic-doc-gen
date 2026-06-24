# How To: Unary Ufunc Where Same

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unary ufunc where same

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core._multiarray_tests`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`


## Step-by-Step Guide

### Step 1: Assign ufunc = value

```python
ufunc = np.invert
```

**Verification:**
```python
assert_array_equal(c1, c2)
```

### Step 2: Assign x = np.arange.astype(...)

```python
x = np.arange(100).astype(np.bool)
```

### Step 3: Call check()

```python
check(x, x, x)
```

### Step 4: Call check()

```python
check(x, x.copy(), x)
```

### Step 5: Call check()

```python
check(x, x, x.copy())
```

### Step 6: Assign c1 = ufunc(...)

```python
c1 = ufunc(a, out=out.copy(), where=mask.copy())
```

### Step 7: Assign c2 = ufunc(...)

```python
c2 = ufunc(a, out=out, where=mask)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(c1, c2)
```


## Complete Example

```python
# Workflow
ufunc = np.invert

def check(a, out, mask):
    c1 = ufunc(a, out=out.copy(), where=mask.copy())
    c2 = ufunc(a, out=out, where=mask)
    assert_array_equal(c1, c2)
x = np.arange(100).astype(np.bool)
check(x, x, x)
check(x, x.copy(), x)
check(x, x, x.copy())
```

## Next Steps


---

*Source: test_mem_overlap.py:869 | Complexity: Advanced | Last updated: 2026-06-02*