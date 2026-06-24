# How To: Utf16 Bom Skiprows

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test utf16 bom skiprows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `tempfile`
- `uuid`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, sep, encoding
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = unknown.replace(...)

```python
data = 'skip this\nskip this too\nA,B,C\n1,2,3\n4,5,6'.replace(',', sep)
```

### Step 3: Assign path = value

```python
path = f'__{uuid.uuid4()}__.csv'
```

### Step 4: Assign kwargs = value

```python
kwargs = {'sep': sep, 'skiprows': 2}
```

### Step 5: Assign utf8 = 'utf-8'

```python
utf8 = 'utf-8'
```

### Step 6: Assign bytes_data = data.encode(...)

```python
bytes_data = data.encode(encoding)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call f.write()

```python
f.write(bytes_data)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(path, encoding=encoding, **kwargs)
```

### Step 10: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(bytes_buffer, encoding=utf8, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, sep, encoding

# Workflow
parser = all_parsers
data = 'skip this\nskip this too\nA,B,C\n1,2,3\n4,5,6'.replace(',', sep)
path = f'__{uuid.uuid4()}__.csv'
kwargs = {'sep': sep, 'skiprows': 2}
utf8 = 'utf-8'
with tm.ensure_clean(path) as path:
    bytes_data = data.encode(encoding)
    with open(path, 'wb') as f:
        f.write(bytes_data)
    with TextIOWrapper(BytesIO(data.encode(utf8)), encoding=utf8) as bytes_buffer:
        result = parser.read_csv(path, encoding=encoding, **kwargs)
        expected = parser.read_csv(bytes_buffer, encoding=utf8, **kwargs)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_encoding.py:53 | Complexity: Advanced | Last updated: 2026-06-02*