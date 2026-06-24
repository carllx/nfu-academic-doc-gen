# How To: Tarfile Root Owner

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tarfile root owner

## Prerequisites

**Required Modules:**
- `functools`
- `operator`
- `os`
- `pathlib`
- `sys`
- `tarfile`
- `distutils`
- `distutils.archive_util`
- `distutils.spawn`
- `distutils.tests`
- `os.path`
- `path`
- `pytest`
- `test.support`
- `unix_compat`


## Step-by-Step Guide

### Step 1: Assign tmpdir = self._create_files(...)

```python
tmpdir = self._create_files()
```

**Verification:**
```python
assert os.path.exists(archive_name)
```

### Step 2: Assign base_name = os.path.join(...)

```python
base_name = os.path.join(self.mkdtemp(), 'archive')
```

**Verification:**
```python
assert member.uid == 0
```

### Step 3: Assign old_dir = os.getcwd(...)

```python
old_dir = os.getcwd()
```

**Verification:**
```python
assert member.gid == 0
```

### Step 4: Call os.chdir()

```python
os.chdir(tmpdir)
```

### Step 5: Assign group = value

```python
group = grp.getgrgid(0)[0]
```

### Step 6: Assign owner = value

```python
owner = pwd.getpwuid(0)[0]
```

**Verification:**
```python
assert os.path.exists(archive_name)
```

### Step 7: Assign archive = tarfile.open(...)

```python
archive = tarfile.open(archive_name)
```

### Step 8: Assign archive_name = make_tarball(...)

```python
archive_name = make_tarball(base_name, 'dist', compress=None, owner=owner, group=group)
```

### Step 9: Call os.chdir()

```python
os.chdir(old_dir)
```

### Step 10: Call archive.close()

```python
archive.close()
```

**Verification:**
```python
assert member.uid == 0
```


## Complete Example

```python
# Workflow
tmpdir = self._create_files()
base_name = os.path.join(self.mkdtemp(), 'archive')
old_dir = os.getcwd()
os.chdir(tmpdir)
group = grp.getgrgid(0)[0]
owner = pwd.getpwuid(0)[0]
try:
    archive_name = make_tarball(base_name, 'dist', compress=None, owner=owner, group=group)
finally:
    os.chdir(old_dir)
assert os.path.exists(archive_name)
archive = tarfile.open(archive_name)
try:
    for member in archive.getmembers():
        assert member.uid == 0
        assert member.gid == 0
finally:
    archive.close()
```

## Next Steps


---

*Source: test_archive_util.py:318 | Complexity: Advanced | Last updated: 2026-06-02*