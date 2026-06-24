# How To: Dtype Endianness Repr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: there was an issue where
repr(array([0], dtype='<u2')) and repr(array([0], dtype='>u2'))
both returned the same thing:
array([0], dtype=uint16)
even though their dtypes have different endianness.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`

**Setup Required:**
```python
# Fixtures: native
```

## Step-by-Step Guide

### Step 1: "\n        there was an issue where\n        repr(array([0], dtype='<u2')) and repr(array([0], dtype='>u2'))\n        both returned the same thing:\n        array([0], dtype=uint16)\n        even though their dtypes have different endianness.\n        "

```python
"\n        there was an issue where\n        repr(array([0], dtype='<u2')) and repr(array([0], dtype='>u2'))\n        both returned the same thing:\n        array([0], dtype=uint16)\n        even though their dtypes have different endianness.\n        "
```

**Verification:**
```python
assert ('dtype' in native_repr) ^ (native_dtype in _typelessdata), "an array's repr should show dtype if and only if the type of the array is NOT one of the standard types (e.g., int32, bool, float64)."
```

### Step 2: Assign native_dtype = np.dtype(...)

```python
native_dtype = np.dtype(native)
```

**Verification:**
```python
assert non_native_repr != native_repr
```

### Step 3: Assign non_native_dtype = native_dtype.newbyteorder(...)

```python
non_native_dtype = native_dtype.newbyteorder()
```

**Verification:**
```python
assert f"dtype='{non_native_dtype.byteorder}" in non_native_repr
```

### Step 4: Assign non_native_repr = repr(...)

```python
non_native_repr = repr(np.array([1], non_native_dtype))
```

### Step 5: Assign native_repr = repr(...)

```python
native_repr = repr(np.array([1], native_dtype))
```

**Verification:**
```python
assert ('dtype' in native_repr) ^ (native_dtype in _typelessdata), "an array's repr should show dtype if and only if the type of the array is NOT one of the standard types (e.g., int32, bool, float64)."
```


## Complete Example

```python
# Setup
# Fixtures: native

# Workflow
"\n        there was an issue where\n        repr(array([0], dtype='<u2')) and repr(array([0], dtype='>u2'))\n        both returned the same thing:\n        array([0], dtype=uint16)\n        even though their dtypes have different endianness.\n        "
native_dtype = np.dtype(native)
non_native_dtype = native_dtype.newbyteorder()
non_native_repr = repr(np.array([1], non_native_dtype))
native_repr = repr(np.array([1], native_dtype))
assert ('dtype' in native_repr) ^ (native_dtype in _typelessdata), "an array's repr should show dtype if and only if the type of the array is NOT one of the standard types (e.g., int32, bool, float64)."
if non_native_dtype.itemsize > 1:
    assert non_native_repr != native_repr
    assert f"dtype='{non_native_dtype.byteorder}" in non_native_repr
```

## Next Steps


---

*Source: test_arrayprint.py:1016 | Complexity: Intermediate | Last updated: 2026-06-02*