# How To: Complex Across Dimensions

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex across dimensions

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

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': s, 'B': s})
```

### Step 4: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='obj', format='table')
```

### Step 6: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'obj')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j])
s = Series(complex128, index=list('abcd'))
df = DataFrame({'A': s, 'B': s})
path = tmp_path / setup_path
df.to_hdf(path, key='obj', format='table')
reread = read_hdf(path, 'obj')
tm.assert_frame_equal(df, reread)
```

## Next Steps


---

*Source: test_complex.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*