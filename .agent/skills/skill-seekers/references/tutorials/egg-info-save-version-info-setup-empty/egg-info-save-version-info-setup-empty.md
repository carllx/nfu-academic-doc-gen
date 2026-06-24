# How To: Egg Info Save Version Info Setup Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: When the egg_info section is empty or not present, running
save_version_info should add the settings to the setup.cfg
in a deterministic order.

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
# Fixtures: tmpdir_cwd, env
```

## Step-by-Step Guide

### Step 1: '\n        When the egg_info section is empty or not present, running\n        save_version_info should add the settings to the setup.cfg\n        in a deterministic order.\n        '

```python
'\n        When the egg_info section is empty or not present, running\n        save_version_info should add the settings to the setup.cfg\n        in a deterministic order.\n        '
```

**Verification:**
```python
assert '[egg_info]' in content
```

### Step 2: Assign setup_cfg = os.path.join(...)

```python
setup_cfg = os.path.join(env.paths['home'], 'setup.cfg')
```

**Verification:**
```python
assert 'tag_build =' in content
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert 'tag_date = 0' in content
```

### Step 4: Assign ei = egg_info(...)

```python
ei = egg_info(dist)
```

### Step 5: Call ei.initialize_options()

```python
ei.initialize_options()
```

### Step 6: Call ei.save_version_info()

```python
ei.save_version_info(setup_cfg)
```

**Verification:**
```python
assert '[egg_info]' in content
```

### Step 7: Assign expected_order = value

```python
expected_order = ('tag_build', 'tag_date')
```

### Step 8: Call self._validate_content_order()

```python
self._validate_content_order(content, expected_order)
```

### Step 9: Assign content = f.read(...)

```python
content = f.read()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
'\n        When the egg_info section is empty or not present, running\n        save_version_info should add the settings to the setup.cfg\n        in a deterministic order.\n        '
setup_cfg = os.path.join(env.paths['home'], 'setup.cfg')
dist = Distribution()
ei = egg_info(dist)
ei.initialize_options()
ei.save_version_info(setup_cfg)
with open(setup_cfg, 'r', encoding='utf-8') as f:
    content = f.read()
assert '[egg_info]' in content
assert 'tag_build =' in content
assert 'tag_date = 0' in content
expected_order = ('tag_build', 'tag_date')
self._validate_content_order(content, expected_order)
```

## Next Steps


---

*Source: test_egg_info.py:80 | Complexity: Advanced | Last updated: 2026-06-02*