# How To: Abi3 Filename

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Filename needs to be loadable by several versions
of Python 3 if 'is_abi3' is truthy on Extension()

## Prerequisites

**Required Modules:**
- `__future__`
- `os`
- `sys`
- `importlib.util`
- `pytest`
- `jaraco`
- `setuptools.command.build_ext`
- `setuptools.dist`
- `setuptools.errors`
- `setuptools.extension`
- `textwrap`
- `distutils.command.build_ext`
- `distutils.sysconfig`


## Step-by-Step Guide

### Step 1: "\n        Filename needs to be loadable by several versions\n        of Python 3 if 'is_abi3' is truthy on Extension()\n        "

```python
"\n        Filename needs to be loadable by several versions\n        of Python 3 if 'is_abi3' is truthy on Extension()\n        "
```

**Verification:**
```python
assert 'spam.eggs' in cmd.ext_map
```

### Step 2: Call print()

```python
print(get_abi3_suffix())
```

**Verification:**
```python
assert res.endswith(get_config_var('EXT_SUFFIX'))
```

### Step 3: Assign extension = Extension(...)

```python
extension = Extension('spam.eggs', ['eggs.c'], py_limited_api=True)
```

**Verification:**
```python
assert res.endswith('eggs.pyd')
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution(dict(ext_modules=[extension]))
```

**Verification:**
```python
assert 'abi3' in res
```

### Step 5: Assign cmd = build_ext(...)

```python
cmd = build_ext(dist)
```

### Step 6: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

**Verification:**
```python
assert 'spam.eggs' in cmd.ext_map
```

### Step 7: Assign res = cmd.get_ext_filename(...)

```python
res = cmd.get_ext_filename('spam.eggs')
```

**Verification:**
```python
assert res.endswith(get_config_var('EXT_SUFFIX'))
```


## Complete Example

```python
# Workflow
"\n        Filename needs to be loadable by several versions\n        of Python 3 if 'is_abi3' is truthy on Extension()\n        "
print(get_abi3_suffix())
extension = Extension('spam.eggs', ['eggs.c'], py_limited_api=True)
dist = Distribution(dict(ext_modules=[extension]))
cmd = build_ext(dist)
cmd.finalize_options()
assert 'spam.eggs' in cmd.ext_map
res = cmd.get_ext_filename('spam.eggs')
if not get_abi3_suffix():
    assert res.endswith(get_config_var('EXT_SUFFIX'))
elif sys.platform == 'win32':
    assert res.endswith('eggs.pyd')
else:
    assert 'abi3' in res
```

## Next Steps


---

*Source: test_build_ext.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*