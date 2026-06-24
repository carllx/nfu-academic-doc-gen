# How To: Purposefully Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test purposefully empty

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
# Fixtures: tmp_path, config_file, param, circumstance
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = self.FILES[circumstance] + ['mod.py', 'other.py', 'src/pkg/__init__.py']
```

**Verification:**
```python
assert getattr(dist, param) == []
```

### Step 2: Call _populate_project_dir()

```python
_populate_project_dir(tmp_path, files, {})
```

**Verification:**
```python
assert getattr(dist, other) is None
```

### Step 3: Assign config = unknown.format(...)

```python
config = self.PURPOSEFULLY_EMPY[config_file].format(param=template_param)
```

### Step 4: Call unknown.write_text()

```python
(tmp_path / config_file).write_text(config, encoding='utf-8')
```

### Step 5: Assign dist = _get_dist(...)

```python
dist = _get_dist(tmp_path, {})
```

**Verification:**
```python
assert getattr(dist, param) == []
```

### Step 6: Assign other = value

```python
other = {'py_modules': 'packages', 'packages': 'py_modules'}[param]
```

**Verification:**
```python
assert getattr(dist, other) is None
```

### Step 7: Assign template_param = param.replace(...)

```python
template_param = param.replace('_', '-')
```

### Step 8: Assign pyproject = value

```python
pyproject = self.PURPOSEFULLY_EMPY['template-pyproject.toml']
```

### Step 9: Call unknown.write_text()

```python
(tmp_path / 'pyproject.toml').write_text(pyproject, encoding='utf-8')
```

### Step 10: Assign template_param = param

```python
template_param = param
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, config_file, param, circumstance

# Workflow
files = self.FILES[circumstance] + ['mod.py', 'other.py', 'src/pkg/__init__.py']
_populate_project_dir(tmp_path, files, {})
if config_file == 'pyproject.toml':
    template_param = param.replace('_', '-')
else:
    pyproject = self.PURPOSEFULLY_EMPY['template-pyproject.toml']
    (tmp_path / 'pyproject.toml').write_text(pyproject, encoding='utf-8')
    template_param = param
config = self.PURPOSEFULLY_EMPY[config_file].format(param=template_param)
(tmp_path / config_file).write_text(config, encoding='utf-8')
dist = _get_dist(tmp_path, {})
assert getattr(dist, param) == []
other = {'py_modules': 'packages', 'packages': 'py_modules'}[param]
assert getattr(dist, other) is None
```

## Next Steps


---

*Source: test_config_discovery.py:171 | Complexity: Advanced | Last updated: 2026-06-02*