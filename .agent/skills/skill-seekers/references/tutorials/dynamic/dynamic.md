# How To: Dynamic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dynamic

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

### Step 1: Call create_example()

```python
create_example(tmp_path, 'src')
```

**Verification:**
```python
assert set(expanded['project']['classifiers']) == {'Framework :: Flask', 'Programming Language :: Haskell'}
```

### Step 2: Assign classifiers = cleandoc(...)

```python
classifiers = cleandoc('\n            Framework :: Flask\n            Programming Language :: Haskell\n            ')
```

### Step 3: Call unknown.write_text()

```python
(tmp_path / 'classifiers.txt').write_text(classifiers, encoding='utf-8')
```

### Step 4: Assign pyproject = value

```python
pyproject = tmp_path / 'pyproject.toml'
```

### Step 5: Assign config = read_configuration(...)

```python
config = read_configuration(pyproject, expand=False)
```

### Step 6: Assign dynamic = value

```python
dynamic = config['project']['dynamic']
```

### Step 7: Assign unknown = list(...)

```python
config['project']['dynamic'] = list({*dynamic, 'classifiers'})
```

### Step 8: Assign dynamic_config = value

```python
dynamic_config = config['tool']['setuptools']['dynamic']
```

### Step 9: Assign unknown = value

```python
dynamic_config['classifiers'] = {'file': 'classifiers.txt'}
```

### Step 10: Call validate()

```python
validate(config, pyproject)
```

### Step 11: Assign expanded = expand_configuration(...)

```python
expanded = expand_configuration(config, tmp_path)
```

**Verification:**
```python
assert set(expanded['project']['classifiers']) == {'Framework :: Flask', 'Programming Language :: Haskell'}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
create_example(tmp_path, 'src')
classifiers = cleandoc('\n            Framework :: Flask\n            Programming Language :: Haskell\n            ')
(tmp_path / 'classifiers.txt').write_text(classifiers, encoding='utf-8')
pyproject = tmp_path / 'pyproject.toml'
config = read_configuration(pyproject, expand=False)
dynamic = config['project']['dynamic']
config['project']['dynamic'] = list({*dynamic, 'classifiers'})
dynamic_config = config['tool']['setuptools']['dynamic']
dynamic_config['classifiers'] = {'file': 'classifiers.txt'}
validate(config, pyproject)
expanded = expand_configuration(config, tmp_path)
assert set(expanded['project']['classifiers']) == {'Framework :: Flask', 'Programming Language :: Haskell'}
```

## Next Steps


---

*Source: test_pyprojecttoml.py:215 | Complexity: Advanced | Last updated: 2026-06-02*