# How To: Listed In Dynamic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test listed in dynamic

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
# Fixtures: tmp_path, attr, field, value
```

## Step-by-Step Guide

### Step 1: Assign pyproject = self.pyproject(...)

```python
pyproject = self.pyproject(tmp_path, [field])
```

**Verification:**
```python
assert dist_value == value
```

### Step 2: Assign dist = makedist(...)

```python
dist = makedist(tmp_path, **{attr: value})
```

### Step 3: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(dist, pyproject)
```

### Step 4: Assign dist_value = _some_attrgetter(...)

```python
dist_value = _some_attrgetter(f'metadata.{attr}', attr)(dist)
```

**Verification:**
```python
assert dist_value == value
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, attr, field, value

# Workflow
pyproject = self.pyproject(tmp_path, [field])
dist = makedist(tmp_path, **{attr: value})
dist = pyprojecttoml.apply_configuration(dist, pyproject)
dist_value = _some_attrgetter(f'metadata.{attr}', attr)(dist)
assert dist_value == value
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:622 | Complexity: Intermediate | Last updated: 2026-06-02*