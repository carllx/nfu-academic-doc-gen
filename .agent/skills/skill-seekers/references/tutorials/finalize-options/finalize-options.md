# How To: Finalize Options

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test finalize options

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
assert cmd.manifest == 'MANIFEST'
```

### Step 2: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

**Verification:**
```python
assert cmd.template == 'MANIFEST.in'
```

### Step 3: Assign cmd.formats = 1

```python
cmd.formats = 1
```

**Verification:**
```python
assert cmd.dist_dir == 'dist'
```

### Step 4: Assign cmd.formats = value

```python
cmd.formats = ['zip']
```

### Step 5: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 6: Assign cmd.formats = 'supazipa'

```python
cmd.formats = 'supazipa'
```

### Step 7: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 8: Call cmd.finalize_options()

```python
cmd.finalize_options()
```


## Complete Example

```python
# Workflow
dist, cmd = self.get_cmd()
cmd.finalize_options()
assert cmd.manifest == 'MANIFEST'
assert cmd.template == 'MANIFEST.in'
assert cmd.dist_dir == 'dist'
cmd.formats = 1
with pytest.raises(DistutilsOptionError):
    cmd.finalize_options()
cmd.formats = ['zip']
cmd.finalize_options()
cmd.formats = 'supazipa'
with pytest.raises(DistutilsOptionError):
    cmd.finalize_options()
```

## Next Steps


---

*Source: test_sdist.py:289 | Complexity: Advanced | Last updated: 2026-06-02*