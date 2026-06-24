# How To: Encoding Errors

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test encoding errors

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `errno`
- `functools`
- `io`
- `mmap`
- `os`
- `pathlib`
- `pickle`
- `tempfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `py.path`

**Setup Required:**
```python
# Fixtures: encoding_errors, format
```

## Step-by-Step Guide

### Step 1: Assign msg = "'utf-8' codec can't decode byte"

```python
msg = "'utf-8' codec can't decode byte"
```

### Step 2: Assign bad_encoding = b'\xe4'

```python
bad_encoding = b'\xe4'
```

### Step 3: Assign content = value

```python
content = b',' + bad_encoding + b'\n' + bad_encoding * 2 + b',' + bad_encoding
```

### Step 4: Assign reader = partial(...)

```python
reader = partial(pd.read_csv, index_col=0)
```

### Step 5: Assign content = value

```python
content = b'{"' + bad_encoding * 2 + b'": {"' + bad_encoding + b'":"' + bad_encoding + b'"}}'
```

### Step 6: Assign reader = partial(...)

```python
reader = partial(pd.read_json, orient='index')
```

### Step 7: Assign file = Path(...)

```python
file = Path(path)
```

### Step 8: Call file.write_bytes()

```python
file.write_bytes(content)
```

### Step 9: Assign df = reader(...)

```python
df = reader(path, encoding_errors=encoding_errors)
```

### Step 10: Assign decoded = bad_encoding.decode(...)

```python
decoded = bad_encoding.decode(errors=encoding_errors)
```

### Step 11: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({decoded: [decoded]}, index=[decoded * 2])
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 13: Call reader()

```python
reader(path, encoding_errors=encoding_errors)
```


## Complete Example

```python
# Setup
# Fixtures: encoding_errors, format

# Workflow
msg = "'utf-8' codec can't decode byte"
bad_encoding = b'\xe4'
if format == 'csv':
    content = b',' + bad_encoding + b'\n' + bad_encoding * 2 + b',' + bad_encoding
    reader = partial(pd.read_csv, index_col=0)
else:
    content = b'{"' + bad_encoding * 2 + b'": {"' + bad_encoding + b'":"' + bad_encoding + b'"}}'
    reader = partial(pd.read_json, orient='index')
with tm.ensure_clean() as path:
    file = Path(path)
    file.write_bytes(content)
    if encoding_errors != 'replace':
        with pytest.raises(UnicodeDecodeError, match=msg):
            reader(path, encoding_errors=encoding_errors)
    else:
        df = reader(path, encoding_errors=encoding_errors)
        decoded = bad_encoding.decode(errors=encoding_errors)
        expected = pd.DataFrame({decoded: [decoded]}, index=[decoded * 2])
        tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_common.py:575 | Complexity: Advanced | Last updated: 2026-06-02*