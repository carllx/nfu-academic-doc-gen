# How To: Default Policy Singleton

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default policy singleton

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
assert get_handler_name() == 'default_allocator'
```

### Step 2: Assign orig_policy = get_module.set_old_policy(...)

```python
orig_policy = get_module.set_old_policy(None)
```

**Verification:**
```python
assert get_handler_name() == 'default_allocator'
```

### Step 3: Assign def_policy_1 = get_module.set_old_policy(...)

```python
def_policy_1 = get_module.set_old_policy(None)
```

**Verification:**
```python
assert def_policy_1 is def_policy_2 is get_module.get_default_policy()
```

### Step 4: Assign def_policy_2 = get_module.set_old_policy(...)

```python
def_policy_2 = get_module.set_old_policy(orig_policy)
```

**Verification:**
```python
assert def_policy_1 is def_policy_2 is get_module.get_default_policy()
```


## Complete Example

```python
# Setup
# Fixtures: get_module

# Workflow
get_handler_name = np._core.multiarray.get_handler_name
orig_policy = get_module.set_old_policy(None)
assert get_handler_name() == 'default_allocator'
def_policy_1 = get_module.set_old_policy(None)
assert get_handler_name() == 'default_allocator'
def_policy_2 = get_module.set_old_policy(orig_policy)
assert def_policy_1 is def_policy_2 is get_module.get_default_policy()
```

## Next Steps


---

*Source: test_mem_policy.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*