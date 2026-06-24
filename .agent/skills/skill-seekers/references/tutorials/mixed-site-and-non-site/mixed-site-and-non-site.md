# How To: Mixed Site And Non Site

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Installing two packages sharing the same namespace, one installed
to a site dir and the other installed just to a path on PYTHONPATH
should leave the namespace in tact and both packages reachable by
import.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `subprocess`
- `sys`
- `setuptools._path`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: '\n        Installing two packages sharing the same namespace, one installed\n        to a site dir and the other installed just to a path on PYTHONPATH\n        should leave the namespace in tact and both packages reachable by\n        import.\n        '

```python
'\n        Installing two packages sharing the same namespace, one installed\n        to a site dir and the other installed just to a path on PYTHONPATH\n        should leave the namespace in tact and both packages reachable by\n        import.\n        '
```

### Step 2: Assign pkg_A = namespaces.build_namespace_package(...)

```python
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
```

### Step 3: Assign pkg_B = namespaces.build_namespace_package(...)

```python
pkg_B = namespaces.build_namespace_package(tmpdir, 'myns.pkgB')
```

### Step 4: Assign site_packages = value

```python
site_packages = tmpdir / 'site-packages'
```

### Step 5: Assign path_packages = value

```python
path_packages = tmpdir / 'path-packages'
```

### Step 6: Assign targets = value

```python
targets = (site_packages, path_packages)
```

### Step 7: Assign install_cmd = value

```python
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(site_packages)]
```

### Step 8: Call subprocess.check_call()

```python
subprocess.check_call(install_cmd)
```

### Step 9: Call namespaces.make_site_dir()

```python
namespaces.make_site_dir(site_packages)
```

### Step 10: Assign install_cmd = value

```python
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_B), '-t', str(path_packages)]
```

### Step 11: Call subprocess.check_call()

```python
subprocess.check_call(install_cmd)
```

### Step 12: Assign try_import = value

```python
try_import = [sys.executable, '-c', 'import myns.pkgA; import myns.pkgB']
```

### Step 13: Call subprocess.check_call()

```python
subprocess.check_call(try_import)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'\n        Installing two packages sharing the same namespace, one installed\n        to a site dir and the other installed just to a path on PYTHONPATH\n        should leave the namespace in tact and both packages reachable by\n        import.\n        '
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
pkg_B = namespaces.build_namespace_package(tmpdir, 'myns.pkgB')
site_packages = tmpdir / 'site-packages'
path_packages = tmpdir / 'path-packages'
targets = (site_packages, path_packages)
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(site_packages)]
subprocess.check_call(install_cmd)
namespaces.make_site_dir(site_packages)
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_B), '-t', str(path_packages)]
subprocess.check_call(install_cmd)
try_import = [sys.executable, '-c', 'import myns.pkgA; import myns.pkgB']
with paths_on_pythonpath(map(str, targets)):
    subprocess.check_call(try_import)
```

## Next Steps


---

*Source: test_namespaces.py:10 | Complexity: Advanced | Last updated: 2026-06-02*