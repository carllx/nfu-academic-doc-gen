# How To: Editable With Prefix

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Editable install to a prefix should be discoverable.

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
# Fixtures: tmp_path, sample_project, editable_opts
```

## Step-by-Step Guide

### Step 1: '\n    Editable install to a prefix should be discoverable.\n    '

```python
'\n    Editable install to a prefix should be discoverable.\n    '
```

### Step 2: Assign prefix = value

```python
prefix = tmp_path / 'prefix'
```

### Step 3: Assign site_packages_all = value

```python
site_packages_all = [prefix / Path(path).relative_to(sys.prefix) for path in sys.path if 'site-packages' in path and path.startswith(sys.prefix)]
```

### Step 4: Call _addsitedirs()

```python
_addsitedirs(site_packages_all)
```

### Step 5: Assign env = dict(...)

```python
env = dict(os.environ, PYTHONPATH=os.pathsep.join(map(str, site_packages_all)))
```

### Step 6: Assign cmd = value

```python
cmd = [sys.executable, '-m', 'pip', 'install', '--editable', str(sample_project), '--prefix', str(prefix), '--no-build-isolation', *editable_opts]
```

### Step 7: Call subprocess.check_call()

```python
subprocess.check_call(cmd, env=env)
```

### Step 8: Assign bin = value

```python
bin = 'Scripts' if platform.system() == 'Windows' else 'bin'
```

### Step 9: Assign exe = value

```python
exe = prefix / bin / 'sample'
```

### Step 10: Call subprocess.check_call()

```python
subprocess.check_call([exe], env=env)
```

### Step 11: Call sp.mkdir()

```python
sp.mkdir(parents=True)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, sample_project, editable_opts

# Workflow
'\n    Editable install to a prefix should be discoverable.\n    '
prefix = tmp_path / 'prefix'
site_packages_all = [prefix / Path(path).relative_to(sys.prefix) for path in sys.path if 'site-packages' in path and path.startswith(sys.prefix)]
for sp in site_packages_all:
    sp.mkdir(parents=True)
_addsitedirs(site_packages_all)
env = dict(os.environ, PYTHONPATH=os.pathsep.join(map(str, site_packages_all)))
cmd = [sys.executable, '-m', 'pip', 'install', '--editable', str(sample_project), '--prefix', str(prefix), '--no-build-isolation', *editable_opts]
subprocess.check_call(cmd, env=env)
bin = 'Scripts' if platform.system() == 'Windows' else 'bin'
exe = prefix / bin / 'sample'
subprocess.check_call([exe], env=env)
```

## Next Steps


---

*Source: test_editable_install.py:401 | Complexity: Advanced | Last updated: 2026-06-02*