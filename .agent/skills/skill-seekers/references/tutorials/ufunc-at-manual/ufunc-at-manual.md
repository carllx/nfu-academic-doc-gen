# How To: Ufunc At Manual

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ufunc at manual

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
check(np.invert, a[::-1], a)
```

### Step 3: Assign a = np.arange(...)

```python
a = np.arange(100, dtype=np.int16)
```

### Step 4: Assign ind = np.arange(...)

```python
ind = np.arange(0, 100, 2, dtype=np.int16)
```

### Step 5: Call check()

```python
check(np.add, a, ind, a[25:75])
```

### Step 6: Assign a0 = a.copy(...)

```python
a0 = a.copy()
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(c1, c2)
```

### Step 8: Call ufunc.at()

```python
ufunc.at(a0, ind.copy())
```

### Step 9: Assign c1 = a0.copy(...)

```python
c1 = a0.copy()
```

### Step 10: Call ufunc.at()

```python
ufunc.at(a, ind)
```

### Step 11: Assign c2 = a.copy(...)

```python
c2 = a.copy()
```

### Step 12: Call ufunc.at()

```python
ufunc.at(a0, ind.copy(), b.copy())
```

### Step 13: Assign c1 = a0.copy(...)

```python
c1 = a0.copy()
```

### Step 14: Call ufunc.at()

```python
ufunc.at(a, ind, b)
```

### Step 15: Assign c2 = a.copy(...)

```python
c2 = a.copy()
```


## Complete Example

```python
# Workflow
def check(ufunc, a, ind, b=None):
    a0 = a.copy()
    if b is None:
        ufunc.at(a0, ind.copy())
        c1 = a0.copy()
        ufunc.at(a, ind)
        c2 = a.copy()
    else:
        ufunc.at(a0, ind.copy(), b.copy())
        c1 = a0.copy()
        ufunc.at(a, ind, b)
        c2 = a.copy()
    assert_array_equal(c1, c2)
a = np.arange(10000, dtype=np.int16)
check(np.invert, a[::-1], a)
a = np.arange(100, dtype=np.int16)
ind = np.arange(0, 100, 2, dtype=np.int16)
check(np.add, a, ind, a[25:75])
```

## Next Steps


---

*Source: test_mem_overlap.py:777 | Complexity: Advanced | Last updated: 2026-06-02*