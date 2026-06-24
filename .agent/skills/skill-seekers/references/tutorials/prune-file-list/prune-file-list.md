# How To: Prune File List

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test prune file list

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

### Step 1: Call os.mkdir()

```python
os.mkdir(join(self.tmp_dir, 'somecode', '.svn'))
```

**Verification:**
```python
assert files == ['ns_fake_pkg-1.0.zip']
```

### Step 2: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', '.svn', 'ok.py'), 'xxx')
```

**Verification:**
```python
assert sorted(content) == ['ns_fake_pkg-1.0/' + x for x in expected]
```

### Step 3: Call os.mkdir()

```python
os.mkdir(join(self.tmp_dir, 'somecode', '.hg'))
```

### Step 4: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', '.hg', 'ok'), 'xxx')
```

### Step 5: Call os.mkdir()

```python
os.mkdir(join(self.tmp_dir, 'somecode', '.git'))
```

### Step 6: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', '.git', 'ok'), 'xxx')
```

### Step 7: Call self.write_file()

```python
self.write_file((self.tmp_dir, 'somecode', '.nfs0001'), 'xxx')
```

### Step 8: Assign unknown = self.get_cmd(...)

```python
dist, cmd = self.get_cmd()
```

### Step 9: Assign cmd.formats = value

```python
cmd.formats = ['zip']
```

### Step 10: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 11: Call cmd.run()

```python
cmd.run()
```

### Step 12: Assign dist_folder = join(...)

```python
dist_folder = join(self.tmp_dir, 'dist')
```

### Step 13: Assign files = os.listdir(...)

```python
files = os.listdir(dist_folder)
```

**Verification:**
```python
assert files == ['ns_fake_pkg-1.0.zip']
```

### Step 14: Assign zip_file = zipfile.ZipFile(...)

```python
zip_file = zipfile.ZipFile(join(dist_folder, 'ns_fake_pkg-1.0.zip'))
```

### Step 15: Assign expected = value

```python
expected = ['', 'PKG-INFO', 'README', 'setup.py', 'somecode/', 'somecode/__init__.py']
```

**Verification:**
```python
assert sorted(content) == ['ns_fake_pkg-1.0/' + x for x in expected]
```

### Step 16: Assign content = zip_file.namelist(...)

```python
content = zip_file.namelist()
```

### Step 17: Call zip_file.close()

```python
zip_file.close()
```


## Complete Example

```python
# Workflow
os.mkdir(join(self.tmp_dir, 'somecode', '.svn'))
self.write_file((self.tmp_dir, 'somecode', '.svn', 'ok.py'), 'xxx')
os.mkdir(join(self.tmp_dir, 'somecode', '.hg'))
self.write_file((self.tmp_dir, 'somecode', '.hg', 'ok'), 'xxx')
os.mkdir(join(self.tmp_dir, 'somecode', '.git'))
self.write_file((self.tmp_dir, 'somecode', '.git', 'ok'), 'xxx')
self.write_file((self.tmp_dir, 'somecode', '.nfs0001'), 'xxx')
dist, cmd = self.get_cmd()
cmd.formats = ['zip']
cmd.ensure_finalized()
cmd.run()
dist_folder = join(self.tmp_dir, 'dist')
files = os.listdir(dist_folder)
assert files == ['ns_fake_pkg-1.0.zip']
zip_file = zipfile.ZipFile(join(dist_folder, 'ns_fake_pkg-1.0.zip'))
try:
    content = zip_file.namelist()
finally:
    zip_file.close()
expected = ['', 'PKG-INFO', 'README', 'setup.py', 'somecode/', 'somecode/__init__.py']
assert sorted(content) == ['ns_fake_pkg-1.0/' + x for x in expected]
```

## Next Steps


---

*Source: test_sdist.py:90 | Complexity: Advanced | Last updated: 2026-06-02*