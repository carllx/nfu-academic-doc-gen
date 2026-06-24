# How To: Fill Package Dir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fill package dir

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `pathlib`
- `pytest`
- `setuptools._static`
- `setuptools.config`
- `setuptools.discovery`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmp_path, files, where, expected_package_dir
```

## Step-by-Step Guide

### Step 1: Call write_files()

```python
write_files({k: '' for k in files}, tmp_path)
```

**Verification:**
```python
assert set(pkg_dir.items()) == set(expected_package_dir.items())
```

### Step 2: Assign pkg_dir = value

```python
pkg_dir = {}
```

**Verification:**
```python
assert os.path.exists(pkg_path)
```

### Step 3: Assign kwargs = value

```python
kwargs = {'root_dir': tmp_path, 'fill_package_dir': pkg_dir, 'namespaces': False}
```

### Step 4: Assign pkgs = expand.find_packages(...)

```python
pkgs = expand.find_packages(where=where, **kwargs)
```

**Verification:**
```python
assert set(pkg_dir.items()) == set(expected_package_dir.items())
```

### Step 5: Assign pkg_path = find_package_path(...)

```python
pkg_path = find_package_path(pkg, pkg_dir, tmp_path)
```

**Verification:**
```python
assert os.path.exists(pkg_path)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, files, where, expected_package_dir

# Workflow
write_files({k: '' for k in files}, tmp_path)
pkg_dir = {}
kwargs = {'root_dir': tmp_path, 'fill_package_dir': pkg_dir, 'namespaces': False}
pkgs = expand.find_packages(where=where, **kwargs)
assert set(pkg_dir.items()) == set(expected_package_dir.items())
for pkg in pkgs:
    pkg_path = find_package_path(pkg, pkg_dir, tmp_path)
    assert os.path.exists(pkg_path)
```

## Next Steps


---

*Source: test_expand.py:239 | Complexity: Intermediate | Last updated: 2026-06-02*