# How To: Editable With Flat Layout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test editable with flat layout

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
# Fixtures: tmp_path, venv, editable_opts
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'mypkg': {'pyproject.toml': dedent('                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "mypkg"\n                version = "3.14159"\n\n                [tool.setuptools]\n                packages = ["pkg"]\n                py-modules = ["mod"]\n                '), 'pkg': {'__init__.py': 'a = 4'}, 'mod.py': 'b = 2'}}
```

**Verification:**
```python
assert venv.run(cmd).strip() == '4 2'
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build(files, prefix=tmp_path)
```

### Step 3: Assign project = value

```python
project = tmp_path / 'mypkg'
```

### Step 4: Assign cmd = value

```python
cmd = ['python', '-m', 'pip', 'install', '--no-build-isolation', '-e', str(project), *editable_opts]
```

### Step 5: Call print()

```python
print(venv.run(cmd))
```

### Step 6: Assign cmd = value

```python
cmd = ['python', '-c', 'import pkg, mod; print(pkg.a, mod.b)']
```

**Verification:**
```python
assert venv.run(cmd).strip() == '4 2'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, venv, editable_opts

# Workflow
files = {'mypkg': {'pyproject.toml': dedent('                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "mypkg"\n                version = "3.14159"\n\n                [tool.setuptools]\n                packages = ["pkg"]\n                py-modules = ["mod"]\n                '), 'pkg': {'__init__.py': 'a = 4'}, 'mod.py': 'b = 2'}}
jaraco.path.build(files, prefix=tmp_path)
project = tmp_path / 'mypkg'
cmd = ['python', '-m', 'pip', 'install', '--no-build-isolation', '-e', str(project), *editable_opts]
print(venv.run(cmd))
cmd = ['python', '-c', 'import pkg, mod; print(pkg.a, mod.b)']
assert venv.run(cmd).strip() == '4 2'
```

## Next Steps


---

*Source: test_editable_install.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*