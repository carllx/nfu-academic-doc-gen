# How To: Series Compression Defaults To Infer

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series compression defaults to infer

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: write_method, write_kwargs, read_method, read_kwargs, compression_only, compression_to_extension
```

## Step-by-Step Guide

### Step 1: Assign input = pd.Series(...)

```python
input = pd.Series([0, 5, -2, 10], name='X')
```

### Step 2: Assign extension = value

```python
extension = compression_to_extension[compression_only]
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(output, input, check_names=False)
```

### Step 4: Call getattr()

```python
getattr(input, write_method)(path, **write_kwargs)
```

### Step 5: Assign kwargs = read_kwargs.copy(...)

```python
kwargs = read_kwargs.copy()
```

### Step 6: Assign output = read_method.squeeze(...)

```python
output = read_method(path, compression=compression_only, **kwargs).squeeze('columns')
```

### Step 7: Assign output = read_method(...)

```python
output = read_method(path, compression=compression_only, **read_kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: write_method, write_kwargs, read_method, read_kwargs, compression_only, compression_to_extension

# Workflow
input = pd.Series([0, 5, -2, 10], name='X')
extension = compression_to_extension[compression_only]
with tm.ensure_clean('compressed' + extension) as path:
    getattr(input, write_method)(path, **write_kwargs)
    if 'squeeze' in read_kwargs:
        kwargs = read_kwargs.copy()
        del kwargs['squeeze']
        output = read_method(path, compression=compression_only, **kwargs).squeeze('columns')
    else:
        output = read_method(path, compression=compression_only, **read_kwargs)
tm.assert_series_equal(output, input, check_names=False)
```

## Next Steps


---

*Source: test_compression.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*