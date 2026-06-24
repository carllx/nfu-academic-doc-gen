# How To: Memmap Persistence Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memmap persistence mixed dtypes

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
assert isinstance(a_clone, np.memmap)
```

### Step 2: Assign a = rnd.random_sample(...)

```python
a = rnd.random_sample(10)
```

**Verification:**
```python
assert not isinstance(b_clone, np.memmap)
```

### Step 3: Assign b = np.array(...)

```python
b = np.array([1, 'b'], dtype=object)
```

### Step 4: Assign construct = value

```python
construct = (a, b)
```

### Step 5: Assign filename = value

```python
filename = tmpdir.join('test.pkl').strpath
```

### Step 6: Call numpy_pickle.dump()

```python
numpy_pickle.dump(construct, filename)
```

### Step 7: Assign unknown = numpy_pickle.load(...)

```python
a_clone, b_clone = numpy_pickle.load(filename, mmap_mode='r')
```

**Verification:**
```python
assert isinstance(a_clone, np.memmap)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
rnd = np.random.RandomState(0)
a = rnd.random_sample(10)
b = np.array([1, 'b'], dtype=object)
construct = (a, b)
filename = tmpdir.join('test.pkl').strpath
numpy_pickle.dump(construct, filename)
a_clone, b_clone = numpy_pickle.load(filename, mmap_mode='r')
assert isinstance(a_clone, np.memmap)
assert not isinstance(b_clone, np.memmap)
```

## Next Steps


---

*Source: test_numpy_pickle.py:247 | Complexity: Intermediate | Last updated: 2026-06-02*