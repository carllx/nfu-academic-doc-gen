# How To: Nested Scatter

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nested scatter

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
# Fixtures: loop, retry_no
```

## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

### Step 2: Assign NUM_INNER_TASKS = 10

```python
NUM_INNER_TASKS = 10
```

### Step 3: Assign NUM_OUTER_TASKS = 10

```python
NUM_OUTER_TASKS = 10
```

### Step 4: Assign client = get_client(...)

```python
client = get_client()
```

### Step 5: Assign results = Parallel(...)

```python
results = Parallel()((delayed(my_sum)(array[j:], i, j) for j in range(NUM_INNER_TASKS)))
```

### Step 6: Assign my_array = np.ones(...)

```python
my_array = np.ones(10000)
```

### Step 7: Assign _ = Parallel(...)

```python
_ = Parallel()((delayed(outer_function_joblib)(my_array[i:], i) for i in range(NUM_OUTER_TASKS)))
```


## Complete Example

```python
# Setup
# Fixtures: loop, retry_no

# Workflow
np = pytest.importorskip('numpy')
NUM_INNER_TASKS = 10
NUM_OUTER_TASKS = 10

def my_sum(x, i, j):
    return np.sum(x)

def outer_function_joblib(array, i):
    client = get_client()
    with parallel_config(backend='dask'):
        results = Parallel()((delayed(my_sum)(array[j:], i, j) for j in range(NUM_INNER_TASKS)))
    return sum(results)
with cluster() as (s, [a, b]):
    with Client(s['address'], loop=loop) as _:
        with parallel_config(backend='dask'):
            my_array = np.ones(10000)
            _ = Parallel()((delayed(outer_function_joblib)(my_array[i:], i) for i in range(NUM_OUTER_TASKS)))
```

## Next Steps


---

*Source: test_dask.py:380 | Complexity: Intermediate | Last updated: 2026-06-02*