# How To: Pool With Memmap Array View

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check that subprocess can access and update shared memory array

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
# Fixtures: factory, tmpdir
```

## Step-by-Step Guide

### Step 1: 'Check that subprocess can access and update shared memory array'

```python
'Check that subprocess can access and update shared memory array'
```

**Verification:**
```python
assert_array_equal = np.testing.assert_array_equal
```

### Step 2: Assign assert_array_equal = value

```python
assert_array_equal = np.testing.assert_array_equal
```

**Verification:**
```python
assert not isinstance(a_view, np.memmap)
```

### Step 3: Assign pool_temp_folder = value

```python
pool_temp_folder = tmpdir.mkdir('pool').strpath
```

**Verification:**
```python
assert has_shareable_memory(a_view)
```

### Step 4: Assign p = factory(...)

```python
p = factory(10, max_nbytes=2, temp_folder=pool_temp_folder)
```

**Verification:**
```python
assert_array_equal(a, 2 * np.ones(a.shape))
```

### Step 5: Assign filename = value

```python
filename = tmpdir.join('test.mmap').strpath
```

**Verification:**
```python
assert_array_equal(a_view, 2 * np.ones(a.shape))
```

### Step 6: Assign a = np.memmap(...)

```python
a = np.memmap(filename, dtype=np.float32, shape=(3, 5), mode='w+')
```

**Verification:**
```python
assert os.listdir(pool_temp_folder) == []
```

### Step 7: Call a.fill()

```python
a.fill(1.0)
```

### Step 8: Assign a_view = np.asarray(...)

```python
a_view = np.asarray(a)
```

**Verification:**
```python
assert not isinstance(a_view, np.memmap)
```

### Step 9: Call p.map()

```python
p.map(inplace_double, [(a_view, (i, j), 1.0) for i in range(a.shape[0]) for j in range(a.shape[1])])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(a, 2 * np.ones(a.shape))
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(a_view, 2 * np.ones(a.shape))
```

**Verification:**
```python
assert os.listdir(pool_temp_folder) == []
```

### Step 12: Call p.terminate()

```python
p.terminate()
```


## Complete Example

```python
# Setup
# Fixtures: factory, tmpdir

# Workflow
'Check that subprocess can access and update shared memory array'
assert_array_equal = np.testing.assert_array_equal
pool_temp_folder = tmpdir.mkdir('pool').strpath
p = factory(10, max_nbytes=2, temp_folder=pool_temp_folder)
try:
    filename = tmpdir.join('test.mmap').strpath
    a = np.memmap(filename, dtype=np.float32, shape=(3, 5), mode='w+')
    a.fill(1.0)
    a_view = np.asarray(a)
    assert not isinstance(a_view, np.memmap)
    assert has_shareable_memory(a_view)
    p.map(inplace_double, [(a_view, (i, j), 1.0) for i in range(a.shape[0]) for j in range(a.shape[1])])
    assert_array_equal(a, 2 * np.ones(a.shape))
    assert_array_equal(a_view, 2 * np.ones(a.shape))
    assert os.listdir(pool_temp_folder) == []
finally:
    p.terminate()
    del p
```

## Next Steps


---

*Source: test_memmapping.py:361 | Complexity: Advanced | Last updated: 2026-06-02*