# How To: Read From Py Localpath

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read from py localpath

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

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
```

### Step 2: Assign filename = value

```python
filename = tmp_path / setup_path
```

### Step 3: Assign path_obj = LocalPath(...)

```python
path_obj = LocalPath(filename)
```

### Step 4: Call expected.to_hdf()

```python
expected.to_hdf(path_obj, key='df', mode='a')
```

### Step 5: Assign actual = read_hdf(...)

```python
actual = read_hdf(path_obj, key='df')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, actual)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
from py.path import local as LocalPath
expected = DataFrame(np.random.default_rng(2).random((4, 5)), index=list('abcd'), columns=list('ABCDE'))
filename = tmp_path / setup_path
path_obj = LocalPath(filename)
expected.to_hdf(path_obj, key='df', mode='a')
actual = read_hdf(path_obj, key='df')
tm.assert_frame_equal(expected, actual)
```

## Next Steps


---

*Source: test_read.py:347 | Complexity: Intermediate | Last updated: 2026-06-02*