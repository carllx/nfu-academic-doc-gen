# How To: Warning Overwritten Dependencies

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test warning overwritten dependencies

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

### Step 1: Assign src = "[project]\nname='pkg'\nversion='0.1'\ndependencies=['click']\n"

```python
src = "[project]\nname='pkg'\nversion='0.1'\ndependencies=['click']\n"
```

**Verification:**
```python
assert 'wheel' not in dist.install_requires
```

### Step 2: Assign pyproject = value

```python
pyproject = tmp_path / 'pyproject.toml'
```

### Step 3: Call pyproject.write_text()

```python
pyproject.write_text(src, encoding='utf-8')
```

### Step 4: Assign dist = makedist(...)

```python
dist = makedist(tmp_path, install_requires=['wheel'])
```

**Verification:**
```python
assert 'wheel' not in dist.install_requires
```

### Step 5: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(dist, pyproject)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
src = "[project]\nname='pkg'\nversion='0.1'\ndependencies=['click']\n"
pyproject = tmp_path / 'pyproject.toml'
pyproject.write_text(src, encoding='utf-8')
dist = makedist(tmp_path, install_requires=['wheel'])
with pytest.warns(match='`install_requires` overwritten'):
    dist = pyprojecttoml.apply_configuration(dist, pyproject)
assert 'wheel' not in dist.install_requires
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:649 | Complexity: Intermediate | Last updated: 2026-06-02*