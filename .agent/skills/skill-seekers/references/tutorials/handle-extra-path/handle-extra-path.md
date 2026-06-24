# How To: Handle Extra Path

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test handle extra path

## Prerequisites

**Required Modules:**
- `logging`
- `os`
- `pathlib`
- `site`
- `sys`
- `distutils`
- `distutils.command`
- `distutils.command.build_ext`
- `distutils.command.install`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.util`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'xx', 'extra_path': 'path,dirs'})
```

**Verification:**
```python
assert cmd.extra_path == ['path', 'dirs']
```

### Step 2: Assign cmd = install(...)

```python
cmd = install(dist)
```

**Verification:**
```python
assert cmd.extra_dirs == 'dirs'
```

### Step 3: Call cmd.handle_extra_path()

```python
cmd.handle_extra_path()
```

**Verification:**
```python
assert cmd.path_file == 'path'
```

### Step 4: Assign cmd.extra_path = value

```python
cmd.extra_path = ['path']
```

**Verification:**
```python
assert cmd.extra_path == ['path']
```

### Step 5: Call cmd.handle_extra_path()

```python
cmd.handle_extra_path()
```

**Verification:**
```python
assert cmd.extra_dirs == 'path'
```

### Step 6: Assign dist.extra_path, cmd.extra_path = None

```python
dist.extra_path = cmd.extra_path = None
```

**Verification:**
```python
assert cmd.path_file == 'path'
```

### Step 7: Call cmd.handle_extra_path()

```python
cmd.handle_extra_path()
```

**Verification:**
```python
assert cmd.extra_path is None
```

### Step 8: Assign cmd.extra_path = 'path,dirs,again'

```python
cmd.extra_path = 'path,dirs,again'
```

**Verification:**
```python
assert cmd.extra_dirs == ''
```

### Step 9: Call cmd.handle_extra_path()

```python
cmd.handle_extra_path()
```

**Verification:**
```python
assert cmd.path_file is None
```


## Complete Example

```python
# Workflow
dist = Distribution({'name': 'xx', 'extra_path': 'path,dirs'})
cmd = install(dist)
cmd.handle_extra_path()
assert cmd.extra_path == ['path', 'dirs']
assert cmd.extra_dirs == 'dirs'
assert cmd.path_file == 'path'
cmd.extra_path = ['path']
cmd.handle_extra_path()
assert cmd.extra_path == ['path']
assert cmd.extra_dirs == 'path'
assert cmd.path_file == 'path'
dist.extra_path = cmd.extra_path = None
cmd.handle_extra_path()
assert cmd.extra_path is None
assert cmd.extra_dirs == ''
assert cmd.path_file is None
cmd.extra_path = 'path,dirs,again'
with pytest.raises(DistutilsOptionError):
    cmd.handle_extra_path()
```

## Next Steps


---

*Source: test_install.py:130 | Complexity: Advanced | Last updated: 2026-06-02*