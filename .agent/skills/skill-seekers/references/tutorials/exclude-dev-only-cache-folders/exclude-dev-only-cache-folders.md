# How To: Exclude Dev Only Cache Folders

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test exclude dev only cache folders

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: source_dir
```

## Step-by-Step Guide

### Step 1: Assign included = value

```python
included = {'MANIFEST.in': 'global-include LICEN[CS]E* COPYING* NOTICE* AUTHORS*\nglobal-include *.txt\n', 'test/.venv/lib/python3.9/site-packages/bar-2.dist-info/AUTHORS.rst': '', 'src/.nox/py/lib/python3.12/site-packages/bar-2.dist-info/COPYING.txt': '', 'doc/.tox/default/lib/python3.11/site-packages/foo-4.dist-info/LICENSE': '', '.venv-requirements.txt': '', '.tox-coveragerc.txt': '', '.noxy/coveragerc.txt': ''}
```

**Verification:**
```python
assert os.path.exists(path)
```

### Step 2: Assign excluded = value

```python
excluded = {'.tox/release/lib/python3.11/site-packages/foo-4.dist-info/LICENSE': '', '.nox/py/lib/python3.12/site-packages/bar-2.dist-info/COPYING.txt': '', '.venv/lib/python3.9/site-packages/bar-2.dist-info/AUTHORS.rst': ''}
```

**Verification:**
```python
assert path not in manifest, (path, manifest)
```

### Step 3: Assign cmd = self.setup_with_extension(...)

```python
cmd = self.setup_with_extension()
```

**Verification:**
```python
assert os.path.exists(path)
```

### Step 4: Call self.assert_package_data_in_manifest()

```python
self.assert_package_data_in_manifest(cmd)
```

**Verification:**
```python
assert path in manifest, (path, manifest)
```

### Step 5: Assign manifest = value

```python
manifest = {f.replace(os.sep, '/') for f in cmd.filelist.files}
```

### Step 6: Call Path.parent.mkdir()

```python
Path(source_dir, file).parent.mkdir(parents=True, exist_ok=True)
```

### Step 7: Call Path.write_text()

```python
Path(source_dir, file).write_text(content, encoding='utf-8')
```

**Verification:**
```python
assert os.path.exists(path)
```


## Complete Example

```python
# Setup
# Fixtures: source_dir

# Workflow
included = {'MANIFEST.in': 'global-include LICEN[CS]E* COPYING* NOTICE* AUTHORS*\nglobal-include *.txt\n', 'test/.venv/lib/python3.9/site-packages/bar-2.dist-info/AUTHORS.rst': '', 'src/.nox/py/lib/python3.12/site-packages/bar-2.dist-info/COPYING.txt': '', 'doc/.tox/default/lib/python3.11/site-packages/foo-4.dist-info/LICENSE': '', '.venv-requirements.txt': '', '.tox-coveragerc.txt': '', '.noxy/coveragerc.txt': ''}
excluded = {'.tox/release/lib/python3.11/site-packages/foo-4.dist-info/LICENSE': '', '.nox/py/lib/python3.12/site-packages/bar-2.dist-info/COPYING.txt': '', '.venv/lib/python3.9/site-packages/bar-2.dist-info/AUTHORS.rst': ''}
for file, content in {**excluded, **included}.items():
    Path(source_dir, file).parent.mkdir(parents=True, exist_ok=True)
    Path(source_dir, file).write_text(content, encoding='utf-8')
cmd = self.setup_with_extension()
self.assert_package_data_in_manifest(cmd)
manifest = {f.replace(os.sep, '/') for f in cmd.filelist.files}
for path in excluded:
    assert os.path.exists(path)
    assert path not in manifest, (path, manifest)
for path in included:
    assert os.path.exists(path)
    assert path in manifest, (path, manifest)
```

## Next Steps


---

*Source: test_sdist.py:423 | Complexity: Intermediate | Last updated: 2026-06-02*