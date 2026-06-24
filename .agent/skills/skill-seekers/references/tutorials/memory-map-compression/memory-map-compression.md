# How To: Memory Map Compression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Support memory map for compressed files.

GH 37621

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `platform`
- `urllib.error`
- `uuid`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, compression
```

## Step-by-Step Guide

### Step 1: '\n    Support memory map for compressed files.\n\n    GH 37621\n    '

```python
'\n    Support memory map for compressed files.\n\n    GH 37621\n    '
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1], 'b': [2]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Call expected.to_csv()

```python
expected.to_csv(path, index=False, compression=compression)
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(path, memory_map=True, compression=compression)
```

### Step 7: Assign msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(path, memory_map=True, compression=compression)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, compression

# Workflow
'\n    Support memory map for compressed files.\n\n    GH 37621\n    '
parser = all_parsers
expected = DataFrame({'a': [1], 'b': [2]})
with tm.ensure_clean() as path:
    expected.to_csv(path, index=False, compression=compression)
    if parser.engine == 'pyarrow':
        msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv(path, memory_map=True, compression=compression)
        return
    result = parser.read_csv(path, memory_map=True, compression=compression)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_file_buffer_url.py:385 | Complexity: Advanced | Last updated: 2026-06-02*