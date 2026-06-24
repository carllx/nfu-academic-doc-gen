# How To: Multiple Generator Call

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple generator call

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
# Fixtures: backend, return_as, n_jobs
```

## Step-by-Step Guide

### Step 1: Assign parallel = Parallel(...)

```python
parallel = Parallel(n_jobs, backend=backend, return_as=return_as)
```

**Verification:**
```python
assert time.time() - t_start < 2, 'The error should be raised immediately when submitting a new task but it took more than 2s.'
```

### Step 2: Assign g = parallel(...)

```python
g = parallel((delayed(sleep)(1) for _ in range(10)))
```

### Step 3: Assign t_start = time.time(...)

```python
t_start = time.time()
```

### Step 4: Assign gen2 = parallel(...)

```python
gen2 = parallel((delayed(id)(i) for i in range(100)))
```


## Complete Example

```python
# Setup
# Fixtures: backend, return_as, n_jobs

# Workflow
with raises(RuntimeError, match='This Parallel instance is already running'):
    parallel = Parallel(n_jobs, backend=backend, return_as=return_as)
    g = parallel((delayed(sleep)(1) for _ in range(10)))
    t_start = time.time()
    gen2 = parallel((delayed(id)(i) for i in range(100)))
assert time.time() - t_start < 2, 'The error should be raised immediately when submitting a new task but it took more than 2s.'
del g
```

## Next Steps


---

*Source: test_parallel.py:1493 | Complexity: Intermediate | Last updated: 2026-06-02*