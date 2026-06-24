# How To: Build With Existing File Present

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test build with existing file present

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `os`
- `re`
- `shutil`
- `signal`
- `sys`
- `tarfile`
- `warnings`
- `concurrent`
- `pathlib`
- `typing`
- `zipfile`
- `pytest`
- `jaraco`
- `packaging.requirements`
- `setuptools.warnings`
- `textwrap`

**Setup Required:**
```python
# Fixtures: build_type, tmpdir_cwd
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'setup.py': 'from setuptools import setup\nsetup()', 'VERSION': '0.0.1', 'setup.cfg': DALS('\n                [metadata]\n                name = foo\n                version = file: VERSION\n                '), 'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n                ')}
```

**Verification:**
```python
assert os.path.isfile(os.path.join(dist_dir, first_result))
```

### Step 2: Call path.build()

```python
path.build(files)
```

**Verification:**
```python
assert first_result != second_result
```

### Step 3: Assign dist_dir = os.path.abspath(...)

```python
dist_dir = os.path.abspath('preexisting-' + build_type)
```

**Verification:**
```python
assert third_result == second_result
```

### Step 4: Assign build_backend = self.get_build_backend(...)

```python
build_backend = self.get_build_backend()
```

**Verification:**
```python
assert os.path.getsize(os.path.join(dist_dir, third_result)) > 0
```

### Step 5: Assign build_method = getattr(...)

```python
build_method = getattr(build_backend, 'build_' + build_type)
```

### Step 6: Assign first_result = build_method(...)

```python
first_result = build_method(dist_dir)
```

### Step 7: Assign second_result = build_method(...)

```python
second_result = build_method(dist_dir)
```

**Verification:**
```python
assert os.path.isfile(os.path.join(dist_dir, first_result))
```

### Step 8: Call open.close()

```python
open(os.path.join(dist_dir, second_result), 'wb').close()
```

### Step 9: Assign third_result = build_method(...)

```python
third_result = build_method(dist_dir)
```

**Verification:**
```python
assert third_result == second_result
```

### Step 10: Call version_file.write()

```python
version_file.write('0.0.2')
```


## Complete Example

```python
# Setup
# Fixtures: build_type, tmpdir_cwd

# Workflow
files = {'setup.py': 'from setuptools import setup\nsetup()', 'VERSION': '0.0.1', 'setup.cfg': DALS('\n                [metadata]\n                name = foo\n                version = file: VERSION\n                '), 'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n                ')}
path.build(files)
dist_dir = os.path.abspath('preexisting-' + build_type)
build_backend = self.get_build_backend()
build_method = getattr(build_backend, 'build_' + build_type)
first_result = build_method(dist_dir)
with open('VERSION', 'wt', encoding='utf-8') as version_file:
    version_file.write('0.0.2')
second_result = build_method(dist_dir)
assert os.path.isfile(os.path.join(dist_dir, first_result))
assert first_result != second_result
open(os.path.join(dist_dir, second_result), 'wb').close()
third_result = build_method(dist_dir)
assert third_result == second_result
assert os.path.getsize(os.path.join(dist_dir, third_result)) > 0
```

## Next Steps


---

*Source: test_build_meta.py:269 | Complexity: Advanced | Last updated: 2026-06-02*