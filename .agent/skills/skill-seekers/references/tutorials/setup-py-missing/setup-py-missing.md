# How To: Setup Py Missing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test setup py missing

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

### Step 6: Call os.remove()

```python
os.remove('setup.py')
```

### Step 7: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Workflow
dist = Distribution(SETUP_ATTRS)
dist.script_name = 'foo.py'
cmd = sdist(dist)
cmd.ensure_finalized()
if os.path.exists('setup.py'):
    os.remove('setup.py')
with quiet():
    cmd.run()
manifest = cmd.filelist.files
assert 'setup.py' not in manifest
```

## Next Steps


---

*Source: test_sdist.py:366 | Complexity: Intermediate | Last updated: 2026-06-02*