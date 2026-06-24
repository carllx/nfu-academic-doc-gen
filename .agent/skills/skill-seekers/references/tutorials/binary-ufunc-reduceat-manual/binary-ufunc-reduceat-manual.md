# How To: Binary Ufunc Reduceat Manual

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test binary ufunc reduceat manual

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

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(10000, dtype=np.int16)
```

**Verification:**
```python
assert_array_equal(c1, c2)
```

### Step 2: Call check()

```python
check(np.add, a, a[::-1].copy(), a)
```

### Step 3: Assign a = np.arange(...)

```python
a = np.arange(10000, dtype=np.int16)
```

### Step 4: Call check()

```python
check(np.add, a, a[::-1], a)
```

### Step 5: Assign c1 = ufunc.reduceat(...)

```python
c1 = ufunc.reduceat(a.copy(), ind.copy(), out=out.copy())
```

### Step 6: Assign c2 = ufunc.reduceat(...)

```python
c2 = ufunc.reduceat(a, ind, out=out)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(c1, c2)
```


## Complete Example

```python
# Workflow
def check(ufunc, a, ind, out):
    c1 = ufunc.reduceat(a.copy(), ind.copy(), out=out.copy())
    c2 = ufunc.reduceat(a, ind, out=out)
    assert_array_equal(c1, c2)
a = np.arange(10000, dtype=np.int16)
check(np.add, a, a[::-1].copy(), a)
a = np.arange(10000, dtype=np.int16)
check(np.add, a, a[::-1], a)
```

## Next Steps


---

*Source: test_mem_overlap.py:719 | Complexity: Intermediate | Last updated: 2026-06-02*