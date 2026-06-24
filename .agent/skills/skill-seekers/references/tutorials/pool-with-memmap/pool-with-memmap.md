# How To: Pool With Memmap

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check that subprocess can access and update shared memory memmap

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

### Step 1: 'Check that subprocess can access and update shared memory memmap'

```python
'Check that subprocess can access and update shared memory memmap'
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
assert_array_equal(a, 2 * np.ones(a.shape))
```

### Step 3: Assign pool_temp_folder = value

```python
pool_temp_folder = tmpdir.mkdir('pool').strpath
```

**Verification:**
```python
assert os.listdir(pool_temp_folder) == []
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
assert_array_equal(b, 2 * np.ones(b.shape))
```

### Step 6: Assign a = np.memmap(...)

```python
a = np.memmap(filename, dtype=np.float32, shape=(3, 5), mode='w+')
```

### Step 7: Call a.fill()

```python
a.fill(1.0)
```

### Step 8: Call p.map()

```python
p.map(inplace_double, [(a, (i, j), 1.0) for i in range(a.shape[0]) for j in range(a.shape[1])])
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(a, 2 * np.ones(a.shape))
```

### Step 10: Assign b = np.memmap(...)

```python
b = np.memmap(filename, dtype=np.float32, shape=(5, 3), mode='c')
```

### Step 11: Call p.map()

```python
p.map(inplace_double, [(b, (i, j), 2.0) for i in range(b.shape[0]) for j in range(b.shape[1])])
```

**Verification:**
```python
assert os.listdir(pool_temp_folder) == []
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(a, 2 * np.ones(a.shape))
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(b, 2 * np.ones(b.shape))
```

### Step 14: Assign c = np.memmap(...)

```python
c = np.memmap(filename, dtype=np.float32, shape=(10,), mode='r', offset=5 * 4)
```

### Step 15: Call p.terminate()

```python
p.terminate()
```

### Step 16: Call p.map()

```python
p.map(check_array, [(c, i, 3.0) for i in range(c.shape[0])])
```

### Step 17: Call p.map()

```python
p.map(inplace_double, [(c, i, 2.0) for i in range(c.shape[0])])
```


## Complete Example

```python
# Setup
# Fixtures: factory, tmpdir

# Workflow
'Check that subprocess can access and update shared memory memmap'
assert_array_equal = np.testing.assert_array_equal
pool_temp_folder = tmpdir.mkdir('pool').strpath
p = factory(10, max_nbytes=2, temp_folder=pool_temp_folder)
try:
    filename = tmpdir.join('test.mmap').strpath
    a = np.memmap(filename, dtype=np.float32, shape=(3, 5), mode='w+')
    a.fill(1.0)
    p.map(inplace_double, [(a, (i, j), 1.0) for i in range(a.shape[0]) for j in range(a.shape[1])])
    assert_array_equal(a, 2 * np.ones(a.shape))
    b = np.memmap(filename, dtype=np.float32, shape=(5, 3), mode='c')
    p.map(inplace_double, [(b, (i, j), 2.0) for i in range(b.shape[0]) for j in range(b.shape[1])])
    assert os.listdir(pool_temp_folder) == []
    assert_array_equal(a, 2 * np.ones(a.shape))
    assert_array_equal(b, 2 * np.ones(b.shape))
    c = np.memmap(filename, dtype=np.float32, shape=(10,), mode='r', offset=5 * 4)
    with raises(AssertionError):
        p.map(check_array, [(c, i, 3.0) for i in range(c.shape[0])])
    with raises((RuntimeError, ValueError)):
        p.map(inplace_double, [(c, i, 2.0) for i in range(c.shape[0])])
finally:
    p.terminate()
    del p
```

## Next Steps


---

*Source: test_memmapping.py:303 | Complexity: Advanced | Last updated: 2026-06-02*