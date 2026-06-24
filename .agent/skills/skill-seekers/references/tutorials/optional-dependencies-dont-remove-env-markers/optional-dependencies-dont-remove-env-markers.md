# How To: Optional Dependencies Dont Remove Env Markers

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Internally setuptools converts dependencies with markers to "extras".
If ``install_requires`` is given by ``setup.py``, we have to ensure that
applying ``optional-dependencies`` does not overwrite the mandatory
dependencies with markers (see #3204).

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

### Step 1: '\n        Internally setuptools converts dependencies with markers to "extras".\n        If ``install_requires`` is given by ``setup.py``, we have to ensure that\n        applying ``optional-dependencies`` does not overwrite the mandatory\n        dependencies with markers (see #3204).\n        '

```python
'\n        Internally setuptools converts dependencies with markers to "extras".\n        If ``install_requires`` is given by ``setup.py``, we have to ensure that\n        applying ``optional-dependencies`` does not overwrite the mandatory\n        dependencies with markers (see #3204).\n        '
```

**Verification:**
```python
assert 'foo' in dist.extras_require
```

### Step 2: Assign extra = "\n[project.optional-dependencies]\nfoo = ['bar>1']\n"

```python
extra = "\n[project.optional-dependencies]\nfoo = ['bar>1']\n"
```

**Verification:**
```python
assert 'importlib-resources' in reqs
```

### Step 3: Assign pyproject = self.pyproject(...)

```python
pyproject = self.pyproject(tmp_path, ['dependencies'], extra)
```

**Verification:**
```python
assert 'bar' in reqs
```

### Step 4: Assign install_req = value

```python
install_req = ['importlib-resources (>=3.0.0) ; python_version < "3.7"']
```

**Verification:**
```python
assert ':python_version < "3.7"' in reqs
```

### Step 5: Assign dist = makedist(...)

```python
dist = makedist(tmp_path, install_requires=install_req)
```

### Step 6: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(dist, pyproject)
```

**Verification:**
```python
assert 'foo' in dist.extras_require
```

### Step 7: Assign egg_info = dist.get_command_obj(...)

```python
egg_info = dist.get_command_obj('egg_info')
```

### Step 8: Call write_requirements()

```python
write_requirements(egg_info, tmp_path, tmp_path / 'requires.txt')
```

### Step 9: Assign reqs = unknown.read_text(...)

```python
reqs = (tmp_path / 'requires.txt').read_text(encoding='utf-8')
```

**Verification:**
```python
assert 'importlib-resources' in reqs
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'\n        Internally setuptools converts dependencies with markers to "extras".\n        If ``install_requires`` is given by ``setup.py``, we have to ensure that\n        applying ``optional-dependencies`` does not overwrite the mandatory\n        dependencies with markers (see #3204).\n        '
extra = "\n[project.optional-dependencies]\nfoo = ['bar>1']\n"
pyproject = self.pyproject(tmp_path, ['dependencies'], extra)
install_req = ['importlib-resources (>=3.0.0) ; python_version < "3.7"']
dist = makedist(tmp_path, install_requires=install_req)
dist = pyprojecttoml.apply_configuration(dist, pyproject)
assert 'foo' in dist.extras_require
egg_info = dist.get_command_obj('egg_info')
write_requirements(egg_info, tmp_path, tmp_path / 'requires.txt')
reqs = (tmp_path / 'requires.txt').read_text(encoding='utf-8')
assert 'importlib-resources' in reqs
assert 'bar' in reqs
assert ':python_version < "3.7"' in reqs
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:658 | Complexity: Advanced | Last updated: 2026-06-02*