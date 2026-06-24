# How To: Array Api Entry Point

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Entry point for Array API implementation can be found with importlib and
returns the main numpy namespace.

## Prerequisites

**Required Modules:**
- `functools`
- `importlib`
- `inspect`
- `pkgutil`
- `subprocess`
- `sys`
- `sysconfig`
- `types`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `ctypes`
- `numpy.core`
- `collections.abc`
- `typing`
- `numpy._core._multiarray_umath`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: '\n    Entry point for Array API implementation can be found with importlib and\n    returns the main numpy namespace.\n    '

```python
'\n    Entry point for Array API implementation can be found with importlib and\n    returns the main numpy namespace.\n    '
```

**Verification:**
```python
assert xp is numpy, msg
```

### Step 2: Assign numpy_in_sitepackages = value

```python
numpy_in_sitepackages = sysconfig.get_path('platlib') in np.__file__
```

### Step 3: Assign eps = importlib.metadata.entry_points(...)

```python
eps = importlib.metadata.entry_points()
```

### Step 4: Assign xp_eps = eps.select(...)

```python
xp_eps = eps.select(group='array_api')
```

### Step 5: Assign xp = ep.load(...)

```python
xp = ep.load()
```

### Step 6: Assign msg = value

```python
msg = f"numpy entry point value '{ep.value}' does not point to our Array API implementation"
```

**Verification:**
```python
assert xp is numpy, msg
```

### Step 7: Assign ep = next(...)

```python
ep = next((ep for ep in xp_eps if ep.name == 'numpy'))
```

### Step 8: Assign msg = "No entry points for 'array_api' found"

```python
msg = "No entry points for 'array_api' found"
```

### Step 9: Assign msg = "'numpy' not in array_api entry points"

```python
msg = "'numpy' not in array_api entry points"
```


## Complete Example

```python
# Workflow
'\n    Entry point for Array API implementation can be found with importlib and\n    returns the main numpy namespace.\n    '
numpy_in_sitepackages = sysconfig.get_path('platlib') in np.__file__
eps = importlib.metadata.entry_points()
xp_eps = eps.select(group='array_api')
if len(xp_eps) == 0:
    if numpy_in_sitepackages:
        msg = "No entry points for 'array_api' found"
        raise AssertionError(msg) from None
    return
try:
    ep = next((ep for ep in xp_eps if ep.name == 'numpy'))
except StopIteration:
    if numpy_in_sitepackages:
        msg = "'numpy' not in array_api entry points"
        raise AssertionError(msg) from None
    return
if ep.value == 'numpy.array_api':
    return
xp = ep.load()
msg = f"numpy entry point value '{ep.value}' does not point to our Array API implementation"
assert xp is numpy, msg
```

## Next Steps


---

*Source: test_public_api.py:437 | Complexity: Advanced | Last updated: 2026-06-02*