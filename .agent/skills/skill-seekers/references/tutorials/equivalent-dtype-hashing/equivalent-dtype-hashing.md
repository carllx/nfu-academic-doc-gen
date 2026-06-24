# How To: Equivalent Dtype Hashing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equivalent dtype hashing

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

### Step 1: Assign uintp = np.dtype(...)

```python
uintp = np.dtype(np.uintp)
```

**Verification:**
```python
assert_(left == right)
```

### Step 2: Call assert_()

```python
assert_(left == right)
```

**Verification:**
```python
assert_(hash(left) == hash(right))
```

### Step 3: Call assert_()

```python
assert_(hash(left) == hash(right))
```

### Step 4: Assign left = uintp

```python
left = uintp
```

### Step 5: Assign right = np.dtype(...)

```python
right = np.dtype(np.uint32)
```

### Step 6: Assign left = uintp

```python
left = uintp
```

### Step 7: Assign right = np.dtype(...)

```python
right = np.dtype(np.ulonglong)
```


## Complete Example

```python
# Workflow
uintp = np.dtype(np.uintp)
if uintp.itemsize == 4:
    left = uintp
    right = np.dtype(np.uint32)
else:
    left = uintp
    right = np.dtype(np.ulonglong)
assert_(left == right)
assert_(hash(left) == hash(right))
```

## Next Steps


---

*Source: test_dtype.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*