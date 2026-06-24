# How To: Thread Locality

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test thread locality

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

### Step 1: Assign orig_policy_name = np._core.multiarray.get_handler_name(...)

```python
orig_policy_name = np._core.multiarray.get_handler_name()
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name() == orig_policy_name
```

### Step 2: Assign event = threading.Event(...)

```python
event = threading.Event()
```

### Step 3: Assign concurrent_task1 = threading.Thread(...)

```python
concurrent_task1 = threading.Thread(target=concurrent_thread1, args=(get_module, event))
```

### Step 4: Assign concurrent_task2 = threading.Thread(...)

```python
concurrent_task2 = threading.Thread(target=concurrent_thread2, args=(get_module, event))
```

### Step 5: Call concurrent_task1.start()

```python
concurrent_task1.start()
```

### Step 6: Call concurrent_task2.start()

```python
concurrent_task2.start()
```

### Step 7: Call concurrent_task1.join()

```python
concurrent_task1.join()
```

### Step 8: Call concurrent_task2.join()

```python
concurrent_task2.join()
```

**Verification:**
```python
assert np._core.multiarray.get_handler_name() == orig_policy_name
```


## Complete Example

```python
# Setup
# Fixtures: get_module

# Workflow
orig_policy_name = np._core.multiarray.get_handler_name()
event = threading.Event()
concurrent_task1 = threading.Thread(target=concurrent_thread1, args=(get_module, event))
concurrent_task2 = threading.Thread(target=concurrent_thread2, args=(get_module, event))
concurrent_task1.start()
concurrent_task2.start()
concurrent_task1.join()
concurrent_task2.join()
assert np._core.multiarray.get_handler_name() == orig_policy_name
```

## Next Steps


---

*Source: test_mem_policy.py:366 | Complexity: Advanced | Last updated: 2026-06-02*