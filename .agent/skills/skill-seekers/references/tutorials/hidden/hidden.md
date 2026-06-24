# How To: Hidden

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden

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
a = self.array(shape, intent.hide, None)
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
a = self.array(shape, intent.hide, None)
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
a = self.array(shape, intent.c.hide, None)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 7: Assign shape = value

```python
shape = (-1, 3)
```

**Verification:**
```python
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
```

### Step 8: Assign a = self.array(...)

```python
a = self.array(shape, intent.hide, None)
```

**Verification:**
```python
assert not a.arr.flags['FORTRAN'] and a.arr.flags['CONTIGUOUS']
```


## Complete Example

```python
# Workflow
shape = (2,)
a = self.array(shape, intent.hide, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
shape = (2, 3)
a = self.array(shape, intent.hide, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
assert a.arr.flags['FORTRAN'] and (not a.arr.flags['CONTIGUOUS'])
shape = (2, 3)
a = self.array(shape, intent.c.hide, None)
assert a.arr.shape == shape
assert a.arr_equal(a.arr, np.zeros(shape, dtype=self.type.dtype))
assert not a.arr.flags['FORTRAN'] and a.arr.flags['CONTIGUOUS']
shape = (-1, 3)
try:
    a = self.array(shape, intent.hide, None)
except ValueError as msg:
    if not str(msg).startswith('failed to create intent(cache|hide)|optional array'):
        raise
else:
    raise SystemError('intent(hide) should have failed on undefined dimensions')
```

## Next Steps


---

*Source: test_array_from_pyobj.py:584 | Complexity: Advanced | Last updated: 2026-06-02*