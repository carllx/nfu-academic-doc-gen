# How To: Manual Manifest

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test manual manifest

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
assert cmd.filelist.files == ['README.manual']
```

### Step 2: Assign cmd.formats = value

```python
cmd.formats = ['gztar']
```

**Verification:**
```python
assert list(clean_lines(cmd.manifest)) == ['README.manual']
```

### Step 3: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

**Verification:**
```python
assert sorted(filenames) == ['ns_fake_pkg-1.0', 'ns_fake_pkg-1.0/PKG-INFO', 'ns_fake_pkg-1.0/README.manual']
```

### Step 4: Call self.write_file()

```python
self.write_file((self.tmp_dir, cmd.manifest), 'README.manual')
```

### Step 5: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'README.manual'), 'This project maintains its MANIFEST file itself.')
```

### Step 6: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert cmd.filelist.files == ['README.manual']
```

### Step 7: Assign archive_name = join(...)

```python
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
```

### Step 8: Assign archive = tarfile.open(...)

```python
archive = tarfile.open(archive_name)
```

**Verification:**
```python
assert sorted(filenames) == ['ns_fake_pkg-1.0', 'ns_fake_pkg-1.0/PKG-INFO', 'ns_fake_pkg-1.0/README.manual']
```

### Step 9: Assign filenames = value

```python
filenames = [tarinfo.name for tarinfo in archive]
```

### Step 10: Call archive.close()

```python
archive.close()
```


## Complete Example

```python
# Workflow
dist, cmd = self.get_cmd()
cmd.formats = ['gztar']
cmd.ensure_finalized()
self.write_file((self.tmp_dir, cmd.manifest), 'README.manual')
self.write_file((self.tmp_dir, 'README.manual'), 'This project maintains its MANIFEST file itself.')
cmd.run()
assert cmd.filelist.files == ['README.manual']
assert list(clean_lines(cmd.manifest)) == ['README.manual']
archive_name = join(self.tmp_dir, 'dist', 'ns_fake_pkg-1.0.tar.gz')
archive = tarfile.open(archive_name)
try:
    filenames = [tarinfo.name for tarinfo in archive]
finally:
    archive.close()
assert sorted(filenames) == ['ns_fake_pkg-1.0', 'ns_fake_pkg-1.0/PKG-INFO', 'ns_fake_pkg-1.0/README.manual']
```

## Next Steps


---

*Source: test_sdist.py:398 | Complexity: Advanced | Last updated: 2026-06-02*