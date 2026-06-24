# How To: Write Fspath Hdf5

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write fspath hdf5

## Prerequisites

**Required Modules:**
- `codecs`
- `errno`
- `functools`
- `io`
- `mmap`
- `os`
- `pathlib`
- `pickle`
- `tempfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `py.path`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('tables')
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2]})
```

### Step 3: Assign p1 = tm.ensure_clean(...)

```python
p1 = tm.ensure_clean('string')
```

### Step 4: Assign p2 = tm.ensure_clean(...)

```python
p2 = tm.ensure_clean('fspath')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign mypath = CustomFSPath(...)

```python
mypath = CustomFSPath(fspath)
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(mypath, key='bar')
```

### Step 8: Call df.to_hdf()

```python
df.to_hdf(string, key='bar')
```

### Step 9: Assign result = pd.read_hdf(...)

```python
result = pd.read_hdf(fspath, key='bar')
```

### Step 10: Assign expected = pd.read_hdf(...)

```python
expected = pd.read_hdf(string, key='bar')
```


## Complete Example

```python
# Workflow
pytest.importorskip('tables')
df = pd.DataFrame({'A': [1, 2]})
p1 = tm.ensure_clean('string')
p2 = tm.ensure_clean('fspath')
with p1 as string, p2 as fspath:
    mypath = CustomFSPath(fspath)
    df.to_hdf(mypath, key='bar')
    df.to_hdf(string, key='bar')
    result = pd.read_hdf(fspath, key='bar')
    expected = pd.read_hdf(string, key='bar')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common.py:381 | Complexity: Advanced | Last updated: 2026-06-02*