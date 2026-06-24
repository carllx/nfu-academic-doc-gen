# How To: Shape Sequence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shape sequence

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3], dtype=np.int16)
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 2: Assign l = value

```python
l = [1, 2, 3]
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape[0], int))
```

### Step 3: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f4', a)])
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 4: Call assert_()

```python
assert_(isinstance(dt['a'].shape, tuple))
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 5: Call assert_()

```python
assert_(isinstance(dt['a'].shape[0], int))
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape[0], int))
```

### Step 6: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f4', l)])
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 7: Call assert_()

```python
assert_(isinstance(dt['a'].shape, tuple))
```

**Verification:**
```python
assert_(isinstance(dt['a'].shape[0], int))
```

### Step 8: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f4', IntLike())])
```

### Step 9: Call assert_()

```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 10: Call assert_()

```python
assert_(isinstance(dt['a'].shape[0], int))
```

### Step 11: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f4', (IntLike(),))])
```

### Step 12: Call assert_()

```python
assert_(isinstance(dt['a'].shape, tuple))
```

### Step 13: Call assert_()

```python
assert_(isinstance(dt['a'].shape[0], int))
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3], dtype=np.int16)
l = [1, 2, 3]
dt = np.dtype([('a', 'f4', a)])
assert_(isinstance(dt['a'].shape, tuple))
assert_(isinstance(dt['a'].shape[0], int))
dt = np.dtype([('a', 'f4', l)])
assert_(isinstance(dt['a'].shape, tuple))

class IntLike:

    def __index__(self):
        return 3

    def __int__(self):
        return 3
dt = np.dtype([('a', 'f4', IntLike())])
assert_(isinstance(dt['a'].shape, tuple))
assert_(isinstance(dt['a'].shape[0], int))
dt = np.dtype([('a', 'f4', (IntLike(),))])
assert_(isinstance(dt['a'].shape, tuple))
assert_(isinstance(dt['a'].shape[0], int))
```

## Next Steps


---

*Source: test_dtype.py:693 | Complexity: Advanced | Last updated: 2026-06-02*