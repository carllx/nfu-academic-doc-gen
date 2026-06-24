# How To: Memory Usage

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memory usage

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `copy`
- `gzip`
- `io`
- `mmap`
- `os`
- `pickle`
- `random`
- `re`
- `socket`
- `sys`
- `warnings`
- `zlib`
- `contextlib`
- `pathlib`
- `pytest`
- `joblib`
- `joblib.compressor`
- `joblib.numpy_pickle_utils`
- `joblib.test`
- `joblib.test.common`
- `joblib.testing`
- `lzma`
- `lz4.frame`

**Setup Required:**
```python
# Fixtures: tmpdir, compress
```

## Step-by-Step Guide

### Step 1: Assign filename = value

```python
filename = tmpdir.join('test.pkl').strpath
```

**Verification:**
```python
assert mem_used <= write_buf_size
```

### Step 2: Assign small_array = np.ones(...)

```python
small_array = np.ones((10, 10))
```

**Verification:**
```python
assert mem_used < size + read_buf_size
```

### Step 3: Assign big_array = np.ones(...)

```python
big_array = np.ones(shape=100 * int(1000000.0), dtype=np.uint8)
```

### Step 4: Assign size = value

```python
size = obj.nbytes / 1000000.0
```

### Step 5: Assign obj_filename = value

```python
obj_filename = filename + str(np.random.randint(0, 1000))
```

### Step 6: Assign mem_used = memory_used(...)

```python
mem_used = memory_used(numpy_pickle.dump, obj, obj_filename, compress=compress)
```

### Step 7: Assign write_buf_size = value

```python
write_buf_size = _IO_BUFFER_SIZE + 16 * 1024 ** 2 / 1000000.0
```

**Verification:**
```python
assert mem_used <= write_buf_size
```

### Step 8: Assign mem_used = memory_used(...)

```python
mem_used = memory_used(numpy_pickle.load, obj_filename)
```

### Step 9: Assign read_buf_size = value

```python
read_buf_size = 32 + _IO_BUFFER_SIZE
```

**Verification:**
```python
assert mem_used < size + read_buf_size
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, compress

# Workflow
filename = tmpdir.join('test.pkl').strpath
small_array = np.ones((10, 10))
big_array = np.ones(shape=100 * int(1000000.0), dtype=np.uint8)
for obj in (small_array, big_array):
    size = obj.nbytes / 1000000.0
    obj_filename = filename + str(np.random.randint(0, 1000))
    mem_used = memory_used(numpy_pickle.dump, obj, obj_filename, compress=compress)
    write_buf_size = _IO_BUFFER_SIZE + 16 * 1024 ** 2 / 1000000.0
    assert mem_used <= write_buf_size
    mem_used = memory_used(numpy_pickle.load, obj_filename)
    read_buf_size = 32 + _IO_BUFFER_SIZE
    assert mem_used < size + read_buf_size
```

## Next Steps


---

*Source: test_numpy_pickle.py:301 | Complexity: Advanced | Last updated: 2026-06-02*