# How To: Joblib Compression Formats

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test joblib compression formats

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
# Fixtures: tmpdir, compress, cmethod
```

## Step-by-Step Guide

### Step 1: Assign filename = value

```python
filename = tmpdir.join('test.pkl').strpath
```

**Verification:**
```python
assert _detect_compressor(f) == cmethod
```

### Step 2: Assign objects = value

```python
objects = (np.ones(shape=(100, 100), dtype='f8'), range(10), {'a': 1, 2: 'b'}, [], (), {}, 0, 1.0)
```

**Verification:**
```python
assert isinstance(obj_reloaded, type(obj))
```

### Step 3: Assign dump_filename = value

```python
dump_filename = filename + '.' + cmethod
```

**Verification:**
```python
assert obj_reloaded == obj
```

### Step 4: Call pytest.skip()

```python
pytest.skip('lzma is support not available')
```

### Step 5: Call numpy_pickle.dump()

```python
numpy_pickle.dump(obj, dump_filename, compress=(cmethod, compress))
```

### Step 6: Assign obj_reloaded = numpy_pickle.load(...)

```python
obj_reloaded = numpy_pickle.load(dump_filename)
```

**Verification:**
```python
assert isinstance(obj_reloaded, type(obj))
```

### Step 7: Call pytest.skip()

```python
pytest.skip('lz4 is not installed.')
```

**Verification:**
```python
assert _detect_compressor(f) == cmethod
```

### Step 8: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj_reloaded, obj)
```

**Verification:**
```python
assert obj_reloaded == obj
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, compress, cmethod

# Workflow
filename = tmpdir.join('test.pkl').strpath
objects = (np.ones(shape=(100, 100), dtype='f8'), range(10), {'a': 1, 2: 'b'}, [], (), {}, 0, 1.0)
if cmethod in ('lzma', 'xz') and lzma is None:
    pytest.skip('lzma is support not available')
elif cmethod == 'lz4' and with_lz4.args[0]:
    pytest.skip('lz4 is not installed.')
dump_filename = filename + '.' + cmethod
for obj in objects:
    numpy_pickle.dump(obj, dump_filename, compress=(cmethod, compress))
    with open(dump_filename, 'rb') as f:
        assert _detect_compressor(f) == cmethod
    obj_reloaded = numpy_pickle.load(dump_filename)
    assert isinstance(obj_reloaded, type(obj))
    if isinstance(obj, np.ndarray):
        np.testing.assert_array_equal(obj_reloaded, obj)
    else:
        assert obj_reloaded == obj
```

## Next Steps


---

*Source: test_numpy_pickle.py:634 | Complexity: Advanced | Last updated: 2026-06-02*