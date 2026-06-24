# How To: Store Dropna

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test store dropna

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

### Step 1: Assign df_with_missing = DataFrame(...)

```python
df_with_missing = DataFrame({'col1': [0.0, np.nan, 2.0], 'col2': [1.0, np.nan, np.nan]}, index=list('abc'))
```

### Step 2: Assign df_without_missing = DataFrame(...)

```python
df_without_missing = DataFrame({'col1': [0.0, 2.0], 'col2': [1.0, np.nan]}, index=list('ac'))
```

### Step 3: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 4: Call df_with_missing.to_hdf()

```python
df_with_missing.to_hdf(path, key='df', format='table')
```

### Step 5: Assign reloaded = read_hdf(...)

```python
reloaded = read_hdf(path, 'df')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_with_missing, reloaded)
```

### Step 7: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 8: Call df_with_missing.to_hdf()

```python
df_with_missing.to_hdf(path, key='df', format='table', dropna=False)
```

### Step 9: Assign reloaded = read_hdf(...)

```python
reloaded = read_hdf(path, 'df')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_with_missing, reloaded)
```

### Step 11: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 12: Call df_with_missing.to_hdf()

```python
df_with_missing.to_hdf(path, key='df', format='table', dropna=True)
```

### Step 13: Assign reloaded = read_hdf(...)

```python
reloaded = read_hdf(path, 'df')
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_without_missing, reloaded)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df_with_missing = DataFrame({'col1': [0.0, np.nan, 2.0], 'col2': [1.0, np.nan, np.nan]}, index=list('abc'))
df_without_missing = DataFrame({'col1': [0.0, 2.0], 'col2': [1.0, np.nan]}, index=list('ac'))
path = tmp_path / setup_path
df_with_missing.to_hdf(path, key='df', format='table')
reloaded = read_hdf(path, 'df')
tm.assert_frame_equal(df_with_missing, reloaded)
path = tmp_path / setup_path
df_with_missing.to_hdf(path, key='df', format='table', dropna=False)
reloaded = read_hdf(path, 'df')
tm.assert_frame_equal(df_with_missing, reloaded)
path = tmp_path / setup_path
df_with_missing.to_hdf(path, key='df', format='table', dropna=True)
reloaded = read_hdf(path, 'df')
tm.assert_frame_equal(df_without_missing, reloaded)
```

## Next Steps


---

*Source: test_store.py:332 | Complexity: Advanced | Last updated: 2026-06-02*