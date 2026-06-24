# How To: Ext Suffix Override

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: SETUPTOOLS_EXT_SUFFIX variable always overrides
default extension options.

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

### Step 1: '\n        SETUPTOOLS_EXT_SUFFIX variable always overrides\n        default extension options.\n        '

```python
'\n        SETUPTOOLS_EXT_SUFFIX variable always overrides\n        default extension options.\n        '
```

**Verification:**
```python
assert 'normal.test-suffix' == res
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert expect == res
```

### Step 3: Assign cmd = build_ext(...)

```python
cmd = build_ext(dist)
```

### Step 4: Assign unknown, ext = Extension(...)

```python
cmd.ext_map['for_abi3'] = ext = Extension('for_abi3', ['s.c'], py_limited_api=True)
```

### Step 5: Assign ext._links_to_dynamic = False

```python
ext._links_to_dynamic = False
```

### Step 6: Assign expect = cmd.get_ext_filename(...)

```python
expect = cmd.get_ext_filename('for_abi3')
```

### Step 7: Assign expect = 'for_abi3.test-suffix'

```python
expect = 'for_abi3.test-suffix'
```

### Step 8: Assign unknown = '.test-suffix'

```python
os.environ['SETUPTOOLS_EXT_SUFFIX'] = '.test-suffix'
```

### Step 9: Assign res = cmd.get_ext_filename(...)

```python
res = cmd.get_ext_filename('normal')
```

**Verification:**
```python
assert 'normal.test-suffix' == res
```

### Step 10: Assign res = cmd.get_ext_filename(...)

```python
res = cmd.get_ext_filename('for_abi3')
```

**Verification:**
```python
assert expect == res
```


## Complete Example

```python
# Workflow
'\n        SETUPTOOLS_EXT_SUFFIX variable always overrides\n        default extension options.\n        '
dist = Distribution()
cmd = build_ext(dist)
cmd.ext_map['for_abi3'] = ext = Extension('for_abi3', ['s.c'], py_limited_api=True)
ext._links_to_dynamic = False
if not IS_PYPY:
    expect = cmd.get_ext_filename('for_abi3')
else:
    expect = 'for_abi3.test-suffix'
try:
    os.environ['SETUPTOOLS_EXT_SUFFIX'] = '.test-suffix'
    res = cmd.get_ext_filename('normal')
    assert 'normal.test-suffix' == res
    res = cmd.get_ext_filename('for_abi3')
    assert expect == res
finally:
    del os.environ['SETUPTOOLS_EXT_SUFFIX']
```

## Next Steps


---

*Source: test_build_ext.py:59 | Complexity: Advanced | Last updated: 2026-06-02*