# How To: Api Default Format

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test api default format

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Required Fixtures:**
- `api_client` fixture

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign path = value

```python
path = tmp_path / setup_path
```

**Verification:**
```python
assert not store.get_storer('df').is_table
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

**Verification:**
```python
assert store.get_storer('df').is_table
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

**Verification:**
```python
assert store.get_storer('df').is_table
```

### Step 4: Call df.to_hdf()

```python
df.to_hdf(path, key='df')
```

**Verification:**
```python
assert not store.get_storer('df').is_table
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='df3')
```

**Verification:**
```python
assert store.get_storer('df3').is_table
```

### Step 6: Call df.to_hdf()

```python
df.to_hdf(path, key='df4', append=True)
```

**Verification:**
```python
assert store.get_storer('df4').is_table
```

### Step 7: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 8: Call store.put()

```python
store.put('df', df)
```

**Verification:**
```python
assert not store.get_storer('df').is_table
```

### Step 9: Assign msg = 'Can only append to Tables'

```python
msg = 'Can only append to Tables'
```

### Step 10: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 11: Call store.put()

```python
store.put('df', df)
```

**Verification:**
```python
assert store.get_storer('df').is_table
```

### Step 12: Call _maybe_remove()

```python
_maybe_remove(store, 'df2')
```

### Step 13: Call store.append()

```python
store.append('df2', df)
```

**Verification:**
```python
assert store.get_storer('df').is_table
```

### Step 14: Call df.to_hdf()

```python
df.to_hdf(path, key='df2', append=True)
```

**Verification:**
```python
assert store.get_storer('df3').is_table
```

### Step 15: Call store.append()

```python
store.append('df2', df)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
with ensure_clean_store(setup_path) as store:
    df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
    with pd.option_context('io.hdf.default_format', 'fixed'):
        _maybe_remove(store, 'df')
        store.put('df', df)
        assert not store.get_storer('df').is_table
        msg = 'Can only append to Tables'
        with pytest.raises(ValueError, match=msg):
            store.append('df2', df)
    with pd.option_context('io.hdf.default_format', 'table'):
        _maybe_remove(store, 'df')
        store.put('df', df)
        assert store.get_storer('df').is_table
        _maybe_remove(store, 'df2')
        store.append('df2', df)
        assert store.get_storer('df').is_table
path = tmp_path / setup_path
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
with pd.option_context('io.hdf.default_format', 'fixed'):
    df.to_hdf(path, key='df')
    with HDFStore(path) as store:
        assert not store.get_storer('df').is_table
    with pytest.raises(ValueError, match=msg):
        df.to_hdf(path, key='df2', append=True)
with pd.option_context('io.hdf.default_format', 'table'):
    df.to_hdf(path, key='df3')
    with HDFStore(path) as store:
        assert store.get_storer('df3').is_table
    df.to_hdf(path, key='df4', append=True)
    with HDFStore(path) as store:
        assert store.get_storer('df4').is_table
```

## Next Steps


---

*Source: test_put.py:47 | Complexity: Advanced | Last updated: 2026-06-02*