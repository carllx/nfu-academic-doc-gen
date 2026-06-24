# How To: Joblib Pickle Across Python Versions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test joblib pickle across python versions

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign expected_list = value

```python
expected_list = [np.arange(5, dtype=np.dtype('<i8')), np.arange(5, dtype=np.dtype('<f8')), np.array([1, 'abc', {'a': 1, 'b': 2}], dtype='O'), np.arange(256, dtype=np.uint8).tobytes(), np.matrix([0, 1, 2], dtype=np.dtype('<i8')), "C'est l'été !"]
```

### Step 2: Assign test_data_dir = os.path.dirname(...)

```python
test_data_dir = os.path.dirname(os.path.abspath(data.__file__))
```

### Step 3: Assign pickle_extensions = value

```python
pickle_extensions = ('.pkl', '.gz', '.gzip', '.bz2', 'lz4')
```

### Step 4: Assign pickle_filenames = value

```python
pickle_filenames = [os.path.join(test_data_dir, fn) for fn in os.listdir(test_data_dir) if any((fn.endswith(ext) for ext in pickle_extensions))]
```

### Step 5: Call _check_pickle()

```python
_check_pickle(fname, expected_list)
```


## Complete Example

```python
# Workflow
expected_list = [np.arange(5, dtype=np.dtype('<i8')), np.arange(5, dtype=np.dtype('<f8')), np.array([1, 'abc', {'a': 1, 'b': 2}], dtype='O'), np.arange(256, dtype=np.uint8).tobytes(), np.matrix([0, 1, 2], dtype=np.dtype('<i8')), "C'est l'été !"]
test_data_dir = os.path.dirname(os.path.abspath(data.__file__))
pickle_extensions = ('.pkl', '.gz', '.gzip', '.bz2', 'lz4')
if lzma is not None:
    pickle_extensions += ('.xz', '.lzma')
pickle_filenames = [os.path.join(test_data_dir, fn) for fn in os.listdir(test_data_dir) if any((fn.endswith(ext) for ext in pickle_extensions))]
for fname in pickle_filenames:
    _check_pickle(fname, expected_list)
```

## Next Steps


---

*Source: test_numpy_pickle.py:482 | Complexity: Intermediate | Last updated: 2026-06-02*