# How To: Distribution Version Missing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, pytest, workflow, integration

## Overview

Workflow: Test Distribution.version when the "Version" header is missing.

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
# Fixtures: tmpdir, suffix, expected_filename, expected_dist_type
```

## Step-by-Step Guide

### Step 1: '\n    Test Distribution.version when the "Version" header is missing.\n    '

```python
'\n    Test Distribution.version when the "Version" header is missing.\n    '
```

**Verification:**
```python
assert expected_text in err, str((expected_text, err))
```

### Step 2: Assign basename = value

```python
basename = f'foo.{suffix}'
```

**Verification:**
```python
assert expected_text in msg
```

### Step 3: Assign unknown = make_distribution_no_version(...)

```python
dist, dist_dir = make_distribution_no_version(tmpdir, basename)
```

**Verification:**
```python
assert metadata_path in msg, str((metadata_path, msg))
```

### Step 4: Assign expected_text = value

```python
expected_text = f"Missing 'Version:' header and/or {expected_filename} file at path: "
```

**Verification:**
```python
assert type(dist) is expected_dist_type
```

### Step 5: Assign metadata_path = os.path.join(...)

```python
metadata_path = os.path.join(dist_dir, expected_filename)
```

### Step 6: Assign err = str(...)

```python
err = str(excinfo.value)
```

**Verification:**
```python
assert expected_text in err, str((expected_text, err))
```

### Step 7: Assign unknown = value

```python
msg, dist = excinfo.value.args
```

**Verification:**
```python
assert expected_text in msg
```

### Step 8: dist.version

```python
dist.version
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, suffix, expected_filename, expected_dist_type

# Workflow
'\n    Test Distribution.version when the "Version" header is missing.\n    '
basename = f'foo.{suffix}'
dist, dist_dir = make_distribution_no_version(tmpdir, basename)
expected_text = f"Missing 'Version:' header and/or {expected_filename} file at path: "
metadata_path = os.path.join(dist_dir, expected_filename)
with pytest.raises(ValueError) as excinfo:
    dist.version
err = str(excinfo.value)
assert expected_text in err, str((expected_text, err))
msg, dist = excinfo.value.args
assert expected_text in msg
assert metadata_path in msg, str((metadata_path, msg))
assert type(dist) is expected_dist_type
```

## Next Steps


---

*Source: test_pkg_resources.py:250 | Complexity: Advanced | Last updated: 2026-06-02*