# How To: Hash Memmap

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check that memmap and arrays hash identically if coerce_mmap is True.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `gc`
- `hashlib`
- `io`
- `itertools`
- `pickle`
- `random`
- `sys`
- `time`
- `concurrent.futures`
- `decimal`
- `joblib.func_inspect`
- `joblib.hashing`
- `joblib.memory`
- `joblib.test.common`
- `joblib.testing`

**Setup Required:**
```python
# Fixtures: tmpdir, coerce_mmap
```

## Step-by-Step Guide

### Step 1: 'Check that memmap and arrays hash identically if coerce_mmap is True.'

```python
'Check that memmap and arrays hash identically if coerce_mmap is True.'
```

**Verification:**
```python
assert are_hashes_equal == coerce_mmap
```

### Step 2: Assign filename = value

```python
filename = tmpdir.join('memmap_temp').strpath
```

### Step 3: Assign m = np.memmap(...)

```python
m = np.memmap(filename, shape=(10, 10), mode='w+')
```

### Step 4: Assign a = np.asarray(...)

```python
a = np.asarray(m)
```

### Step 5: Assign are_hashes_equal = value

```python
are_hashes_equal = hash(a, coerce_mmap=coerce_mmap) == hash(m, coerce_mmap=coerce_mmap)
```

**Verification:**
```python
assert are_hashes_equal == coerce_mmap
```

### Step 6: Call gc.collect()

```python
gc.collect()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, coerce_mmap

# Workflow
'Check that memmap and arrays hash identically if coerce_mmap is True.'
filename = tmpdir.join('memmap_temp').strpath
try:
    m = np.memmap(filename, shape=(10, 10), mode='w+')
    a = np.asarray(m)
    are_hashes_equal = hash(a, coerce_mmap=coerce_mmap) == hash(m, coerce_mmap=coerce_mmap)
    assert are_hashes_equal == coerce_mmap
finally:
    if 'm' in locals():
        del m
        gc.collect()
```

## Next Steps


---

*Source: test_hashing.py:183 | Complexity: Advanced | Last updated: 2026-06-02*