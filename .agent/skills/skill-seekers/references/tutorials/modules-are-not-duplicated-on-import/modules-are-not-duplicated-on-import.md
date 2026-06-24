# How To: Modules Are Not Duplicated On Import

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test modules are not duplicated on import

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `platform`
- `sys`
- `textwrap`
- `pytest`

**Setup Required:**
```python
# Fixtures: distutils_version, imported_module, venv
```

## Step-by-Step Guide

### Step 1: Assign env = dict(...)

```python
env = dict(SETUPTOOLS_USE_DISTUTILS=distutils_version)
```

**Verification:**
```python
assert output == 'success'
```

### Step 2: Assign script = ENSURE_IMPORTS_ARE_NOT_DUPLICATED.format(...)

```python
script = ENSURE_IMPORTS_ARE_NOT_DUPLICATED.format(imported_module=imported_module)
```

### Step 3: Assign cmd = value

```python
cmd = ['python', '-c', script]
```

### Step 4: Assign output = venv.run.strip(...)

```python
output = venv.run(cmd, env=win_sr(env), **_TEXT_KWARGS).strip()
```

**Verification:**
```python
assert output == 'success'
```


## Complete Example

```python
# Setup
# Fixtures: distutils_version, imported_module, venv

# Workflow
env = dict(SETUPTOOLS_USE_DISTUTILS=distutils_version)
script = ENSURE_IMPORTS_ARE_NOT_DUPLICATED.format(imported_module=imported_module)
cmd = ['python', '-c', script]
output = venv.run(cmd, env=win_sr(env), **_TEXT_KWARGS).strip()
assert output == 'success'
```

## Next Steps


---

*Source: test_distutils_adoption.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*