# How To: Defaults Case Sensitivity

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Make sure default files (README.*, etc.) are added in a case-sensitive
way to avoid problems with packages built on Windows.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `io`
- `logging`
- `os`
- `pathlib`
- `sys`
- `tarfile`
- `tempfile`
- `unicodedata`
- `inspect`
- `pathlib`
- `unittest`
- `jaraco.path`
- `pytest`
- `setuptools`
- `setuptools._importlib`
- `setuptools.command.egg_info`
- `setuptools.command.sdist`
- `setuptools.dist`
- `setuptools.extension`
- `setuptools.tests`
- `text`
- `distutils`
- `distutils.core`
- `distutils.command.build_py`

**Setup Required:**
```python
# Fixtures: source_dir
```

## Step-by-Step Guide

### Step 1: '\n        Make sure default files (README.*, etc.) are added in a case-sensitive\n        way to avoid problems with packages built on Windows.\n        '

```python
'\n        Make sure default files (README.*, etc.) are added in a case-sensitive\n        way to avoid problems with packages built on Windows.\n        '
```

**Verification:**
```python
assert 'readme.rst' not in manifest, manifest
```

### Step 2: Call touch()

```python
touch(source_dir / 'readme.rst')
```

**Verification:**
```python
assert 'setup.py' not in manifest, manifest
```

### Step 3: Call touch()

```python
touch(source_dir / 'SETUP.cfg')
```

**Verification:**
```python
assert 'setup.cfg' not in manifest, manifest
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution(SETUP_ATTRS)
```

### Step 5: Assign dist.script_name = 'setup.PY'

```python
dist.script_name = 'setup.PY'
```

### Step 6: Assign cmd = sdist(...)

```python
cmd = sdist(dist)
```

### Step 7: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 8: Assign manifest = map(...)

```python
manifest = map(lambda x: x.lower(), cmd.filelist.files)
```

**Verification:**
```python
assert 'readme.rst' not in manifest, manifest
```

### Step 9: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Setup
# Fixtures: source_dir

# Workflow
'\n        Make sure default files (README.*, etc.) are added in a case-sensitive\n        way to avoid problems with packages built on Windows.\n        '
touch(source_dir / 'readme.rst')
touch(source_dir / 'SETUP.cfg')
dist = Distribution(SETUP_ATTRS)
dist.script_name = 'setup.PY'
cmd = sdist(dist)
cmd.ensure_finalized()
with quiet():
    cmd.run()
manifest = map(lambda x: x.lower(), cmd.filelist.files)
assert 'readme.rst' not in manifest, manifest
assert 'setup.py' not in manifest, manifest
assert 'setup.cfg' not in manifest, manifest
```

## Next Steps


---

*Source: test_sdist.py:395 | Complexity: Advanced | Last updated: 2026-06-02*