# How To: Mixed Extras Require Optional Dependencies

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed extras require optional dependencies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `pytest`
- `jaraco`
- `setuptools.config.pyprojecttoml`
- `setuptools.dist`
- `setuptools.warnings`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            optional-dependencies.docs = ["sphinx"]\n            ')}
```

**Verification:**
```python
assert dist.extras_require == {'docs': ['sphinx']}
```

### Step 2: Call path.build()

```python
path.build(files, prefix=tmp_path)
```

### Step 3: Assign pyproject = value

```python
pyproject = tmp_path / 'pyproject.toml'
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution({'extras_require': {'hello': ['world']}})
```

**Verification:**
```python
assert dist.extras_require == {'docs': ['sphinx']}
```

### Step 5: Assign dist = apply_configuration(...)

```python
dist = apply_configuration(dist, pyproject)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
files = {'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            optional-dependencies.docs = ["sphinx"]\n            ')}
path.build(files, prefix=tmp_path)
pyproject = tmp_path / 'pyproject.toml'
dist = Distribution({'extras_require': {'hello': ['world']}})
with pytest.warns(SetuptoolsWarning, match='.extras_require. overwritten'):
    dist = apply_configuration(dist, pyproject)
assert dist.extras_require == {'docs': ['sphinx']}
```

## Next Steps


---

*Source: test_pyprojecttoml_dynamic_deps.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*