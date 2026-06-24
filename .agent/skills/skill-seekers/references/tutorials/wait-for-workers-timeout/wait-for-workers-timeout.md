# How To: Wait For Workers Timeout

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wait for workers timeout

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign cluster = LocalCluster(...)

```python
cluster = LocalCluster(n_workers=0, processes=False, threads_per_worker=2)
```

### Step 2: Assign client = Client(...)

```python
client = Client(cluster)
```

### Step 3: Call client.close()

```python
client.close()
```

### Step 4: Call cluster.close()

```python
cluster.close()
```

### Step 5: Assign msg = 'DaskDistributedBackend has no worker after 0.1 seconds.'

```python
msg = 'DaskDistributedBackend has no worker after 0.1 seconds.'
```

### Step 6: Assign msg = 'DaskDistributedBackend has no active worker'

```python
msg = 'DaskDistributedBackend has no active worker'
```

### Step 7: Call Parallel()

```python
Parallel()((delayed(inc)(i) for i in range(10)))
```

### Step 8: Call Parallel()

```python
Parallel()((delayed(inc)(i) for i in range(10)))
```


## Complete Example

```python
# Workflow
cluster = LocalCluster(n_workers=0, processes=False, threads_per_worker=2)
client = Client(cluster)
try:
    with parallel_config(backend='dask', wait_for_workers_timeout=0.1):
        msg = 'DaskDistributedBackend has no worker after 0.1 seconds.'
        with pytest.raises(TimeoutError, match=msg):
            Parallel()((delayed(inc)(i) for i in range(10)))
    with parallel_config(backend='dask', wait_for_workers_timeout=0):
        msg = 'DaskDistributedBackend has no active worker'
        with pytest.raises(RuntimeError, match=msg):
            Parallel()((delayed(inc)(i) for i in range(10)))
finally:
    client.close()
    cluster.close()
```

## Next Steps


---

*Source: test_dask.py:561 | Complexity: Advanced | Last updated: 2026-06-02*