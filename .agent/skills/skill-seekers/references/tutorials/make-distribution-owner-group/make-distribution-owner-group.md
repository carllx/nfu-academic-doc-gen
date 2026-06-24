# How To: Make Distribution Owner Group

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test make distribution owner group

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `shutil`
- `tarfile`
- `zipfile`
- `distutils.archive_util`
- `distutils.command.sdist`
- `distutils.core`
- `distutils.errors`
- `distutils.filelist`
- `os.path`
- `textwrap`
- `jaraco.path`
- `path`
- `pytest`
- `more_itertools`
- `unix_compat`


## Step-by-Step Guide

### Step 1: Assign unknown = self.get_cmd(...)

```python
dist, cmd = self.get_cmd()
```

**Verification:**
```python
assert member.uid == 0
```

### Step 2: Assign cmd.formats = value

```python
cmd.formats = ['gztar']
```

**Verification:**
```python
assert member.gid == 0
```

### Step 3: Assign cmd.owner = value

```python
cmd.owner = pwd.getpwuid(0)[0]
```

**Verification:**
```python
assert member.uid == os.getuid()
```

### Step 4: Assign cmd.group = value

```python
cmd.group = grp.getgrgid(0)[0]
```

### Step 5: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 6: Call cmd.run()

```python
cmd.run()
```

### Step 7: Assign archive_name = join(...)

```python
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
```

### Step 8: Assign archive = tarfile.open(...)

```python
archive = tarfile.open(archive_name)
```

### Step 9: Assign unknown = self.get_cmd(...)

```python
dist, cmd = self.get_cmd()
```

### Step 10: Assign cmd.formats = value

```python
cmd.formats = ['gztar']
```

### Step 11: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 12: Call cmd.run()

```python
cmd.run()
```

### Step 13: Assign archive_name = join(...)

```python
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
```

### Step 14: Assign archive = tarfile.open(...)

```python
archive = tarfile.open(archive_name)
```

### Step 15: Call archive.close()

```python
archive.close()
```

### Step 16: Call archive.close()

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
dist, cmd = self.get_cmd()
cmd.formats = ['gztar']
cmd.owner = pwd.getpwuid(0)[0]
cmd.group = grp.getgrgid(0)[0]
cmd.ensure_finalized()
cmd.run()
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
archive = tarfile.open(archive_name)
try:
    for member in archive.getmembers():
        assert member.uid == 0
        assert member.gid == 0
finally:
    archive.close()
dist, cmd = self.get_cmd()
cmd.formats = ['gztar']
cmd.ensure_finalized()
cmd.run()
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
archive = tarfile.open(archive_name)
try:
    for member in archive.getmembers():
        assert member.uid == os.getuid()
finally:
    archive.close()
```

## Next Steps


---

*Source: test_sdist.py:430 | Complexity: Advanced | Last updated: 2026-06-02*