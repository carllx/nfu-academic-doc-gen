# How To: Duplicate Column Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicate column name

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['a', 'a'], data=[[0, 0]])
```

**Verification:**
```python
assert df.equals(other)
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

**Verification:**
```python
assert other.equals(df)
```

### Step 3: Assign msg = 'Columns index has to be unique for fixed format'

```python
msg = 'Columns index has to be unique for fixed format'
```

### Step 4: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table')
```

### Step 5: Assign other = read_hdf(...)

```python
other = read_hdf(path, 'df')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, other)
```

**Verification:**
```python
assert df.equals(other)
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='fixed')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame(columns=['a', 'a'], data=[[0, 0]])
path = tmp_path / setup_path
msg = 'Columns index has to be unique for fixed format'
with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, key='df', format='fixed')
df.to_hdf(path, key='df', format='table')
other = read_hdf(path, 'df')
tm.assert_frame_equal(df, other)
assert df.equals(other)
assert other.equals(df)
```

## Next Steps


---

*Source: test_store.py:1024 | Complexity: Intermediate | Last updated: 2026-06-02*