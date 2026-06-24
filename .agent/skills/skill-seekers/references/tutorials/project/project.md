# How To: Project

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test project

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
# Fixtures: tmp_path, circumstance
```

## Step-by-Step Guide

### Step 1: Assign unknown = self._get_info(...)

```python
files, options = self._get_info(circumstance)
```

**Verification:**
```python
assert sdist_files >= set(files)
```

### Step 2: Call _populate_project_dir()

```python
_populate_project_dir(tmp_path, files, options)
```

**Verification:**
```python
assert wheel_files >= orig_files
```

### Step 3: Call unknown.mkdir()

```python
(tmp_path / 'build').mkdir()
```

**Verification:**
```python
assert 'build' not in files
```

### Step 4: Call unknown.mkdir()

```python
(tmp_path / 'build/lib').mkdir()
```

**Verification:**
```python
assert 'dist' not in files
```

### Step 5: Call unknown.mkdir()

```python
(tmp_path / 'build/bdist.linux-x86_64').mkdir()
```

### Step 6: Call unknown.touch()

```python
(tmp_path / 'build/bdist.linux-x86_64/file.py').touch()
```

### Step 7: Call unknown.touch()

```python
(tmp_path / 'build/lib/__init__.py').touch()
```

### Step 8: Call unknown.touch()

```python
(tmp_path / 'build/lib/file.py').touch()
```

### Step 9: Call unknown.mkdir()

```python
(tmp_path / 'dist').mkdir()
```

### Step 10: Call unknown.touch()

```python
(tmp_path / 'dist/file.py').touch()
```

### Step 11: Call _run_build()

```python
_run_build(tmp_path)
```

### Step 12: Assign sdist_files = get_sdist_members(...)

```python
sdist_files = get_sdist_members(next(tmp_path.glob('dist/*.tar.gz')))
```

### Step 13: Call print()

```python
print('~~~~~ sdist_members ~~~~~')
```

### Step 14: Call print()

```python
print('\n'.join(sdist_files))
```

**Verification:**
```python
assert sdist_files >= set(files)
```

### Step 15: Assign wheel_files = get_wheel_members(...)

```python
wheel_files = get_wheel_members(next(tmp_path.glob('dist/*.whl')))
```

### Step 16: Call print()

```python
print('~~~~~ wheel_members ~~~~~')
```

### Step 17: Call print()

```python
print('\n'.join(wheel_files))
```

### Step 18: Assign orig_files = value

```python
orig_files = {f.replace('src/', '').replace('lib/', '') for f in files}
```

**Verification:**
```python
assert wheel_files >= orig_files
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, circumstance

# Workflow
files, options = self._get_info(circumstance)
_populate_project_dir(tmp_path, files, options)
(tmp_path / 'build').mkdir()
(tmp_path / 'build/lib').mkdir()
(tmp_path / 'build/bdist.linux-x86_64').mkdir()
(tmp_path / 'build/bdist.linux-x86_64/file.py').touch()
(tmp_path / 'build/lib/__init__.py').touch()
(tmp_path / 'build/lib/file.py').touch()
(tmp_path / 'dist').mkdir()
(tmp_path / 'dist/file.py').touch()
_run_build(tmp_path)
sdist_files = get_sdist_members(next(tmp_path.glob('dist/*.tar.gz')))
print('~~~~~ sdist_members ~~~~~')
print('\n'.join(sdist_files))
assert sdist_files >= set(files)
wheel_files = get_wheel_members(next(tmp_path.glob('dist/*.whl')))
print('~~~~~ wheel_members ~~~~~')
print('\n'.join(wheel_files))
orig_files = {f.replace('src/', '').replace('lib/', '') for f in files}
assert wheel_files >= orig_files
for file in wheel_files:
    assert 'build' not in files
    assert 'dist' not in files
```

## Next Steps


---

*Source: test_config_discovery.py:88 | Complexity: Advanced | Last updated: 2026-06-02*