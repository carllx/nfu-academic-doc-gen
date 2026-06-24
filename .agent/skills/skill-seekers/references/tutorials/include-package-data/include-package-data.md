# How To: Include Package Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Make sure auto-discovery does not affect package include_package_data.
See issue #3196.

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
# Fixtures: tmp_path, src_root, files
```

## Step-by-Step Guide

### Step 1: '\n        Make sure auto-discovery does not affect package include_package_data.\n        See issue #3196.\n        '

```python
'\n        Make sure auto-discovery does not affect package include_package_data.\n        See issue #3196.\n        '
```

**Verification:**
```python
assert sdist_files >= expected
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build(files, prefix=str(tmp_path))
```

**Verification:**
```python
assert wheel_files >= orig_files
```

### Step 3: Call self._simulate_package_with_data_files()

```python
self._simulate_package_with_data_files(tmp_path, src_root)
```

### Step 4: Assign expected = value

```python
expected = {os.path.normpath(f'{src_root}/proj/file1.txt').replace(os.sep, '/'), os.path.normpath(f'{src_root}/proj/nested/file2.txt').replace(os.sep, '/')}
```

### Step 5: Call _run_build()

```python
_run_build(tmp_path)
```

### Step 6: Assign sdist_files = get_sdist_members(...)

```python
sdist_files = get_sdist_members(next(tmp_path.glob('dist/*.tar.gz')))
```

### Step 7: Call print()

```python
print('~~~~~ sdist_members ~~~~~')
```

### Step 8: Call print()

```python
print('\n'.join(sdist_files))
```

**Verification:**
```python
assert sdist_files >= expected
```

### Step 9: Assign wheel_files = get_wheel_members(...)

```python
wheel_files = get_wheel_members(next(tmp_path.glob('dist/*.whl')))
```

### Step 10: Call print()

```python
print('~~~~~ wheel_members ~~~~~')
```

### Step 11: Call print()

```python
print('\n'.join(wheel_files))
```

### Step 12: Assign orig_files = value

```python
orig_files = {f.replace('src/', '').replace('lib/', '') for f in expected}
```

**Verification:**
```python
assert wheel_files >= orig_files
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, src_root, files

# Workflow
'\n        Make sure auto-discovery does not affect package include_package_data.\n        See issue #3196.\n        '
jaraco.path.build(files, prefix=str(tmp_path))
self._simulate_package_with_data_files(tmp_path, src_root)
expected = {os.path.normpath(f'{src_root}/proj/file1.txt').replace(os.sep, '/'), os.path.normpath(f'{src_root}/proj/nested/file2.txt').replace(os.sep, '/')}
_run_build(tmp_path)
sdist_files = get_sdist_members(next(tmp_path.glob('dist/*.tar.gz')))
print('~~~~~ sdist_members ~~~~~')
print('\n'.join(sdist_files))
assert sdist_files >= expected
wheel_files = get_wheel_members(next(tmp_path.glob('dist/*.whl')))
print('~~~~~ wheel_members ~~~~~')
print('\n'.join(wheel_files))
orig_files = {f.replace('src/', '').replace('lib/', '') for f in expected}
assert wheel_files >= orig_files
```

## Next Steps


---

*Source: test_config_discovery.py:485 | Complexity: Advanced | Last updated: 2026-06-02*