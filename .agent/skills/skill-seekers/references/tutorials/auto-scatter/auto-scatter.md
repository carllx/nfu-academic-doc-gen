# How To: Auto Scatter

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test auto scatter

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
# Fixtures: loop_in_thread
```

## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert counts[a['address']] + counts[b['address']] == 2
```

### Step 2: Assign data1 = np.ones(...)

```python
data1 = np.ones(int(10000.0), dtype=np.uint8)
```

**Verification:**
```python
assert counts[a['address']] == 0
```

### Step 3: Assign data2 = np.ones(...)

```python
data2 = np.ones(int(10000.0), dtype=np.uint8)
```

**Verification:**
```python
assert counts[b['address']] == 0
```

### Step 4: Assign data_to_process = value

```python
data_to_process = [data1] * 3 + [data2] * 3
```

### Step 5: Assign counts = count_events(...)

```python
counts = count_events('receive-from-scatter', client)
```

**Verification:**
```python
assert counts[a['address']] + counts[b['address']] == 2
```

### Step 6: Assign counts = count_events(...)

```python
counts = count_events('receive-from-scatter', client)
```

**Verification:**
```python
assert counts[a['address']] == 0
```

### Step 7: Call Parallel()

```python
Parallel()((delayed(noop)(data, data, i, opt=data) for i, data in enumerate(data_to_process)))
```

### Step 8: Call Parallel()

```python
Parallel()((delayed(noop)(data1[:3], i) for i in range(5)))
```


## Complete Example

```python
# Setup
# Fixtures: loop_in_thread

# Workflow
np = pytest.importorskip('numpy')
data1 = np.ones(int(10000.0), dtype=np.uint8)
data2 = np.ones(int(10000.0), dtype=np.uint8)
data_to_process = [data1] * 3 + [data2] * 3
with cluster() as (s, [a, b]):
    with Client(s['address'], loop=loop_in_thread) as client:
        with parallel_config(backend='dask'):
            Parallel()((delayed(noop)(data, data, i, opt=data) for i, data in enumerate(data_to_process)))
        counts = count_events('receive-from-scatter', client)
        assert counts[a['address']] + counts[b['address']] == 2
with cluster() as (s, [a, b]):
    with Client(s['address'], loop=loop_in_thread) as client:
        with parallel_config(backend='dask'):
            Parallel()((delayed(noop)(data1[:3], i) for i in range(5)))
        counts = count_events('receive-from-scatter', client)
        assert counts[a['address']] == 0
        assert counts[b['address']] == 0
```

## Next Steps


---

*Source: test_dask.py:347 | Complexity: Advanced | Last updated: 2026-06-02*