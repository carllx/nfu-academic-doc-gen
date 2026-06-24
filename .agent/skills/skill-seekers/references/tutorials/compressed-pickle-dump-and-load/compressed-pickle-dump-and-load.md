# How To: Compressed Pickle Dump And Load

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compressed pickle dump and load

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

### Step 1: Assign expected_list = value

```python
expected_list = [np.arange(5, dtype=np.dtype('<i8')), np.arange(5, dtype=np.dtype('>i8')), np.arange(5, dtype=np.dtype('<f8')), np.arange(5, dtype=np.dtype('>f8')), np.array([1, 'abc', {'a': 1, 'b': 2}], dtype='O'), np.arange(256, dtype=np.uint8).tobytes(), "C'est l'été !"]
```

**Verification:**
```python
assert len(dumped_filenames) == 1
```

### Step 2: Assign fname = value

```python
fname = tmpdir.join('temp.pkl.gz').strpath
```

**Verification:**
```python
assert result.dtype == expected.dtype
```

### Step 3: Assign dumped_filenames = numpy_pickle.dump(...)

```python
dumped_filenames = numpy_pickle.dump(expected_list, fname, compress=1)
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result_list = numpy_pickle.load(...)

```python
result_list = numpy_pickle.load(fname)
```

### Step 5: Assign expected = _ensure_native_byte_order(...)

```python
expected = _ensure_native_byte_order(expected)
```

**Verification:**
```python
assert result.dtype == expected.dtype
```

### Step 6: Call np.testing.assert_equal()

```python
np.testing.assert_equal(result, expected)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
expected_list = [np.arange(5, dtype=np.dtype('<i8')), np.arange(5, dtype=np.dtype('>i8')), np.arange(5, dtype=np.dtype('<f8')), np.arange(5, dtype=np.dtype('>f8')), np.array([1, 'abc', {'a': 1, 'b': 2}], dtype='O'), np.arange(256, dtype=np.uint8).tobytes(), "C'est l'été !"]
fname = tmpdir.join('temp.pkl.gz').strpath
dumped_filenames = numpy_pickle.dump(expected_list, fname, compress=1)
assert len(dumped_filenames) == 1
result_list = numpy_pickle.load(fname)
for result, expected in zip(result_list, expected_list):
    if isinstance(expected, np.ndarray):
        expected = _ensure_native_byte_order(expected)
        assert result.dtype == expected.dtype
        np.testing.assert_equal(result, expected)
    else:
        assert result == expected
```

## Next Steps


---

*Source: test_numpy_pickle.py:325 | Complexity: Intermediate | Last updated: 2026-06-02*