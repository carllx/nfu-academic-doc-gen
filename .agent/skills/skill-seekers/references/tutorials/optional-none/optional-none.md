# How To: Optional None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test optional none

## Prerequisites

**Required Modules:**
- `copy`
- `platform`
- `sys`
- `pathlib`
- `pytest`
- `numpy`
- `numpy._core._type_aliases`


## Step-by-Step Guide

### Step 1: Assign shape = value

```python
shape = (2,)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 2: Assign a = self.array(...)

```python
a = self.array(shape, intent.optional, None)
```

**Verification:**
```python
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
```

### Step 3: Assign shape = value

```python
shape = (2, 3)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 4: Assign a = self.array(...)

```python
a = self.array(shape, intent.optional, None)
```

**Verification:**
```python
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
```

### Step 5: Assign shape = value

```python
shape = (2, 3)
```

**Verification:**
```python
assert a.arr.flags['FORTRAN'] and (not a.arr.flags['CONTIGUOUS'])
```

### Step 6: Assign a = self.array(...)

```python
a = self.array(shape, intent.c.optional, None)
```

**Verification:**
```python
assert a.arr.shape == shape
```


## Complete Example

```python
# Workflow
shape = (2,)
a = self.array(shape, intent.optional, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
shape = (2, 3)
a = self.array(shape, intent.optional, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
assert a.arr.flags['FORTRAN'] and (not a.arr.flags['CONTIGUOUS'])
shape = (2, 3)
a = self.array(shape, intent.c.optional, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
assert not a.arr.flags['FORTRAN'] and a.arr.flags['CONTIGUOUS']
```

## Next Steps


---

*Source: test_array_from_pyobj.py:613 | Complexity: Intermediate | Last updated: 2026-06-02*