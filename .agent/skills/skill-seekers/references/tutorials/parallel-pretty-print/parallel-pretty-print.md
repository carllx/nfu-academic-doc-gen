# How To: Parallel Pretty Print

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parallel pretty print

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
# Fixtures: backend, n_jobs
```

## Step-by-Step Guide

### Step 1: Assign n_tasks = 100

```python
n_tasks = 100
```

**Verification:**
```python
assert len(lens) == 1
```

### Step 2: Assign pattern = re.compile(...)

```python
pattern = re.compile('(Done\\s+\\d+ out of \\d+ \\|)')
```

### Step 3: Assign executor = ParallelLog(...)

```python
executor = ParallelLog(n_jobs=n_jobs, backend=backend, verbose=10000)
```

### Step 4: Call executor()

```python
executor([delayed(f)(i) for i in range(n_tasks)])
```

### Step 5: Assign lens = set(...)

```python
lens = set()
```

**Verification:**
```python
assert len(lens) == 1
```

### Step 6: Assign messages = value

```python
messages = []
```

### Step 7: Call self.messages.append()

```python
self.messages.append(msg)
```

### Step 8: Assign unknown = s.span(...)

```python
a, b = s.span()
```

### Step 9: Call lens.add()

```python
lens.add(b - a)
```


## Complete Example

```python
# Setup
# Fixtures: backend, n_jobs

# Workflow
n_tasks = 100
pattern = re.compile('(Done\\s+\\d+ out of \\d+ \\|)')

class ParallelLog(Parallel):
    messages = []

    def _print(self, msg):
        self.messages.append(msg)
executor = ParallelLog(n_jobs=n_jobs, backend=backend, verbose=10000)
executor([delayed(f)(i) for i in range(n_tasks)])
lens = set()
for message in executor.messages:
    if (s := pattern.search(message)):
        a, b = s.span()
        lens.add(b - a)
assert len(lens) == 1
```

## Next Steps


---

*Source: test_parallel.py:195 | Complexity: Advanced | Last updated: 2026-06-02*