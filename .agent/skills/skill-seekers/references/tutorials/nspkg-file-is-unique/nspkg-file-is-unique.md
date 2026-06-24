# How To: Nspkg File Is Unique

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test nspkg file is unique

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
# Fixtures: tmp_path, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign deprecation = pytest.warns(...)

```python
deprecation = pytest.warns(SetuptoolsDeprecationWarning, match='.*namespace_packages parameter.*')
```

**Verification:**
```python
assert len(files) == len(examples)
```

### Step 2: Assign installation_dir = value

```python
installation_dir = tmp_path / '.installation_dir'
```

### Step 3: Call installation_dir.mkdir()

```python
installation_dir.mkdir()
```

### Step 4: Assign examples = value

```python
examples = ('myns.pkgA', 'myns.pkgB', 'myns.n.pkgA', 'myns.n.pkgB')
```

### Step 5: Assign files = list(...)

```python
files = list(installation_dir.glob('*-nspkg.pth'))
```

**Verification:**
```python
assert len(files) == len(examples)
```

### Step 6: Assign pkg = namespaces.build_namespace_package(...)

```python
pkg = namespaces.build_namespace_package(tmp_path, name, version='42')
```

### Step 7: Call ctx.chdir()

```python
ctx.chdir(pkg)
```

### Step 8: Assign dist = run_setup(...)

```python
dist = run_setup('setup.py', stop_after='config')
```

### Step 9: Assign cmd = editable_wheel(...)

```python
cmd = editable_wheel(dist)
```

### Step 10: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 11: Assign editable_name = value

```python
editable_name = cmd.get_finalized_command('dist_info').name
```

### Step 12: Call cmd._install_namespaces()

```python
cmd._install_namespaces(installation_dir, editable_name)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, monkeypatch

# Workflow
deprecation = pytest.warns(SetuptoolsDeprecationWarning, match='.*namespace_packages parameter.*')
installation_dir = tmp_path / '.installation_dir'
installation_dir.mkdir()
examples = ('myns.pkgA', 'myns.pkgB', 'myns.n.pkgA', 'myns.n.pkgB')
for name in examples:
    pkg = namespaces.build_namespace_package(tmp_path, name, version='42')
    with deprecation, monkeypatch.context() as ctx:
        ctx.chdir(pkg)
        dist = run_setup('setup.py', stop_after='config')
        cmd = editable_wheel(dist)
        cmd.finalize_options()
        editable_name = cmd.get_finalized_command('dist_info').name
        cmd._install_namespaces(installation_dir, editable_name)
files = list(installation_dir.glob('*-nspkg.pth'))
assert len(files) == len(examples)
```

## Next Steps


---

*Source: test_editable_install.py:237 | Complexity: Advanced | Last updated: 2026-06-02*