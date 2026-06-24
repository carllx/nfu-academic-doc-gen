# How To: Output Dir

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test output dir

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
# Fixtures: tmp_path, keep_egg_info
```

## Step-by-Step Guide

### Step 1: Assign config = '[metadata]\nname=proj\nversion=42\n'

```python
config = '[metadata]\nname=proj\nversion=42\n'
```

**Verification:**
```python
assert len(list(out.glob('*.dist-info'))) == 1
```

### Step 2: Call unknown.write_text()

```python
(tmp_path / 'setup.cfg').write_text(config, encoding='utf-8')
```

**Verification:**
```python
assert len(list(tmp_path.glob('*.dist-info'))) == 0
```

### Step 3: Assign out = value

```python
out = tmp_path / '__out'
```

**Verification:**
```python
assert len(list(out.glob('*.egg-info'))) == expected_egg_info
```

### Step 4: Call out.mkdir()

```python
out.mkdir()
```

**Verification:**
```python
assert len(list(tmp_path.glob('*.egg-info'))) == 0
```

### Step 5: Assign opts = value

```python
opts = ['--keep-egg-info'] if keep_egg_info else []
```

**Verification:**
```python
assert len(list(out.glob('*.__bkp__'))) == 0
```

### Step 6: Call run_command()

```python
run_command('dist_info', '--output-dir', out, *opts, cwd=tmp_path)
```

**Verification:**
```python
assert len(list(tmp_path.glob('*.__bkp__'))) == 0
```

### Step 7: Assign expected_egg_info = int(...)

```python
expected_egg_info = int(keep_egg_info)
```

**Verification:**
```python
assert len(list(out.glob('*.egg-info'))) == expected_egg_info
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, keep_egg_info

# Workflow
config = '[metadata]\nname=proj\nversion=42\n'
(tmp_path / 'setup.cfg').write_text(config, encoding='utf-8')
out = tmp_path / '__out'
out.mkdir()
opts = ['--keep-egg-info'] if keep_egg_info else []
run_command('dist_info', '--output-dir', out, *opts, cwd=tmp_path)
assert len(list(out.glob('*.dist-info'))) == 1
assert len(list(tmp_path.glob('*.dist-info'))) == 0
expected_egg_info = int(keep_egg_info)
assert len(list(out.glob('*.egg-info'))) == expected_egg_info
assert len(list(tmp_path.glob('*.egg-info'))) == 0
assert len(list(out.glob('*.__bkp__'))) == 0
assert len(list(tmp_path.glob('*.__bkp__'))) == 0
```

## Next Steps


---

*Source: test_dist_info.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*