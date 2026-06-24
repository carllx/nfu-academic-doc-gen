# How To: Memmap With Big Offset

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memmap with big offset

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `mmap`
- `os`
- `re`
- `sys`
- `threading`
- `time`
- `warnings`
- `weakref`
- `contextlib`
- `math`
- `multiprocessing`
- `pickle`
- `time`
- `traceback`
- `pytest`
- `joblib`
- `joblib`
- `joblib._multiprocessing_helpers`
- `joblib.test.common`
- `joblib.testing`
- `queue`
- `joblib._parallel_backends`
- `joblib.parallel`
- `joblib.externals.loky`
- `posix`
- `_openmp_test_helper.parallel_sum`
- `distributed`
- `contextlib`
- `numpy`
- `joblib.externals.loky.process_executor`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign fname = value

```python
fname = tmpdir.join('test.mmap').strpath
```

**Verification:**
```python
assert isinstance(memmap[1], np.memmap)
```

### Step 2: Assign size = value

```python
size = mmap.ALLOCATIONGRANULARITY
```

**Verification:**
```python
assert memmap[1].offset > size
```

### Step 3: Assign obj = value

```python
obj = [np.zeros(size, dtype='uint8'), np.ones(size, dtype='uint8')]
```

### Step 4: Call dump()

```python
dump(obj, fname)
```

### Step 5: Assign memmap = load(...)

```python
memmap = load(fname, mmap_mode='r')
```

### Step 6: Assign unknown = Parallel(...)

```python
result, = Parallel(n_jobs=2)((delayed(identity)(memmap) for _ in [0]))
```

**Verification:**
```python
assert isinstance(memmap[1], np.memmap)
```

### Step 7: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(obj, result)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
fname = tmpdir.join('test.mmap').strpath
size = mmap.ALLOCATIONGRANULARITY
obj = [np.zeros(size, dtype='uint8'), np.ones(size, dtype='uint8')]
dump(obj, fname)
memmap = load(fname, mmap_mode='r')
result, = Parallel(n_jobs=2)((delayed(identity)(memmap) for _ in [0]))
assert isinstance(memmap[1], np.memmap)
assert memmap[1].offset > size
np.testing.assert_array_equal(obj, result)
```

## Next Steps


---

*Source: test_parallel.py:1368 | Complexity: Intermediate | Last updated: 2026-06-02*