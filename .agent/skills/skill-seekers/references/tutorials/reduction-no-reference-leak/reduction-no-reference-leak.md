# How To: Reduction No Reference Leak

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reduction no reference leak

## Prerequisites

**Required Modules:**
- `ctypes`
- `inspect`
- `itertools`
- `pickle`
- `sys`
- `warnings`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._operand_flag_tests`
- `numpy._core._rational_tests`
- `numpy._core._umath_tests`
- `numpy._core.umath`
- `numpy.linalg._umath_linalg`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy._core._struct_ufunc_tests`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype=np.int32)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 2: Assign count = sys.getrefcount(...)

```python
count = sys.getrefcount(arr)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 3: Call np.add.reduce()

```python
np.add.reduce(arr, dtype=np.int32, initial=0)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 4: Call np.add.accumulate()

```python
np.add.accumulate(arr, dtype=np.int32)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 5: Call np.add.reduceat()

```python
np.add.reduceat(arr, [0, 1], dtype=np.int32)
```

**Verification:**
```python
assert out_count == sys.getrefcount(out)
```

### Step 6: Assign out = np.empty(...)

```python
out = np.empty((), dtype=np.int32)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 7: Assign out_count = sys.getrefcount(...)

```python
out_count = sys.getrefcount(out)
```

**Verification:**
```python
assert out_count == sys.getrefcount(out)
```

### Step 8: Call np.add.reduce()

```python
np.add.reduce(arr, dtype=np.int32, out=out, initial=0)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 9: Assign out = np.empty(...)

```python
out = np.empty(arr.shape, dtype=np.int32)
```

**Verification:**
```python
assert out_count == sys.getrefcount(out)
```

### Step 10: Assign out_count = sys.getrefcount(...)

```python
out_count = sys.getrefcount(out)
```

### Step 11: Call np.add.accumulate()

```python
np.add.accumulate(arr, dtype=np.int32, out=out)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```

### Step 12: Assign out = np.empty(...)

```python
out = np.empty((2,), dtype=np.int32)
```

### Step 13: Assign out_count = sys.getrefcount(...)

```python
out_count = sys.getrefcount(out)
```

### Step 14: Call np.add.reduceat()

```python
np.add.reduceat(arr, [0, 1], dtype=np.int32, out=out)
```

**Verification:**
```python
assert count == sys.getrefcount(arr)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype=np.int32)
count = sys.getrefcount(arr)
np.add.reduce(arr, dtype=np.int32, initial=0)
assert count == sys.getrefcount(arr)
np.add.accumulate(arr, dtype=np.int32)
assert count == sys.getrefcount(arr)
np.add.reduceat(arr, [0, 1], dtype=np.int32)
assert count == sys.getrefcount(arr)
out = np.empty((), dtype=np.int32)
out_count = sys.getrefcount(out)
np.add.reduce(arr, dtype=np.int32, out=out, initial=0)
assert count == sys.getrefcount(arr)
assert out_count == sys.getrefcount(out)
out = np.empty(arr.shape, dtype=np.int32)
out_count = sys.getrefcount(out)
np.add.accumulate(arr, dtype=np.int32, out=out)
assert count == sys.getrefcount(arr)
assert out_count == sys.getrefcount(out)
out = np.empty((2,), dtype=np.int32)
out_count = sys.getrefcount(out)
np.add.reduceat(arr, [0, 1], dtype=np.int32, out=out)
assert count == sys.getrefcount(arr)
assert out_count == sys.getrefcount(out)
```

## Next Steps


---

*Source: test_ufunc.py:3033 | Complexity: Advanced | Last updated: 2026-06-02*