# How To: Dispatch Multiprocessing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Check that using pre_dispatch Parallel does indeed dispatch items
lazily.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `mmap`
- `os`
- `re`
- `sys`
- `threading`
- `time`
- `warnings`
- `weakref`
- `contextlib`
- `math`
- `multiprocessing`
- `pickle`
- `time`
- `traceback`
- `pytest`
- `joblib`
- `joblib`
- `joblib._multiprocessing_helpers`
- `joblib.test.common`
- `joblib.testing`
- `queue`
- `joblib._parallel_backends`
- `joblib.parallel`
- `joblib.externals.loky`
- `posix`
- `_openmp_test_helper.parallel_sum`
- `distributed`
- `contextlib`
- `numpy`
- `joblib.externals.loky.process_executor`

**Setup Required:**
```python
# Fixtures: backend
```

## Step-by-Step Guide

### Step 1: 'Check that using pre_dispatch Parallel does indeed dispatch items\n    lazily.\n    '

```python
'Check that using pre_dispatch Parallel does indeed dispatch items\n    lazily.\n    '
```

**Verification:**
```python
assert queue_contents[0] == 'Produced 0'
```

### Step 2: Assign manager = mp.Manager(...)

```python
manager = mp.Manager()
```

**Verification:**
```python
assert first_consumption_index > -1
```

### Step 3: Assign queue = manager.list(...)

```python
queue = manager.list()
```

**Verification:**
```python
assert produced_3_index > first_consumption_index
```

### Step 4: Call Parallel()

```python
Parallel(n_jobs=2, batch_size=1, pre_dispatch=3, backend=backend)((delayed(consumer)(queue, 'any') for _ in producer()))
```

**Verification:**
```python
assert len(queue) == 12
```

### Step 5: Assign queue_contents = list(...)

```python
queue_contents = list(queue)
```

**Verification:**
```python
assert queue_contents[0] == 'Produced 0'
```

### Step 6: Assign first_consumption_index = unknown.index(...)

```python
first_consumption_index = queue_contents[:4].index('Consumed any')
```

**Verification:**
```python
assert first_consumption_index > -1
```

### Step 7: Assign produced_3_index = queue_contents.index(...)

```python
produced_3_index = queue_contents.index('Produced 3')
```

**Verification:**
```python
assert produced_3_index > first_consumption_index
```

### Step 8: Call queue.append()

```python
queue.append('Produced %i' % i)
```

### Step 9: yield i

```python
yield i
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
'Check that using pre_dispatch Parallel does indeed dispatch items\n    lazily.\n    '
manager = mp.Manager()
queue = manager.list()

def producer():
    for i in range(6):
        queue.append('Produced %i' % i)
        yield i
Parallel(n_jobs=2, batch_size=1, pre_dispatch=3, backend=backend)((delayed(consumer)(queue, 'any') for _ in producer()))
queue_contents = list(queue)
assert queue_contents[0] == 'Produced 0'
first_consumption_index = queue_contents[:4].index('Consumed any')
assert first_consumption_index > -1
produced_3_index = queue_contents.index('Produced 3')
assert produced_3_index > first_consumption_index
assert len(queue) == 12
```

## Next Steps


---

*Source: test_parallel.py:646 | Complexity: Advanced | Last updated: 2026-06-02*