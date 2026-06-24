# How To: Gzip Reproducibility File Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Gzip should create reproducible archives with mtime.

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

### Step 1: '\n    Gzip should create reproducible archives with mtime.\n\n    GH 28103\n    '

```python
'\n    Gzip should create reproducible archives with mtime.\n\n    GH 28103\n    '
```

**Verification:**
```python
assert output == buffer.getvalue()
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=pd.Index(list('ABCD')), index=pd.Index([f'i-{i}' for i in range(30)]))
```

### Step 3: Assign compression_options = value

```python
compression_options = {'method': 'gzip', 'mtime': 1}
```

### Step 4: Assign buffer = io.BytesIO(...)

```python
buffer = io.BytesIO()
```

### Step 5: Call df.to_csv()

```python
df.to_csv(buffer, compression=compression_options, mode='wb')
```

### Step 6: Assign output = buffer.getvalue(...)

```python
output = buffer.getvalue()
```

### Step 7: Call time.sleep()

```python
time.sleep(0.1)
```

### Step 8: Assign buffer = io.BytesIO(...)

```python
buffer = io.BytesIO()
```

### Step 9: Call df.to_csv()

```python
df.to_csv(buffer, compression=compression_options, mode='wb')
```

**Verification:**
```python
assert output == buffer.getvalue()
```


## Complete Example

```python
# Workflow
'\n    Gzip should create reproducible archives with mtime.\n\n    GH 28103\n    '
df = pd.DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=pd.Index(list('ABCD')), index=pd.Index([f'i-{i}' for i in range(30)]))
compression_options = {'method': 'gzip', 'mtime': 1}
buffer = io.BytesIO()
df.to_csv(buffer, compression=compression_options, mode='wb')
output = buffer.getvalue()
time.sleep(0.1)
buffer = io.BytesIO()
df.to_csv(buffer, compression=compression_options, mode='wb')
assert output == buffer.getvalue()
```

## Next Steps


---

*Source: test_compression.py:195 | Complexity: Advanced | Last updated: 2026-06-02*