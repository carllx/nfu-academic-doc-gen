# How To: Infer Compression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infer compression

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
# Fixtures: all_parsers, csv1, buffer, ext
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign kwargs = value

```python
kwargs = {'index_col': 0, 'parse_dates': True}
```

### Step 3: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(csv1, **kwargs)
```

### Step 4: Assign unknown = 'infer'

```python
kwargs['compression'] = 'infer'
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign ext = value

```python
ext = '.' + ext if ext else ''
```

### Step 7: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(csv1 + ext, **kwargs)
```

### Step 8: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(f, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv1, buffer, ext

# Workflow
parser = all_parsers
kwargs = {'index_col': 0, 'parse_dates': True}
expected = parser.read_csv(csv1, **kwargs)
kwargs['compression'] = 'infer'
if buffer:
    with open(csv1, encoding='utf-8') as f:
        result = parser.read_csv(f, **kwargs)
else:
    ext = '.' + ext if ext else ''
    result = parser.read_csv(csv1 + ext, **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compression.py:125 | Complexity: Advanced | Last updated: 2026-06-02*