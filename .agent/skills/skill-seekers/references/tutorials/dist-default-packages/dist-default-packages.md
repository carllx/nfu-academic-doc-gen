# How To: Dist Default Packages

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dist default packages

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `re`
- `urllib.parse`
- `urllib.request`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `fixtures`
- `test_find_packages`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmp_path, dist_name, package_dir, package_files, packages
```

## Step-by-Step Guide

### Step 1: Call ensure_files()

```python
ensure_files(tmp_path, package_files)
```

**Verification:**
```python
assert not dist.py_modules
```

### Step 2: Call unknown.touch()

```python
(tmp_path / 'setup.py').touch()
```

**Verification:**
```python
assert not dist.py_modules
```

### Step 3: Call unknown.touch()

```python
(tmp_path / 'noxfile.py').touch()
```

**Verification:**
```python
assert set(dist.packages) == set(packages)
```

### Step 4: Assign attrs = value

```python
attrs = {**EXAMPLE_BASE_INFO, 'name': dist_name, 'src_root': str(tmp_path), 'package_dir': package_dir}
```

**Verification:**
```python
assert not dist.packages
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

**Verification:**
```python
assert set(dist.py_modules) == {'explicit_py_module'}
```

### Step 6: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert not dist.py_modules
```

### Step 7: Assign dist = Distribution(...)

```python
dist = Distribution({**attrs, 'py_modules': ['explicit_py_module']})
```

**Verification:**
```python
assert set(dist.packages) == {'explicit_package'}
```

### Step 8: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert not dist.packages
```

### Step 9: Assign dist = Distribution(...)

```python
dist = Distribution({**attrs, 'packages': ['explicit_package']})
```

### Step 10: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert not dist.py_modules
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, dist_name, package_dir, package_files, packages

# Workflow
ensure_files(tmp_path, package_files)
(tmp_path / 'setup.py').touch()
(tmp_path / 'noxfile.py').touch()
attrs = {**EXAMPLE_BASE_INFO, 'name': dist_name, 'src_root': str(tmp_path), 'package_dir': package_dir}
dist = Distribution(attrs)
dist.set_defaults()
assert not dist.py_modules
assert not dist.py_modules
assert set(dist.packages) == set(packages)
dist = Distribution({**attrs, 'py_modules': ['explicit_py_module']})
dist.set_defaults()
assert not dist.packages
assert set(dist.py_modules) == {'explicit_py_module'}
dist = Distribution({**attrs, 'packages': ['explicit_package']})
dist.set_defaults()
assert not dist.py_modules
assert set(dist.packages) == {'explicit_package'}
```

## Next Steps


---

*Source: test_dist.py:216 | Complexity: Advanced | Last updated: 2026-06-02*