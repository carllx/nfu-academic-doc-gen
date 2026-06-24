# How To: Numpy Persistence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy persistence

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
assert len(filenames) == 1
```

### Step 2: Assign rnd = np.random.RandomState(...)

```python
rnd = np.random.RandomState(0)
```

**Verification:**
```python
assert filenames[0] == filename
```

### Step 3: Assign a = rnd.random_sample(...)

```python
a = rnd.random_sample((10, 2))
```

**Verification:**
```python
assert os.path.exists(filenames[0])
```

### Step 4: Assign obj = np.memmap(...)

```python
obj = np.memmap(filename + 'mmap', mode='w+', shape=4, dtype=np.float64)
```

**Verification:**
```python
assert isinstance(item, np.ndarray)
```

### Step 5: Assign filenames = numpy_pickle.dump(...)

```python
filenames = numpy_pickle.dump(obj, filename, compress=compress)
```

**Verification:**
```python
assert len(filenames) == 1
```

### Step 6: Assign obj_ = numpy_pickle.load(...)

```python
obj_ = numpy_pickle.load(filename)
```

**Verification:**
```python
assert isinstance(obj_, type(obj))
```

### Step 7: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj_, obj)
```

**Verification:**
```python
assert len(filenames) == 1
```

### Step 8: Assign obj = ComplexTestObject(...)

```python
obj = ComplexTestObject()
```

**Verification:**
```python
assert isinstance(obj_loaded, type(obj))
```

### Step 9: Assign filenames = numpy_pickle.dump(...)

```python
filenames = numpy_pickle.dump(obj, filename, compress=compress)
```

**Verification:**
```python
assert len(filenames) == 1
```

### Step 10: Assign obj_loaded = numpy_pickle.load(...)

```python
obj_loaded = numpy_pickle.load(filename)
```

**Verification:**
```python
assert isinstance(obj_loaded, type(obj))
```

### Step 11: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj_loaded.array_float, obj.array_float)
```

### Step 12: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj_loaded.array_int, obj.array_int)
```

### Step 13: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj_loaded.array_obj, obj.array_obj)
```

### Step 14: Assign filenames = numpy_pickle.dump(...)

```python
filenames = numpy_pickle.dump(obj, filename, compress=compress)
```

**Verification:**
```python
assert len(filenames) == 1
```

### Step 15: Assign obj_ = numpy_pickle.load(...)

```python
obj_ = numpy_pickle.load(filename)
```

### Step 16: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(np.array(obj), np.array(obj_))
```

**Verification:**
```python
assert isinstance(obj_, type(obj))
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, compress

# Workflow
filename = tmpdir.join('test.pkl').strpath
rnd = np.random.RandomState(0)
a = rnd.random_sample((10, 2))
for index, obj in enumerate(((a,), (a.T,), (a, a), [a, a, a])):
    filenames = numpy_pickle.dump(obj, filename, compress=compress)
    assert len(filenames) == 1
    assert filenames[0] == filename
    assert os.path.exists(filenames[0])
    obj_ = numpy_pickle.load(filename)
    for item in obj_:
        assert isinstance(item, np.ndarray)
    np.testing.assert_array_equal(np.array(obj), np.array(obj_))
obj = np.memmap(filename + 'mmap', mode='w+', shape=4, dtype=np.float64)
filenames = numpy_pickle.dump(obj, filename, compress=compress)
assert len(filenames) == 1
obj_ = numpy_pickle.load(filename)
if type(obj) is not np.memmap and hasattr(obj, '__array_prepare__'):
    assert isinstance(obj_, type(obj))
np.testing.assert_array_equal(obj_, obj)
obj = ComplexTestObject()
filenames = numpy_pickle.dump(obj, filename, compress=compress)
assert len(filenames) == 1
obj_loaded = numpy_pickle.load(filename)
assert isinstance(obj_loaded, type(obj))
np.testing.assert_array_equal(obj_loaded.array_float, obj.array_float)
np.testing.assert_array_equal(obj_loaded.array_int, obj.array_int)
np.testing.assert_array_equal(obj_loaded.array_obj, obj.array_obj)
```

## Next Steps


---

*Source: test_numpy_pickle.py:142 | Complexity: Advanced | Last updated: 2026-06-02*