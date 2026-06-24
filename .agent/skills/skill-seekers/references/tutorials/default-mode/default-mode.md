# How To: Default Mode

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default mode

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 3: Call df.to_hdf()

```python
df.to_hdf(path, key='df', mode='w')
```

### Step 4: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df')
```

### Step 5: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype('str')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path, using_infer_string

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
path = tmp_path / setup_path
df.to_hdf(path, key='df', mode='w')
result = read_hdf(path, 'df')
expected = df.copy()
if using_infer_string:
    expected.columns = expected.columns.astype('str')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_file_handling.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*