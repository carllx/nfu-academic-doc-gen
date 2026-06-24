# How To: Existing Egg Info

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: When provided with the ``existing_egg_info_dir`` attribute, build_py should not
attempt to run egg_info again.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `stat`
- `warnings`
- `pathlib`
- `unittest.mock`
- `jaraco.path`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `textwrap`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'When provided with the ``existing_egg_info_dir`` attribute, build_py should not\n    attempt to run egg_info again.\n    '

```python
'When provided with the ``existing_egg_info_dir`` attribute, build_py should not\n    attempt to run egg_info again.\n    '
```

**Verification:**
```python
assert dist.include_package_data
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build(EXAMPLE_WITH_MANIFEST)
```

**Verification:**
```python
assert egg_info_dir.is_dir()
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution({'script_name': '%PEP 517%'})
```

**Verification:**
```python
assert build_py.data_files
```

### Step 4: Call dist.parse_config_files()

```python
dist.parse_config_files()
```

**Verification:**
```python
assert outputs
```

### Step 5: Assign egg_info = dist.get_command_obj(...)

```python
egg_info = dist.get_command_obj('egg_info')
```

**Verification:**
```python
assert example in outputs
```

### Step 6: Call dist.run_command()

```python
dist.run_command('egg_info')
```

### Step 7: Assign egg_info_dir = next(...)

```python
egg_info_dir = next(Path(egg_info.egg_base).glob('*.egg-info'))
```

**Verification:**
```python
assert egg_info_dir.is_dir()
```

### Step 8: Assign build_py = dist.get_command_obj(...)

```python
build_py = dist.get_command_obj('build_py')
```

### Step 9: Call build_py.finalize_options()

```python
build_py.finalize_options()
```

### Step 10: Assign egg_info = dist.get_command_obj(...)

```python
egg_info = dist.get_command_obj('egg_info')
```

### Step 11: Assign egg_info_run = Mock(...)

```python
egg_info_run = Mock(side_effect=egg_info.run)
```

### Step 12: Call monkeypatch.setattr()

```python
monkeypatch.setattr(egg_info, 'run', egg_info_run)
```

### Step 13: Call build_py.__dict__.pop()

```python
build_py.__dict__.pop('data_files', None)
```

### Step 14: Call dist.reinitialize_command()

```python
dist.reinitialize_command(egg_info)
```

### Step 15: Assign build_py.existing_egg_info_dir = None

```python
build_py.existing_egg_info_dir = None
```

### Step 16: Call build_py.run()

```python
build_py.run()
```

### Step 17: Call egg_info_run.assert_called()

```python
egg_info_run.assert_called()
```

### Step 18: Call egg_info_run.reset_mock()

```python
egg_info_run.reset_mock()
```

### Step 19: Call build_py.__dict__.pop()

```python
build_py.__dict__.pop('data_files', None)
```

### Step 20: Call dist.reinitialize_command()

```python
dist.reinitialize_command(egg_info)
```

### Step 21: Assign build_py.existing_egg_info_dir = egg_info_dir

```python
build_py.existing_egg_info_dir = egg_info_dir
```

### Step 22: Call build_py.run()

```python
build_py.run()
```

### Step 23: Call egg_info_run.assert_not_called()

```python
egg_info_run.assert_not_called()
```

**Verification:**
```python
assert build_py.data_files
```

### Step 24: Assign outputs = map(...)

```python
outputs = map(lambda x: x.replace(os.sep, '/'), build_py.get_outputs())
```

**Verification:**
```python
assert outputs
```

### Step 25: Assign example = str.replace(...)

```python
example = str(Path(build_py.build_lib, 'mypkg/__init__.py')).replace(os.sep, '/')
```

**Verification:**
```python
assert example in outputs
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, monkeypatch

# Workflow
'When provided with the ``existing_egg_info_dir`` attribute, build_py should not\n    attempt to run egg_info again.\n    '
jaraco.path.build(EXAMPLE_WITH_MANIFEST)
dist = Distribution({'script_name': '%PEP 517%'})
dist.parse_config_files()
assert dist.include_package_data
egg_info = dist.get_command_obj('egg_info')
dist.run_command('egg_info')
egg_info_dir = next(Path(egg_info.egg_base).glob('*.egg-info'))
assert egg_info_dir.is_dir()
build_py = dist.get_command_obj('build_py')
build_py.finalize_options()
egg_info = dist.get_command_obj('egg_info')
egg_info_run = Mock(side_effect=egg_info.run)
monkeypatch.setattr(egg_info, 'run', egg_info_run)
build_py.__dict__.pop('data_files', None)
dist.reinitialize_command(egg_info)
build_py.existing_egg_info_dir = None
build_py.run()
egg_info_run.assert_called()
egg_info_run.reset_mock()
build_py.__dict__.pop('data_files', None)
dist.reinitialize_command(egg_info)
build_py.existing_egg_info_dir = egg_info_dir
build_py.run()
egg_info_run.assert_not_called()
assert build_py.data_files
outputs = map(lambda x: x.replace(os.sep, '/'), build_py.get_outputs())
assert outputs
example = str(Path(build_py.build_lib, 'mypkg/__init__.py')).replace(os.sep, '/')
assert example in outputs
```

## Next Steps


---

*Source: test_build_py.py:207 | Complexity: Advanced | Last updated: 2026-06-02*