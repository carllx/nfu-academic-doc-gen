# How To: Npyiter Api

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test npyiter api

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `subprocess`
- `sys`
- `sysconfig`
- `datetime`
- `pytest`
- `numpy`
- `numpy.testing`
- `cython`
- `Cython.Compiler.Version`
- `numpy._utils`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`

**Required Fixtures:**
- `api_client` fixture

**Setup Required:**
```python
# Fixtures: install_temp
```

## Step-by-Step Guide

### Step 1: Assign arr = np.random.rand(...)

```python
arr = np.random.rand(3, 2)
```

**Verification:**
```python
assert checks.get_npyiter_size(it) == it.itersize == np.prod(arr.shape)
```

### Step 2: Assign it = np.nditer(...)

```python
it = np.nditer(arr)
```

**Verification:**
```python
assert checks.get_npyiter_ndim(it) == it.ndim == 1
```

### Step 3: Assign it = np.nditer(...)

```python
it = np.nditer(arr, flags=['c_index'])
```

**Verification:**
```python
assert checks.npyiter_has_index(it) == it.has_index == False
```

### Step 4: Assign it = np.nditer(...)

```python
it = np.nditer(arr, flags=['buffered', 'delay_bufalloc'])
```

**Verification:**
```python
assert checks.npyiter_has_index(it) == it.has_index == True
```

### Step 5: Assign it = np.nditer(...)

```python
it = np.nditer(arr, flags=['multi_index'])
```

**Verification:**
```python
assert checks.npyiter_has_delayed_bufalloc(it) == it.has_delayed_bufalloc == False
```

### Step 6: Assign arr2 = np.random.rand(...)

```python
arr2 = np.random.rand(2, 1, 2)
```

**Verification:**
```python
assert checks.npyiter_has_delayed_bufalloc(it) == it.has_delayed_bufalloc == True
```

### Step 7: Assign it = np.nditer(...)

```python
it = np.nditer([arr, arr2])
```

**Verification:**
```python
assert checks.get_npyiter_size(it) == it.itersize == np.prod(arr.shape)
```


## Complete Example

```python
# Setup
# Fixtures: install_temp

# Workflow
import checks
arr = np.random.rand(3, 2)
it = np.nditer(arr)
assert checks.get_npyiter_size(it) == it.itersize == np.prod(arr.shape)
assert checks.get_npyiter_ndim(it) == it.ndim == 1
assert checks.npyiter_has_index(it) == it.has_index == False
it = np.nditer(arr, flags=['c_index'])
assert checks.npyiter_has_index(it) == it.has_index == True
assert checks.npyiter_has_delayed_bufalloc(it) == it.has_delayed_bufalloc == False
it = np.nditer(arr, flags=['buffered', 'delay_bufalloc'])
assert checks.npyiter_has_delayed_bufalloc(it) == it.has_delayed_bufalloc == True
it = np.nditer(arr, flags=['multi_index'])
assert checks.get_npyiter_size(it) == it.itersize == np.prod(arr.shape)
assert checks.npyiter_has_multi_index(it) == it.has_multi_index == True
assert checks.get_npyiter_ndim(it) == it.ndim == 2
assert checks.test_get_multi_index_iter_next(it, arr)
arr2 = np.random.rand(2, 1, 2)
it = np.nditer([arr, arr2])
assert checks.get_npyiter_nop(it) == it.nop == 2
assert checks.get_npyiter_size(it) == it.itersize == 12
assert checks.get_npyiter_ndim(it) == it.ndim == 3
assert all((x is y for x, y in zip(checks.get_npyiter_operands(it), it.operands)))
assert all((np.allclose(x, y) for x, y in zip(checks.get_npyiter_itviews(it), it.itviews)))
```

## Next Steps


---

*Source: test_cython.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*