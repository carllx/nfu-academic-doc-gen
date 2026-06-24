# How To: Get Cache Path Race

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test get cache path race

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign patched_isdir.dirnames = value

```python
patched_isdir.dirnames = []
```

**Verification:**
```python
assert len(called_dirnames) == 2
```

### Step 2: Assign mgr = pkg_resources.ResourceManager(...)

```python
mgr = pkg_resources.ResourceManager()
```

**Verification:**
```python
assert called_dirnames[0].split(os.sep)[-2:] == ['foo', 'bar']
```

### Step 3: Call mgr.set_extraction_path()

```python
mgr.set_extraction_path(str(tmpdir))
```

**Verification:**
```python
assert called_dirnames[1].split(os.sep)[-1:] == ['foo']
```

### Step 4: Assign archive_name = os.sep.join(...)

```python
archive_name = os.sep.join(('foo', 'bar', 'baz'))
```

### Step 5: Assign called_dirnames = value

```python
called_dirnames = patched_isdir.dirnames
```

**Verification:**
```python
assert len(called_dirnames) == 2
```

### Step 6: Call patched_isdir.dirnames.append()

```python
patched_isdir.dirnames.append(dirname)
```

### Step 7: Assign was_dir = unpatched_isdir(...)

```python
was_dir = unpatched_isdir(dirname)
```

### Step 8: Call mgr.get_cache_path()

```python
mgr.get_cache_path(archive_name)
```

### Step 9: Call os.makedirs()

```python
os.makedirs(dirname)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
def patched_isdir(dirname, unpatched_isdir=pkg_resources.isdir):
    patched_isdir.dirnames.append(dirname)
    was_dir = unpatched_isdir(dirname)
    if not was_dir:
        os.makedirs(dirname)
    return was_dir
patched_isdir.dirnames = []
mgr = pkg_resources.ResourceManager()
mgr.set_extraction_path(str(tmpdir))
archive_name = os.sep.join(('foo', 'bar', 'baz'))
with mock.patch.object(pkg_resources, 'isdir', new=patched_isdir):
    mgr.get_cache_path(archive_name)
called_dirnames = patched_isdir.dirnames
assert len(called_dirnames) == 2
assert called_dirnames[0].split(os.sep)[-2:] == ['foo', 'bar']
assert called_dirnames[1].split(os.sep)[-1:] == ['foo']
```

## Next Steps


---

*Source: test_pkg_resources.py:130 | Complexity: Advanced | Last updated: 2026-06-02*