# How To: Make Distribution

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test make distribution

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
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
```

### Step 2: Assign cmd.formats = value

```python
cmd.formats = ['gztar', 'tar']
```

**Verification:**
```python
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
```

### Step 3: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 4: Call cmd.run()

```python
cmd.run()
```

### Step 5: Assign dist_folder = join(...)

```python
dist_folder = join(self.tmp_dir, 'dist')
```

### Step 6: Assign result = os.listdir(...)

```python
result = os.listdir(dist_folder)
```

### Step 7: Call result.sort()

```python
result.sort()
```

**Verification:**
```python
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
```

### Step 8: Call os.remove()

```python
os.remove(join(dist_folder, 'ns_fake_pkg-1.0.tar'))
```

### Step 9: Call os.remove()

```python
os.remove(join(dist_folder, 'ns_fake_pkg-1.0.tar.gz'))
```

### Step 10: Assign cmd.formats = value

```python
cmd.formats = ['tar', 'gztar']
```

### Step 11: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 12: Call cmd.run()

```python
cmd.run()
```

### Step 13: Assign result = os.listdir(...)

```python
result = os.listdir(dist_folder)
```

### Step 14: Call result.sort()

```python
result.sort()
```

**Verification:**
```python
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
```


## Complete Example

```python
# Workflow
dist, cmd = self.get_cmd()
cmd.formats = ['gztar', 'tar']
cmd.ensure_finalized()
cmd.run()
dist_folder = join(self.tmp_dir, 'dist')
result = os.listdir(dist_folder)
result.sort()
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
os.remove(join(dist_folder, 'ns_fake_pkg-1.0.tar'))
os.remove(join(dist_folder, 'ns_fake_pkg-1.0.tar.gz'))
cmd.formats = ['tar', 'gztar']
cmd.ensure_finalized()
cmd.run()
result = os.listdir(dist_folder)
result.sort()
assert result == ['ns_fake_pkg-1.0.tar', 'ns_fake_pkg-1.0.tar.gz']
```

## Next Steps


---

*Source: test_sdist.py:141 | Complexity: Advanced | Last updated: 2026-06-02*