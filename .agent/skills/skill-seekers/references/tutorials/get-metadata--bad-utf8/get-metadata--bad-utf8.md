# How To: Get Metadata  Bad Utf8

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Test a metadata file with bytes that can't be decoded as utf-8.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `builtins`
- `datetime`
- `inspect`
- `os`
- `plistlib`
- `stat`
- `subprocess`
- `sys`
- `tempfile`
- `zipfile`
- `unittest`
- `pytest`
- `pkg_resources`
- `pkg_resources`
- `distutils.command.install_egg_info`
- `distutils.dist`
- `mod`
- `mod2`
- `mod`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: "\n    Test a metadata file with bytes that can't be decoded as utf-8.\n    "

```python
"\n    Test a metadata file with bytes that can't be decoded as utf-8.\n    "
```

**Verification:**
```python
assert expected in actual, f'actual: {actual}'
```

### Step 2: Assign filename = 'METADATA'

```python
filename = 'METADATA'
```

**Verification:**
```python
assert actual.endswith(metadata_path), f'actual: {actual}'
```

### Step 3: Assign metadata_path = os.path.join(...)

```python
metadata_path = os.path.join(str(tmpdir), 'foo.dist-info', filename)
```

### Step 4: Assign metadata = unknown.encode(...)

```python
metadata = 'née'.encode('iso-8859-1')
```

### Step 5: Assign dist = make_test_distribution(...)

```python
dist = make_test_distribution(metadata_path, metadata=metadata)
```

### Step 6: Assign exc = value

```python
exc = excinfo.value
```

### Step 7: Assign actual = str(...)

```python
actual = str(exc)
```

### Step 8: Assign expected = "codec can't decode byte 0xe9 in position 1: invalid continuation byte in METADATA file at path: "

```python
expected = "codec can't decode byte 0xe9 in position 1: invalid continuation byte in METADATA file at path: "
```

**Verification:**
```python
assert expected in actual, f'actual: {actual}'
```

### Step 9: Call dist.get_metadata()

```python
dist.get_metadata(filename)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
"\n    Test a metadata file with bytes that can't be decoded as utf-8.\n    "
filename = 'METADATA'
metadata_path = os.path.join(str(tmpdir), 'foo.dist-info', filename)
metadata = 'née'.encode('iso-8859-1')
dist = make_test_distribution(metadata_path, metadata=metadata)
with pytest.raises(UnicodeDecodeError) as excinfo:
    dist.get_metadata(filename)
exc = excinfo.value
actual = str(exc)
expected = "codec can't decode byte 0xe9 in position 1: invalid continuation byte in METADATA file at path: "
assert expected in actual, f'actual: {actual}'
assert actual.endswith(metadata_path), f'actual: {actual}'
```

## Next Steps


---

*Source: test_pkg_resources.py:196 | Complexity: Advanced | Last updated: 2026-06-02*