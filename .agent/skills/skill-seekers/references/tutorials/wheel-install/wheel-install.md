# How To: Wheel Install

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test wheel install

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `contextlib`
- `glob`
- `inspect`
- `os`
- `pathlib`
- `stat`
- `subprocess`
- `sys`
- `sysconfig`
- `zipfile`
- `typing`
- `pytest`
- `jaraco`
- `packaging.tags`
- `setuptools._importlib`
- `setuptools.wheel`
- `contexts`
- `textwrap`
- `distutils.sysconfig`
- `distutils.util`

**Setup Required:**
```python
# Fixtures: params
```

## Step-by-Step Guide

### Step 1: Assign project_name = params.get(...)

```python
project_name = params.get('name', 'foo')
```

### Step 2: Assign version = params.get(...)

```python
version = params.get('version', '1.0')
```

### Step 3: Assign install_requires = params.get(...)

```python
install_requires = params.get('install_requires', [])
```

### Step 4: Assign extras_require = params.get(...)

```python
extras_require = params.get('extras_require', {})
```

### Step 5: Assign requires_txt = params.get(...)

```python
requires_txt = params.get('requires_txt', None)
```

### Step 6: Assign install_tree = params.get(...)

```python
install_tree = params.get('install_tree')
```

### Step 7: Assign file_defs = params.get(...)

```python
file_defs = params.get('file_defs', {})
```

### Step 8: Assign setup_kwargs = params.get(...)

```python
setup_kwargs = params.get('setup_kwargs', {})
```

### Step 9: Call _check_wheel_install()

```python
_check_wheel_install(filename, install_dir, install_tree, project_name, version, requires_txt)
```


## Complete Example

```python
# Setup
# Fixtures: params

# Workflow
project_name = params.get('name', 'foo')
version = params.get('version', '1.0')
install_requires = params.get('install_requires', [])
extras_require = params.get('extras_require', {})
requires_txt = params.get('requires_txt', None)
install_tree = params.get('install_tree')
file_defs = params.get('file_defs', {})
setup_kwargs = params.get('setup_kwargs', {})
with build_wheel(name=project_name, version=version, install_requires=install_requires, extras_require=extras_require, extra_file_defs=file_defs, **setup_kwargs) as filename, tempdir() as install_dir:
    _check_wheel_install(filename, install_dir, install_tree, project_name, version, requires_txt)
```

## Next Steps


---

*Source: test_wheel.py:554 | Complexity: Advanced | Last updated: 2026-06-02*