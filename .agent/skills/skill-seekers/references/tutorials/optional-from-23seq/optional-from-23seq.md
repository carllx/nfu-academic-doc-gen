# How To: Optional From 23Seq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test optional from 23seq

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

### Step 1: Assign obj = value

```python
obj = self.num23seq
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 2: Assign shape = value

```python
shape = (len(obj), len(obj[0]))
```

**Verification:**
```python
assert not a.has_shared_memory()
```

### Step 3: Assign a = self.array(...)

```python
a = self.array(shape, intent.optional, obj)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 4: Assign a = self.array(...)

```python
a = self.array(shape, intent.optional.c, obj)
```

**Verification:**
```python
assert not a.has_shared_memory()
```


## Complete Example

```python
# Workflow
obj = self.num23seq
shape = (len(obj), len(obj[0]))
a = self.array(shape, intent.optional, obj)
assert a.arr.shape == shape
assert not a.has_shared_memory()
a = self.array(shape, intent.optional.c, obj)
assert a.arr.shape == shape
assert not a.has_shared_memory()
```

## Next Steps


---

*Source: test_array_from_pyobj.py:638 | Complexity: Intermediate | Last updated: 2026-06-02*