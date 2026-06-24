# How To: Read Infer String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read infer string

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
df = DataFrame({'a': ['a', 'b', None]})
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 3: Call df.to_hdf()

```python
df.to_hdf(path, key='data', format='table')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['a', 'b', None]}, dtype=pd.StringDtype(na_value=np.nan), columns=Index(['a'], dtype=pd.StringDtype(na_value=np.nan)))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = read_hdf(...)

```python
result = read_hdf(path, key='data', mode='r')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame({'a': ['a', 'b', None]})
path = tmp_path / setup_path
df.to_hdf(path, key='data', format='table')
with pd.option_context('future.infer_string', True):
    result = read_hdf(path, key='data', mode='r')
expected = DataFrame({'a': ['a', 'b', None]}, dtype=pd.StringDtype(na_value=np.nan), columns=Index(['a'], dtype=pd.StringDtype(na_value=np.nan)))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read.py:405 | Complexity: Intermediate | Last updated: 2026-06-02*