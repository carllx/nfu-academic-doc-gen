# How To: Api Invalid

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test api invalid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
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

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

### Step 3: Assign msg = 'Can only append to Tables'

```python
msg = 'Can only append to Tables'
```

### Step 4: Assign msg = 'invalid HDFStore format specified \\[foo\\]'

```python
msg = 'invalid HDFStore format specified \\[foo\\]'
```

### Step 5: Assign path = ''

```python
path = ''
```

### Step 6: Assign msg = value

```python
msg = f'File {path} does not exist'
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(path, key='df', append=True, format='f')
```

### Step 8: Call df.to_hdf()

```python
df.to_hdf(path, key='df', append=True, format='fixed')
```

### Step 9: Call df.to_hdf()

```python
df.to_hdf(path, key='df', append=True, format='foo')
```

### Step 10: Call df.to_hdf()

```python
df.to_hdf(path, key='df', append=False, format='foo')
```

### Step 11: Call read_hdf()

```python
read_hdf(path, 'df')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
path = tmp_path / setup_path
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
msg = 'Can only append to Tables'
with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, key='df', append=True, format='f')
with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, key='df', append=True, format='fixed')
msg = 'invalid HDFStore format specified \\[foo\\]'
with pytest.raises(TypeError, match=msg):
    df.to_hdf(path, key='df', append=True, format='foo')
with pytest.raises(TypeError, match=msg):
    df.to_hdf(path, key='df', append=False, format='foo')
path = ''
msg = f'File {path} does not exist'
with pytest.raises(FileNotFoundError, match=msg):
    read_hdf(path, 'df')
```

## Next Steps


---

*Source: test_round_trip.py:143 | Complexity: Advanced | Last updated: 2026-06-02*