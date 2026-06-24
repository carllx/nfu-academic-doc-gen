# How To: Setupcfg Metadata

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test setupcfg metadata

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `configparser`
- `itertools`
- `typing`
- `jaraco.path`
- `pytest`
- `path`
- `setuptools`
- `setuptools.command.sdist`
- `setuptools.discovery`
- `setuptools.dist`
- `setuptools.errors`
- `contexts`
- `integration.helpers`
- `textwrap`
- `distutils.core`
- `setuptools`

**Setup Required:**
```python
# Fixtures: tmp_path, folder, opts
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = [f'{folder}/pkg/__init__.py', 'setup.cfg']
```

**Verification:**
```python
assert dist.get_name() == 'pkg'
```

### Step 2: Call _populate_project_dir()

```python
_populate_project_dir(tmp_path, files, opts)
```

**Verification:**
```python
assert dist.get_version() == '42'
```

### Step 3: Assign config = unknown.read_text(...)

```python
config = (tmp_path / 'setup.cfg').read_text(encoding='utf-8')
```

**Verification:**
```python
assert dist.package_dir
```

### Step 4: Assign overwrite = value

```python
overwrite = {folder: {'pkg': {'__init__.py': 'version = 42'}}, 'setup.cfg': '[metadata]\nversion = attr: pkg.version\n' + config}
```

**Verification:**
```python
assert os.path.exists(package_path)
```

### Step 5: Call jaraco.path.build()

```python
jaraco.path.build(overwrite, prefix=tmp_path)
```

**Verification:**
```python
assert folder in Path(package_path).parts()
```

### Step 6: Assign dist = _get_dist(...)

```python
dist = _get_dist(tmp_path, {})
```

**Verification:**
```python
assert dist_file.is_file()
```

### Step 7: Assign package_path = find_package_path(...)

```python
package_path = find_package_path('pkg', dist.package_dir, tmp_path)
```

**Verification:**
```python
assert os.path.exists(package_path)
```

### Step 8: Call _run_build()

```python
_run_build(tmp_path, '--sdist')
```

### Step 9: Assign dist_file = value

```python
dist_file = tmp_path / 'dist/pkg-42.tar.gz'
```

**Verification:**
```python
assert dist_file.is_file()
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, folder, opts

# Workflow
files = [f'{folder}/pkg/__init__.py', 'setup.cfg']
_populate_project_dir(tmp_path, files, opts)
config = (tmp_path / 'setup.cfg').read_text(encoding='utf-8')
overwrite = {folder: {'pkg': {'__init__.py': 'version = 42'}}, 'setup.cfg': '[metadata]\nversion = attr: pkg.version\n' + config}
jaraco.path.build(overwrite, prefix=tmp_path)
dist = _get_dist(tmp_path, {})
assert dist.get_name() == 'pkg'
assert dist.get_version() == '42'
assert dist.package_dir
package_path = find_package_path('pkg', dist.package_dir, tmp_path)
assert os.path.exists(package_path)
assert folder in Path(package_path).parts()
_run_build(tmp_path, '--sdist')
dist_file = tmp_path / 'dist/pkg-42.tar.gz'
assert dist_file.is_file()
```

## Next Steps


---

*Source: test_config_discovery.py:293 | Complexity: Advanced | Last updated: 2026-06-02*