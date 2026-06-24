# How To: Memory Numpy

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test memory with a function with numpy arrays.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `gc`
- `logging`
- `os`
- `os.path`
- `pickle`
- `shutil`
- `sys`
- `textwrap`
- `time`
- `pathlib`
- `pytest`
- `joblib._store_backends`
- `joblib.hashing`
- `joblib.memory`
- `joblib.parallel`
- `joblib.test.common`
- `joblib.testing`
- `functools`
- `tmp_joblib_`
- `tmp_joblib_`
- `datetime`
- `time`

**Setup Required:**
```python
# Fixtures: tmpdir, mmap_mode
```

## Step-by-Step Guide

### Step 1: 'Test memory with a function with numpy arrays.'

```python
'Test memory with a function with numpy arrays.'
```

**Verification:**
```python
assert np.all(cached_n(a) == a)
```

### Step 2: Assign accumulator = list(...)

```python
accumulator = list()
```

**Verification:**
```python
assert len(accumulator) == i + 1
```

### Step 3: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, mmap_mode=mmap_mode, verbose=0)
```

### Step 4: Assign cached_n = memory.cache(...)

```python
cached_n = memory.cache(n)
```

### Step 5: Assign rnd = np.random.RandomState(...)

```python
rnd = np.random.RandomState(0)
```

### Step 6: Call accumulator.append()

```python
accumulator.append(1)
```

### Step 7: Assign a = rnd.random_sample(...)

```python
a = rnd.random_sample((10, 10))
```

**Verification:**
```python
assert np.all(cached_n(a) == a)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, mmap_mode

# Workflow
'Test memory with a function with numpy arrays.'
accumulator = list()

def n(arg=None):
    accumulator.append(1)
    return arg
memory = Memory(location=tmpdir.strpath, mmap_mode=mmap_mode, verbose=0)
cached_n = memory.cache(n)
rnd = np.random.RandomState(0)
for i in range(3):
    a = rnd.random_sample((10, 10))
    for _ in range(3):
        assert np.all(cached_n(a) == a)
        assert len(accumulator) == i + 1
```

## Next Steps


---

*Source: test_memory.py:400 | Complexity: Intermediate | Last updated: 2026-06-02*