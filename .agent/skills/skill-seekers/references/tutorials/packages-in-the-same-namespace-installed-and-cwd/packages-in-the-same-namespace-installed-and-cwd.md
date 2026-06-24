# How To: Packages In The Same Namespace Installed And Cwd

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Installing one namespace package and also have another in the same
namespace in the current working directory, both of them must be
importable.

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

### Step 1: '\n        Installing one namespace package and also have another in the same\n        namespace in the current working directory, both of them must be\n        importable.\n        '

```python
'\n        Installing one namespace package and also have another in the same\n        namespace in the current working directory, both of them must be\n        importable.\n        '
```

### Step 2: Assign pkg_A = namespaces.build_namespace_package(...)

```python
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
```

### Step 3: Assign pkg_B = namespaces.build_namespace_package(...)

```python
pkg_B = namespaces.build_namespace_package(tmpdir, 'myns.pkgB')
```

### Step 4: Assign target = value

```python
target = tmpdir / 'packages'
```

### Step 5: Assign install_cmd = value

```python
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(target)]
```

### Step 6: Call subprocess.check_call()

```python
subprocess.check_call(install_cmd)
```

### Step 7: Call namespaces.make_site_dir()

```python
namespaces.make_site_dir(target)
```

### Step 8: Assign pkg_resources_imp = value

```python
pkg_resources_imp = [sys.executable, '-c', 'import pkg_resources; import myns.pkgA; import myns.pkgB']
```

### Step 9: Call subprocess.check_call()

```python
subprocess.check_call(pkg_resources_imp, cwd=str(pkg_B))
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'\n        Installing one namespace package and also have another in the same\n        namespace in the current working directory, both of them must be\n        importable.\n        '
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
pkg_B = namespaces.build_namespace_package(tmpdir, 'myns.pkgB')
target = tmpdir / 'packages'
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(target)]
subprocess.check_call(install_cmd)
namespaces.make_site_dir(target)
pkg_resources_imp = [sys.executable, '-c', 'import pkg_resources; import myns.pkgA; import myns.pkgB']
with paths_on_pythonpath([str(target)]):
    subprocess.check_call(pkg_resources_imp, cwd=str(pkg_B))
```

## Next Steps


---

*Source: test_namespaces.py:109 | Complexity: Advanced | Last updated: 2026-06-02*