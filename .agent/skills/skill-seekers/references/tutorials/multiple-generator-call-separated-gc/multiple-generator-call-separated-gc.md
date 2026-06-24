# How To: Multiple Generator Call Separated Gc

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple generator call separated gc

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
# Fixtures: backend, return_as_1, return_as_2, error
```

## Step-by-Step Guide

### Step 1: Assign parallel = Parallel(...)

```python
parallel = Parallel(2, backend=backend, return_as=return_as_1)
```

**Verification:**
```python
assert all((res == i for res, i in zip(g, range(10, 20))))
```

### Step 2: Assign g = parallel(...)

```python
g = parallel((delayed(sleep)(10) for i in range(10)))
```

**Verification:**
```python
assert time.time() - t_start < 5
```

### Step 3: Assign g_wr = weakref.finalize(...)

```python
g_wr = weakref.finalize(g, lambda: print('Generator collected'))
```

**Verification:**
```python
assert time.time() - t_start < 5
```

### Step 4: Assign ctx = value

```python
ctx = raises(RuntimeError, match='The executor underlying Parallel') if error else nullcontext()
```

**Verification:**
```python
assert parallel._aborting
```

### Step 5: Assign retry = 0

```python
retry = 0
```

**Verification:**
```python
assert time.time() - t_start < 5
```

### Step 6: Call pytest.skip()

```python
pytest.skip('Requires multiprocessing')
```

### Step 7: Assign t_start = time.time(...)

```python
t_start = time.time()
```

### Step 8: Assign g = Parallel(...)

```python
g = Parallel(2, backend=backend, return_as=return_as_2)((delayed(sqrt)(i ** 2) for i in range(10, 20)))
```

**Verification:**
```python
assert all((res == i for res, i in zip(g, range(10, 20))))
```

### Step 9: Call time.sleep()

```python
time.sleep(0.5)
```

**Verification:**
```python
assert parallel._aborting
```

### Step 10: Assign g = sorted(...)

```python
g = sorted(g)
```


## Complete Example

```python
# Setup
# Fixtures: backend, return_as_1, return_as_2, error

# Workflow
if backend == 'loky' and mp is None:
    pytest.skip('Requires multiprocessing')
parallel = Parallel(2, backend=backend, return_as=return_as_1)
g = parallel((delayed(sleep)(10) for i in range(10)))
g_wr = weakref.finalize(g, lambda: print('Generator collected'))
ctx = raises(RuntimeError, match='The executor underlying Parallel') if error else nullcontext()
with ctx:
    t_start = time.time()
    g = Parallel(2, backend=backend, return_as=return_as_2)((delayed(sqrt)(i ** 2) for i in range(10, 20)))
    if return_as_2 == 'generator_unordered':
        g = sorted(g)
    assert all((res == i for res, i in zip(g, range(10, 20))))
assert time.time() - t_start < 5
retry = 0
while g_wr.alive and retry < 3:
    retry += 1
    time.sleep(0.5)
assert time.time() - t_start < 5
if parallel._effective_n_jobs() != 1:
    assert parallel._aborting
```

## Next Steps


---

*Source: test_parallel.py:1567 | Complexity: Advanced | Last updated: 2026-06-02*