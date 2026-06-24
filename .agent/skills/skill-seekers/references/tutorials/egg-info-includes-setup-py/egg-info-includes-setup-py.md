# How To: Egg Info Includes Setup Py

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test egg info includes setup py

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
# Fixtures: tmpdir_cwd
```

## Step-by-Step Guide

### Step 1: Call self._create_project()

```python
self._create_project()
```

**Verification:**
```python
assert 'setup.py' in egg_info_instance.filelist.files
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'foo', 'version': '0.0.1'})
```

**Verification:**
```python
assert 'setup.py' in sources
```

### Step 3: Assign dist.script_name = 'non_setup.py'

```python
dist.script_name = 'non_setup.py'
```

### Step 4: Assign egg_info_instance = egg_info(...)

```python
egg_info_instance = egg_info(dist)
```

### Step 5: Call egg_info_instance.finalize_options()

```python
egg_info_instance.finalize_options()
```

### Step 6: Call egg_info_instance.run()

```python
egg_info_instance.run()
```

**Verification:**
```python
assert 'setup.py' in egg_info_instance.filelist.files
```

### Step 7: Assign sources = f.read.split(...)

```python
sources = f.read().split('\n')
```

**Verification:**
```python
assert 'setup.py' in sources
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd

# Workflow
self._create_project()
dist = Distribution({'name': 'foo', 'version': '0.0.1'})
dist.script_name = 'non_setup.py'
egg_info_instance = egg_info(dist)
egg_info_instance.finalize_options()
egg_info_instance.run()
assert 'setup.py' in egg_info_instance.filelist.files
with open(egg_info_instance.egg_info + '/SOURCES.txt', encoding='utf-8') as f:
    sources = f.read().split('\n')
    assert 'setup.py' in sources
```

## Next Steps


---

*Source: test_egg_info.py:1233 | Complexity: Intermediate | Last updated: 2026-06-02*