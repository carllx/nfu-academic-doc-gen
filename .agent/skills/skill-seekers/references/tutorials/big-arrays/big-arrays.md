# How To: Big Arrays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test big arrays

## Prerequisites

**Required Modules:**
- `gc`
- `gzip`
- `locale`
- `os`
- `re`
- `sys`
- `threading`
- `time`
- `warnings`
- `zipfile`
- `ctypes`
- `datetime`
- `io`
- `multiprocessing`
- `pathlib`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.lib`
- `numpy.lib._iotools`
- `numpy.lib._npyio_impl`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `bz2`
- `lzma`


## Step-by-Step Guide

### Step 1: Assign L = value

```python
L = (1 << 31) + 100000
```

### Step 2: Assign a = np.empty(...)

```python
a = np.empty(L, dtype=np.uint8)
```

### Step 3: Call np.savez()

```python
np.savez(tmp, a=a)
```

### Step 4: Assign npfile = np.load(...)

```python
npfile = np.load(tmp)
```

### Step 5: Assign a = value

```python
a = npfile['a']
```

### Step 6: Call npfile.close()

```python
npfile.close()
```


## Complete Example

```python
# Workflow
L = (1 << 31) + 100000
a = np.empty(L, dtype=np.uint8)
with temppath(prefix='numpy_test_big_arrays_', suffix='.npz') as tmp:
    np.savez(tmp, a=a)
    del a
    npfile = np.load(tmp)
    a = npfile['a']
    npfile.close()
```

## Next Steps


---

*Source: test_io.py:239 | Complexity: Intermediate | Last updated: 2026-06-02*