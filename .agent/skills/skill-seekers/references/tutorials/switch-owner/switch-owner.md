# How To: Switch Owner

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test switch owner

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
# Fixtures: get_module, policy
```

## Step-by-Step Guide

### Step 1: Assign a = get_module.get_array(...)

```python
a = get_module.get_array()
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name(a) is None
```

### Step 2: Call get_module.set_own()

```python
get_module.set_own(a)
```

### Step 3: Assign policy = value

```python
policy = os.getenv('NUMPY_WARN_IF_NO_MEM_POLICY', '0') == '1'
```

### Step 4: Assign oldval = None

```python
oldval = None
```

### Step 5: Assign policy = value

```python
policy = policy == '1'
```

### Step 6: Assign oldval = np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy(...)

```python
oldval = np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy(policy)
```

### Step 7: Call gc.collect()

```python
gc.collect()
```

### Step 8: Call np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy()

```python
np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy(oldval)
```

### Step 9: Call gc.collect()

```python
gc.collect()
```


## Complete Example

```python
# Setup
# Fixtures: get_module, policy

# Workflow
a = get_module.get_array()
assert np._core.multiarray.get_handler_name(a) is None
get_module.set_own(a)
if policy is None:
    policy = os.getenv('NUMPY_WARN_IF_NO_MEM_POLICY', '0') == '1'
    oldval = None
else:
    policy = policy == '1'
    oldval = np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy(policy)
try:
    if policy:
        with pytest.warns(RuntimeWarning) as w:
            del a
            gc.collect()
    else:
        del a
        gc.collect()
finally:
    if oldval is not None:
        np._core._multiarray_umath._set_numpy_warn_if_no_mem_policy(oldval)
```

## Next Steps


---

*Source: test_mem_policy.py:419 | Complexity: Advanced | Last updated: 2026-06-02*