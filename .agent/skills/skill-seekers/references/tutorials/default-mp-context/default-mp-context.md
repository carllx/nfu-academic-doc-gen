# How To: Default Mp Context

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default mp context

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign mp_start_method = mp.get_start_method(...)

```python
mp_start_method = mp.get_start_method()
```

**Verification:**
```python
assert start_method == mp_start_method
```

### Step 2: Assign p = Parallel(...)

```python
p = Parallel(n_jobs=2, backend='multiprocessing')
```

### Step 3: Assign context = p._backend_kwargs.get(...)

```python
context = p._backend_kwargs.get('context')
```

### Step 4: Assign start_method = context.get_start_method(...)

```python
start_method = context.get_start_method()
```

**Verification:**
```python
assert start_method == mp_start_method
```


## Complete Example

```python
# Workflow
mp_start_method = mp.get_start_method()
p = Parallel(n_jobs=2, backend='multiprocessing')
context = p._backend_kwargs.get('context')
start_method = context.get_start_method()
assert start_method == mp_start_method
```

## Next Steps


---

*Source: test_parallel.py:1088 | Complexity: Intermediate | Last updated: 2026-06-02*