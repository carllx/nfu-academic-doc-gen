# How To: Dist Info Is The Same As In Wheel

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dist info is the same as in wheel

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pathlib`
- `re`
- `shutil`
- `subprocess`
- `sys`
- `functools`
- `pytest`
- `setuptools.archive_util`
- `textwrap`

**Setup Required:**
```python
# Fixtures: name, version, tmp_path, suffix, cfg
```

## Step-by-Step Guide

### Step 1: Assign config = value

```python
config = self.SETUPCFG.format(name=name, version=version) + cfg
```

**Verification:**
```python
assert dist_info.name == wheel_dist_info.name
```

### Step 2: Call run_command()

```python
run_command('bdist_wheel', cwd=tmp_path / 'dir_wheel')
```

**Verification:**
```python
assert dist_info.name.startswith(f'my_proj-{version}{suffix}')
```

### Step 3: Assign wheel = next(...)

```python
wheel = next(tmp_path.glob('dir_wheel/dist/*.whl'))
```

**Verification:**
```python
assert read(dist_info / file) == read(wheel_dist_info / file)
```

### Step 4: Call unpack_archive()

```python
unpack_archive(wheel, tmp_path / 'unpack')
```

### Step 5: Assign wheel_dist_info = next(...)

```python
wheel_dist_info = next(tmp_path.glob('unpack/*.dist-info'))
```

### Step 6: Call run_command()

```python
run_command('dist_info', cwd=tmp_path / 'dir_dist')
```

### Step 7: Assign dist_info = next(...)

```python
dist_info = next(tmp_path.glob('dir_dist/*.dist-info'))
```

**Verification:**
```python
assert dist_info.name == wheel_dist_info.name
```

### Step 8: Call unknown.mkdir()

```python
(tmp_path / i).mkdir()
```

### Step 9: Call unknown.write_text()

```python
(tmp_path / i / 'setup.cfg').write_text(config, encoding='utf-8')
```

**Verification:**
```python
assert read(dist_info / file) == read(wheel_dist_info / file)
```


## Complete Example

```python
# Setup
# Fixtures: name, version, tmp_path, suffix, cfg

# Workflow
config = self.SETUPCFG.format(name=name, version=version) + cfg
for i in ('dir_wheel', 'dir_dist'):
    (tmp_path / i).mkdir()
    (tmp_path / i / 'setup.cfg').write_text(config, encoding='utf-8')
run_command('bdist_wheel', cwd=tmp_path / 'dir_wheel')
wheel = next(tmp_path.glob('dir_wheel/dist/*.whl'))
unpack_archive(wheel, tmp_path / 'unpack')
wheel_dist_info = next(tmp_path.glob('unpack/*.dist-info'))
run_command('dist_info', cwd=tmp_path / 'dir_dist')
dist_info = next(tmp_path.glob('dir_dist/*.dist-info'))
assert dist_info.name == wheel_dist_info.name
assert dist_info.name.startswith(f'my_proj-{version}{suffix}')
for file in ('METADATA', 'entry_points.txt'):
    assert read(dist_info / file) == read(wheel_dist_info / file)
```

## Next Steps


---

*Source: test_dist_info.py:110 | Complexity: Advanced | Last updated: 2026-06-02*