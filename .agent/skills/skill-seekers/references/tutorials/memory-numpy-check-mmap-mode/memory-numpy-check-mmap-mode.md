# How To: Memory Numpy Check Mmap Mode

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Check that mmap_mode is respected even at the first call

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
# Fixtures: tmpdir, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Check that mmap_mode is respected even at the first call'

```python
'Check that mmap_mode is respected even at the first call'
```

**Verification:**
```python
assert isinstance(c, np.memmap)
```

### Step 2: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, mmap_mode='r', verbose=0)
```

**Verification:**
```python
assert c.mode == 'r'
```

### Step 3: Assign a = np.ones(...)

```python
a = np.ones(3)
```

**Verification:**
```python
assert isinstance(b, np.memmap)
```

### Step 4: Assign b = twice(...)

```python
b = twice(a)
```

**Verification:**
```python
assert b.mode == 'r'
```

### Step 5: Assign c = twice(...)

```python
c = twice(a)
```

**Verification:**
```python
assert len(recorded_warnings) == 1
```

### Step 6: Call gc.collect()

```python
gc.collect()
```

**Verification:**
```python
assert exception_msg in recorded_warnings[0]
```

### Step 7: Call corrupt_single_cache_item()

```python
corrupt_single_cache_item(memory)
```

**Verification:**
```python
assert isinstance(d, np.memmap)
```

### Step 8: Assign recorded_warnings = monkeypatch_cached_func_warn(...)

```python
recorded_warnings = monkeypatch_cached_func_warn(twice, monkeypatch)
```

**Verification:**
```python
assert d.mode == 'r'
```

### Step 9: Assign d = twice(...)

```python
d = twice(a)
```

**Verification:**
```python
assert len(recorded_warnings) == 1
```

### Step 10: Assign exception_msg = 'Exception while loading results'

```python
exception_msg = 'Exception while loading results'
```

**Verification:**
```python
assert exception_msg in recorded_warnings[0]
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, monkeypatch

# Workflow
'Check that mmap_mode is respected even at the first call'
memory = Memory(location=tmpdir.strpath, mmap_mode='r', verbose=0)

@memory.cache()
def twice(a):
    return a * 2
a = np.ones(3)
b = twice(a)
c = twice(a)
assert isinstance(c, np.memmap)
assert c.mode == 'r'
assert isinstance(b, np.memmap)
assert b.mode == 'r'
del b
del c
gc.collect()
corrupt_single_cache_item(memory)
recorded_warnings = monkeypatch_cached_func_warn(twice, monkeypatch)
d = twice(a)
assert len(recorded_warnings) == 1
exception_msg = 'Exception while loading results'
assert exception_msg in recorded_warnings[0]
assert isinstance(d, np.memmap)
assert d.mode == 'r'
```

## Next Steps


---

*Source: test_memory.py:420 | Complexity: Advanced | Last updated: 2026-06-02*