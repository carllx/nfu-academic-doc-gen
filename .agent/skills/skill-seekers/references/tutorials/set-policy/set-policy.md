# How To: Set Policy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set policy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `asyncio`
- `gc`
- `os`
- `sys`
- `sysconfig`
- `threading`
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`
- `mem_policy`

**Setup Required:**
```python
# Fixtures: get_module
```

## Step-by-Step Guide

### Step 1: Assign get_handler_name = value

```python
get_handler_name = np._core.multiarray.get_handler_name
```

**Verification:**
```python
assert get_handler_name(a) is None
```

### Step 2: Assign get_handler_version = value

```python
get_handler_version = np._core.multiarray.get_handler_version
```

**Verification:**
```python
assert get_handler_version(a) is None
```

### Step 3: Assign orig_policy_name = get_handler_name(...)

```python
orig_policy_name = get_handler_name()
```

**Verification:**
```python
assert get_handler_name(a.base) == orig_policy_name
```

### Step 4: Assign a = np.arange.reshape(...)

```python
a = np.arange(10).reshape((2, 5))
```

**Verification:**
```python
assert get_handler_version(a.base) == 1
```

### Step 5: Assign orig_policy = get_module.set_secret_data_policy(...)

```python
orig_policy = get_module.set_secret_data_policy()
```

**Verification:**
```python
assert get_handler_name(b) is None
```

### Step 6: Assign b = np.arange.reshape(...)

```python
b = np.arange(10).reshape((2, 5))
```

**Verification:**
```python
assert get_handler_version(b) is None
```

### Step 7: Call get_module.set_old_policy()

```python
get_module.set_old_policy(None)
```

**Verification:**
```python
assert get_handler_name(b.base) == 'secret_data_allocator'
```

### Step 8: Call get_module.set_old_policy()

```python
get_module.set_old_policy(orig_policy)
```

**Verification:**
```python
assert get_handler_version(b.base) == 1
```

### Step 9: Call get_module.set_wrong_capsule_name_data_policy()

```python
get_module.set_wrong_capsule_name_data_policy()
```

**Verification:**
```python
assert get_handler_name() == 'default_allocator'
```


## Complete Example

```python
# Setup
# Fixtures: get_module

# Workflow
get_handler_name = np._core.multiarray.get_handler_name
get_handler_version = np._core.multiarray.get_handler_version
orig_policy_name = get_handler_name()
a = np.arange(10).reshape((2, 5))
assert get_handler_name(a) is None
assert get_handler_version(a) is None
assert get_handler_name(a.base) == orig_policy_name
assert get_handler_version(a.base) == 1
orig_policy = get_module.set_secret_data_policy()
b = np.arange(10).reshape((2, 5))
assert get_handler_name(b) is None
assert get_handler_version(b) is None
assert get_handler_name(b.base) == 'secret_data_allocator'
assert get_handler_version(b.base) == 1
if orig_policy_name == 'default_allocator':
    get_module.set_old_policy(None)
    assert get_handler_name() == 'default_allocator'
else:
    get_module.set_old_policy(orig_policy)
    assert get_handler_name() == orig_policy_name
with pytest.raises(ValueError, match="Capsule must be named 'mem_handler'"):
    get_module.set_wrong_capsule_name_data_policy()
```

## Next Steps


---

*Source: test_mem_policy.py:234 | Complexity: Advanced | Last updated: 2026-06-02*