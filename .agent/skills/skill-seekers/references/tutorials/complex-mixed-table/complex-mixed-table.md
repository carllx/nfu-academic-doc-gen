# How To: Complex Mixed Table

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex mixed table

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

### Step 1: Assign complex64 = np.array(...)

```python
complex64 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j], dtype=np.complex64)
```

### Step 2: Assign complex128 = np.array(...)

```python
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j], dtype=np.complex128)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd'], 'C': complex64, 'D': complex128, 'E': [1.0, 2.0, 3.0, 4.0]}, index=list('abcd'))
```

### Step 4: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table')
```

### Step 6: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'df')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```

### Step 8: Call store.append()

```python
store.append('df', df, data_columns=['A', 'B'])
```

### Step 9: Assign result = store.select(...)

```python
result = store.select('df', where='A>2')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[df.A > 2], result)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
complex64 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j], dtype=np.complex64)
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j], dtype=np.complex128)
df = DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd'], 'C': complex64, 'D': complex128, 'E': [1.0, 2.0, 3.0, 4.0]}, index=list('abcd'))
with ensure_clean_store(setup_path) as store:
    store.append('df', df, data_columns=['A', 'B'])
    result = store.select('df', where='A>2')
    tm.assert_frame_equal(df.loc[df.A > 2], result)
path = tmp_path / setup_path
df.to_hdf(path, key='df', format='table')
reread = read_hdf(path, 'df')
tm.assert_frame_equal(df, reread)
```

## Next Steps


---

*Source: test_complex.py:85 | Complexity: Advanced | Last updated: 2026-06-02*