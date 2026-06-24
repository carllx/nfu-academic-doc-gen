# How To: Default Patterns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default patterns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `re`
- `tarfile`
- `inspect`
- `pathlib`
- `unittest.mock`
- `pytest`
- `ini2toml.api`
- `packaging.metadata`
- `setuptools`
- `setuptools._static`
- `setuptools.command.egg_info`
- `setuptools.config`
- `setuptools.config._apply_pyprojecttoml`
- `setuptools.dist`
- `setuptools.errors`
- `setuptools.warnings`
- `downloads`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign setuptools_config = '[tool.setuptools]\nzip-safe = false'

```python
setuptools_config = '[tool.setuptools]\nzip-safe = false'
```

**Verification:**
```python
assert (tmp_path / 'LICENSE.txt').exists()
```

### Step 2: Assign pyproject = self.base_pyproject(...)

```python
pyproject = self.base_pyproject(tmp_path, setuptools_config, license_toml='')
```

**Verification:**
```python
assert set(dist.metadata.license_files) == {*license_files, 'LICENSE.txt'}
```

### Step 3: Assign license_files = unknown.split(...)

```python
license_files = 'LICENCE-a.html COPYING-abc.txt AUTHORS-xyz NOTICE,def'.split()
```

### Step 4: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
```

**Verification:**
```python
assert (tmp_path / 'LICENSE.txt').exists()
```

### Step 5: Call unknown.write_text()

```python
(tmp_path / fname).write_text(f'{fname}\n', encoding='utf-8')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
setuptools_config = '[tool.setuptools]\nzip-safe = false'
pyproject = self.base_pyproject(tmp_path, setuptools_config, license_toml='')
license_files = 'LICENCE-a.html COPYING-abc.txt AUTHORS-xyz NOTICE,def'.split()
for fname in license_files:
    (tmp_path / fname).write_text(f'{fname}\n', encoding='utf-8')
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
assert (tmp_path / 'LICENSE.txt').exists()
assert set(dist.metadata.license_files) == {*license_files, 'LICENSE.txt'}
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:465 | Complexity: Intermediate | Last updated: 2026-06-02*