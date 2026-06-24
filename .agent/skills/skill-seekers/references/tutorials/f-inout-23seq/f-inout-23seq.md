# How To: F Inout 23Seq

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test f inout 23seq

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
obj = np.array(self.num23seq, dtype=self.type.dtype, order='F')
```

**Verification:**
```python
assert a.has_shared_memory()
```

### Step 2: Assign shape = value

```python
shape = (len(self.num23seq), len(self.num23seq[0]))
```

### Step 3: Assign a = self.array(...)

```python
a = self.array(shape, intent.in_.inout, obj)
```

**Verification:**
```python
assert a.has_shared_memory()
```

### Step 4: Assign obj = np.array(...)

```python
obj = np.array(self.num23seq, dtype=self.type.dtype, order='C')
```

### Step 5: Assign shape = value

```python
shape = (len(self.num23seq), len(self.num23seq[0]))
```

### Step 6: Assign a = self.array(...)

```python
a = self.array(shape, intent.in_.inout, obj)
```


## Complete Example

```python
# Workflow
obj = np.array(self.num23seq, dtype=self.type.dtype, order='F')
shape = (len(self.num23seq), len(self.num23seq[0]))
a = self.array(shape, intent.in_.inout, obj)
assert a.has_shared_memory()
obj = np.array(self.num23seq, dtype=self.type.dtype, order='C')
shape = (len(self.num23seq), len(self.num23seq[0]))
try:
    a = self.array(shape, intent.in_.inout, obj)
except ValueError as msg:
    if not str(msg).startswith('failed to initialize intent(inout) array'):
        raise
else:
    raise SystemError('intent(inout) should have failed on improper array')
```

## Next Steps


---

*Source: test_array_from_pyobj.py:433 | Complexity: Advanced | Last updated: 2026-06-02*