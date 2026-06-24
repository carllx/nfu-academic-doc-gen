# How To: Project Urls

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test project urls

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

### Step 1: Call self._setup_script_with_requires()

```python
self._setup_script_with_requires("project_urls={\n                'Link One': 'https://example.com/one/',\n                'Link Two': 'https://example.com/two/',\n                },")
```

**Verification:**
```python
assert expected_line in pkg_info_lines
```

### Step 2: Assign environ = os.environ.copy.update(...)

```python
environ = os.environ.copy().update(HOME=env.paths['home'])
```

**Verification:**
```python
assert expected_line in pkg_info_lines
```

### Step 3: Call environment.run_setup_py()

```python
environment.run_setup_py(cmd=['egg_info'], pypath=os.pathsep.join([env.paths['lib'], str(tmpdir_cwd)]), data_stream=1, env=environ)
```

**Verification:**
```python
assert self._extract_mv_version(pkg_info_lines) >= (1, 2)
```

### Step 4: Assign egg_info_dir = os.path.join(...)

```python
egg_info_dir = os.path.join('.', 'foo.egg-info')
```

### Step 5: Assign expected_line = 'Project-URL: Link One, https://example.com/one/'

```python
expected_line = 'Project-URL: Link One, https://example.com/one/'
```

**Verification:**
```python
assert expected_line in pkg_info_lines
```

### Step 6: Assign expected_line = 'Project-URL: Link Two, https://example.com/two/'

```python
expected_line = 'Project-URL: Link Two, https://example.com/two/'
```

**Verification:**
```python
assert expected_line in pkg_info_lines
```

### Step 7: Assign pkg_info_lines = fp.read.split(...)

```python
pkg_info_lines = fp.read().split('\n')
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
self._setup_script_with_requires("project_urls={\n                'Link One': 'https://example.com/one/',\n                'Link Two': 'https://example.com/two/',\n                },")
environ = os.environ.copy().update(HOME=env.paths['home'])
environment.run_setup_py(cmd=['egg_info'], pypath=os.pathsep.join([env.paths['lib'], str(tmpdir_cwd)]), data_stream=1, env=environ)
egg_info_dir = os.path.join('.', 'foo.egg-info')
with open(os.path.join(egg_info_dir, 'PKG-INFO'), encoding='utf-8') as fp:
    pkg_info_lines = fp.read().split('\n')
expected_line = 'Project-URL: Link One, https://example.com/one/'
assert expected_line in pkg_info_lines
expected_line = 'Project-URL: Link Two, https://example.com/two/'
assert expected_line in pkg_info_lines
assert self._extract_mv_version(pkg_info_lines) >= (1, 2)
```

## Next Steps


---

*Source: test_egg_info.py:1144 | Complexity: Intermediate | Last updated: 2026-06-02*