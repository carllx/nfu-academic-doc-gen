# How To: Memmapping Pool For Large Arrays

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check that large arrays are not copied in memory

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

### Step 1: 'Check that large arrays are not copied in memory'

```python
'Check that large arrays are not copied in memory'
```

**Verification:**
```python
assert os.listdir(tmpdir.strpath) == []
```

### Step 2: Assign p = factory(...)

```python
p = factory(3, max_nbytes=40, temp_folder=tmpdir.strpath, verbose=2)
```

**Verification:**
```python
assert os.listdir(tmpdir.strpath) == []
```

### Step 3: Assign small = np.ones(...)

```python
small = np.ones(5, dtype=np.float32)
```

**Verification:**
```python
assert not os.path.exists(p._temp_folder)
```

### Step 4: Call p.map()

```python
p.map(check_array, [(small, i, 1.0) for i in range(small.shape[0])])
```

**Verification:**
```python
assert small.nbytes == 20
```

### Step 5: Assign large = np.ones(...)

```python
large = np.ones(100, dtype=np.float64)
```

**Verification:**
```python
assert os.listdir(tmpdir.strpath) == []
```

### Step 6: Call p.map()

```python
p.map(check_array, [(large, i, 1.0) for i in range(large.shape[0])])
```

**Verification:**
```python
assert large.nbytes == 800
```

### Step 7: Assign dumped_filenames = os.listdir(...)

```python
dumped_filenames = os.listdir(p._temp_folder)
```

**Verification:**
```python
assert os.path.isdir(p._temp_folder)
```

### Step 8: Assign objects = np.array(...)

```python
objects = np.array(['abc'] * 100, dtype='object')
```

**Verification:**
```python
assert len(dumped_filenames) == 1
```

### Step 9: Assign results = p.map(...)

```python
results = p.map(has_shareable_memory, [objects])
```

**Verification:**
```python
assert not results[0]
```

### Step 10: Call p.terminate()

```python
p.terminate()
```

### Step 11: Call sleep()

```python
sleep(0.1)
```


## Complete Example

```python
# Setup
# Fixtures: factory, tmpdir

# Workflow
'Check that large arrays are not copied in memory'
assert os.listdir(tmpdir.strpath) == []
p = factory(3, max_nbytes=40, temp_folder=tmpdir.strpath, verbose=2)
try:
    assert os.listdir(tmpdir.strpath) == []
    assert not os.path.exists(p._temp_folder)
    small = np.ones(5, dtype=np.float32)
    assert small.nbytes == 20
    p.map(check_array, [(small, i, 1.0) for i in range(small.shape[0])])
    assert os.listdir(tmpdir.strpath) == []
    large = np.ones(100, dtype=np.float64)
    assert large.nbytes == 800
    p.map(check_array, [(large, i, 1.0) for i in range(large.shape[0])])
    assert os.path.isdir(p._temp_folder)
    dumped_filenames = os.listdir(p._temp_folder)
    assert len(dumped_filenames) == 1
    objects = np.array(['abc'] * 100, dtype='object')
    results = p.map(has_shareable_memory, [objects])
    assert not results[0]
finally:
    p.terminate()
    for i in range(10):
        sleep(0.1)
        if not os.path.exists(p._temp_folder):
            break
    else:
        raise AssertionError('temporary folder {} was not deleted'.format(p._temp_folder))
    del p
```

## Next Steps


---

*Source: test_memmapping.py:743 | Complexity: Advanced | Last updated: 2026-06-02*