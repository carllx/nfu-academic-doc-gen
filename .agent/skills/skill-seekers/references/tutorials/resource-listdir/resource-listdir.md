# How To: Resource Listdir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test resource listdir

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign zp = pkg_resources.ZipProvider(...)

```python
zp = pkg_resources.ZipProvider(mod)
```

**Verification:**
```python
assert sorted(zp.resource_listdir('')) == expected_root
```

### Step 2: Assign expected_root = value

```python
expected_root = ['data.dat', 'mod.py', 'subdir']
```

**Verification:**
```python
assert sorted(zp.resource_listdir('subdir')) == expected_subdir
```

### Step 3: Assign expected_subdir = value

```python
expected_subdir = ['data2.dat', 'mod2.py']
```

**Verification:**
```python
assert sorted(zp.resource_listdir('subdir/')) == expected_subdir
```

### Step 4: Assign zp2 = pkg_resources.ZipProvider(...)

```python
zp2 = pkg_resources.ZipProvider(mod2)
```

**Verification:**
```python
assert zp.resource_listdir('nonexistent') == []
```


## Complete Example

```python
# Workflow
import mod
zp = pkg_resources.ZipProvider(mod)
expected_root = ['data.dat', 'mod.py', 'subdir']
assert sorted(zp.resource_listdir('')) == expected_root
expected_subdir = ['data2.dat', 'mod2.py']
assert sorted(zp.resource_listdir('subdir')) == expected_subdir
assert sorted(zp.resource_listdir('subdir/')) == expected_subdir
assert zp.resource_listdir('nonexistent') == []
assert zp.resource_listdir('nonexistent/') == []
import mod2
zp2 = pkg_resources.ZipProvider(mod2)
assert sorted(zp2.resource_listdir('')) == expected_subdir
assert zp2.resource_listdir('subdir') == []
assert zp2.resource_listdir('subdir/') == []
```

## Next Steps


---

*Source: test_pkg_resources.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*