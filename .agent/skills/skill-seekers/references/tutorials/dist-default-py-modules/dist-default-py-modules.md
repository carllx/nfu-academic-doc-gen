# How To: Dist Default Py Modules

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dist default py modules

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `re`
- `urllib.parse`
- `urllib.request`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `fixtures`
- `test_find_packages`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmp_path, dist_name, py_module
```

## Step-by-Step Guide

### Step 1: Call unknown.touch()

```python
(tmp_path / f'{py_module}.py').touch()
```

**Verification:**
```python
assert dist.py_modules == [py_module]
```

### Step 2: Call unknown.touch()

```python
(tmp_path / 'setup.py').touch()
```

**Verification:**
```python
assert dist.py_modules == ['explicity_py_module']
```

### Step 3: Call unknown.touch()

```python
(tmp_path / 'noxfile.py').touch()
```

**Verification:**
```python
assert not dist.py_modules
```

### Step 4: Assign attrs = value

```python
attrs = {**EXAMPLE_BASE_INFO, 'name': dist_name, 'src_root': str(tmp_path)}
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 6: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert dist.py_modules == [py_module]
```

### Step 7: Assign dist = Distribution(...)

```python
dist = Distribution({**attrs, 'py_modules': ['explicity_py_module']})
```

### Step 8: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert dist.py_modules == ['explicity_py_module']
```

### Step 9: Assign dist = Distribution(...)

```python
dist = Distribution({**attrs, 'packages': ['explicity_package']})
```

### Step 10: Call dist.set_defaults()

```python
dist.set_defaults()
```

**Verification:**
```python
assert not dist.py_modules
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, dist_name, py_module

# Workflow
(tmp_path / f'{py_module}.py').touch()
(tmp_path / 'setup.py').touch()
(tmp_path / 'noxfile.py').touch()
attrs = {**EXAMPLE_BASE_INFO, 'name': dist_name, 'src_root': str(tmp_path)}
dist = Distribution(attrs)
dist.set_defaults()
assert dist.py_modules == [py_module]
dist = Distribution({**attrs, 'py_modules': ['explicity_py_module']})
dist.set_defaults()
assert dist.py_modules == ['explicity_py_module']
dist = Distribution({**attrs, 'packages': ['explicity_package']})
dist.set_defaults()
assert not dist.py_modules
```

## Next Steps


---

*Source: test_dist.py:173 | Complexity: Advanced | Last updated: 2026-06-02*