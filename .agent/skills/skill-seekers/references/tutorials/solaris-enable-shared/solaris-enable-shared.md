# How To: Solaris Enable Shared

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test solaris enable shared

## Prerequisites

**Required Modules:**
- `contextlib`
- `glob`
- `importlib`
- `os.path`
- `platform`
- `re`
- `shutil`
- `site`
- `subprocess`
- `sys`
- `tempfile`
- `textwrap`
- `time`
- `distutils`
- `distutils.command.build_ext`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.tests.support`
- `io`
- `jaraco.path`
- `path`
- `pytest`
- `test`
- `compat`
- `distutils.command`
- `xx`
- `distutils.sysconfig`
- `site`
- `pprint`


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'xx'})
```

**Verification:**
```python
assert len(cmd.library_dirs) > 0
```

### Step 2: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

### Step 3: Assign old = value

```python
old = sys.platform
```

### Step 4: Assign sys.platform = 'sunos'

```python
sys.platform = 'sunos'
```

### Step 5: Assign old_var = _config_vars.get(...)

```python
old_var = _config_vars.get('Py_ENABLE_SHARED')
```

### Step 6: Assign unknown = True

```python
_config_vars['Py_ENABLE_SHARED'] = True
```

**Verification:**
```python
assert len(cmd.library_dirs) > 0
```

### Step 7: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 8: Assign sys.platform = old

```python
sys.platform = old
```

### Step 9: Assign unknown = old_var

```python
_config_vars['Py_ENABLE_SHARED'] = old_var
```


## Complete Example

```python
# Workflow
dist = Distribution({'name': 'xx'})
cmd = self.build_ext(dist)
old = sys.platform
sys.platform = 'sunos'
from distutils.sysconfig import _config_vars
old_var = _config_vars.get('Py_ENABLE_SHARED')
_config_vars['Py_ENABLE_SHARED'] = True
try:
    cmd.ensure_finalized()
finally:
    sys.platform = old
    if old_var is None:
        del _config_vars['Py_ENABLE_SHARED']
    else:
        _config_vars['Py_ENABLE_SHARED'] = old_var
assert len(cmd.library_dirs) > 0
```

## Next Steps


---

*Source: test_build_ext.py:185 | Complexity: Advanced | Last updated: 2026-06-02*