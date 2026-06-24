# How To: Stata Compression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stata compression

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
# Fixtures: compression_only, read_infer, to_infer, compression_to_extension
```

## Step-by-Step Guide

### Step 1: Assign compression = compression_only

```python
compression = compression_only
```

### Step 2: Assign ext = value

```python
ext = compression_to_extension[compression]
```

### Step 3: Assign filename = value

```python
filename = f'test.{ext}'
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame([[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
```

### Step 5: Assign df.index.name = 'index'

```python
df.index.name = 'index'
```

### Step 6: Assign to_compression = value

```python
to_compression = 'infer' if to_infer else compression
```

### Step 7: Assign read_compression = value

```python
read_compression = 'infer' if read_infer else compression
```

### Step 8: Call df.to_stata()

```python
df.to_stata(path, compression=to_compression)
```

### Step 9: Assign result = read_stata(...)

```python
result = read_stata(path, compression=read_compression, index_col='index')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: compression_only, read_infer, to_infer, compression_to_extension

# Workflow
compression = compression_only
ext = compression_to_extension[compression]
filename = f'test.{ext}'
df = DataFrame([[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
df.index.name = 'index'
to_compression = 'infer' if to_infer else compression
read_compression = 'infer' if read_infer else compression
with tm.ensure_clean(filename) as path:
    df.to_stata(path, compression=to_compression)
    result = read_stata(path, compression=read_compression, index_col='index')
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_stata.py:2204 | Complexity: Advanced | Last updated: 2026-06-02*