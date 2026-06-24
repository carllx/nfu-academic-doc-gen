# How To: Pkg Resources Import

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Ensure that a namespace package doesn't break on import
of pkg_resources.

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

### Step 1: "\n        Ensure that a namespace package doesn't break on import\n        of pkg_resources.\n        "

```python
"\n        Ensure that a namespace package doesn't break on import\n        of pkg_resources.\n        "
```

### Step 2: Assign pkg = namespaces.build_namespace_package(...)

```python
pkg = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
```

### Step 3: Assign target = value

```python
target = tmpdir / 'packages'
```

### Step 4: Call target.mkdir()

```python
target.mkdir()
```

### Step 5: Assign install_cmd = value

```python
install_cmd = [sys.executable, '-m', 'pip', 'install', '-t', str(target), str(pkg)]
```

### Step 6: Call namespaces.make_site_dir()

```python
namespaces.make_site_dir(target)
```

### Step 7: Assign try_import = value

```python
try_import = [sys.executable, '-c', 'import pkg_resources']
```

### Step 8: Call subprocess.check_call()

```python
subprocess.check_call(install_cmd)
```

### Step 9: Call subprocess.check_call()

```python
subprocess.check_call(try_import)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
"\n        Ensure that a namespace package doesn't break on import\n        of pkg_resources.\n        "
pkg = namespaces.build_namespace_package(tmpdir, 'myns.pkgA')
target = tmpdir / 'packages'
target.mkdir()
install_cmd = [sys.executable, '-m', 'pip', 'install', '-t', str(target), str(pkg)]
with paths_on_pythonpath([str(target)]):
    subprocess.check_call(install_cmd)
namespaces.make_site_dir(target)
try_import = [sys.executable, '-c', 'import pkg_resources']
with paths_on_pythonpath([str(target)]):
    subprocess.check_call(try_import)
```

## Next Steps


---

*Source: test_namespaces.py:52 | Complexity: Advanced | Last updated: 2026-06-02*