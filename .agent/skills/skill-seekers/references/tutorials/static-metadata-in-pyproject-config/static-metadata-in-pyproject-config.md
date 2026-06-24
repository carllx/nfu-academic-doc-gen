# How To: Static Metadata In Pyproject Config

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test static metadata in pyproject config

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `os`
- `re`
- `shutil`
- `signal`
- `sys`
- `tarfile`
- `warnings`
- `concurrent`
- `pathlib`
- `typing`
- `zipfile`
- `pytest`
- `jaraco`
- `packaging.requirements`
- `setuptools.warnings`
- `textwrap`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "foo"\n                description = "This is a Python package"\n                version = "42"\n                dependencies = ["six"]\n                '), 'hello.py': DALS("\n                def run():\n                    print('hello')\n                "), 'setup.py': DALS("\n                __import__('setuptools').setup(\n                    name='bar',\n                    version='13',\n                )\n                ")}
```

**Verification:**
```python
assert (tmpdir / 'temp/foo-42.tar.gz').exists()
```

### Step 2: Assign build_backend = self.get_build_backend(...)

```python
build_backend = self.get_build_backend()
```

**Verification:**
```python
assert (tmpdir / 'temp/foo-42-py3-none-any.whl').exists()
```

### Step 3: Call path.build()

```python
path.build(files)
```

**Verification:**
```python
assert not (tmpdir / 'temp/bar-13.tar.gz').exists()
```

### Step 4: Assign sdist_path = build_backend.build_sdist(...)

```python
sdist_path = build_backend.build_sdist('temp')
```

**Verification:**
```python
assert not (tmpdir / 'temp/bar-42.tar.gz').exists()
```

### Step 5: Assign wheel_file = build_backend.build_wheel(...)

```python
wheel_file = build_backend.build_wheel('temp')
```

**Verification:**
```python
assert not (tmpdir / 'temp/foo-13.tar.gz').exists()
```

### Step 6: Assign pkg_info = str(...)

```python
pkg_info = str(tar.extractfile('foo-42/PKG-INFO').read(), 'utf-8')
```

**Verification:**
```python
assert not (tmpdir / 'temp/bar-13-py3-none-any.whl').exists()
```

### Step 7: Assign members = tar.getnames(...)

```python
members = tar.getnames()
```

**Verification:**
```python
assert not (tmpdir / 'temp/bar-42-py3-none-any.whl').exists()
```

### Step 8: Assign metadata = str(...)

```python
metadata = str(zipfile.read('foo-42.dist-info/METADATA'), 'utf-8')
```

**Verification:**
```python
assert not (tmpdir / 'temp/foo-13-py3-none-any.whl').exists()
```

### Step 9: Assign members = zipfile.namelist(...)

```python
members = zipfile.namelist()
```

**Verification:**
```python
assert 'bar-13/PKG-INFO' not in members
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
files = {'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "foo"\n                description = "This is a Python package"\n                version = "42"\n                dependencies = ["six"]\n                '), 'hello.py': DALS("\n                def run():\n                    print('hello')\n                "), 'setup.py': DALS("\n                __import__('setuptools').setup(\n                    name='bar',\n                    version='13',\n                )\n                ")}
build_backend = self.get_build_backend()
with tmpdir.as_cwd():
    path.build(files)
    sdist_path = build_backend.build_sdist('temp')
    wheel_file = build_backend.build_wheel('temp')
assert (tmpdir / 'temp/foo-42.tar.gz').exists()
assert (tmpdir / 'temp/foo-42-py3-none-any.whl').exists()
assert not (tmpdir / 'temp/bar-13.tar.gz').exists()
assert not (tmpdir / 'temp/bar-42.tar.gz').exists()
assert not (tmpdir / 'temp/foo-13.tar.gz').exists()
assert not (tmpdir / 'temp/bar-13-py3-none-any.whl').exists()
assert not (tmpdir / 'temp/bar-42-py3-none-any.whl').exists()
assert not (tmpdir / 'temp/foo-13-py3-none-any.whl').exists()
with tarfile.open(os.path.join(tmpdir, 'temp', sdist_path)) as tar:
    pkg_info = str(tar.extractfile('foo-42/PKG-INFO').read(), 'utf-8')
    members = tar.getnames()
    assert 'bar-13/PKG-INFO' not in members
with ZipFile(os.path.join(tmpdir, 'temp', wheel_file)) as zipfile:
    metadata = str(zipfile.read('foo-42.dist-info/METADATA'), 'utf-8')
    members = zipfile.namelist()
    assert 'bar-13.dist-info/METADATA' not in members
for file in (pkg_info, metadata):
    for line in ('Name: foo', 'Version: 42'):
        assert line in file
    for line in ('Name: bar', 'Version: 13'):
        assert line not in file
```

## Next Steps


---

*Source: test_build_meta.py:465 | Complexity: Advanced | Last updated: 2026-06-02*