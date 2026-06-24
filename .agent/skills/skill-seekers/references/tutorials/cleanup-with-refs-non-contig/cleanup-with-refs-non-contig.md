# How To: Cleanup With Refs Non Contig

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cleanup with refs non contig

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('O,i')
```

**Verification:**
```python
assert actual_ref_dtype == expected_ref_dtype
```

### Step 2: Assign obj = object(...)

```python
obj = object()
```

**Verification:**
```python
assert actual_ref_obj == actual_ref_dtype
```

### Step 3: Assign expected_ref_dtype = sys.getrefcount(...)

```python
expected_ref_dtype = sys.getrefcount(dtype)
```

### Step 4: Assign expected_ref_obj = sys.getrefcount(...)

```python
expected_ref_obj = sys.getrefcount(obj)
```

### Step 5: Assign proto = np.full(...)

```python
proto = np.full((3, 4, 5, 6, 7), np.array((obj, 2), dtype=dtype))
```

### Step 6: Assign arr = proto.transpose.copy(...)

```python
arr = proto.transpose((2, 0, 3, 1, 4)).copy('K')
```

### Step 7: Assign actual_ref_dtype = sys.getrefcount(...)

```python
actual_ref_dtype = sys.getrefcount(dtype)
```

### Step 8: Assign actual_ref_obj = sys.getrefcount(...)

```python
actual_ref_obj = sys.getrefcount(obj)
```

**Verification:**
```python
assert actual_ref_dtype == expected_ref_dtype
```


## Complete Example

```python
# Workflow
dtype = np.dtype('O,i')
obj = object()
expected_ref_dtype = sys.getrefcount(dtype)
expected_ref_obj = sys.getrefcount(obj)
proto = np.full((3, 4, 5, 6, 7), np.array((obj, 2), dtype=dtype))
arr = proto.transpose((2, 0, 3, 1, 4)).copy('K')
del proto, arr
actual_ref_dtype = sys.getrefcount(dtype)
actual_ref_obj = sys.getrefcount(obj)
assert actual_ref_dtype == expected_ref_dtype
assert actual_ref_obj == actual_ref_dtype
```

## Next Steps


---

*Source: test_arrayobject.py:81 | Complexity: Advanced | Last updated: 2026-06-02*