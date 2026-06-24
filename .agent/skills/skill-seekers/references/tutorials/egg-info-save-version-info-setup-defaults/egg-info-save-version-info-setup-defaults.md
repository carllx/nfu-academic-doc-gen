# How To: Egg Info Save Version Info Setup Defaults

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: When running save_version_info on an existing setup.cfg
with the 'default' values present from a previous run,
the file should remain unchanged.

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

### Step 1: "\n        When running save_version_info on an existing setup.cfg\n        with the 'default' values present from a previous run,\n        the file should remain unchanged.\n        "

```python
"\n        When running save_version_info on an existing setup.cfg\n        with the 'default' values present from a previous run,\n        the file should remain unchanged.\n        "
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

### Step 3: Call path.build()

```python
path.build({setup_cfg: DALS('\n            [egg_info]\n            tag_build =\n            tag_date = 0\n            ')})
```

**Verification:**
```python
assert 'tag_date = 0' in content
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 5: Assign ei = egg_info(...)

```python
ei = egg_info(dist)
```

### Step 6: Call ei.initialize_options()

```python
ei.initialize_options()
```

### Step 7: Call ei.save_version_info()

```python
ei.save_version_info(setup_cfg)
```

**Verification:**
```python
assert '[egg_info]' in content
```

### Step 8: Assign expected_order = value

```python
expected_order = ('tag_build', 'tag_date')
```

### Step 9: Call self._validate_content_order()

```python
self._validate_content_order(content, expected_order)
```

### Step 10: Assign content = f.read(...)

```python
content = f.read()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
"\n        When running save_version_info on an existing setup.cfg\n        with the 'default' values present from a previous run,\n        the file should remain unchanged.\n        "
setup_cfg = os.path.join(env.paths['home'], 'setup.cfg')
path.build({setup_cfg: DALS('\n            [egg_info]\n            tag_build =\n            tag_date = 0\n            ')})
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

*Source: test_egg_info.py:116 | Complexity: Advanced | Last updated: 2026-06-02*