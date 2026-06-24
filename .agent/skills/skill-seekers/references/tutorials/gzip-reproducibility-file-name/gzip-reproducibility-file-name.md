# How To: Gzip Reproducibility File Name

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Gzip should create reproducible archives with mtime.

Note: Archives created with different filenames will still be different!

GH 28103

## Prerequisites

**Required Modules:**
- `gzip`
- `io`
- `os`
- `pathlib`
- `subprocess`
- `sys`
- `tarfile`
- `textwrap`
- `time`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.io.common`


## Step-by-Step Guide

### Step 1: '\n    Gzip should create reproducible archives with mtime.\n\n    Note: Archives created with different filenames will still be different!\n\n    GH 28103\n    '

```python
'\n    Gzip should create reproducible archives with mtime.\n\n    Note: Archives created with different filenames will still be different!\n\n    GH 28103\n    '
```

**Verification:**
```python
assert output == path.read_bytes()
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=pd.Index(list('ABCD')), index=pd.Index([f'i-{i}' for i in range(30)]))
```

### Step 3: Assign compression_options = value

```python
compression_options = {'method': 'gzip', 'mtime': 1}
```

### Step 4: Assign path = Path(...)

```python
path = Path(path)
```

### Step 5: Call df.to_csv()

```python
df.to_csv(path, compression=compression_options)
```

### Step 6: Call time.sleep()

```python
time.sleep(0.1)
```

### Step 7: Assign output = path.read_bytes(...)

```python
output = path.read_bytes()
```

### Step 8: Call df.to_csv()

```python
df.to_csv(path, compression=compression_options)
```

**Verification:**
```python
assert output == path.read_bytes()
```


## Complete Example

```python
# Workflow
'\n    Gzip should create reproducible archives with mtime.\n\n    Note: Archives created with different filenames will still be different!\n\n    GH 28103\n    '
df = pd.DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=pd.Index(list('ABCD')), index=pd.Index([f'i-{i}' for i in range(30)]))
compression_options = {'method': 'gzip', 'mtime': 1}
with tm.ensure_clean() as path:
    path = Path(path)
    df.to_csv(path, compression=compression_options)
    time.sleep(0.1)
    output = path.read_bytes()
    df.to_csv(path, compression=compression_options)
    assert output == path.read_bytes()
```

## Next Steps


---

*Source: test_compression.py:170 | Complexity: Advanced | Last updated: 2026-06-02*