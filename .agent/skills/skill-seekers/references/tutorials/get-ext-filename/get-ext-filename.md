# How To: Get Ext Filename

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Setuptools needs to give back the same
result as distutils, even if the fullname
is not in ext_map.

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

### Step 1: '\n        Setuptools needs to give back the same\n        result as distutils, even if the fullname\n        is not in ext_map.\n        '

```python
'\n        Setuptools needs to give back the same\n        result as distutils, even if the fullname\n        is not in ext_map.\n        '
```

**Verification:**
```python
assert res == wanted
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 3: Assign cmd = build_ext(...)

```python
cmd = build_ext(dist)
```

### Step 4: Assign unknown = ''

```python
cmd.ext_map['foo/bar'] = ''
```

### Step 5: Assign res = cmd.get_ext_filename(...)

```python
res = cmd.get_ext_filename('foo')
```

### Step 6: Assign wanted = orig.build_ext.get_ext_filename(...)

```python
wanted = orig.build_ext.get_ext_filename(cmd, 'foo')
```

**Verification:**
```python
assert res == wanted
```


## Complete Example

```python
# Workflow
'\n        Setuptools needs to give back the same\n        result as distutils, even if the fullname\n        is not in ext_map.\n        '
dist = Distribution()
cmd = build_ext(dist)
cmd.ext_map['foo/bar'] = ''
res = cmd.get_ext_filename('foo')
wanted = orig.build_ext.get_ext_filename(cmd, 'foo')
assert res == wanted
```

## Next Steps


---

*Source: test_build_ext.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*