# How To: No Undesired Distributed Cache Hit

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no undesired distributed cache hit

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

### Step 1: Assign lists = value

```python
lists = [[] for _ in range(100)]
```

**Verification:**
```python
assert lists == [[] for _ in range(100)]
```

### Step 2: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert sum(counts.values()) == 0
```

### Step 3: Assign X = np.arange(...)

```python
X = np.arange(int(1000000.0))
```

**Verification:**
```python
assert all([len(r) == 1 for r in res])
```

### Step 4: Assign cluster = LocalCluster(...)

```python
cluster = LocalCluster(n_workers=1, threads_per_worker=2)
```

**Verification:**
```python
assert sum(counts.values()) > 0
```

### Step 5: Assign client = Client(...)

```python
client = Client(cluster)
```

**Verification:**
```python
assert all([len(r) == 1 for r in res])
```

### Step 6: Call list_.append()

```python
list_.append(uuid4().hex)
```

**Verification:**
```python
assert lists == [[] for _ in range(100)]
```

### Step 7: Assign counts = count_events(...)

```python
counts = count_events('receive-from-scatter', client)
```

**Verification:**
```python
assert sum(counts.values()) == 0
```

### Step 8: Assign counts = count_events(...)

```python
counts = count_events('receive-from-scatter', client)
```

**Verification:**
```python
assert sum(counts.values()) > 0
```

### Step 9: Call client.close()

```python
client.close(timeout=30)
```

### Step 10: Call cluster.close()

```python
cluster.close(timeout=30)
```

### Step 11: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(data, X)
```

### Step 12: Assign res = Parallel(...)

```python
res = Parallel()((delayed(isolated_operation)(list_) for list_ in lists))
```

### Step 13: Assign res = Parallel(...)

```python
res = Parallel()((delayed(isolated_operation)(list_, data=X) for list_ in lists))
```


## Complete Example

```python
# Workflow
lists = [[] for _ in range(100)]
np = pytest.importorskip('numpy')
X = np.arange(int(1000000.0))

def isolated_operation(list_, data=None):
    if data is not None:
        np.testing.assert_array_equal(data, X)
    list_.append(uuid4().hex)
    return list_
cluster = LocalCluster(n_workers=1, threads_per_worker=2)
client = Client(cluster)
try:
    with parallel_config(backend='dask'):
        res = Parallel()((delayed(isolated_operation)(list_) for list_ in lists))
    assert lists == [[] for _ in range(100)]
    counts = count_events('receive-from-scatter', client)
    assert sum(counts.values()) == 0
    assert all([len(r) == 1 for r in res])
    with parallel_config(backend='dask'):
        res = Parallel()((delayed(isolated_operation)(list_, data=X) for list_ in lists))
    counts = count_events('receive-from-scatter', client)
    assert sum(counts.values()) > 0
    assert all([len(r) == 1 for r in res])
finally:
    client.close(timeout=30)
    cluster.close(timeout=30)
```

## Next Steps


---

*Source: test_dask.py:187 | Complexity: Advanced | Last updated: 2026-06-02*