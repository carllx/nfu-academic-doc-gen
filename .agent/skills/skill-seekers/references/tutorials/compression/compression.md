# How To: Compression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compression

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `pathlib`
- `tarfile`
- `zipfile`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: request, parser_and_data, compression_only, buffer, filename, compression_to_extension
```

## Step-by-Step Guide

### Step 1: Assign unknown = parser_and_data

```python
parser, data, expected = parser_and_data
```

### Step 2: Assign compress_type = compression_only

```python
compress_type = compression_only
```

### Step 3: Assign ext = value

```python
ext = compression_to_extension[compress_type]
```

### Step 4: Assign filename = value

```python
filename = filename if filename is None else filename.format(ext=ext)
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Cannot deduce compression from buffer of compressed data.'))
```

### Step 6: Call tm.write_to_compressed()

```python
tm.write_to_compressed(compress_type, path, data)
```

### Step 7: Assign compression = value

```python
compression = 'infer' if filename else compress_type
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(path, compression=compression)
```

### Step 10: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(f, compression=compression)
```


## Complete Example

```python
# Setup
# Fixtures: request, parser_and_data, compression_only, buffer, filename, compression_to_extension

# Workflow
parser, data, expected = parser_and_data
compress_type = compression_only
ext = compression_to_extension[compress_type]
filename = filename if filename is None else filename.format(ext=ext)
if filename and buffer:
    request.applymarker(pytest.mark.xfail(reason='Cannot deduce compression from buffer of compressed data.'))
with tm.ensure_clean(filename=filename) as path:
    tm.write_to_compressed(compress_type, path, data)
    compression = 'infer' if filename else compress_type
    if buffer:
        with open(path, 'rb') as f:
            result = parser.read_csv(f, compression=compression)
    else:
        result = parser.read_csv(path, compression=compression)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compression.py:90 | Complexity: Advanced | Last updated: 2026-06-02*