# How To: Utf8 Maintainer In Metadata

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test utf8 maintainer in metadata

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
# Fixtures: expected_maintainers_meta_value, pyproject_text, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign pyproject = _pep621_example_project(...)

```python
pyproject = _pep621_example_project(tmp_path, 'README', pyproject_text=pyproject_text)
```

**Verification:**
```python
assert dist.metadata.maintainer_email == expected_maintainers_meta_value
```

### Step 2: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
```

**Verification:**
```python
assert f'Maintainer-email: {expected_maintainers_meta_value}' in content
```

### Step 3: Assign pkg_file = value

```python
pkg_file = tmp_path / 'PKG-FILE'
```

### Step 4: Assign content = pkg_file.read_text(...)

```python
content = pkg_file.read_text(encoding='utf-8')
```

**Verification:**
```python
assert f'Maintainer-email: {expected_maintainers_meta_value}' in content
```

### Step 5: Call dist.metadata.write_pkg_file()

```python
dist.metadata.write_pkg_file(fh)
```


## Complete Example

```python
# Setup
# Fixtures: expected_maintainers_meta_value, pyproject_text, tmp_path

# Workflow
pyproject = _pep621_example_project(tmp_path, 'README', pyproject_text=pyproject_text)
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
assert dist.metadata.maintainer_email == expected_maintainers_meta_value
pkg_file = tmp_path / 'PKG-FILE'
with open(pkg_file, 'w', encoding='utf-8') as fh:
    dist.metadata.write_pkg_file(fh)
content = pkg_file.read_text(encoding='utf-8')
assert f'Maintainer-email: {expected_maintainers_meta_value}' in content
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*