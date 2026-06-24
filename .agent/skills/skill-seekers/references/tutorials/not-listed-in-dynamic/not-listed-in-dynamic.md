# How To: Not Listed In Dynamic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Setuptools cannot set a field if not listed in ``dynamic``

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

### Step 1: 'Setuptools cannot set a field if not listed in ``dynamic``'

```python
'Setuptools cannot set a field if not listed in ``dynamic``'
```

**Verification:**
```python
assert not dist_value
```

### Step 2: Assign pyproject = self.pyproject(...)

```python
pyproject = self.pyproject(tmp_path, [])
```

### Step 3: Assign dist = makedist(...)

```python
dist = makedist(tmp_path, **{attr: value})
```

### Step 4: Assign msg = re.compile(...)

```python
msg = re.compile(f'defined outside of `pyproject.toml`:.*{field}', re.DOTALL)
```

### Step 5: Assign dist_value = _some_attrgetter(...)

```python
dist_value = _some_attrgetter(f'metadata.{attr}', attr)(dist)
```

**Verification:**
```python
assert not dist_value
```

### Step 6: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(dist, pyproject)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, attr, field, value

# Workflow
'Setuptools cannot set a field if not listed in ``dynamic``'
pyproject = self.pyproject(tmp_path, [])
dist = makedist(tmp_path, **{attr: value})
msg = re.compile(f'defined outside of `pyproject.toml`:.*{field}', re.DOTALL)
with pytest.warns(_MissingDynamic, match=msg):
    dist = pyprojecttoml.apply_configuration(dist, pyproject)
dist_value = _some_attrgetter(f'metadata.{attr}', attr)(dist)
assert not dist_value
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:601 | Complexity: Intermediate | Last updated: 2026-06-02*