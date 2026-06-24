# How To: Inplace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inplace

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

### Step 1: Assign obj = np.array(...)

```python
obj = np.array(self.num23seq, dtype=self.type.dtype)
```

**Verification:**
```python
assert not obj.flags['FORTRAN'] and obj.flags['CONTIGUOUS']
```

### Step 2: Assign shape = value

```python
shape = obj.shape
```

**Verification:**
```python
assert obj[1][2] == a.arr[1][2], repr((obj, a.arr))
```

### Step 3: Assign a = self.array(...)

```python
a = self.array(shape, intent.inplace, obj)
```

**Verification:**
```python
assert obj[1][2] == a.arr[1][2] == np.array(54, dtype=self.type.dtype)
```

### Step 4: Assign unknown = 54

```python
a.arr[1][2] = 54
```

**Verification:**
```python
assert a.arr is obj
```


## Complete Example

```python
# Workflow
obj = np.array(self.num23seq, dtype=self.type.dtype)
assert not obj.flags['FORTRAN'] and obj.flags['CONTIGUOUS']
shape = obj.shape
a = self.array(shape, intent.inplace, obj)
assert obj[1][2] == a.arr[1][2], repr((obj, a.arr))
a.arr[1][2] = 54
assert obj[1][2] == a.arr[1][2] == np.array(54, dtype=self.type.dtype)
assert a.arr is obj
assert obj.flags['FORTRAN']
assert not obj.flags['CONTIGUOUS']
```

## Next Steps


---

*Source: test_array_from_pyobj.py:649 | Complexity: Intermediate | Last updated: 2026-06-02*