# How To: Memory Integration

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Simple test of memory lazy evaluation.

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
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: 'Simple test of memory lazy evaluation.'

```python
'Simple test of memory lazy evaluation.'
```

**Verification:**
```python
assert len(accumulator) == current_accumulator + 1
```

### Step 2: Assign accumulator = list(...)

```python
accumulator = list()
```

**Verification:**
```python
assert memory.eval(f, 1) == out
```

### Step 3: Call check_identity_lazy()

```python
check_identity_lazy(f, accumulator, tmpdir.strpath)
```

**Verification:**
```python
assert len(accumulator) == current_accumulator + 1
```

### Step 4: Assign f.__module__ = '__main__'

```python
f.__module__ = '__main__'
```

### Step 5: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=0)
```

### Step 6: Call memory.cache()

```python
memory.cache(f)(1)
```

### Step 7: Call accumulator.append()

```python
accumulator.append(1)
```

**Verification:**
```python
assert len(accumulator) == current_accumulator + 1
```

### Step 8: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=10, mmap_mode=mmap_mode, compress=compress)
```

### Step 9: Call shutil.rmtree()

```python
shutil.rmtree(tmpdir.strpath, ignore_errors=True)
```

### Step 10: Assign g = memory.cache(...)

```python
g = memory.cache(f)
```

### Step 11: Call g()

```python
g(1)
```

### Step 12: Call g.clear()

```python
g.clear(warn=False)
```

### Step 13: Assign current_accumulator = len(...)

```python
current_accumulator = len(accumulator)
```

### Step 14: Assign out = g(...)

```python
out = g(1)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'Simple test of memory lazy evaluation.'
accumulator = list()

def f(arg):
    accumulator.append(1)
    return arg
check_identity_lazy(f, accumulator, tmpdir.strpath)
for compress in (False, True):
    for mmap_mode in ('r', None):
        memory = Memory(location=tmpdir.strpath, verbose=10, mmap_mode=mmap_mode, compress=compress)
        shutil.rmtree(tmpdir.strpath, ignore_errors=True)
        g = memory.cache(f)
        g(1)
        g.clear(warn=False)
        current_accumulator = len(accumulator)
        out = g(1)
    assert len(accumulator) == current_accumulator + 1
    assert memory.eval(f, 1) == out
    assert len(accumulator) == current_accumulator + 1
f.__module__ = '__main__'
memory = Memory(location=tmpdir.strpath, verbose=0)
memory.cache(f)(1)
```

## Next Steps


---

*Source: test_memory.py:92 | Complexity: Advanced | Last updated: 2026-06-02*