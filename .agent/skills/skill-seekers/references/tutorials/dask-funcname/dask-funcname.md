# How To: Dask Funcname

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test dask funcname

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `warnings`
- `random`
- `time`
- `uuid`
- `pytest`
- `_dask`
- `parallel`
- `common`
- `test_parallel`
- `distributed`
- `distributed.metrics`
- `distributed.utils_test`
- `joblib._parallel_backends`
- `joblib._dask`
- `distributed`

**Setup Required:**
```python
# Fixtures: loop, mixed
```

## Step-by-Step Guide

### Step 1: Assign tasks = value

```python
tasks = [delayed(inc)(i) for i in range(4)]
```

**Verification:**
```python
assert repr(Batch(tasks)) == batch_repr
```

### Step 2: Assign batch_repr = 'batch_of_inc_4_calls'

```python
batch_repr = 'batch_of_inc_4_calls'
```

**Verification:**
```python
assert all(('batch_of_inc' in tup[0] for tup in log))
```

### Step 3: Assign tasks = value

```python
tasks = [delayed(abs)(i) if i % 2 else delayed(inc)(i) for i in range(4)]
```

### Step 4: Assign batch_repr = 'mixed_batch_of_inc_4_calls'

```python
batch_repr = 'mixed_batch_of_inc_4_calls'
```

### Step 5: Assign batch_repr = batch_repr.replace(...)

```python
batch_repr = batch_repr.replace('4', '2')
```

### Step 6: Assign log = client.run_on_scheduler(...)

```python
log = client.run_on_scheduler(f)
```

**Verification:**
```python
assert all(('batch_of_inc' in tup[0] for tup in log))
```

### Step 7: Assign _ = Parallel(...)

```python
_ = Parallel(batch_size=2, pre_dispatch='all')(tasks)
```


## Complete Example

```python
# Setup
# Fixtures: loop, mixed

# Workflow
from joblib._dask import Batch
if not mixed:
    tasks = [delayed(inc)(i) for i in range(4)]
    batch_repr = 'batch_of_inc_4_calls'
else:
    tasks = [delayed(abs)(i) if i % 2 else delayed(inc)(i) for i in range(4)]
    batch_repr = 'mixed_batch_of_inc_4_calls'
assert repr(Batch(tasks)) == batch_repr
with cluster() as (s, [a, b]):
    with Client(s['address'], loop=loop) as client:
        with parallel_config(backend='dask'):
            _ = Parallel(batch_size=2, pre_dispatch='all')(tasks)

        def f(dask_scheduler):
            return list(dask_scheduler.transition_log)
        batch_repr = batch_repr.replace('4', '2')
        log = client.run_on_scheduler(f)
        assert all(('batch_of_inc' in tup[0] for tup in log))
```

## Next Steps


---

*Source: test_dask.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*