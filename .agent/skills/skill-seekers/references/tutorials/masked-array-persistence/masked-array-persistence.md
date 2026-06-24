# How To: Masked Array Persistence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked array persistence

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
assert isinstance(b, np.ma.masked_array)
```

### Step 2: Assign a = rnd.random_sample(...)

```python
a = rnd.random_sample(10)
```

### Step 3: Assign a = np.ma.masked_greater(...)

```python
a = np.ma.masked_greater(a, 0.5)
```

### Step 4: Assign filename = value

```python
filename = tmpdir.join('test.pkl').strpath
```

### Step 5: Call numpy_pickle.dump()

```python
numpy_pickle.dump(a, filename)
```

### Step 6: Assign b = numpy_pickle.load(...)

```python
b = numpy_pickle.load(filename, mmap_mode='r')
```

**Verification:**
```python
assert isinstance(b, np.ma.masked_array)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
rnd = np.random.RandomState(0)
a = rnd.random_sample(10)
a = np.ma.masked_greater(a, 0.5)
filename = tmpdir.join('test.pkl').strpath
numpy_pickle.dump(a, filename)
b = numpy_pickle.load(filename, mmap_mode='r')
assert isinstance(b, np.ma.masked_array)
```

## Next Steps


---

*Source: test_numpy_pickle.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*