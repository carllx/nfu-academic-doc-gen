# How To: Namespace Created Via Package Dir

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Currently users can create a namespace by tweaking `package_dir`

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `platform`
- `stat`
- `subprocess`
- `sys`
- `copy`
- `importlib`
- `importlib.machinery`
- `pathlib`
- `textwrap`
- `typing`
- `unittest.mock`
- `uuid`
- `jaraco.envs`
- `jaraco.path`
- `pytest`
- `path`
- `setuptools._importlib`
- `setuptools.command.editable_wheel`
- `setuptools.dist`
- `setuptools.extension`
- `setuptools.warnings`
- `distutils.core`
- `distutils.command.build_ext`

**Setup Required:**
```python
# Fixtures: venv, tmp_path, editable_opts
```

## Step-by-Step Guide

### Step 1: 'Currently users can create a namespace by tweaking `package_dir`'

```python
'Currently users can create a namespace by tweaking `package_dir`'
```

### Step 2: Assign files = value

```python
files = {'pkgA': {'pyproject.toml': dedent('                    [build-system]\n                    requires = ["setuptools", "wheel"]\n                    build-backend = "setuptools.build_meta"\n\n                    [project]\n                    name = "pkgA"\n                    version = "3.14159"\n\n                    [tool.setuptools]\n                    package-dir = {"myns.n.pkgA" = "src"}\n                    '), 'src': {'__init__.py': 'a = 1'}}}
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build(files, prefix=tmp_path)
```

### Step 4: Assign pkg_A = value

```python
pkg_A = tmp_path / 'pkgA'
```

### Step 5: Assign pkg_B = namespaces.build_pep420_namespace_package(...)

```python
pkg_B = namespaces.build_pep420_namespace_package(tmp_path, 'myns.n.pkgB')
```

### Step 6: Assign pkg_C = namespaces.build_pep420_namespace_package(...)

```python
pkg_C = namespaces.build_pep420_namespace_package(tmp_path, 'myns.n.pkgC')
```

### Step 7: Assign opts = value

```python
opts = editable_opts[:]
```

### Step 8: Call opts.append()

```python
opts.append('--no-build-isolation')
```

### Step 9: Call venv.run()

```python
venv.run(['python', '-m', 'pip', 'install', str(pkg_A), *opts])
```

### Step 10: Call venv.run()

```python
venv.run(['python', '-m', 'pip', 'install', '-e', str(pkg_B), *opts])
```

### Step 11: Call venv.run()

```python
venv.run(['python', '-m', 'pip', 'install', '-e', str(pkg_C), *opts])
```

### Step 12: Call venv.run()

```python
venv.run(['python', '-c', 'from myns.n import pkgA, pkgB, pkgC'])
```


## Complete Example

```python
# Setup
# Fixtures: venv, tmp_path, editable_opts

# Workflow
'Currently users can create a namespace by tweaking `package_dir`'
files = {'pkgA': {'pyproject.toml': dedent('                    [build-system]\n                    requires = ["setuptools", "wheel"]\n                    build-backend = "setuptools.build_meta"\n\n                    [project]\n                    name = "pkgA"\n                    version = "3.14159"\n\n                    [tool.setuptools]\n                    package-dir = {"myns.n.pkgA" = "src"}\n                    '), 'src': {'__init__.py': 'a = 1'}}}
jaraco.path.build(files, prefix=tmp_path)
pkg_A = tmp_path / 'pkgA'
pkg_B = namespaces.build_pep420_namespace_package(tmp_path, 'myns.n.pkgB')
pkg_C = namespaces.build_pep420_namespace_package(tmp_path, 'myns.n.pkgC')
opts = editable_opts[:]
opts.append('--no-build-isolation')
venv.run(['python', '-m', 'pip', 'install', str(pkg_A), *opts])
venv.run(['python', '-m', 'pip', 'install', '-e', str(pkg_B), *opts])
venv.run(['python', '-m', 'pip', 'install', '-e', str(pkg_C), *opts])
venv.run(['python', '-c', 'from myns.n import pkgA, pkgB, pkgC'])
```

## Next Steps


---

*Source: test_editable_install.py:316 | Complexity: Advanced | Last updated: 2026-06-02*