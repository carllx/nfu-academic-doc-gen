# How To: Both License And License Files Defined

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test both license and license files defined

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

### Step 1: Assign setuptools_config = '[tool.setuptools]\nlicense-files = ["_FILE*"]'

```python
setuptools_config = '[tool.setuptools]\nlicense-files = ["_FILE*"]'
```

**Verification:**
```python
assert set(dist.metadata.license_files) == {'_FILE.rst', '_FILE.txt'}
```

### Step 2: Assign pyproject = self.base_pyproject(...)

```python
pyproject = self.base_pyproject(tmp_path, setuptools_config)
```

**Verification:**
```python
assert dist.metadata.license == 'LicenseRef-Proprietary\n'
```

### Step 3: Call unknown.touch()

```python
(tmp_path / '_FILE.txt').touch()
```

### Step 4: Call unknown.touch()

```python
(tmp_path / '_FILE.rst').touch()
```

### Step 5: Assign license = value

```python
license = tmp_path / 'LICENSE.txt'
```

### Step 6: Call license.write_text()

```python
license.write_text('LicenseRef-Proprietary\n', encoding='utf-8')
```

### Step 7: Assign msg1 = "'tool.setuptools.license-files' is deprecated in favor of 'project.license-files'"

```python
msg1 = "'tool.setuptools.license-files' is deprecated in favor of 'project.license-files'"
```

### Step 8: Assign msg2 = '.project.license. as a TOML table is deprecated'

```python
msg2 = '.project.license. as a TOML table is deprecated'
```

**Verification:**
```python
assert set(dist.metadata.license_files) == {'_FILE.rst', '_FILE.txt'}
```

### Step 9: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
setuptools_config = '[tool.setuptools]\nlicense-files = ["_FILE*"]'
pyproject = self.base_pyproject(tmp_path, setuptools_config)
(tmp_path / '_FILE.txt').touch()
(tmp_path / '_FILE.rst').touch()
license = tmp_path / 'LICENSE.txt'
license.write_text('LicenseRef-Proprietary\n', encoding='utf-8')
msg1 = "'tool.setuptools.license-files' is deprecated in favor of 'project.license-files'"
msg2 = '.project.license. as a TOML table is deprecated'
with pytest.warns(SetuptoolsDeprecationWarning, match=msg1), pytest.warns(SetuptoolsDeprecationWarning, match=msg2):
    dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
assert set(dist.metadata.license_files) == {'_FILE.rst', '_FILE.txt'}
assert dist.metadata.license == 'LicenseRef-Proprietary\n'
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:419 | Complexity: Advanced | Last updated: 2026-06-02*