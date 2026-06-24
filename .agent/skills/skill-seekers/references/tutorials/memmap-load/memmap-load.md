# How To: Memmap Load

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memmap load

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
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign little_endian_dtype = np.dtype(...)

```python
little_endian_dtype = np.dtype('<i8')
```

**Verification:**
```python
assert le_array_native_load.dtype == be_array_native_load.dtype
```

### Step 2: Assign big_endian_dtype = np.dtype(...)

```python
big_endian_dtype = np.dtype('>i8')
```

**Verification:**
```python
assert le_array_native_load.dtype in all_dtypes
```

### Step 3: Assign all_dtypes = value

```python
all_dtypes = (little_endian_dtype, big_endian_dtype)
```

**Verification:**
```python
assert le_array_nonnative_load.dtype == le_array.dtype
```

### Step 4: Assign le_array = np.arange(...)

```python
le_array = np.arange(5, dtype=little_endian_dtype)
```

**Verification:**
```python
assert be_array_nonnative_load.dtype == be_array.dtype
```

### Step 5: Assign be_array = np.arange(...)

```python
be_array = np.arange(5, dtype=big_endian_dtype)
```

### Step 6: Assign fname = value

```python
fname = tmpdir.join('temp.pkl').strpath
```

### Step 7: Call numpy_pickle.dump()

```python
numpy_pickle.dump([le_array, be_array], fname)
```

### Step 8: Assign unknown = numpy_pickle.load(...)

```python
le_array_native_load, be_array_native_load = numpy_pickle.load(fname, ensure_native_byte_order=True)
```

**Verification:**
```python
assert le_array_native_load.dtype == be_array_native_load.dtype
```

### Step 9: Assign unknown = numpy_pickle.load(...)

```python
le_array_nonnative_load, be_array_nonnative_load = numpy_pickle.load(fname, ensure_native_byte_order=False)
```

**Verification:**
```python
assert le_array_nonnative_load.dtype == le_array.dtype
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
little_endian_dtype = np.dtype('<i8')
big_endian_dtype = np.dtype('>i8')
all_dtypes = (little_endian_dtype, big_endian_dtype)
le_array = np.arange(5, dtype=little_endian_dtype)
be_array = np.arange(5, dtype=big_endian_dtype)
fname = tmpdir.join('temp.pkl').strpath
numpy_pickle.dump([le_array, be_array], fname)
le_array_native_load, be_array_native_load = numpy_pickle.load(fname, ensure_native_byte_order=True)
assert le_array_native_load.dtype == be_array_native_load.dtype
assert le_array_native_load.dtype in all_dtypes
le_array_nonnative_load, be_array_nonnative_load = numpy_pickle.load(fname, ensure_native_byte_order=False)
assert le_array_nonnative_load.dtype == le_array.dtype
assert be_array_nonnative_load.dtype == be_array.dtype
```

## Next Steps


---

*Source: test_numpy_pickle.py:351 | Complexity: Advanced | Last updated: 2026-06-02*