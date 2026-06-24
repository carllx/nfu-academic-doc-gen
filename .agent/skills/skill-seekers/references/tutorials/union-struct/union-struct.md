# How To: Union Struct

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union struct

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
dt = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [0, 0, 2]}, align=True)
```

**Verification:**
```python
assert_equal(dt.itemsize, 4)
```

### Step 2: Call assert_equal()

```python
assert_equal(dt.itemsize, 4)
```

**Verification:**
```python
assert_equal(a['f0'], 10 + 36 * 256 * 256)
```

### Step 3: Assign a = np.array.view(...)

```python
a = np.array([3], dtype='<u4').view(dt)
```

**Verification:**
```python
assert_equal(dt.itemsize, 8)
```

### Step 4: Assign unknown = 10

```python
a['f1'] = 10
```

**Verification:**
```python
assert_equal(a.astype(dt2), b)
```

### Step 5: Assign unknown = 36

```python
a['f2'] = 36
```

**Verification:**
```python
assert_equal(b.astype(dt), a)
```

### Step 6: Call assert_equal()

```python
assert_equal(a['f0'], 10 + 36 * 256 * 256)
```

**Verification:**
```python
assert_equal(a.view(dt2), b)
```

### Step 7: Assign dt = np.dtype(...)

```python
dt = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [4, 0, 2]}, align=True)
```

**Verification:**
```python
assert_equal(b.view(dt), a)
```

### Step 8: Call assert_equal()

```python
assert_equal(dt.itemsize, 8)
```

**Verification:**
```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['O', 'i1'], 'offsets': [0, 2]})
```

### Step 9: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype({'names': ['f2', 'f0', 'f1'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [4, 0, 2]}, align=True)
```

**Verification:**
```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', 'O'], 'offsets': [0, 3]})
```

### Step 10: Assign vals = value

```python
vals = [(0, 1, 2), (3, 2 ** 15 - 1, 4)]
```

**Verification:**
```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': [[('a', 'O')], 'i1'], 'offsets': [0, 2]})
```

### Step 11: Assign vals2 = value

```python
vals2 = [(0, 1, 2), (3, 2 ** 15 - 1, 4)]
```

**Verification:**
```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', [('a', 'O')]], 'offsets': [0, 3]})
```

### Step 12: Assign a = np.array(...)

```python
a = np.array(vals, dt)
```

### Step 13: Assign b = np.array(...)

```python
b = np.array(vals2, dt2)
```

### Step 14: Call assert_equal()

```python
assert_equal(a.astype(dt2), b)
```

### Step 15: Call assert_equal()

```python
assert_equal(b.astype(dt), a)
```

### Step 16: Call assert_equal()

```python
assert_equal(a.view(dt2), b)
```

### Step 17: Call assert_equal()

```python
assert_equal(b.view(dt), a)
```

### Step 18: Call assert_raises()

```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['O', 'i1'], 'offsets': [0, 2]})
```

### Step 19: Call assert_raises()

```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', 'O'], 'offsets': [0, 3]})
```

### Step 20: Call assert_raises()

```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': [[('a', 'O')], 'i1'], 'offsets': [0, 2]})
```

### Step 21: Call assert_raises()

```python
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', [('a', 'O')]], 'offsets': [0, 3]})
```

### Step 22: Assign dt = np.dtype(...)

```python
dt = np.dtype({'names': ['f0', 'f1'], 'formats': ['i1', 'O'], 'offsets': [np.dtype('intp').itemsize, 0]})
```


## Complete Example

```python
# Workflow
dt = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [0, 0, 2]}, align=True)
assert_equal(dt.itemsize, 4)
a = np.array([3], dtype='<u4').view(dt)
a['f1'] = 10
a['f2'] = 36
assert_equal(a['f0'], 10 + 36 * 256 * 256)
dt = np.dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [4, 0, 2]}, align=True)
assert_equal(dt.itemsize, 8)
dt2 = np.dtype({'names': ['f2', 'f0', 'f1'], 'formats': ['<u4', '<u2', '<u2'], 'offsets': [4, 0, 2]}, align=True)
vals = [(0, 1, 2), (3, 2 ** 15 - 1, 4)]
vals2 = [(0, 1, 2), (3, 2 ** 15 - 1, 4)]
a = np.array(vals, dt)
b = np.array(vals2, dt2)
assert_equal(a.astype(dt2), b)
assert_equal(b.astype(dt), a)
assert_equal(a.view(dt2), b)
assert_equal(b.view(dt), a)
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['O', 'i1'], 'offsets': [0, 2]})
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', 'O'], 'offsets': [0, 3]})
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': [[('a', 'O')], 'i1'], 'offsets': [0, 2]})
assert_raises(TypeError, np.dtype, {'names': ['f0', 'f1'], 'formats': ['i4', [('a', 'O')]], 'offsets': [0, 3]})
dt = np.dtype({'names': ['f0', 'f1'], 'formats': ['i1', 'O'], 'offsets': [np.dtype('intp').itemsize, 0]})
```

## Next Steps


---

*Source: test_dtype.py:410 | Complexity: Advanced | Last updated: 2026-06-02*