# How To: High Dimension Memmap Array Reducing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test high dimension memmap array reducing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `faulthandler`
- `gc`
- `itertools`
- `mmap`
- `os`
- `pickle`
- `platform`
- `subprocess`
- `sys`
- `threading`
- `time`
- `pytest`
- `joblib._memmapping_reducer`
- `joblib._memmapping_reducer`
- `joblib.backports`
- `joblib.executor`
- `joblib.parallel`
- `joblib.pool`
- `joblib.test.common`
- `joblib.testing`
- `joblib._memmapping_reducer`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign assert_array_equal = value

```python
assert_array_equal = np.testing.assert_array_equal
```

**Verification:**
```python
assert_array_equal = np.testing.assert_array_equal
```

### Step 2: Assign filename = value

```python
filename = tmpdir.join('test.mmap').strpath
```

**Verification:**
```python
assert has_shareable_memory(a_reconstructed)
```

### Step 3: Assign a = np.memmap(...)

```python
a = np.memmap(filename, dtype=np.float64, shape=(100, 15, 15, 3), mode='w+')
```

**Verification:**
```python
assert isinstance(a_reconstructed, np.memmap)
```

### Step 4: Assign unknown = np.arange.reshape(...)

```python
a[:] = np.arange(100 * 15 * 15 * 3).reshape(a.shape)
```

**Verification:**
```python
assert_array_equal(a_reconstructed, a)
```

### Step 5: Assign b = value

```python
b = a[0:10]
```

**Verification:**
```python
assert has_shareable_memory(b_reconstructed)
```

### Step 6: Assign c = value

```python
c = a[:, 5:10]
```

**Verification:**
```python
assert_array_equal(b_reconstructed, b)
```

### Step 7: Assign d = value

```python
d = a[:, :, :, 0]
```

**Verification:**
```python
assert has_shareable_memory(c_reconstructed)
```

### Step 8: Assign e = value

```python
e = a[1:3:4]
```

**Verification:**
```python
assert_array_equal(c_reconstructed, c)
```

### Step 9: Assign reducer = ArrayMemmapForwardReducer(...)

```python
reducer = ArrayMemmapForwardReducer(None, tmpdir.strpath, 'c', True)
```

**Verification:**
```python
assert has_shareable_memory(d_reconstructed)
```

### Step 10: Assign a_reconstructed = reconstruct_array_or_memmap(...)

```python
a_reconstructed = reconstruct_array_or_memmap(a)
```

**Verification:**
```python
assert_array_equal(d_reconstructed, d)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(a_reconstructed, a)
```

**Verification:**
```python
assert has_shareable_memory(e_reconstructed)
```

### Step 12: Assign b_reconstructed = reconstruct_array_or_memmap(...)

```python
b_reconstructed = reconstruct_array_or_memmap(b)
```

**Verification:**
```python
assert_array_equal(e_reconstructed, e)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(b_reconstructed, b)
```

### Step 14: Assign c_reconstructed = reconstruct_array_or_memmap(...)

```python
c_reconstructed = reconstruct_array_or_memmap(c)
```

**Verification:**
```python
assert has_shareable_memory(c_reconstructed)
```

### Step 15: Call assert_array_equal()

```python
assert_array_equal(c_reconstructed, c)
```

### Step 16: Assign d_reconstructed = reconstruct_array_or_memmap(...)

```python
d_reconstructed = reconstruct_array_or_memmap(d)
```

**Verification:**
```python
assert has_shareable_memory(d_reconstructed)
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(d_reconstructed, d)
```

### Step 18: Assign e_reconstructed = reconstruct_array_or_memmap(...)

```python
e_reconstructed = reconstruct_array_or_memmap(e)
```

**Verification:**
```python
assert has_shareable_memory(e_reconstructed)
```

### Step 19: Call assert_array_equal()

```python
assert_array_equal(e_reconstructed, e)
```

### Step 20: Assign unknown = reducer(...)

```python
cons, args = reducer(x)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
assert_array_equal = np.testing.assert_array_equal
filename = tmpdir.join('test.mmap').strpath
a = np.memmap(filename, dtype=np.float64, shape=(100, 15, 15, 3), mode='w+')
a[:] = np.arange(100 * 15 * 15 * 3).reshape(a.shape)
b = a[0:10]
c = a[:, 5:10]
d = a[:, :, :, 0]
e = a[1:3:4]
reducer = ArrayMemmapForwardReducer(None, tmpdir.strpath, 'c', True)

def reconstruct_array_or_memmap(x):
    cons, args = reducer(x)
    return cons(*args)
a_reconstructed = reconstruct_array_or_memmap(a)
assert has_shareable_memory(a_reconstructed)
assert isinstance(a_reconstructed, np.memmap)
assert_array_equal(a_reconstructed, a)
b_reconstructed = reconstruct_array_or_memmap(b)
assert has_shareable_memory(b_reconstructed)
assert_array_equal(b_reconstructed, b)
c_reconstructed = reconstruct_array_or_memmap(c)
assert has_shareable_memory(c_reconstructed)
assert_array_equal(c_reconstructed, c)
d_reconstructed = reconstruct_array_or_memmap(d)
assert has_shareable_memory(d_reconstructed)
assert_array_equal(d_reconstructed, d)
e_reconstructed = reconstruct_array_or_memmap(e)
assert has_shareable_memory(e_reconstructed)
assert_array_equal(e_reconstructed, e)
```

## Next Steps


---

*Source: test_memmapping.py:217 | Complexity: Advanced | Last updated: 2026-06-02*