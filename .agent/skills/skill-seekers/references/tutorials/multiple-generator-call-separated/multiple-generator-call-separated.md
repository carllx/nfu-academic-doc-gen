# How To: Multiple Generator Call Separated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple generator call separated

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
# Fixtures: backend, return_as_1, return_as_2, n_jobs
```

## Step-by-Step Guide

### Step 1: Assign g = Parallel(...)

```python
g = Parallel(n_jobs, backend=backend, return_as=return_as_1)((delayed(sqrt)(i ** 2) for i in range(10)))
```

**Verification:**
```python
assert all((res == i for res, i in zip(g, range(10))))
```

### Step 2: Assign g2 = Parallel(...)

```python
g2 = Parallel(n_jobs, backend=backend, return_as=return_as_2)((delayed(sqrt)(i ** 2) for i in range(10, 20)))
```

**Verification:**
```python
assert all((res == i for res, i in zip(g2, range(10, 20))))
```

### Step 3: Assign g = sorted(...)

```python
g = sorted(g)
```

### Step 4: Assign g2 = sorted(...)

```python
g2 = sorted(g2)
```


## Complete Example

```python
# Setup
# Fixtures: backend, return_as_1, return_as_2, n_jobs

# Workflow
g = Parallel(n_jobs, backend=backend, return_as=return_as_1)((delayed(sqrt)(i ** 2) for i in range(10)))
g2 = Parallel(n_jobs, backend=backend, return_as=return_as_2)((delayed(sqrt)(i ** 2) for i in range(10, 20)))
if return_as_1 == 'generator_unordered':
    g = sorted(g)
if return_as_2 == 'generator_unordered':
    g2 = sorted(g2)
assert all((res == i for res, i in zip(g, range(10))))
assert all((res == i for res, i in zip(g2, range(10, 20))))
```

## Next Steps


---

*Source: test_parallel.py:1538 | Complexity: Intermediate | Last updated: 2026-06-02*