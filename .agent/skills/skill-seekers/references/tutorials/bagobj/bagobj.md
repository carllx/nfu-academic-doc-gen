# How To: Bagobj

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test BagObj

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([[1, 2], [3, 4]], float)
```

**Verification:**
```python
assert_equal(sorted(dir(l.f)), ['file_a', 'file_b'])
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([[1 + 2j, 2 + 7j], [3 - 6j, 4 + 12j]], complex)
```

**Verification:**
```python
assert_equal(a, l.f.file_a)
```

### Step 3: Assign c = BytesIO(...)

```python
c = BytesIO()
```

**Verification:**
```python
assert_equal(b, l.f.file_b)
```

### Step 4: Call np.savez()

```python
np.savez(c, file_a=a, file_b=b)
```

### Step 5: Call c.seek()

```python
c.seek(0)
```

### Step 6: Assign l = np.load(...)

```python
l = np.load(c)
```

### Step 7: Call assert_equal()

```python
assert_equal(sorted(dir(l.f)), ['file_a', 'file_b'])
```

### Step 8: Call assert_equal()

```python
assert_equal(a, l.f.file_a)
```

### Step 9: Call assert_equal()

```python
assert_equal(b, l.f.file_b)
```


## Complete Example

```python
# Workflow
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[1 + 2j, 2 + 7j], [3 - 6j, 4 + 12j]], complex)
c = BytesIO()
np.savez(c, file_a=a, file_b=b)
c.seek(0)
l = np.load(c)
assert_equal(sorted(dir(l.f)), ['file_a', 'file_b'])
assert_equal(a, l.f.file_a)
assert_equal(b, l.f.file_b)
```

## Next Steps


---

*Source: test_io.py:274 | Complexity: Advanced | Last updated: 2026-06-02*