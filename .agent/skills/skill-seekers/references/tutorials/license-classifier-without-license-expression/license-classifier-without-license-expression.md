# How To: License Classifier Without License Expression

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test license classifier without license expression

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

### Step 1: Assign text = '    [project]\n    name = "spam"\n    version = "2020.0.0"\n    license = {text = "mit or apache-2.0"}\n    classifiers = ["License :: OSI Approved :: MIT License"]\n    '

```python
text = '    [project]\n    name = "spam"\n    version = "2020.0.0"\n    license = {text = "mit or apache-2.0"}\n    classifiers = ["License :: OSI Approved :: MIT License"]\n    '
```

**Verification:**
```python
assert dist.metadata.get_classifiers() == ['License :: OSI Approved :: MIT License']
```

### Step 2: Assign pyproject = _pep621_example_project(...)

```python
pyproject = _pep621_example_project(tmp_path, 'README', text)
```

### Step 3: Assign msg1 = 'License classifiers are deprecated(?:.|\n)*MIT License'

```python
msg1 = 'License classifiers are deprecated(?:.|\n)*MIT License'
```

### Step 4: Assign msg2 = '.project.license. as a TOML table is deprecated'

```python
msg2 = '.project.license. as a TOML table is deprecated'
```

**Verification:**
```python
assert dist.metadata.get_classifiers() == ['License :: OSI Approved :: MIT License']
```

### Step 5: Assign dist = pyprojecttoml.apply_configuration(...)

```python
dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
text = '    [project]\n    name = "spam"\n    version = "2020.0.0"\n    license = {text = "mit or apache-2.0"}\n    classifiers = ["License :: OSI Approved :: MIT License"]\n    '
pyproject = _pep621_example_project(tmp_path, 'README', text)
msg1 = 'License classifiers are deprecated(?:.|\n)*MIT License'
msg2 = '.project.license. as a TOML table is deprecated'
with pytest.warns(SetuptoolsDeprecationWarning, match=msg1), pytest.warns(SetuptoolsDeprecationWarning, match=msg2):
    dist = pyprojecttoml.apply_configuration(makedist(tmp_path), pyproject)
assert dist.metadata.get_classifiers() == ['License :: OSI Approved :: MIT License']
```

## Next Steps


---

*Source: test_apply_pyprojecttoml.py:364 | Complexity: Intermediate | Last updated: 2026-06-02*