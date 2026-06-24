# How To: Symlinked Extension Sources

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Similar to test_extension_sources_in_sdist but the referenced files are
instead symbolic links to project-local files. Referenced file paths
should be included. Symlink targets themselves should NOT be included.

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

### Step 1: '\n        Similar to test_extension_sources_in_sdist but the referenced files are\n        instead symbolic links to project-local files. Referenced file paths\n        should be included. Symlink targets themselves should NOT be included.\n        '

```python
'\n        Similar to test_extension_sources_in_sdist but the referenced files are\n        instead symbolic links to project-local files. Referenced file paths\n        should be included. Symlink targets themselves should NOT be included.\n        '
```

**Verification:**
```python
assert path in manifest
```

### Step 2: Assign symlinked = value

```python
symlinked = []
```

**Verification:**
```python
assert path not in manifest
```

### Step 3: Assign cmd = self.setup_with_extension(...)

```python
cmd = self.setup_with_extension()
```

### Step 4: Call self.assert_package_data_in_manifest()

```python
self.assert_package_data_in_manifest(cmd)
```

### Step 5: Assign manifest = value

```python
manifest = cmd.filelist.files
```

### Step 6: Assign unknown = os.path.splitext(...)

```python
base, ext = os.path.splitext(path)
```

### Step 7: Assign target = value

```python
target = base + '_target.' + ext
```

### Step 8: Call os.rename()

```python
os.rename(path, target)
```

### Step 9: Call symlink_or_skip_test()

```python
symlink_or_skip_test(os.path.basename(target), path)
```

### Step 10: Call symlinked.append()

```python
symlinked.append(target)
```

**Verification:**
```python
assert path in manifest
```


## Complete Example

```python
# Workflow
'\n        Similar to test_extension_sources_in_sdist but the referenced files are\n        instead symbolic links to project-local files. Referenced file paths\n        should be included. Symlink targets themselves should NOT be included.\n        '
symlinked = []
for path in EXTENSION_SOURCES:
    base, ext = os.path.splitext(path)
    target = base + '_target.' + ext
    os.rename(path, target)
    symlink_or_skip_test(os.path.basename(target), path)
    symlinked.append(target)
cmd = self.setup_with_extension()
self.assert_package_data_in_manifest(cmd)
manifest = cmd.filelist.files
for path in EXTENSION_SOURCES:
    assert path in manifest
for path in symlinked:
    assert path not in manifest
```

## Next Steps


---

*Source: test_sdist.py:234 | Complexity: Advanced | Last updated: 2026-06-02*