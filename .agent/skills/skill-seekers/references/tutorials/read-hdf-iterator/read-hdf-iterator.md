# How To: Read Hdf Iterator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read hdf iterator

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

**Verification:**
```python
assert isinstance(iterator, TableIterator)
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
df.to_hdf(path, key='df', mode='w', format='t')
```

### Step 6: Assign direct = read_hdf(...)

```python
direct = read_hdf(path, 'df')
```

### Step 7: Assign iterator = read_hdf(...)

```python
iterator = read_hdf(path, 'df', iterator=True)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(direct, indirect)
```

**Verification:**
```python
assert isinstance(iterator, TableIterator)
```

### Step 9: Assign indirect = next(...)

```python
indirect = next(iterator.__iter__())
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
df.index.name = 'letters'
df = df.set_index(keys='E', append=True)
path = tmp_path / setup_path
df.to_hdf(path, key='df', mode='w', format='t')
direct = read_hdf(path, 'df')
iterator = read_hdf(path, 'df', iterator=True)
with closing(iterator.store):
    assert isinstance(iterator, TableIterator)
    indirect = next(iterator.__iter__())
tm.assert_frame_equal(direct, indirect)
```

## Next Steps


---

*Source: test_read.py:263 | Complexity: Advanced | Last updated: 2026-06-02*