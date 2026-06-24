# How To: Int Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: kind, mix, all_arithmetic_functions
```

## Step-by-Step Guide

### Step 1: Assign op = all_arithmetic_functions

```python
op = all_arithmetic_functions
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype)
```

### Step 2: Assign dtype = value

```python
dtype = np.int64
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype)
```

### Step 3: Assign values = np.array(...)

```python
values = np.array([0, 1, 2, 0, 0, 0, 1, 2, 1, 0], dtype=dtype)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype)
```

### Step 4: Assign rvalues = np.array(...)

```python
rvalues = np.array([2, 0, 2, 3, 0, 0, 1, 5, 2, 0], dtype=dtype)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype)
```

### Step 5: Assign a = SparseArray(...)

```python
a = SparseArray(values, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype)
```

### Step 6: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype)
```

### Step 7: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype, fill_value=1)
```

### Step 8: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b * 0, values, rvalues * 0, mix, op)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype, fill_value=2)
```

### Step 9: Assign a = SparseArray(...)

```python
a = SparseArray(values, fill_value=0, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype)
```

### Step 10: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype)
```

### Step 11: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

### Step 12: Assign a = SparseArray(...)

```python
a = SparseArray(values, fill_value=0, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype)
```

### Step 13: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, fill_value=0, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype)
```

### Step 14: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

### Step 15: Assign a = SparseArray(...)

```python
a = SparseArray(values, fill_value=1, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert a.dtype == SparseDtype(dtype, fill_value=1)
```

### Step 16: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, fill_value=2, dtype=dtype, kind=kind)
```

**Verification:**
```python
assert b.dtype == SparseDtype(dtype, fill_value=2)
```

### Step 17: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```


## Complete Example

```python
# Setup
# Fixtures: kind, mix, all_arithmetic_functions

# Workflow
op = all_arithmetic_functions
dtype = np.int64
values = np.array([0, 1, 2, 0, 0, 0, 1, 2, 1, 0], dtype=dtype)
rvalues = np.array([2, 0, 2, 3, 0, 0, 1, 5, 2, 0], dtype=dtype)
a = SparseArray(values, dtype=dtype, kind=kind)
assert a.dtype == SparseDtype(dtype)
b = SparseArray(rvalues, dtype=dtype, kind=kind)
assert b.dtype == SparseDtype(dtype)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
self._check_numeric_ops(a, b * 0, values, rvalues * 0, mix, op)
a = SparseArray(values, fill_value=0, dtype=dtype, kind=kind)
assert a.dtype == SparseDtype(dtype)
b = SparseArray(rvalues, dtype=dtype, kind=kind)
assert b.dtype == SparseDtype(dtype)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
a = SparseArray(values, fill_value=0, dtype=dtype, kind=kind)
assert a.dtype == SparseDtype(dtype)
b = SparseArray(rvalues, fill_value=0, dtype=dtype, kind=kind)
assert b.dtype == SparseDtype(dtype)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
a = SparseArray(values, fill_value=1, dtype=dtype, kind=kind)
assert a.dtype == SparseDtype(dtype, fill_value=1)
b = SparseArray(rvalues, fill_value=2, dtype=dtype, kind=kind)
assert b.dtype == SparseDtype(dtype, fill_value=2)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

## Next Steps


---

*Source: test_arithmetics.py:247 | Complexity: Advanced | Last updated: 2026-06-02*