# How To: Requires

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, pytest, workflow, integration

## Overview

Workflow: test requires

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `ast`
- `glob`
- `os`
- `re`
- `stat`
- `sys`
- `time`
- `pathlib`
- `unittest`
- `pytest`
- `jaraco`
- `setuptools`
- `setuptools.command.egg_info`
- `setuptools.dist`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, env, requires, use_setup_cfg, expected_requires, install_cmd_kwargs
```

## Step-by-Step Guide

### Step 1: Call self._setup_script_with_requires()

```python
self._setup_script_with_requires(requires, use_setup_cfg)
```

**Verification:**
```python
assert install_requires.lstrip() == expected_requires
```

### Step 2: Call self._run_egg_info_command()

```python
self._run_egg_info_command(tmpdir_cwd, env, **install_cmd_kwargs)
```

**Verification:**
```python
assert glob.glob(os.path.join(env.paths['lib'], 'barbazquux*')) == []
```

### Step 3: Assign egg_info_dir = os.path.join(...)

```python
egg_info_dir = os.path.join('.', 'foo.egg-info')
```

### Step 4: Assign requires_txt = os.path.join(...)

```python
requires_txt = os.path.join(egg_info_dir, 'requires.txt')
```

**Verification:**
```python
assert install_requires.lstrip() == expected_requires
```

### Step 5: Assign install_requires = ''

```python
install_requires = ''
```

### Step 6: Assign install_requires = fp.read(...)

```python
install_requires = fp.read()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env, requires, use_setup_cfg, expected_requires, install_cmd_kwargs

# Workflow
self._setup_script_with_requires(requires, use_setup_cfg)
self._run_egg_info_command(tmpdir_cwd, env, **install_cmd_kwargs)
egg_info_dir = os.path.join('.', 'foo.egg-info')
requires_txt = os.path.join(egg_info_dir, 'requires.txt')
if os.path.exists(requires_txt):
    with open(requires_txt, encoding='utf-8') as fp:
        install_requires = fp.read()
else:
    install_requires = ''
assert install_requires.lstrip() == expected_requires
assert glob.glob(os.path.join(env.paths['lib'], 'barbazquux*')) == []
```

## Next Steps


---

*Source: test_egg_info.py:462 | Complexity: Intermediate | Last updated: 2026-06-02*