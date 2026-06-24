# How To: Install Sdist

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test install sdist

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `shutil`
- `sys`
- `enum`
- `glob`
- `hashlib`
- `urllib.request`
- `pytest`
- `packaging.requirements`
- `helpers`
- `setuptools.compat.py310`

**Setup Required:**
```python
# Fixtures: package, version, tmp_path, venv_python, setuptools_wheel
```

## Step-by-Step Guide

### Step 1: Assign venv_pip = value

```python
venv_pip = (venv_python, '-m', 'pip')
```

### Step 2: Assign sdist = retrieve_sdist(...)

```python
sdist = retrieve_sdist(package, version, tmp_path)
```

### Step 3: Assign deps = build_deps(...)

```python
deps = build_deps(package, sdist)
```

### Step 4: Assign env = EXTRA_ENV_VARS.get(...)

```python
env = EXTRA_ENV_VARS.get(package, {})
```

### Step 5: Call run()

```python
run([*venv_pip, 'install', '--force-reinstall', setuptools_wheel])
```

### Step 6: Call run()

```python
run([*venv_pip, 'install', *INSTALL_OPTIONS, sdist], env)
```

### Step 7: Assign pkg = IMPORT_NAME.get.replace(...)

```python
pkg = IMPORT_NAME.get(package, package).replace('-', '_')
```

### Step 8: Assign script = value

```python
script = f"import {pkg}; print(getattr({pkg}, '__version__', 0))"
```

### Step 9: Call run()

```python
run([venv_python, '-c', script])
```

### Step 10: Call print()

```python
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
```

### Step 11: Call print()

```python
print('Dependencies:', deps)
```

### Step 12: Call run()

```python
run([*venv_pip, 'install', *deps])
```


## Complete Example

```python
# Setup
# Fixtures: package, version, tmp_path, venv_python, setuptools_wheel

# Workflow
venv_pip = (venv_python, '-m', 'pip')
sdist = retrieve_sdist(package, version, tmp_path)
deps = build_deps(package, sdist)
if deps:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Dependencies:', deps)
    run([*venv_pip, 'install', *deps])
env = EXTRA_ENV_VARS.get(package, {})
run([*venv_pip, 'install', '--force-reinstall', setuptools_wheel])
run([*venv_pip, 'install', *INSTALL_OPTIONS, sdist], env)
pkg = IMPORT_NAME.get(package, package).replace('-', '_')
script = f"import {pkg}; print(getattr({pkg}, '__version__', 0))"
run([venv_python, '-c', script])
```

## Next Steps


---

*Source: test_pip_install_sdist.py:127 | Complexity: Advanced | Last updated: 2026-06-02*