# How To: Structured Advanced Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test structured advanced indexing

## Prerequisites

**Required Modules:**
- `concurrent.futures`
- `sys`
- `threading`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core.tests.test_stringdtype`
- `numpy.testing`
- `numpy.testing._private.utils`
- `concurrent.futures`
- `inspect`
- `inspect`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('', 'f8')])
```

**Verification:**
```python
assert arr.dtype is dt
```

### Step 2: Assign dt = np.dtype(...)

```python
dt = np.dtype([('', dt)] * 2)
```

### Step 3: Assign dt = np.dtype(...)

```python
dt = np.dtype([('', dt)] * 2)
```

### Step 4: Assign arr = value

```python
arr = np.random.uniform(size=(6000, 8)).view(dt)[:, 0]
```

### Step 5: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng()
```

### Step 6: Assign tpe = concurrent.futures.ThreadPoolExecutor(...)

```python
tpe = concurrent.futures.ThreadPoolExecutor(max_workers=8)
```

### Step 7: Assign futures = value

```python
futures = [tpe.submit(func, arr) for _ in range(10)]
```

**Verification:**
```python
assert arr.dtype is dt
```

### Step 8: Assign indx = rng.integers(...)

```python
indx = rng.integers(0, len(arr), size=6000, dtype=np.intp)
```

### Step 9: arr[indx]

```python
arr[indx]
```

### Step 10: Call f.result()

```python
f.result()
```


## Complete Example

```python
# Workflow
dt = np.dtype([('', 'f8')])
dt = np.dtype([('', dt)] * 2)
dt = np.dtype([('', dt)] * 2)
arr = np.random.uniform(size=(6000, 8)).view(dt)[:, 0]
rng = np.random.default_rng()

def func(arr):
    indx = rng.integers(0, len(arr), size=6000, dtype=np.intp)
    arr[indx]
tpe = concurrent.futures.ThreadPoolExecutor(max_workers=8)
futures = [tpe.submit(func, arr) for _ in range(10)]
for f in futures:
    f.result()
assert arr.dtype is dt
```

## Next Steps


---

*Source: test_multithreading.py:189 | Complexity: Advanced | Last updated: 2026-06-02*