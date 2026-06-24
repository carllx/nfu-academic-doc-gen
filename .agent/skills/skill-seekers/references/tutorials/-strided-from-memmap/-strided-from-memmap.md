# How To:  Strided From Memmap

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test  strided from memmap

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `faulthandler`
- `gc`
- `itertools`
- `mmap`
- `os`
- `pickle`
- `platform`
- `subprocess`
- `sys`
- `threading`
- `time`
- `pytest`
- `joblib._memmapping_reducer`
- `joblib._memmapping_reducer`
- `joblib.backports`
- `joblib.executor`
- `joblib.parallel`
- `joblib.pool`
- `joblib.test.common`
- `joblib.testing`
- `joblib._memmapping_reducer`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign fname = value

```python
fname = tmpdir.join('test.mmap').strpath
```

**Verification:**
```python
assert isinstance(memmap_obj, np.memmap)
```

### Step 2: Assign size = value

```python
size = 5 * mmap.ALLOCATIONGRANULARITY
```

**Verification:**
```python
assert memmap_obj.offset == offset
```

### Step 3: Assign offset = value

```python
offset = mmap.ALLOCATIONGRANULARITY + 1
```

**Verification:**
```python
assert _get_backing_memmap(memmap_backed_obj).offset == offset
```

### Step 4: Assign memmap_obj = np.memmap(...)

```python
memmap_obj = np.memmap(fname, mode='w+', shape=size + offset)
```

### Step 5: Assign memmap_obj = _strided_from_memmap(...)

```python
memmap_obj = _strided_from_memmap(fname, dtype='uint8', mode='r', offset=offset, order='C', shape=size, strides=None, total_buffer_len=None, unlink_on_gc_collect=False)
```

**Verification:**
```python
assert isinstance(memmap_obj, np.memmap)
```

### Step 6: Assign memmap_backed_obj = _strided_from_memmap(...)

```python
memmap_backed_obj = _strided_from_memmap(fname, dtype='uint8', mode='r', offset=offset, order='C', shape=(size // 2,), strides=(2,), total_buffer_len=size, unlink_on_gc_collect=False)
```

**Verification:**
```python
assert _get_backing_memmap(memmap_backed_obj).offset == offset
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
fname = tmpdir.join('test.mmap').strpath
size = 5 * mmap.ALLOCATIONGRANULARITY
offset = mmap.ALLOCATIONGRANULARITY + 1
memmap_obj = np.memmap(fname, mode='w+', shape=size + offset)
memmap_obj = _strided_from_memmap(fname, dtype='uint8', mode='r', offset=offset, order='C', shape=size, strides=None, total_buffer_len=None, unlink_on_gc_collect=False)
assert isinstance(memmap_obj, np.memmap)
assert memmap_obj.offset == offset
memmap_backed_obj = _strided_from_memmap(fname, dtype='uint8', mode='r', offset=offset, order='C', shape=(size // 2,), strides=(2,), total_buffer_len=size, unlink_on_gc_collect=False)
assert _get_backing_memmap(memmap_backed_obj).offset == offset
```

## Next Steps


---

*Source: test_memmapping.py:262 | Complexity: Intermediate | Last updated: 2026-06-02*