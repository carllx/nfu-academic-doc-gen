# How To: Find Packages

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test find packages

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
# Fixtures: tmp_path, args, pkgs
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'pkg/__init__.py', 'other/__init__.py', 'dir1/dir2/__init__.py'}
```

**Verification:**
```python
assert set(expand.find_packages(**kwargs)) == pkgs
```

### Step 2: Call write_files()

```python
write_files({k: '' for k in files}, tmp_path)
```

**Verification:**
```python
assert os.path.exists(pkg_path)
```

### Step 3: Assign package_dir = value

```python
package_dir = {}
```

**Verification:**
```python
assert set(expand.find_packages(where=where, **args)) == pkgs
```

### Step 4: Assign kwargs = value

```python
kwargs = {'root_dir': tmp_path, 'fill_package_dir': package_dir, **args}
```

### Step 5: Assign where = kwargs.get(...)

```python
where = kwargs.get('where', ['.'])
```

**Verification:**
```python
assert set(expand.find_packages(**kwargs)) == pkgs
```

### Step 6: Assign where = value

```python
where = [str((tmp_path / p).resolve()).replace(os.sep, '/') for p in args.pop('where', ['.'])]
```

**Verification:**
```python
assert set(expand.find_packages(where=where, **args)) == pkgs
```

### Step 7: Assign pkg_path = find_package_path(...)

```python
pkg_path = find_package_path(pkg, package_dir, tmp_path)
```

**Verification:**
```python
assert os.path.exists(pkg_path)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, args, pkgs

# Workflow
files = {'pkg/__init__.py', 'other/__init__.py', 'dir1/dir2/__init__.py'}
write_files({k: '' for k in files}, tmp_path)
package_dir = {}
kwargs = {'root_dir': tmp_path, 'fill_package_dir': package_dir, **args}
where = kwargs.get('where', ['.'])
assert set(expand.find_packages(**kwargs)) == pkgs
for pkg in pkgs:
    pkg_path = find_package_path(pkg, package_dir, tmp_path)
    assert os.path.exists(pkg_path)
where = [str((tmp_path / p).resolve()).replace(os.sep, '/') for p in args.pop('where', ['.'])]
assert set(expand.find_packages(where=where, **args)) == pkgs
```

## Next Steps


---

*Source: test_expand.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*