# How To: Namespace Package Importable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Installing two packages sharing the same namespace, one installed
naturally using pip or `--single-version-externally-managed`
and the other installed in editable mode should leave the namespace
intact and both packages reachable by import.
(Ported from test_develop).

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
# Fixtures: venv, tmp_path, ns, impl, editable_opts
```

## Step-by-Step Guide

### Step 1: '\n        Installing two packages sharing the same namespace, one installed\n        naturally using pip or `--single-version-externally-managed`\n        and the other installed in editable mode should leave the namespace\n        intact and both packages reachable by import.\n        (Ported from test_develop).\n        '

```python
'\n        Installing two packages sharing the same namespace, one installed\n        naturally using pip or `--single-version-externally-managed`\n        and the other installed in editable mode should leave the namespace\n        intact and both packages reachable by import.\n        (Ported from test_develop).\n        '
```

### Step 2: Assign build_system = '        [build-system]\n        requires = ["setuptools"]\n        build-backend = "setuptools.build_meta"\n        '

```python
build_system = '        [build-system]\n        requires = ["setuptools"]\n        build-backend = "setuptools.build_meta"\n        '
```

### Step 3: Assign pkg_A = namespaces.build_namespace_package(...)

```python
pkg_A = namespaces.build_namespace_package(tmp_path, f'{ns}.pkgA', impl=impl)
```

### Step 4: Assign pkg_B = namespaces.build_namespace_package(...)

```python
pkg_B = namespaces.build_namespace_package(tmp_path, f'{ns}.pkgB', impl=impl)
```

### Step 5: Call unknown.write_text()

```python
(pkg_A / 'pyproject.toml').write_text(build_system, encoding='utf-8')
```

### Step 6: Call unknown.write_text()

```python
(pkg_B / 'pyproject.toml').write_text(build_system, encoding='utf-8')
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
venv.run(['python', '-c', f'import {ns}.pkgA; import {ns}.pkgB'])
```

### Step 12: Call venv.run()

```python
venv.run(['python', '-c', 'import pkg_resources'])
```


## Complete Example

```python
# Setup
# Fixtures: venv, tmp_path, ns, impl, editable_opts

# Workflow
'\n        Installing two packages sharing the same namespace, one installed\n        naturally using pip or `--single-version-externally-managed`\n        and the other installed in editable mode should leave the namespace\n        intact and both packages reachable by import.\n        (Ported from test_develop).\n        '
build_system = '        [build-system]\n        requires = ["setuptools"]\n        build-backend = "setuptools.build_meta"\n        '
pkg_A = namespaces.build_namespace_package(tmp_path, f'{ns}.pkgA', impl=impl)
pkg_B = namespaces.build_namespace_package(tmp_path, f'{ns}.pkgB', impl=impl)
(pkg_A / 'pyproject.toml').write_text(build_system, encoding='utf-8')
(pkg_B / 'pyproject.toml').write_text(build_system, encoding='utf-8')
opts = editable_opts[:]
opts.append('--no-build-isolation')
venv.run(['python', '-m', 'pip', 'install', str(pkg_A), *opts])
venv.run(['python', '-m', 'pip', 'install', '-e', str(pkg_B), *opts])
venv.run(['python', '-c', f'import {ns}.pkgA; import {ns}.pkgB'])
venv.run(['python', '-c', 'import pkg_resources'])
```

## Next Steps


---

*Source: test_editable_install.py:271 | Complexity: Advanced | Last updated: 2026-06-02*