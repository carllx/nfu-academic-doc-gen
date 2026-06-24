# How To: Cache Hidden

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cache hidden

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
a = self.array(shape, intent.cache.hide, None)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 3: Assign shape = value

```python
shape = (2, 3)
```

### Step 4: Assign a = self.array(...)

```python
a = self.array(shape, intent.cache.hide, None)
```

**Verification:**
```python
assert a.arr.shape == shape
```

### Step 5: Assign shape = value

```python
shape = (-1, 3)
```

### Step 6: Assign a = self.array(...)

```python
a = self.array(shape, intent.cache.hide, None)
```


## Complete Example

```python
# Workflow
shape = (2,)
a = self.array(shape, intent.cache.hide, None)
assert a.arr.shape == shape
shape = (2, 3)
a = self.array(shape, intent.cache.hide, None)
assert a.arr.shape == shape
shape = (-1, 3)
try:
    a = self.array(shape, intent.cache.hide, None)
except ValueError as msg:
    if not str(msg).startswith('failed to create intent(cache|hide)|optional array'):
        raise
else:
    raise SystemError('intent(cache) should have failed on undefined dimensions')
```

## Next Steps


---

*Source: test_array_from_pyobj.py:564 | Complexity: Advanced | Last updated: 2026-06-02*