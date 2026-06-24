# How To: Complex Series Error

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex series error

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

### Step 1: Assign complex128 = np.array(...)

```python
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j])
```

### Step 2: Assign s = Series(...)

```python
s = Series(complex128, index=list('abcd'))
```

### Step 3: Assign msg = 'Columns containing complex values can be stored but cannot be indexed when using table format. Either use fixed format, set index=False, or do not include the columns containing complex values to data_columns when initializing the table.'

```python
msg = 'Columns containing complex values can be stored but cannot be indexed when using table format. Either use fixed format, set index=False, or do not include the columns containing complex values to data_columns when initializing the table.'
```

### Step 4: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 5: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 6: Call s.to_hdf()

```python
s.to_hdf(path, key='obj', format='t', index=False)
```

### Step 7: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'obj')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, reread)
```

### Step 9: Call s.to_hdf()

```python
s.to_hdf(path, key='obj', format='t')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j])
s = Series(complex128, index=list('abcd'))
msg = 'Columns containing complex values can be stored but cannot be indexed when using table format. Either use fixed format, set index=False, or do not include the columns containing complex values to data_columns when initializing the table.'
path = tmp_path / setup_path
with pytest.raises(TypeError, match=msg):
    s.to_hdf(path, key='obj', format='t')
path = tmp_path / setup_path
s.to_hdf(path, key='obj', format='t', index=False)
reread = read_hdf(path, 'obj')
tm.assert_series_equal(s, reread)
```

## Next Steps


---

*Source: test_complex.py:161 | Complexity: Advanced | Last updated: 2026-06-02*