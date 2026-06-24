# How To: Gzip Load

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gzip load

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

### Step 1: Assign a = np.random.random(...)

```python
a = np.random.random((5, 5))
```

**Verification:**
```python
assert_array_equal(np.load(f), a)
```

### Step 2: Assign s = BytesIO(...)

```python
s = BytesIO()
```

### Step 3: Assign f = gzip.GzipFile(...)

```python
f = gzip.GzipFile(fileobj=s, mode='w')
```

### Step 4: Call np.save()

```python
np.save(f, a)
```

### Step 5: Call f.close()

```python
f.close()
```

### Step 6: Call s.seek()

```python
s.seek(0)
```

### Step 7: Assign f = gzip.GzipFile(...)

```python
f = gzip.GzipFile(fileobj=s, mode='r')
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(np.load(f), a)
```


## Complete Example

```python
# Workflow
a = np.random.random((5, 5))
s = BytesIO()
f = gzip.GzipFile(fileobj=s, mode='w')
np.save(f, a)
f.close()
s.seek(0)
f = gzip.GzipFile(fileobj=s, mode='r')
assert_array_equal(np.load(f), a)
```

## Next Steps


---

*Source: test_io.py:2696 | Complexity: Advanced | Last updated: 2026-06-02*