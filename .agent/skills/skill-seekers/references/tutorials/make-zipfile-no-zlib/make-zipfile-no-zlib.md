# How To: Make Zipfile No Zlib

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test make zipfile no zlib

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
assert called == [((tarball, 'w'), {'compression': zipfile.ZIP_STORED})]
```

### Step 2: Call patch()

```python
patch(self, archive_util.zipfile, 'zlib', None)
```

**Verification:**
```python
assert os.path.exists(tarball)
```

### Step 3: Assign called = value

```python
called = []
```

**Verification:**
```python
assert sorted(zf.namelist()) == self._zip_created_files
```

### Step 4: Assign zipfile_class = value

```python
zipfile_class = zipfile.ZipFile
```

### Step 5: Call patch()

```python
patch(self, archive_util.zipfile, 'ZipFile', fake_zipfile)
```

### Step 6: Assign tmpdir = self._create_files(...)

```python
tmpdir = self._create_files()
```

### Step 7: Assign base_name = os.path.join(...)

```python
base_name = os.path.join(self.mkdtemp(), 'archive')
```

### Step 8: Assign tarball = value

```python
tarball = base_name + '.zip'
```

**Verification:**
```python
assert called == [((tarball, 'w'), {'compression': zipfile.ZIP_STORED})]
```

### Step 9: Call make_zipfile()

```python
make_zipfile(base_name, 'dist')
```

**Verification:**
```python
assert sorted(zf.namelist()) == self._zip_created_files
```

### Step 10: Call called.append()

```python
called.append((a, kw))
```


## Complete Example

```python
# Workflow
zipfile = pytest.importorskip('zipfile')
patch(self, archive_util.zipfile, 'zlib', None)
called = []
zipfile_class = zipfile.ZipFile

def fake_zipfile(*a, **kw):
    if kw.get('compression', None) == zipfile.ZIP_STORED:
        called.append((a, kw))
    return zipfile_class(*a, **kw)
patch(self, archive_util.zipfile, 'ZipFile', fake_zipfile)
tmpdir = self._create_files()
base_name = os.path.join(self.mkdtemp(), 'archive')
with path.Path(tmpdir):
    make_zipfile(base_name, 'dist')
tarball = base_name + '.zip'
assert called == [((tarball, 'w'), {'compression': zipfile.ZIP_STORED})]
assert os.path.exists(tarball)
with zipfile.ZipFile(tarball) as zf:
    assert sorted(zf.namelist()) == self._zip_created_files
```

## Next Steps


---

*Source: test_archive_util.py:195 | Complexity: Advanced | Last updated: 2026-06-02*