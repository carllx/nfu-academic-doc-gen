# How To: Get File List

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get file list

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
assert ilen(clean_lines(cmd.manifest)) == 5
```

### Step 2: Assign dist.package_data = value

```python
dist.package_data = {'somecode': ['*.txt']}
```

**Verification:**
```python
assert len(manifest2) == 6
```

### Step 3: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', 'doc.txt'), '#')
```

**Verification:**
```python
assert 'doc2.txt' in manifest2[-1]
```

### Step 4: Assign cmd.formats = value

```python
cmd.formats = ['gztar']
```

### Step 5: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 6: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert ilen(clean_lines(cmd.manifest)) == 5
```

### Step 7: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', 'doc2.txt'), '#')
```

### Step 8: Assign build_py = dist.get_command_obj(...)

```python
build_py = dist.get_command_obj('build_py')
```

### Step 9: Assign build_py.finalized = False

```python
build_py.finalized = False
```

### Step 10: Call build_py.ensure_finalized()

```python
build_py.ensure_finalized()
```

### Step 11: Call cmd.run()

```python
cmd.run()
```

### Step 12: Assign manifest2 = list(...)

```python
manifest2 = list(clean_lines(cmd.manifest))
```

**Verification:**
```python
assert len(manifest2) == 6
```


## Complete Example

```python
# Workflow
dist, cmd = self.get_cmd()
dist.package_data = {'somecode': ['*.txt']}
self.write_file((self.tmp_dir, 'somecode', 'doc.txt'), '#')
cmd.formats = ['gztar']
cmd.ensure_finalized()
cmd.run()
assert ilen(clean_lines(cmd.manifest)) == 5
self.write_file((self.tmp_dir, 'somecode', 'doc2.txt'), '#')
build_py = dist.get_command_obj('build_py')
build_py.finalized = False
build_py.ensure_finalized()
cmd.run()
manifest2 = list(clean_lines(cmd.manifest))
assert len(manifest2) == 6
assert 'doc2.txt' in manifest2[-1]
```

## Next Steps


---

*Source: test_sdist.py:337 | Complexity: Advanced | Last updated: 2026-06-02*