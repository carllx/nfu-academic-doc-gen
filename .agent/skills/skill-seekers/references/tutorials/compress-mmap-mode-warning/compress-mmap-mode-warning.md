# How To: Compress Mmap Mode Warning

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compress mmap mode warning

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

### Step 1: Assign rnd = np.random.RandomState(...)

```python
rnd = np.random.RandomState(0)
```

**Verification:**
```python
assert not isinstance(reloaded_obj, np.memmap)
```

### Step 2: Assign obj = rnd.random_sample(...)

```python
obj = rnd.random_sample(10)
```

**Verification:**
```python
assert len(warninfo) == 1, debug_msg
```

### Step 3: Assign this_filename = value

```python
this_filename = tmpdir.join('test.pkl').strpath
```

**Verification:**
```python
assert str(warninfo[0]) == f'mmap_mode "r+" is not compatible with compressed file {this_filename}. "r+" flag will be ignored.'
```

### Step 4: Call numpy_pickle.dump()

```python
numpy_pickle.dump(obj, this_filename, compress=1)
```

### Step 5: Assign debug_msg = unknown.join(...)

```python
debug_msg = '\n'.join([str(w) for w in warninfo])
```

### Step 6: Assign warninfo = value

```python
warninfo = [w.message for w in warninfo]
```

**Verification:**
```python
assert not isinstance(reloaded_obj, np.memmap)
```

### Step 7: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj, reloaded_obj)
```

**Verification:**
```python
assert len(warninfo) == 1, debug_msg
```

### Step 8: Assign reloaded_obj = numpy_pickle.load(...)

```python
reloaded_obj = numpy_pickle.load(this_filename, mmap_mode='r+')
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
rnd = np.random.RandomState(0)
obj = rnd.random_sample(10)
this_filename = tmpdir.join('test.pkl').strpath
numpy_pickle.dump(obj, this_filename, compress=1)
with warns(UserWarning) as warninfo:
    reloaded_obj = numpy_pickle.load(this_filename, mmap_mode='r+')
debug_msg = '\n'.join([str(w) for w in warninfo])
warninfo = [w.message for w in warninfo]
assert not isinstance(reloaded_obj, np.memmap)
np.testing.assert_array_equal(obj, reloaded_obj)
assert len(warninfo) == 1, debug_msg
assert str(warninfo[0]) == f'mmap_mode "r+" is not compatible with compressed file {this_filename}. "r+" flag will be ignored.'
```

## Next Steps


---

*Source: test_numpy_pickle.py:279 | Complexity: Advanced | Last updated: 2026-06-02*