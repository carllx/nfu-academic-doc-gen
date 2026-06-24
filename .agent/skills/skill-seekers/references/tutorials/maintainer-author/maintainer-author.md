# How To: Maintainer Author

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maintainer author

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `functools`
- `io`
- `email`
- `email.generator`
- `email.message`
- `email.parser`
- `email.policy`
- `inspect`
- `pathlib`
- `unittest.mock`
- `jaraco.path`
- `pytest`
- `packaging.metadata`
- `setuptools`
- `setuptools._core_metadata`
- `setuptools.config`
- `setuptools.dist`
- `config.downloads`

**Setup Required:**
```python
# Fixtures: name, attrs, tmpdir
```

## Step-by-Step Guide

### Step 1: Assign tested_keys = value

```python
tested_keys = {'author': 'Author', 'author_email': 'Author-email', 'maintainer': 'Maintainer', 'maintainer_email': 'Maintainer-email'}
```

**Verification:**
```python
assert _valid_metadata(pkg_info)
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

**Verification:**
```python
assert len(pkg_lines) == len(pkg_lines_set)
```

### Step 3: Assign fn = tmpdir.mkdir(...)

```python
fn = tmpdir.mkdir('pkg_info')
```

**Verification:**
```python
assert not line.startswith(fkey + ':')
```

### Step 4: Assign fn_s = str(...)

```python
fn_s = str(fn)
```

**Verification:**
```python
assert line in pkg_lines_set
```

### Step 5: Call dist.metadata.write_pkg_info()

```python
dist.metadata.write_pkg_info(fn_s)
```

**Verification:**
```python
assert _valid_metadata(pkg_info)
```

### Step 6: Assign raw_pkg_lines = pkg_info.splitlines(...)

```python
raw_pkg_lines = pkg_info.splitlines()
```

### Step 7: Assign pkg_lines = list(...)

```python
pkg_lines = list(filter(None, raw_pkg_lines[:-2]))
```

### Step 8: Assign pkg_lines_set = set(...)

```python
pkg_lines_set = set(pkg_lines)
```

**Verification:**
```python
assert len(pkg_lines) == len(pkg_lines_set)
```

### Step 9: Assign pkg_info = f.read(...)

```python
pkg_info = f.read()
```

### Step 10: Assign val = attrs.get(...)

```python
val = attrs.get(dkey, None)
```

### Step 11: Assign line = value

```python
line = f'{fkey}: {val}'
```

**Verification:**
```python
assert line in pkg_lines_set
```


## Complete Example

```python
# Setup
# Fixtures: name, attrs, tmpdir

# Workflow
tested_keys = {'author': 'Author', 'author_email': 'Author-email', 'maintainer': 'Maintainer', 'maintainer_email': 'Maintainer-email'}
dist = Distribution(attrs)
fn = tmpdir.mkdir('pkg_info')
fn_s = str(fn)
dist.metadata.write_pkg_info(fn_s)
with open(str(fn.join('PKG-INFO')), 'r', encoding='utf-8') as f:
    pkg_info = f.read()
assert _valid_metadata(pkg_info)
raw_pkg_lines = pkg_info.splitlines()
pkg_lines = list(filter(None, raw_pkg_lines[:-2]))
pkg_lines_set = set(pkg_lines)
assert len(pkg_lines) == len(pkg_lines_set)
for fkey, dkey in tested_keys.items():
    val = attrs.get(dkey, None)
    if val is None:
        for line in pkg_lines:
            assert not line.startswith(fkey + ':')
    else:
        line = f'{fkey}: {val}'
        assert line in pkg_lines_set
```

## Next Steps


---

*Source: test_core_metadata.py:278 | Complexity: Advanced | Last updated: 2026-06-02*