# How To: No Track Times

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no track times

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `hashlib`
- `tempfile`
- `time`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign checksum_0_tt_false = create_h5_and_return_checksum(...)

```python
checksum_0_tt_false = create_h5_and_return_checksum(tmp_path, track_times=False)
```

**Verification:**
```python
assert checksum_0_tt_false == checksum_1_tt_false
```

### Step 2: Assign checksum_0_tt_true = create_h5_and_return_checksum(...)

```python
checksum_0_tt_true = create_h5_and_return_checksum(tmp_path, track_times=True)
```

**Verification:**
```python
assert checksum_0_tt_true != checksum_1_tt_true
```

### Step 3: Call time.sleep()

```python
time.sleep(1)
```

### Step 4: Assign checksum_1_tt_false = create_h5_and_return_checksum(...)

```python
checksum_1_tt_false = create_h5_and_return_checksum(tmp_path, track_times=False)
```

### Step 5: Assign checksum_1_tt_true = create_h5_and_return_checksum(...)

```python
checksum_1_tt_true = create_h5_and_return_checksum(tmp_path, track_times=True)
```

**Verification:**
```python
assert checksum_0_tt_false == checksum_1_tt_false
```

### Step 6: Assign h = hash_factory(...)

```python
h = hash_factory()
```

### Step 7: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1]})
```

### Step 9: Call hdf.put()

```python
hdf.put('table', df, format='table', data_columns=True, index=None, track_times=track_times)
```

### Step 10: Call h.update()

```python
h.update(chunk)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
def checksum(filename, hash_factory=hashlib.md5, chunk_num_blocks=128):
    h = hash_factory()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_num_blocks * h.block_size), b''):
            h.update(chunk)
    return h.digest()

def create_h5_and_return_checksum(tmp_path, track_times):
    path = tmp_path / setup_path
    df = DataFrame({'a': [1]})
    with HDFStore(path, mode='w') as hdf:
        hdf.put('table', df, format='table', data_columns=True, index=None, track_times=track_times)
    return checksum(path)
checksum_0_tt_false = create_h5_and_return_checksum(tmp_path, track_times=False)
checksum_0_tt_true = create_h5_and_return_checksum(tmp_path, track_times=True)
time.sleep(1)
checksum_1_tt_false = create_h5_and_return_checksum(tmp_path, track_times=False)
checksum_1_tt_true = create_h5_and_return_checksum(tmp_path, track_times=True)
assert checksum_0_tt_false == checksum_1_tt_false
assert checksum_0_tt_true != checksum_1_tt_true
```

## Next Steps


---

*Source: test_store.py:57 | Complexity: Advanced | Last updated: 2026-06-02*