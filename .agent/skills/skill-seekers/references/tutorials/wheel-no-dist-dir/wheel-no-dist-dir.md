# How To: Wheel No Dist Dir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wheel no dist dir

## Prerequisites

**Required Modules:**
- `__future__`
- `contextlib`
- `glob`
- `inspect`
- `os`
- `pathlib`
- `stat`
- `subprocess`
- `sys`
- `sysconfig`
- `zipfile`
- `typing`
- `pytest`
- `jaraco`
- `packaging.tags`
- `setuptools._importlib`
- `setuptools.wheel`
- `contexts`
- `textwrap`
- `distutils.sysconfig`
- `distutils.util`


## Step-by-Step Guide

### Step 1: Assign project_name = 'nodistinfo'

```python
project_name = 'nodistinfo'
```

### Step 2: Assign version = '1.0'

```python
version = '1.0'
```

### Step 3: Assign wheel_name = value

```python
wheel_name = f'{project_name}-{version}-py2.py3-none-any.whl'
```

### Step 4: Assign wheel_path = os.path.join(...)

```python
wheel_path = os.path.join(source_dir, wheel_name)
```

### Step 5: Call zipfile.ZipFile.close()

```python
zipfile.ZipFile(wheel_path, 'w').close()
```

### Step 6: Call _check_wheel_install()

```python
_check_wheel_install(wheel_path, install_dir, None, project_name, version, None)
```


## Complete Example

```python
# Workflow
project_name = 'nodistinfo'
version = '1.0'
wheel_name = f'{project_name}-{version}-py2.py3-none-any.whl'
with tempdir() as source_dir:
    wheel_path = os.path.join(source_dir, wheel_name)
    zipfile.ZipFile(wheel_path, 'w').close()
    with tempdir() as install_dir:
        with pytest.raises(ValueError):
            _check_wheel_install(wheel_path, install_dir, None, project_name, version, None)
```

## Next Steps


---

*Source: test_wheel.py:579 | Complexity: Intermediate | Last updated: 2026-06-02*