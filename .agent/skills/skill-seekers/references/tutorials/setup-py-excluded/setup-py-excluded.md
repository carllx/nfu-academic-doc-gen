# How To: Setup Py Excluded

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test setup py excluded

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution(SETUP_ATTRS)
```

**Verification:**
```python
assert 'setup.py' not in manifest
```

### Step 2: Assign dist.script_name = 'foo.py'

```python
dist.script_name = 'foo.py'
```

### Step 3: Assign cmd = sdist(...)

```python
cmd = sdist(dist)
```

### Step 4: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 5: Assign manifest = value

```python
manifest = cmd.filelist.files
```

**Verification:**
```python
assert 'setup.py' not in manifest
```

### Step 6: Call manifest_file.write()

```python
manifest_file.write('exclude setup.py')
```

### Step 7: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Workflow
with open('MANIFEST.in', 'w', encoding='utf-8') as manifest_file:
    manifest_file.write('exclude setup.py')
dist = Distribution(SETUP_ATTRS)
dist.script_name = 'foo.py'
cmd = sdist(dist)
cmd.ensure_finalized()
with quiet():
    cmd.run()
manifest = cmd.filelist.files
assert 'setup.py' not in manifest
```

## Next Steps


---

*Source: test_sdist.py:380 | Complexity: Intermediate | Last updated: 2026-06-02*