# How To: Read Csv File Handle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test whether read_csv does not close user-provided file handles.

GH 36980

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
# Fixtures: all_parsers, io_class, encoding
```

## Step-by-Step Guide

### Step 1: '\n    Test whether read_csv does not close user-provided file handles.\n\n    GH 36980\n    '

```python
'\n    Test whether read_csv does not close user-provided file handles.\n\n    GH 36980\n    '
```

**Verification:**
```python
assert not handle.closed
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1], 'b': [2]})
```

### Step 4: Assign content = 'a,b\n1,2'

```python
content = 'a,b\n1,2'
```

### Step 5: Assign handle = io_class(...)

```python
handle = io_class(content.encode('utf-8') if io_class == BytesIO else content)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(parser.read_csv(handle, encoding=encoding), expected)
```

**Verification:**
```python
assert not handle.closed
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, io_class, encoding

# Workflow
'\n    Test whether read_csv does not close user-provided file handles.\n\n    GH 36980\n    '
parser = all_parsers
expected = DataFrame({'a': [1], 'b': [2]})
content = 'a,b\n1,2'
handle = io_class(content.encode('utf-8') if io_class == BytesIO else content)
tm.assert_frame_equal(parser.read_csv(handle, encoding=encoding), expected)
assert not handle.closed
```

## Next Steps


---

*Source: test_file_buffer_url.py:369 | Complexity: Intermediate | Last updated: 2026-06-02*