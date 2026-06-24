# How To: Read Nokey

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read nokey

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
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 3: Call df.to_hdf()

```python
df.to_hdf(path, key='df', mode='a')
```

### Step 4: Assign reread = read_hdf(...)

```python
reread = read_hdf(path)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```

### Step 6: Call df.to_hdf()

```python
df.to_hdf(path, key='df2', mode='a')
```

### Step 7: Assign msg = 'key must be provided when HDF5 file contains multiple datasets.'

```python
msg = 'key must be provided when HDF5 file contains multiple datasets.'
```

### Step 8: Call read_hdf()

```python
read_hdf(path)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
path = tmp_path / setup_path
df.to_hdf(path, key='df', mode='a')
reread = read_hdf(path)
tm.assert_frame_equal(df, reread)
df.to_hdf(path, key='df2', mode='a')
msg = 'key must be provided when HDF5 file contains multiple datasets.'
with pytest.raises(ValueError, match=msg):
    read_hdf(path)
```

## Next Steps


---

*Source: test_read.py:282 | Complexity: Advanced | Last updated: 2026-06-02*