# How To: Aligned Size

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aligned size

## Prerequisites

**Required Modules:**
- `contextlib`
- `ctypes`
- `gc`
- `inspect`
- `operator`
- `pickle`
- `sys`
- `types`
- `itertools`
- `typing`
- `hypothesis`
- `pytest`
- `hypothesis.extra`
- `numpy`
- `numpy.dtypes`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype('i4, i1', align=True)
```

**Verification:**
```python
assert_equal(dt.itemsize, 8)
```

### Step 2: Call assert_equal()

```python
assert_equal(dt.itemsize, 8)
```

**Verification:**
```python
assert_equal(dt.itemsize, 8)
```

### Step 3: Assign dt = np.dtype(...)

```python
dt = np.dtype([('f0', 'i4'), ('f1', 'i1')], align=True)
```

**Verification:**
```python
assert_equal(dt.itemsize, 8)
```

### Step 4: Call assert_equal()

```python
assert_equal(dt.itemsize, 8)
```

**Verification:**
```python
assert_equal(dt.itemsize, 8)
```

### Step 5: Assign dt = np.dtype(...)

```python
dt = np.dtype({'names': ['f0', 'f1'], 'formats': ['i4', 'u1'], 'offsets': [0, 4]}, align=True)
```

**Verification:**
```python
assert_equal(dt1.itemsize, 20)
```

### Step 6: Call assert_equal()

```python
assert_equal(dt.itemsize, 8)
```

**Verification:**
```python
assert_equal(dt2.itemsize, 20)
```

### Step 7: Assign dt = np.dtype(...)

```python
dt = np.dtype({'f0': ('i4', 0), 'f1': ('u1', 4)}, align=True)
```

**Verification:**
```python
assert_equal(dt3.itemsize, 20)
```

### Step 8: Call assert_equal()

```python
assert_equal(dt.itemsize, 8)
```

**Verification:**
```python
assert_equal(dt1, dt2)
```

### Step 9: Assign dt1 = np.dtype(...)

```python
dt1 = np.dtype([('f0', 'i4'), ('f1', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')]), ('f2', 'i1')], align=True)
```

**Verification:**
```python
assert_equal(dt2, dt3)
```

### Step 10: Call assert_equal()

```python
assert_equal(dt1.itemsize, 20)
```

**Verification:**
```python
assert_equal(dt1.itemsize, 11)
```

### Step 11: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['i4', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 'i1'], 'offsets': [0, 4, 16]}, align=True)
```

**Verification:**
```python
assert_equal(dt2.itemsize, 11)
```

### Step 12: Call assert_equal()

```python
assert_equal(dt2.itemsize, 20)
```

**Verification:**
```python
assert_equal(dt3.itemsize, 11)
```

### Step 13: Assign dt3 = np.dtype(...)

```python
dt3 = np.dtype({'f0': ('i4', 0), 'f1': ([('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 4), 'f2': ('i1', 16)}, align=True)
```

**Verification:**
```python
assert_equal(dt1, dt2)
```

### Step 14: Call assert_equal()

```python
assert_equal(dt3.itemsize, 20)
```

**Verification:**
```python
assert_equal(dt2, dt3)
```

### Step 15: Call assert_equal()

```python
assert_equal(dt1, dt2)
```

**Verification:**
```python
assert_equal(dt1.descr, [('a', '|i1'), ('', '|V3'), ('b', [('f0', '<i2'), ('', '|V2'), ('f1', '<f4')], (2,))])
```

### Step 16: Call assert_equal()

```python
assert_equal(dt2, dt3)
```

### Step 17: Assign dt1 = np.dtype(...)

```python
dt1 = np.dtype([('f0', 'i4'), ('f1', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')]), ('f2', 'i1')], align=False)
```

### Step 18: Call assert_equal()

```python
assert_equal(dt1.itemsize, 11)
```

### Step 19: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['i4', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 'i1'], 'offsets': [0, 4, 10]}, align=False)
```

### Step 20: Call assert_equal()

```python
assert_equal(dt2.itemsize, 11)
```

### Step 21: Assign dt3 = np.dtype(...)

```python
dt3 = np.dtype({'f0': ('i4', 0), 'f1': ([('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 4), 'f2': ('i1', 10)}, align=False)
```

### Step 22: Call assert_equal()

```python
assert_equal(dt3.itemsize, 11)
```

### Step 23: Call assert_equal()

```python
assert_equal(dt1, dt2)
```

### Step 24: Call assert_equal()

```python
assert_equal(dt2, dt3)
```

### Step 25: Assign dt1 = np.dtype(...)

```python
dt1 = np.dtype([('a', '|i1'), ('b', [('f0', '<i2'), ('f1', '<f4')], 2)], align=True)
```

### Step 26: Call assert_equal()

```python
assert_equal(dt1.descr, [('a', '|i1'), ('', '|V3'), ('b', [('f0', '<i2'), ('', '|V2'), ('f1', '<f4')], (2,))])
```


## Complete Example

```python
# Workflow
dt = np.dtype('i4, i1', align=True)
assert_equal(dt.itemsize, 8)
dt = np.dtype([('f0', 'i4'), ('f1', 'i1')], align=True)
assert_equal(dt.itemsize, 8)
dt = np.dtype({'names': ['f0', 'f1'], 'formats': ['i4', 'u1'], 'offsets': [0, 4]}, align=True)
assert_equal(dt.itemsize, 8)
dt = np.dtype({'f0': ('i4', 0), 'f1': ('u1', 4)}, align=True)
assert_equal(dt.itemsize, 8)
dt1 = np.dtype([('f0', 'i4'), ('f1', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')]), ('f2', 'i1')], align=True)
assert_equal(dt1.itemsize, 20)
dt2 = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['i4', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 'i1'], 'offsets': [0, 4, 16]}, align=True)
assert_equal(dt2.itemsize, 20)
dt3 = np.dtype({'f0': ('i4', 0), 'f1': ([('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 4), 'f2': ('i1', 16)}, align=True)
assert_equal(dt3.itemsize, 20)
assert_equal(dt1, dt2)
assert_equal(dt2, dt3)
dt1 = np.dtype([('f0', 'i4'), ('f1', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')]), ('f2', 'i1')], align=False)
assert_equal(dt1.itemsize, 11)
dt2 = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['i4', [('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 'i1'], 'offsets': [0, 4, 10]}, align=False)
assert_equal(dt2.itemsize, 11)
dt3 = np.dtype({'f0': ('i4', 0), 'f1': ([('f1', 'i1'), ('f2', 'i4'), ('f3', 'i1')], 4), 'f2': ('i1', 10)}, align=False)
assert_equal(dt3.itemsize, 11)
assert_equal(dt1, dt2)
assert_equal(dt2, dt3)
dt1 = np.dtype([('a', '|i1'), ('b', [('f0', '<i2'), ('f1', '<f4')], 2)], align=True)
assert_equal(dt1.descr, [('a', '|i1'), ('', '|V3'), ('b', [('f0', '<i2'), ('', '|V2'), ('f1', '<f4')], (2,))])
```

## Next Steps


---

*Source: test_dtype.py:341 | Complexity: Advanced | Last updated: 2026-06-02*