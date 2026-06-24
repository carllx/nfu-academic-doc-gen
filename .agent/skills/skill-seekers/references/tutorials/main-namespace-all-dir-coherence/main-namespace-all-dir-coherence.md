# How To: Main Namespace All Dir Coherence

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Checks if `dir(np)` and `np.__all__` are consistent and return
the same content, excluding exceptions and private members.

## Prerequisites

**Required Modules:**
- `functools`
- `importlib`
- `inspect`
- `pkgutil`
- `subprocess`
- `sys`
- `sysconfig`
- `types`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `ctypes`
- `numpy.core`
- `collections.abc`
- `typing`
- `numpy._core._multiarray_umath`


## Step-by-Step Guide

### Step 1: '\n    Checks if `dir(np)` and `np.__all__` are consistent and return\n    the same content, excluding exceptions and private members.\n    '

```python
'\n    Checks if `dir(np)` and `np.__all__` are consistent and return\n    the same content, excluding exceptions and private members.\n    '
```

**Verification:**
```python
assert all_members == dir_members, f'Members that break symmetry: {all_members.symmetric_difference(dir_members)}'
```

### Step 2: Assign all_members = _remove_private_members(...)

```python
all_members = _remove_private_members(np.__all__)
```

### Step 3: Assign all_members = _remove_exceptions(...)

```python
all_members = _remove_exceptions(all_members)
```

### Step 4: Assign dir_members = _remove_private_members(...)

```python
dir_members = _remove_private_members(np.__dir__())
```

### Step 5: Assign dir_members = _remove_exceptions(...)

```python
dir_members = _remove_exceptions(dir_members)
```

**Verification:**
```python
assert all_members == dir_members, f'Members that break symmetry: {all_members.symmetric_difference(dir_members)}'
```


## Complete Example

```python
# Workflow
'\n    Checks if `dir(np)` and `np.__all__` are consistent and return\n    the same content, excluding exceptions and private members.\n    '

def _remove_private_members(member_set):
    return {m for m in member_set if not m.startswith('_')}

def _remove_exceptions(member_set):
    return member_set.difference({'bool'})
all_members = _remove_private_members(np.__all__)
all_members = _remove_exceptions(all_members)
dir_members = _remove_private_members(np.__dir__())
dir_members = _remove_exceptions(dir_members)
assert all_members == dir_members, f'Members that break symmetry: {all_members.symmetric_difference(dir_members)}'
```

## Next Steps


---

*Source: test_public_api.py:479 | Complexity: Advanced | Last updated: 2026-06-02*