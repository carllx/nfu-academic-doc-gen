# How To: Ext Fullpath

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ext fullpath

## Prerequisites

**Required Modules:**
- `contextlib`
- `glob`
- `importlib`
- `os.path`
- `platform`
- `re`
- `shutil`
- `site`
- `subprocess`
- `sys`
- `tempfile`
- `textwrap`
- `time`
- `distutils`
- `distutils.command.build_ext`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.tests.support`
- `io`
- `jaraco.path`
- `path`
- `pytest`
- `test`
- `compat`
- `distutils.command`
- `xx`
- `distutils.sysconfig`
- `site`
- `pprint`


## Step-by-Step Guide

### Step 1: Assign ext = sysconfig.get_config_var(...)

```python
ext = sysconfig.get_config_var('EXT_SUFFIX')
```

**Verification:**
```python
assert wanted == path
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert wanted == path
```

### Step 3: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

**Verification:**
```python
assert wanted == path
```

### Step 4: Assign cmd.inplace = True

```python
cmd.inplace = True
```

**Verification:**
```python
assert wanted == path
```

### Step 5: Assign cmd.distribution.package_dir = value

```python
cmd.distribution.package_dir = {'': 'src'}
```

### Step 6: Assign cmd.distribution.packages = value

```python
cmd.distribution.packages = ['lxml', 'lxml.html']
```

### Step 7: Assign curdir = os.getcwd(...)

```python
curdir = os.getcwd()
```

### Step 8: Assign wanted = os.path.join(...)

```python
wanted = os.path.join(curdir, 'src', 'lxml', 'etree' + ext)
```

### Step 9: Assign path = cmd.get_ext_fullpath(...)

```python
path = cmd.get_ext_fullpath('lxml.etree')
```

**Verification:**
```python
assert wanted == path
```

### Step 10: Assign cmd.inplace = False

```python
cmd.inplace = False
```

### Step 11: Assign cmd.build_lib = os.path.join(...)

```python
cmd.build_lib = os.path.join(curdir, 'tmpdir')
```

### Step 12: Assign wanted = os.path.join(...)

```python
wanted = os.path.join(curdir, 'tmpdir', 'lxml', 'etree' + ext)
```

### Step 13: Assign path = cmd.get_ext_fullpath(...)

```python
path = cmd.get_ext_fullpath('lxml.etree')
```

**Verification:**
```python
assert wanted == path
```

### Step 14: Assign build_py = cmd.get_finalized_command(...)

```python
build_py = cmd.get_finalized_command('build_py')
```

### Step 15: Assign build_py.package_dir = value

```python
build_py.package_dir = {}
```

### Step 16: Assign cmd.distribution.packages = value

```python
cmd.distribution.packages = ['twisted', 'twisted.runner.portmap']
```

### Step 17: Assign path = cmd.get_ext_fullpath(...)

```python
path = cmd.get_ext_fullpath('twisted.runner.portmap')
```

### Step 18: Assign wanted = os.path.join(...)

```python
wanted = os.path.join(curdir, 'tmpdir', 'twisted', 'runner', 'portmap' + ext)
```

**Verification:**
```python
assert wanted == path
```

### Step 19: Assign cmd.inplace = True

```python
cmd.inplace = True
```

### Step 20: Assign path = cmd.get_ext_fullpath(...)

```python
path = cmd.get_ext_fullpath('twisted.runner.portmap')
```

### Step 21: Assign wanted = os.path.join(...)

```python
wanted = os.path.join(curdir, 'twisted', 'runner', 'portmap' + ext)
```

**Verification:**
```python
assert wanted == path
```


## Complete Example

```python
# Workflow
ext = sysconfig.get_config_var('EXT_SUFFIX')
dist = Distribution()
cmd = self.build_ext(dist)
cmd.inplace = True
cmd.distribution.package_dir = {'': 'src'}
cmd.distribution.packages = ['lxml', 'lxml.html']
curdir = os.getcwd()
wanted = os.path.join(curdir, 'src', 'lxml', 'etree' + ext)
path = cmd.get_ext_fullpath('lxml.etree')
assert wanted == path
cmd.inplace = False
cmd.build_lib = os.path.join(curdir, 'tmpdir')
wanted = os.path.join(curdir, 'tmpdir', 'lxml', 'etree' + ext)
path = cmd.get_ext_fullpath('lxml.etree')
assert wanted == path
build_py = cmd.get_finalized_command('build_py')
build_py.package_dir = {}
cmd.distribution.packages = ['twisted', 'twisted.runner.portmap']
path = cmd.get_ext_fullpath('twisted.runner.portmap')
wanted = os.path.join(curdir, 'tmpdir', 'twisted', 'runner', 'portmap' + ext)
assert wanted == path
cmd.inplace = True
path = cmd.get_ext_fullpath('twisted.runner.portmap')
wanted = os.path.join(curdir, 'twisted', 'runner', 'portmap' + ext)
assert wanted == path
```

## Next Steps


---

*Source: test_build_ext.py:490 | Complexity: Advanced | Last updated: 2026-06-02*