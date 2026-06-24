# How To: Dynamic Readme From Setup Script Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dynamic readme from setup script args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `configparser`
- `inspect`
- `jaraco.path`
- `pytest`
- `tomli_w`
- `path`
- `setuptools`
- `setuptools.config.pyprojecttoml`
- `setuptools.dist`
- `setuptools.errors`
- `distutils.core`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign config = '\n        [project]\n        name = "myproj"\n        version = \'42\'\n        dynamic = ["readme"]\n        '

```python
config = '\n        [project]\n        name = "myproj"\n        version = \'42\'\n        dynamic = ["readme"]\n        '
```

**Verification:**
```python
assert dist.metadata.long_description == '42'
```

### Step 2: Assign pyproject = value

```python
pyproject = tmp_path / 'pyproject.toml'
```

### Step 3: Call pyproject.write_text()

```python
pyproject.write_text(cleandoc(config), encoding='utf-8')
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution(attrs={'long_description': '42'})
```

### Step 5: Assign dist = apply_configuration(...)

```python
dist = apply_configuration(dist, pyproject)
```

**Verification:**
```python
assert dist.metadata.long_description == '42'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
config = '\n        [project]\n        name = "myproj"\n        version = \'42\'\n        dynamic = ["readme"]\n        '
pyproject = tmp_path / 'pyproject.toml'
pyproject.write_text(cleandoc(config), encoding='utf-8')
dist = Distribution(attrs={'long_description': '42'})
dist = apply_configuration(dist, pyproject)
assert dist.metadata.long_description == '42'
```

## Next Steps


---

*Source: test_pyprojecttoml.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*