# How To: No Blas Crash Or Freeze With Subprocesses

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no blas crash or freeze with subprocesses

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

### Step 1: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(42)
```

### Step 2: Assign a = rng.randn(...)

```python
a = rng.randn(1000, 1000)
```

### Step 3: Call np.dot()

```python
np.dot(a, a.T)
```

### Step 4: Call Parallel()

```python
Parallel(n_jobs=2, backend=backend)((delayed(np.dot)(a, a.T) for i in range(2)))
```

### Step 5: Assign backend = mp.get_context(...)

```python
backend = mp.get_context('spawn')
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
if backend == 'multiprocessing':
    backend = mp.get_context('spawn')
rng = np.random.RandomState(42)
a = rng.randn(1000, 1000)
np.dot(a, a.T)
Parallel(n_jobs=2, backend=backend)((delayed(np.dot)(a, a.T) for i in range(2)))
```

## Next Steps


---

*Source: test_parallel.py:1099 | Complexity: Intermediate | Last updated: 2026-06-02*