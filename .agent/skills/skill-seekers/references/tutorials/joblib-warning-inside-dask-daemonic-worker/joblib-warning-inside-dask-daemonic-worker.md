# How To: Joblib Warning Inside Dask Daemonic Worker

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test joblib warning inside dask daemonic worker

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
# Fixtures: backend
```

## Step-by-Step Guide

### Step 1: Assign cluster = LocalCluster(...)

```python
cluster = LocalCluster(n_workers=2)
```

**Verification:**
```python
assert len(record) == 1
```

### Step 2: Assign client = Client(...)

```python
client = Client(cluster)
```

**Verification:**
```python
assert isinstance(warning, UserWarning)
```

### Step 3: Assign fut = client.submit(...)

```python
fut = client.submit(func_using_joblib_parallel)
```

**Verification:**
```python
assert 'distributed.worker.daemon' in str(warning)
```

### Step 4: Assign record = fut.result(...)

```python
record = fut.result()
```

**Verification:**
```python
assert len(record) == 1
```

### Step 5: Assign warning = value

```python
warning = record[0].message
```

**Verification:**
```python
assert isinstance(warning, UserWarning)
```

### Step 6: Call client.close()

```python
client.close(timeout=30)
```

### Step 7: Call cluster.close()

```python
cluster.close(timeout=30)
```

### Step 8: Call Parallel()

```python
Parallel(n_jobs=2, backend=backend)((delayed(inc)(i) for i in range(10)))
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
cluster = LocalCluster(n_workers=2)
client = Client(cluster)
try:

    def func_using_joblib_parallel():
        with warnings.catch_warnings(record=True) as record:
            Parallel(n_jobs=2, backend=backend)((delayed(inc)(i) for i in range(10)))
        return record
    fut = client.submit(func_using_joblib_parallel)
    record = fut.result()
    assert len(record) == 1
    warning = record[0].message
    assert isinstance(warning, UserWarning)
    assert 'distributed.worker.daemon' in str(warning)
finally:
    client.close(timeout=30)
    cluster.close(timeout=30)
```

## Next Steps


---

*Source: test_dask.py:583 | Complexity: Advanced | Last updated: 2026-06-02*