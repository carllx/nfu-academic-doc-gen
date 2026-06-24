# How To: Read Explicit

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read explicit

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `array`
- `bz2`
- `datetime`
- `functools`
- `functools`
- `gzip`
- `io`
- `os`
- `pathlib`
- `pickle`
- `shutil`
- `tarfile`
- `typing`
- `uuid`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._optional`
- `pandas.compat.compressors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.generate_legacy_storage_files`
- `pandas.io.common`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: compression, get_random_path
```

## Step-by-Step Guide

### Step 1: Assign base = get_random_path

```python
base = get_random_path
```

### Step 2: Assign path1 = value

```python
path1 = base + '.raw'
```

### Step 3: Assign path2 = value

```python
path2 = base + '.compressed'
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
```

### Step 5: Call df.to_pickle()

```python
df.to_pickle(p1, compression=None)
```

### Step 6: Call self.compress_file()

```python
self.compress_file(p1, p2, compression=compression)
```

### Step 7: Assign df2 = pd.read_pickle(...)

```python
df2 = pd.read_pickle(p2, compression=compression)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df2)
```


## Complete Example

```python
# Setup
# Fixtures: compression, get_random_path

# Workflow
base = get_random_path
path1 = base + '.raw'
path2 = base + '.compressed'
with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
    df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
    df.to_pickle(p1, compression=None)
    self.compress_file(p1, p2, compression=compression)
    df2 = pd.read_pickle(p2, compression=compression)
    tm.assert_frame_equal(df, df2)
```

## Next Steps


---

*Source: test_pickle.py:348 | Complexity: Advanced | Last updated: 2026-06-02*