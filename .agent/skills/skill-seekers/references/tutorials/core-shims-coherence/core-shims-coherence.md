# How To: Core Shims Coherence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Check that all "semi-public" members of `numpy._core` are also accessible
from `numpy.core` shims.

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

### Step 1: '\n    Check that all "semi-public" members of `numpy._core` are also accessible\n    from `numpy.core` shims.\n    '

```python
'\n    Check that all "semi-public" members of `numpy._core` are also accessible\n    from `numpy.core` shims.\n    '
```

**Verification:**
```python
assert submodule_member is getattr(core_submodule, submodule_member_name)
```

### Step 2: Assign member = getattr(...)

```python
member = getattr(np._core, member_name)
```

**Verification:**
```python
assert member is getattr(core, member_name)
```

### Step 3: Assign submodule = member

```python
submodule = member
```

### Step 4: Assign submodule_name = member_name

```python
submodule_name = member_name
```

**Verification:**
```python
assert member is getattr(core, member_name)
```

### Step 5: Assign submodule_member = getattr(...)

```python
submodule_member = getattr(submodule, submodule_member_name)
```

### Step 6: Assign core_submodule = __import__(...)

```python
core_submodule = __import__(f'numpy.core.{submodule_name}', fromlist=[submodule_member_name])
```

**Verification:**
```python
assert submodule_member is getattr(core_submodule, submodule_member_name)
```


## Complete Example

```python
# Workflow
'\n    Check that all "semi-public" members of `numpy._core` are also accessible\n    from `numpy.core` shims.\n    '
import numpy.core as core
for member_name in dir(np._core):
    if member_name.startswith('_') or member_name in ['tests', 'strings'] or f'numpy.{member_name}' in PUBLIC_ALIASED_MODULES:
        continue
    member = getattr(np._core, member_name)
    if inspect.ismodule(member) and member.__spec__ and (member.__spec__.origin is not None):
        submodule = member
        submodule_name = member_name
        for submodule_member_name in dir(submodule):
            if submodule_member_name.startswith('__'):
                continue
            submodule_member = getattr(submodule, submodule_member_name)
            core_submodule = __import__(f'numpy.core.{submodule_name}', fromlist=[submodule_member_name])
            assert submodule_member is getattr(core_submodule, submodule_member_name)
    else:
        assert member is getattr(core, member_name)
```

## Next Steps


---

*Source: test_public_api.py:507 | Complexity: Intermediate | Last updated: 2026-06-02*