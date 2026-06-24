# How To: Manifest Is Written With Utf8 Encoding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test manifest is written with utf8 encoding

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
assert posix(filename) in u_contents
```

### Step 2: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
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
filename = os.path.join('sdist_test', 'smörbröd.py')
```

### Step 7: Call touch()

```python
touch(filename)
```

### Step 8: Assign contents = read_all_bytes(...)

```python
contents = read_all_bytes(mm.manifest)
```

### Step 9: Assign u_contents = contents.decode(...)

```python
u_contents = contents.decode('UTF-8')
```

**Verification:**
```python
assert posix(filename) in u_contents
```

### Step 10: Call mm.run()

```python
mm.run()
```

### Step 11: Call mm.filelist.append()

```python
mm.filelist.append(filename)
```

### Step 12: Call mm.write_manifest()

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
filename = os.path.join('sdist_test', 'smörbröd.py')
touch(filename)
with quiet():
    mm.run()
    mm.filelist.append(filename)
    mm.write_manifest()
contents = read_all_bytes(mm.manifest)
u_contents = contents.decode('UTF-8')
assert posix(filename) in u_contents
```

## Next Steps


---

*Source: test_sdist.py:464 | Complexity: Advanced | Last updated: 2026-06-02*