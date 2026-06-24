# How To: Compression Dict

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compression dict

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`

**Setup Required:**
```python
# Fixtures: method, file_ext
```

## Step-by-Step Guide

### Step 1: Assign file_name = value

```python
file_name = f'test.{file_ext}'
```

**Verification:**
```python
assert len(zp.filelist) == 1
```

### Step 2: Assign archive_name = 'test.dta'

```python
archive_name = 'test.dta'
```

**Verification:**
```python
assert zp.filelist[0].filename == archive_name
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 2)), columns=list('AB'))
```

### Step 4: Assign df.index.name = 'index'

```python
df.index.name = 'index'
```

### Step 5: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 6: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(np.int32)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(reread, expected)
```

### Step 8: Assign compression = value

```python
compression = {'method': method, 'archive_name': archive_name}
```

### Step 9: Call df.to_stata()

```python
df.to_stata(path, compression=compression)
```

### Step 10: Assign reread = read_stata(...)

```python
reread = read_stata(fp, index_col='index')
```

### Step 11: Assign fp = path

```python
fp = path
```

**Verification:**
```python
assert len(zp.filelist) == 1
```

### Step 12: Assign fp = io.BytesIO(...)

```python
fp = io.BytesIO(zp.read(zp.filelist[0]))
```


## Complete Example

```python
# Setup
# Fixtures: method, file_ext

# Workflow
file_name = f'test.{file_ext}'
archive_name = 'test.dta'
df = DataFrame(np.random.default_rng(2).standard_normal((10, 2)), columns=list('AB'))
df.index.name = 'index'
with tm.ensure_clean(file_name) as path:
    compression = {'method': method, 'archive_name': archive_name}
    df.to_stata(path, compression=compression)
    if method == 'zip' or file_ext == 'zip':
        with zipfile.ZipFile(path, 'r') as zp:
            assert len(zp.filelist) == 1
            assert zp.filelist[0].filename == archive_name
            fp = io.BytesIO(zp.read(zp.filelist[0]))
    else:
        fp = path
    reread = read_stata(fp, index_col='index')
expected = df.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(reread, expected)
```

## Next Steps


---

*Source: test_stata.py:2081 | Complexity: Advanced | Last updated: 2026-06-02*