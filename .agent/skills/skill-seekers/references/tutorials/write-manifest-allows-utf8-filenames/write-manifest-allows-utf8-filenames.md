# How To: Write Manifest Allows Utf8 Filenames

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test write manifest allows utf8 filenames

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
assert posix(filename) in contents
```

### Step 2: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

**Verification:**
```python
assert u_filename in mm.filelist.files
```

### Step 3: Assign mm = manifest_maker(...)

```python
mm = manifest_maker(dist)
```

### Step 4: Assign mm.manifest = os.path.join(...)

```python
mm.manifest = os.path.join('sdist_test.egg-info', 'SOURCES.txt')
```

### Step 5: Call os.mkdir()

```python
os.mkdir('sdist_test.egg-info')
```

### Step 6: Assign filename = os.path.join(...)

```python
filename = os.path.join(b'sdist_test', Filenames.utf_8)
```

### Step 7: Call touch()

```python
touch(filename)
```

### Step 8: Assign contents = read_all_bytes(...)

```python
contents = read_all_bytes(mm.manifest)
```

### Step 9: Call contents.decode()

```python
contents.decode('UTF-8')
```

**Verification:**
```python
assert posix(filename) in contents
```

### Step 10: Call mm.run()

```python
mm.run()
```

### Step 11: Assign u_filename = filename.decode(...)

```python
u_filename = filename.decode('utf-8')
```

### Step 12: Call mm.filelist.files.append()

```python
mm.filelist.files.append(u_filename)
```

### Step 13: Call mm.write_manifest()

```python
mm.write_manifest()
```


## Complete Example

```python
# Workflow
dist = Distribution(SETUP_ATTRS)
dist.script_name = 'setup.py'
mm = manifest_maker(dist)
mm.manifest = os.path.join('sdist_test.egg-info', 'SOURCES.txt')
os.mkdir('sdist_test.egg-info')
filename = os.path.join(b'sdist_test', Filenames.utf_8)
touch(filename)
with quiet():
    mm.run()
    u_filename = filename.decode('utf-8')
    mm.filelist.files.append(u_filename)
    mm.write_manifest()
contents = read_all_bytes(mm.manifest)
contents.decode('UTF-8')
assert posix(filename) in contents
assert u_filename in mm.filelist.files
```

## Next Steps


---

*Source: test_sdist.py:493 | Complexity: Advanced | Last updated: 2026-06-02*