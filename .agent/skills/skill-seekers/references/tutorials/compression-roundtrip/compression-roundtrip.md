# How To: Compression Roundtrip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compression roundtrip

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
# Fixtures: compression
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
```

### Step 2: Assign df.index.name = 'index'

```python
df.index.name = 'index'
```

### Step 3: Call df.to_stata()

```python
df.to_stata(path, compression=compression)
```

### Step 4: Assign reread = read_stata(...)

```python
reread = read_stata(path, compression=compression, index_col='index')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```

### Step 6: Assign reread = read_stata(...)

```python
reread = read_stata(contents, index_col='index')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, reread)
```

### Step 8: Assign contents = io.BytesIO(...)

```python
contents = io.BytesIO(fh.read())
```


## Complete Example

```python
# Setup
# Fixtures: compression

# Workflow
df = DataFrame([[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
df.index.name = 'index'
with tm.ensure_clean() as path:
    df.to_stata(path, compression=compression)
    reread = read_stata(path, compression=compression, index_col='index')
    tm.assert_frame_equal(df, reread)
    with tm.decompress_file(path, compression) as fh:
        contents = io.BytesIO(fh.read())
    reread = read_stata(contents, index_col='index')
    tm.assert_frame_equal(df, reread)
```

## Next Steps


---

*Source: test_stata.py:2182 | Complexity: Advanced | Last updated: 2026-06-02*