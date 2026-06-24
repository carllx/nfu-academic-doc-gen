# How To: Find Config Files Disable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find config files disable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `email`
- `email.generator`
- `email.policy`
- `functools`
- `io`
- `os`
- `sys`
- `textwrap`
- `unittest.mock`
- `warnings`
- `distutils.cmd`
- `distutils.dist`
- `distutils.tests`
- `typing`
- `jaraco.path`
- `pytest`
- `distutils.tests.test_dist`

**Setup Required:**
```python
# Fixtures: temp_home
```

## Step-by-Step Guide

### Step 1: Call jaraco.path.build()

```python
jaraco.path.build({pydistutils_cfg: '[distutils]\n'}, temp_home)
```

**Verification:**
```python
assert len(all_files) - 1 == len(files)
```

### Step 2: Assign d = Distribution(...)

```python
d = Distribution()
```

### Step 3: Assign all_files = d.find_config_files(...)

```python
all_files = d.find_config_files()
```

### Step 4: Assign d = Distribution(...)

```python
d = Distribution(attrs={'script_args': ['--no-user-cfg']})
```

### Step 5: Assign files = d.find_config_files(...)

```python
files = d.find_config_files()
```

**Verification:**
```python
assert len(all_files) - 1 == len(files)
```


## Complete Example

```python
# Setup
# Fixtures: temp_home

# Workflow
jaraco.path.build({pydistutils_cfg: '[distutils]\n'}, temp_home)
d = Distribution()
all_files = d.find_config_files()
d = Distribution(attrs={'script_args': ['--no-user-cfg']})
files = d.find_config_files()
assert len(all_files) - 1 == len(files)
```

## Next Steps


---

*Source: test_dist.py:237 | Complexity: Intermediate | Last updated: 2026-06-02*