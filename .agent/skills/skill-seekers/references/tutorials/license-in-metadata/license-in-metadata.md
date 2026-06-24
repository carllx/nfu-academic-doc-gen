# How To: License In Metadata

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test license in metadata

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
# Fixtures: license, license_expression, content_str, not_content_str, pyproject_text, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign pyproject = _pep621_example_project(...)

```python
pyproject = _pep621_example_project(tmp_path, 'README', pyproject_text=pyproject_text)
```

**Verification:**
```python
assert dist.metadata.license == license
```

### Step 2: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
```

**Verification:**
```python
assert dist.metadata.license_expression == license_expression
```

### Step 3: Assign pkg_file = value

```python
pkg_file = tmp_path / 'PKG-FILE'
```

**Verification:**
```python
assert 'Metadata-Version: 2.4' in content
```

### Step 4: Assign content = pkg_file.read_text(...)

```python
content = pkg_file.read_text(encoding='utf-8')
```

**Verification:**
```python
assert content_str in content
```

### Step 5: Call dist.metadata.write_pkg_file()

```python
dist.metadata.write_pkg_file(fh)
```

**Verification:**
```python
assert not_content_str not in content
```


## Complete Example

```python
# Setup
# Fixtures: license, license_expression, content_str, not_content_str, pyproject_text, tmp_path

# Workflow
pyproject = _pep621_example_project(tmp_path, 'README', pyproject_text=pyproject_text)
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
assert dist.metadata.license == license
assert dist.metadata.license_expression == license_expression
pkg_file = tmp_path / 'PKG-FILE'
with open(pkg_file, 'w', encoding='utf-8') as fh:
    dist.metadata.write_pkg_file(fh)
content = pkg_file.read_text(encoding='utf-8')
assert 'Metadata-Version: 2.4' in content
assert content_str in content
assert not_content_str not in content
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:325 | Complexity: Intermediate | Last updated: 2026-06-02*