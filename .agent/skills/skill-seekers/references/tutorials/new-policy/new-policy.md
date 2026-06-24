# How To: New Policy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test new policy

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

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(10)
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name(b) == 'secret_data_allocator'
```

### Step 2: Assign orig_policy_name = np._core.multiarray.get_handler_name(...)

```python
orig_policy_name = np._core.multiarray.get_handler_name(a)
```

**Verification:**
```python
assert np._core.test('full', verbose=1, extra_argv=[])
```

### Step 3: Assign orig_policy = get_module.set_secret_data_policy(...)

```python
orig_policy = get_module.set_secret_data_policy()
```

**Verification:**
```python
assert np.ma.test('full', verbose=1, extra_argv=[])
```

### Step 4: Assign b = np.arange(...)

```python
b = np.arange(10)
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name(c) == orig_policy_name
```

### Step 5: Call get_module.set_old_policy()

```python
get_module.set_old_policy(orig_policy)
```

### Step 6: Assign c = np.arange(...)

```python
c = np.arange(10)
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name(c) == orig_policy_name
```


## Complete Example

```python
# Setup
# Fixtures: get_module

# Workflow
a = np.arange(10)
orig_policy_name = np._core.multiarray.get_handler_name(a)
orig_policy = get_module.set_secret_data_policy()
b = np.arange(10)
assert np._core.multiarray.get_handler_name(b) == 'secret_data_allocator'
if orig_policy_name == 'default_allocator':
    assert np._core.test('full', verbose=1, extra_argv=[])
    assert np.ma.test('full', verbose=1, extra_argv=[])
get_module.set_old_policy(orig_policy)
c = np.arange(10)
assert np._core.multiarray.get_handler_name(c) == orig_policy_name
```

## Next Steps


---

*Source: test_mem_policy.py:385 | Complexity: Intermediate | Last updated: 2026-06-02*