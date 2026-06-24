# How To: Backend Batch Statistics Reset

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that a parallel backend correctly resets its batch statistics.

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

### Step 1: 'Test that a parallel backend correctly resets its batch statistics.'

```python
'Test that a parallel backend correctly resets its batch statistics.'
```

**Verification:**
```python
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
```

### Step 2: Assign n_jobs = 2

```python
n_jobs = 2
```

**Verification:**
```python
assert p._backend._smoothed_batch_duration == p._backend._DEFAULT_SMOOTHED_BATCH_DURATION
```

### Step 3: Assign n_inputs = 500

```python
n_inputs = 500
```

**Verification:**
```python
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
```

### Step 4: Assign task_time = value

```python
task_time = 2.0 / n_inputs
```

**Verification:**
```python
assert p._backend._smoothed_batch_duration == p._backend._DEFAULT_SMOOTHED_BATCH_DURATION
```

### Step 5: Assign p = Parallel(...)

```python
p = Parallel(verbose=10, n_jobs=n_jobs, backend=backend)
```

### Step 6: Call p()

```python
p((delayed(time.sleep)(task_time) for i in range(n_inputs)))
```

**Verification:**
```python
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
```

### Step 7: Call p()

```python
p((delayed(time.sleep)(task_time) for i in range(n_inputs)))
```

**Verification:**
```python
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
'Test that a parallel backend correctly resets its batch statistics.'
n_jobs = 2
n_inputs = 500
task_time = 2.0 / n_inputs
p = Parallel(verbose=10, n_jobs=n_jobs, backend=backend)
p((delayed(time.sleep)(task_time) for i in range(n_inputs)))
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
assert p._backend._smoothed_batch_duration == p._backend._DEFAULT_SMOOTHED_BATCH_DURATION
p((delayed(time.sleep)(task_time) for i in range(n_inputs)))
assert p._backend._effective_batch_size == p._backend._DEFAULT_EFFECTIVE_BATCH_SIZE
assert p._backend._smoothed_batch_duration == p._backend._DEFAULT_SMOOTHED_BATCH_DURATION
```

## Next Steps


---

*Source: test_parallel.py:1661 | Complexity: Intermediate | Last updated: 2026-06-02*