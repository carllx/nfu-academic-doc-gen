# How To: Home Installation Scheme

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test home installation scheme

## Prerequisites

**Required Modules:**
- `logging`
- `os`
- `pathlib`
- `site`
- `sys`
- `distutils`
- `distutils.command`
- `distutils.command.build_ext`
- `distutils.command.install`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.util`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign builddir = self.mkdtemp(...)

```python
builddir = self.mkdtemp()
```

**Verification:**
```python
assert cmd.install_base == destination
```

### Step 2: Assign destination = os.path.join(...)

```python
destination = os.path.join(builddir, 'installation')
```

**Verification:**
```python
assert cmd.install_platbase == destination
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'foopkg'})
```

**Verification:**
```python
assert got == expected
```

### Step 4: Assign dist.script_name = os.path.join(...)

```python
dist.script_name = os.path.join(builddir, 'setup.py')
```

### Step 5: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['build'] = support.DummyCommand(build_base=builddir, build_lib=os.path.join(builddir, 'lib'))
```

### Step 6: Assign cmd = install(...)

```python
cmd = install(dist)
```

### Step 7: Assign cmd.home = destination

```python
cmd.home = destination
```

### Step 8: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

**Verification:**
```python
assert cmd.install_base == destination
```

### Step 9: Assign impl_name = sys.implementation.name.replace(...)

```python
impl_name = sys.implementation.name.replace('cpython', 'python')
```

### Step 10: Assign libdir = os.path.join(...)

```python
libdir = os.path.join(destination, 'lib', impl_name)
```

### Step 11: Call check_path()

```python
check_path(cmd.install_lib, libdir)
```

### Step 12: Assign _platlibdir = getattr(...)

```python
_platlibdir = getattr(sys, 'platlibdir', 'lib')
```

### Step 13: Assign platlibdir = os.path.join(...)

```python
platlibdir = os.path.join(destination, _platlibdir, impl_name)
```

### Step 14: Call check_path()

```python
check_path(cmd.install_platlib, platlibdir)
```

### Step 15: Call check_path()

```python
check_path(cmd.install_purelib, libdir)
```

### Step 16: Call check_path()

```python
check_path(cmd.install_headers, os.path.join(destination, 'include', impl_name, 'foopkg'))
```

### Step 17: Call check_path()

```python
check_path(cmd.install_scripts, os.path.join(destination, 'bin'))
```

### Step 18: Call check_path()

```python
check_path(cmd.install_data, destination)
```

### Step 19: Assign got = os.path.normpath(...)

```python
got = os.path.normpath(got)
```

### Step 20: Assign expected = os.path.normpath(...)

```python
expected = os.path.normpath(expected)
```

**Verification:**
```python
assert got == expected
```


## Complete Example

```python
# Workflow
builddir = self.mkdtemp()
destination = os.path.join(builddir, 'installation')
dist = Distribution({'name': 'foopkg'})
dist.script_name = os.path.join(builddir, 'setup.py')
dist.command_obj['build'] = support.DummyCommand(build_base=builddir, build_lib=os.path.join(builddir, 'lib'))
cmd = install(dist)
cmd.home = destination
cmd.ensure_finalized()
assert cmd.install_base == destination
assert cmd.install_platbase == destination

def check_path(got, expected):
    got = os.path.normpath(got)
    expected = os.path.normpath(expected)
    assert got == expected
impl_name = sys.implementation.name.replace('cpython', 'python')
libdir = os.path.join(destination, 'lib', impl_name)
check_path(cmd.install_lib, libdir)
_platlibdir = getattr(sys, 'platlibdir', 'lib')
platlibdir = os.path.join(destination, _platlibdir, impl_name)
check_path(cmd.install_platlib, platlibdir)
check_path(cmd.install_purelib, libdir)
check_path(cmd.install_headers, os.path.join(destination, 'include', impl_name, 'foopkg'))
check_path(cmd.install_scripts, os.path.join(destination, 'bin'))
check_path(cmd.install_data, destination)
```

## Next Steps


---

*Source: test_install.py:34 | Complexity: Advanced | Last updated: 2026-06-02*