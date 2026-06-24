# How To: Read Hdf Open Store

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read hdf open store

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `pathlib`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`
- `pandas.io.pytables`
- `py.path`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
```

**Verification:**
```python
assert store.is_open
```

### Step 2: Assign df.index.name = 'letters'

```python
df.index.name = 'letters'
```

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index(keys='E', append=True)
```

### Step 4: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='df', mode='w')
```

### Step 6: Assign direct = read_hdf(...)

```python
direct = read_hdf(path, 'df')
```

### Step 7: Assign msg = 'Saving a MultiIndex with an extension dtype is not supported.'

```python
msg = 'Saving a MultiIndex with an extension dtype is not supported.'
```

### Step 8: Assign indirect = read_hdf(...)

```python
indirect = read_hdf(store, 'df')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(direct, indirect)
```

**Verification:**
```python
assert store.is_open
```

### Step 10: Call df.to_hdf()

```python
df.to_hdf(path, key='df', mode='w')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path, using_infer_string

# Workflow
df = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
df.index.name = 'letters'
df = df.set_index(keys='E', append=True)
path = tmp_path / setup_path
if using_infer_string:
    msg = 'Saving a MultiIndex with an extension dtype is not supported.'
    with pytest.raises(NotImplementedError, match=msg):
        df.to_hdf(path, key='df', mode='w')
    return
df.to_hdf(path, key='df', mode='w')
direct = read_hdf(path, 'df')
with HDFStore(path, mode='r') as store:
    indirect = read_hdf(store, 'df')
    tm.assert_frame_equal(direct, indirect)
    assert store.is_open
```

## Next Steps


---

*Source: test_read.py:219 | Complexity: Advanced | Last updated: 2026-06-02*