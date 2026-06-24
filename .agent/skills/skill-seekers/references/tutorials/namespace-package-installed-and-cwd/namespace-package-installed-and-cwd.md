# How To: Namespace Package Installed And Cwd

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Installing a namespace packages but also having it in the current
working directory, only one version should take precedence.

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

### Step 1: '\n        Installing a namespace packages but also having it in the current\n        working directory, only one version should take precedence.\n        '

```python
'\n        Installing a namespace packages but also having it in the current\n        working directory, only one version should take precedence.\n        '
```

### Step 2: Assign pkg_A = namespaces.build_namespace_package(...)

```python
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
```

### Step 3: Assign target = value

```python
target = tmpdir / 'packages'
```

### Step 4: Assign install_cmd = value

```python
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(target)]
```

### Step 5: Call subprocess.check_call()

```python
subprocess.check_call(install_cmd)
```

### Step 6: Call namespaces.make_site_dir()

```python
namespaces.make_site_dir(target)
```

### Step 7: Assign pkg_resources_imp = value

```python
pkg_resources_imp = [sys.executable, '-c', 'import pkg_resources; import myns.pkgA']
```

### Step 8: Call subprocess.check_call()

```python
subprocess.check_call(pkg_resources_imp, cwd=str(pkg_A))
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'\n        Installing a namespace packages but also having it in the current\n        working directory, only one version should take precedence.\n        '
pkg_A = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
target = tmpdir / 'packages'
install_cmd = [sys.executable, '-m', 'pip.__main__', 'install', str(pkg_A), '-t', str(target)]
subprocess.check_call(install_cmd)
namespaces.make_site_dir(target)
pkg_resources_imp = [sys.executable, '-c', 'import pkg_resources; import myns.pkgA']
with paths_on_pythonpath([str(target)]):
    subprocess.check_call(pkg_resources_imp, cwd=str(pkg_A))
```

## Next Steps


---

*Source: test_namespaces.py:80 | Complexity: Advanced | Last updated: 2026-06-02*