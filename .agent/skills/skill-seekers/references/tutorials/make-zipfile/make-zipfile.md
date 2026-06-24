# How To: Make Zipfile

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test make zipfile

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

### Step 1: Assign zipfile = pytest.importorskip(...)

```python
zipfile = pytest.importorskip('zipfile')
```

**Verification:**
```python
assert os.path.exists(tarball)
```

### Step 2: Assign tmpdir = self._create_files(...)

```python
tmpdir = self._create_files()
```

**Verification:**
```python
assert sorted(zf.namelist()) == self._zip_created_files
```

### Step 3: Assign base_name = os.path.join(...)

```python
base_name = os.path.join(self.mkdtemp(), 'archive')
```

### Step 4: Assign tarball = value

```python
tarball = base_name + '.zip'
```

**Verification:**
```python
assert os.path.exists(tarball)
```

### Step 5: Call make_zipfile()

```python
make_zipfile(base_name, 'dist')
```

**Verification:**
```python
assert sorted(zf.namelist()) == self._zip_created_files
```


## Complete Example

```python
# Workflow
zipfile = pytest.importorskip('zipfile')
tmpdir = self._create_files()
base_name = os.path.join(self.mkdtemp(), 'archive')
with path.Path(tmpdir):
    make_zipfile(base_name, 'dist')
tarball = base_name + '.zip'
assert os.path.exists(tarball)
with zipfile.ZipFile(tarball) as zf:
    assert sorted(zf.namelist()) == self._zip_created_files
```

## Next Steps


---

*Source: test_archive_util.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*