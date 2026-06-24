# How To: Package Data And Include Package Data In Sdist

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Ensure package_data and include_package_data work
together.

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

### Step 1: '\n        Ensure package_data and include_package_data work\n        together.\n        '

```python
'\n        Ensure package_data and include_package_data work\n        together.\n        '
```

**Verification:**
```python
assert setup_attrs['package_data']
```

### Step 2: Assign setup_attrs = value

```python
setup_attrs = {**SETUP_ATTRS, 'include_package_data': True}
```

**Verification:**
```python
assert setup_attrs['package_data']
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution(setup_attrs)
```

### Step 4: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 5: Assign cmd = sdist(...)

```python
cmd = sdist(dist)
```

### Step 6: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 7: Call self.assert_package_data_in_manifest()

```python
self.assert_package_data_in_manifest(cmd)
```

### Step 8: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Workflow
'\n        Ensure package_data and include_package_data work\n        together.\n        '
setup_attrs = {**SETUP_ATTRS, 'include_package_data': True}
assert setup_attrs['package_data']
dist = Distribution(setup_attrs)
dist.script_name = 'setup.py'
cmd = sdist(dist)
cmd.ensure_finalized()
with quiet():
    cmd.run()
self.assert_package_data_in_manifest(cmd)
```

## Next Steps


---

*Source: test_sdist.py:191 | Complexity: Advanced | Last updated: 2026-06-02*