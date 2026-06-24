# How To: Complex Fixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex fixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
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
df = DataFrame(np.random.default_rng(2).random((4, 5)).astype(np.complex64), index=list('abcd'), columns=list('ABCDE'))
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 3: Call df.to_hdf()

```python
df.to_hdf(path, key='df')
```

### Step 4: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'df')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((4, 5)).astype(np.complex128), index=list('abcd'), columns=list('ABCDE'))
```

### Step 7: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 8: Call df.to_hdf()

```python
df.to_hdf(path, key='df')
```

### Step 9: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'df')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame(np.random.default_rng(2).random((4, 5)).astype(np.complex64), index=list('abcd'), columns=list('ABCDE'))
path = tmp_path / setup_path
df.to_hdf(path, key='df')
reread = read_hdf(path, 'df')
tm.assert_frame_equal(df, reread)
df = DataFrame(np.random.default_rng(2).random((4, 5)).astype(np.complex128), index=list('abcd'), columns=list('ABCDE'))
path = tmp_path / setup_path
df.to_hdf(path, key='df')
reread = read_hdf(path, 'df')
tm.assert_frame_equal(df, reread)
```

## Next Steps


---

*Source: test_complex.py:15 | Complexity: Advanced | Last updated: 2026-06-02*