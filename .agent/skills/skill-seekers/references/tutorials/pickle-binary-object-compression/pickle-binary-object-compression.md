# How To: Pickle Binary Object Compression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Read/write from binary file-objects w/wo compression.

GH 26237, GH 29054, and GH 29570

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
# Fixtures: compression
```

## Step-by-Step Guide

### Step 1: '\n    Read/write from binary file-objects w/wo compression.\n\n    GH 26237, GH 29054, and GH 29570\n    '

```python
'\n    Read/write from binary file-objects w/wo compression.\n\n    GH 26237, GH 29054, and GH 29570\n    '
```

**Verification:**
```python
assert buffer.getvalue() == reference or compression in ('gzip', 'zip', 'tar')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
```

### Step 3: Assign buffer = io.BytesIO(...)

```python
buffer = io.BytesIO()
```

### Step 4: Call df.to_pickle()

```python
df.to_pickle(buffer, compression=compression)
```

### Step 5: Call buffer.seek()

```python
buffer.seek(0)
```

**Verification:**
```python
assert buffer.getvalue() == reference or compression in ('gzip', 'zip', 'tar')
```

### Step 6: Assign read_df = pd.read_pickle(...)

```python
read_df = pd.read_pickle(buffer, compression=compression)
```

### Step 7: Call buffer.seek()

```python
buffer.seek(0)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, read_df)
```

### Step 9: Call df.to_pickle()

```python
df.to_pickle(path, compression=compression)
```

### Step 10: Assign reference = Path.read_bytes(...)

```python
reference = Path(path).read_bytes()
```


## Complete Example

```python
# Setup
# Fixtures: compression

# Workflow
'\n    Read/write from binary file-objects w/wo compression.\n\n    GH 26237, GH 29054, and GH 29570\n    '
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
with tm.ensure_clean() as path:
    df.to_pickle(path, compression=compression)
    reference = Path(path).read_bytes()
buffer = io.BytesIO()
df.to_pickle(buffer, compression=compression)
buffer.seek(0)
assert buffer.getvalue() == reference or compression in ('gzip', 'zip', 'tar')
read_df = pd.read_pickle(buffer, compression=compression)
buffer.seek(0)
tm.assert_frame_equal(df, read_df)
```

## Next Steps


---

*Source: test_pickle.py:535 | Complexity: Advanced | Last updated: 2026-06-02*