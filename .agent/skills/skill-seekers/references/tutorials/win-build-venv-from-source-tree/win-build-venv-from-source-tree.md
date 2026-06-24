# How To: Win Build Venv From Source Tree

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Ensure distutils.sysconfig detects venvs from source tree builds.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `distutils`
- `os`
- `pathlib`
- `subprocess`
- `sys`
- `distutils`
- `distutils.ccompiler`
- `distutils.unixccompiler`
- `jaraco.envs`
- `path`
- `pytest`
- `jaraco.text`
- `test.support`
- `sysconfig`
- `sysconfig`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'Ensure distutils.sysconfig detects venvs from source tree builds.'

```python
'Ensure distutils.sysconfig detects venvs from source tree builds.'
```

**Verification:**
```python
assert out == 'True'
```

### Step 2: Assign env = jaraco.envs.VEnv(...)

```python
env = jaraco.envs.VEnv()
```

### Step 3: Assign env.create_opts = value

```python
env.create_opts = env.clean_opts
```

### Step 4: Assign env.root = tmp_path

```python
env.root = tmp_path
```

### Step 5: Call env.ensure_env()

```python
env.ensure_env()
```

### Step 6: Assign cmd = value

```python
cmd = [env.exe(), '-c', 'import distutils.sysconfig; print(distutils.sysconfig.python_build)']
```

### Step 7: Assign distutils_path = os.path.dirname(...)

```python
distutils_path = os.path.dirname(os.path.dirname(distutils.__file__))
```

### Step 8: Assign out = subprocess.check_output(...)

```python
out = subprocess.check_output(cmd, env={**os.environ, 'PYTHONPATH': distutils_path})
```

**Verification:**
```python
assert out == 'True'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Ensure distutils.sysconfig detects venvs from source tree builds.'
env = jaraco.envs.VEnv()
env.create_opts = env.clean_opts
env.root = tmp_path
env.ensure_env()
cmd = [env.exe(), '-c', 'import distutils.sysconfig; print(distutils.sysconfig.python_build)']
distutils_path = os.path.dirname(os.path.dirname(distutils.__file__))
out = subprocess.check_output(cmd, env={**os.environ, 'PYTHONPATH': distutils_path})
assert out == 'True'
```

## Next Steps


---

*Source: test_sysconfig.py:285 | Complexity: Advanced | Last updated: 2026-06-02*