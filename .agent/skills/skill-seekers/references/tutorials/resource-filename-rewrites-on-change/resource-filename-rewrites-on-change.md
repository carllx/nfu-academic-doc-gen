# How To: Resource Filename Rewrites On Change

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: If a previous call to get_resource_filename has saved the file, but
the file has been subsequently mutated with different file of the
same size and modification time, it should not be overwritten on a
subsequent call to get_resource_filename.

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

### Step 1: '\n        If a previous call to get_resource_filename has saved the file, but\n        the file has been subsequently mutated with different file of the\n        same size and modification time, it should not be overwritten on a\n        subsequent call to get_resource_filename.\n        '

```python
'\n        If a previous call to get_resource_filename has saved the file, but\n        the file has been subsequently mutated with different file of the\n        same size and modification time, it should not be overwritten on a\n        subsequent call to get_resource_filename.\n        '
```

**Verification:**
```python
assert actual == self.ref_time
```

### Step 2: Assign manager = pkg_resources.ResourceManager(...)

```python
manager = pkg_resources.ResourceManager()
```

**Verification:**
```python
assert f.read() == 'hello, world!'
```

### Step 3: Assign zp = pkg_resources.ZipProvider(...)

```python
zp = pkg_resources.ZipProvider(mod)
```

### Step 4: Assign filename = zp.get_resource_filename(...)

```python
filename = zp.get_resource_filename(manager, 'data.dat')
```

### Step 5: Assign actual = datetime.datetime.fromtimestamp(...)

```python
actual = datetime.datetime.fromtimestamp(os.stat(filename).st_mtime)
```

**Verification:**
```python
assert actual == self.ref_time
```

### Step 6: Assign f = open(...)

```python
f = open(filename, 'w', encoding='utf-8')
```

### Step 7: Call f.write()

```python
f.write('hello, world?')
```

### Step 8: Call f.close()

```python
f.close()
```

### Step 9: Assign ts = self.ref_time.timestamp(...)

```python
ts = self.ref_time.timestamp()
```

### Step 10: Call os.utime()

```python
os.utime(filename, (ts, ts))
```

### Step 11: Assign filename = zp.get_resource_filename(...)

```python
filename = zp.get_resource_filename(manager, 'data.dat')
```

### Step 12: Call manager.cleanup_resources()

```python
manager.cleanup_resources()
```

**Verification:**
```python
assert f.read() == 'hello, world!'
```


## Complete Example

```python
# Workflow
'\n        If a previous call to get_resource_filename has saved the file, but\n        the file has been subsequently mutated with different file of the\n        same size and modification time, it should not be overwritten on a\n        subsequent call to get_resource_filename.\n        '
import mod
manager = pkg_resources.ResourceManager()
zp = pkg_resources.ZipProvider(mod)
filename = zp.get_resource_filename(manager, 'data.dat')
actual = datetime.datetime.fromtimestamp(os.stat(filename).st_mtime)
assert actual == self.ref_time
f = open(filename, 'w', encoding='utf-8')
f.write('hello, world?')
f.close()
ts = self.ref_time.timestamp()
os.utime(filename, (ts, ts))
filename = zp.get_resource_filename(manager, 'data.dat')
with open(filename, encoding='utf-8') as f:
    assert f.read() == 'hello, world!'
manager.cleanup_resources()
```

## Next Steps


---

*Source: test_pkg_resources.py:97 | Complexity: Advanced | Last updated: 2026-06-02*