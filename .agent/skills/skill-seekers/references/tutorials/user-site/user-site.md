# How To: User Site

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test user site

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
assert 'user' in options
```

### Step 2: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

**Verification:**
```python
assert lib in cmd.library_dirs
```

### Step 3: Assign options = value

```python
options = [name for name, short, label in cmd.user_options]
```

**Verification:**
```python
assert lib in cmd.rpath
```

### Step 4: Assign cmd.user = True

```python
cmd.user = True
```

**Verification:**
```python
assert incl in cmd.include_dirs
```

### Step 5: Assign lib = os.path.join(...)

```python
lib = os.path.join(site.USER_BASE, 'lib')
```

### Step 6: Assign incl = os.path.join(...)

```python
incl = os.path.join(site.USER_BASE, 'include')
```

### Step 7: Call os.mkdir()

```python
os.mkdir(lib)
```

### Step 8: Call os.mkdir()

```python
os.mkdir(incl)
```

### Step 9: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

**Verification:**
```python
assert lib in cmd.library_dirs
```


## Complete Example

```python
# Workflow
import site
dist = Distribution({'name': 'xx'})
cmd = self.build_ext(dist)
options = [name for name, short, label in cmd.user_options]
assert 'user' in options
cmd.user = True
lib = os.path.join(site.USER_BASE, 'lib')
incl = os.path.join(site.USER_BASE, 'include')
os.mkdir(lib)
os.mkdir(incl)
cmd.ensure_finalized()
assert lib in cmd.library_dirs
assert lib in cmd.rpath
assert incl in cmd.include_dirs
```

## Next Steps


---

*Source: test_build_ext.py:207 | Complexity: Advanced | Last updated: 2026-06-02*