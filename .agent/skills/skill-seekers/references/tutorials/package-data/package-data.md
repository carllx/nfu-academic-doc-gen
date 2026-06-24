# How To: Package Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test package data

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `distutils.command.build_py`
- `distutils.core`
- `distutils.errors`
- `distutils.tests`
- `jaraco.path`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign sources = self.mkdtemp(...)

```python
sources = self.mkdtemp()
```

**Verification:**
```python
assert cmd.package_data == dist.package_data
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build({'__init__.py': '# Pretend this is a package.', 'README.txt': 'Info about this package'}, sources)
```

**Verification:**
```python
assert len(cmd.get_outputs()) == 3
```

### Step 3: Assign destination = self.mkdtemp(...)

```python
destination = self.mkdtemp()
```

**Verification:**
```python
assert '__init__.py' in files
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution({'packages': ['pkg'], 'package_dir': {'pkg': sources}})
```

**Verification:**
```python
assert 'README.txt' in files
```

### Step 5: Assign dist.script_name = os.path.join(...)

```python
dist.script_name = os.path.join(sources, 'setup.py')
```

**Verification:**
```python
assert not os.path.exists(pycache_dir)
```

### Step 6: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['build'] = support.DummyCommand(force=False, build_lib=destination)
```

**Verification:**
```python
assert f'__init__.{sys.implementation.cache_tag}.pyc' in pyc_files
```

### Step 7: Assign dist.packages = value

```python
dist.packages = ['pkg']
```

### Step 8: Assign dist.package_data = value

```python
dist.package_data = {'pkg': ['README.txt']}
```

### Step 9: Assign dist.package_dir = value

```python
dist.package_dir = {'pkg': sources}
```

### Step 10: Assign cmd = build_py(...)

```python
cmd = build_py(dist)
```

### Step 11: Assign cmd.compile = True

```python
cmd.compile = True
```

### Step 12: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

**Verification:**
```python
assert cmd.package_data == dist.package_data
```

### Step 13: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert len(cmd.get_outputs()) == 3
```

### Step 14: Assign pkgdest = os.path.join(...)

```python
pkgdest = os.path.join(destination, 'pkg')
```

### Step 15: Assign files = os.listdir(...)

```python
files = os.listdir(pkgdest)
```

### Step 16: Assign pycache_dir = os.path.join(...)

```python
pycache_dir = os.path.join(pkgdest, '__pycache__')
```

**Verification:**
```python
assert '__init__.py' in files
```

### Step 17: Assign pyc_files = os.listdir(...)

```python
pyc_files = os.listdir(pycache_dir)
```

**Verification:**
```python
assert f'__init__.{sys.implementation.cache_tag}.pyc' in pyc_files
```


## Complete Example

```python
# Workflow
sources = self.mkdtemp()
jaraco.path.build({'__init__.py': '# Pretend this is a package.', 'README.txt': 'Info about this package'}, sources)
destination = self.mkdtemp()
dist = Distribution({'packages': ['pkg'], 'package_dir': {'pkg': sources}})
dist.script_name = os.path.join(sources, 'setup.py')
dist.command_obj['build'] = support.DummyCommand(force=False, build_lib=destination)
dist.packages = ['pkg']
dist.package_data = {'pkg': ['README.txt']}
dist.package_dir = {'pkg': sources}
cmd = build_py(dist)
cmd.compile = True
cmd.ensure_finalized()
assert cmd.package_data == dist.package_data
cmd.run()
assert len(cmd.get_outputs()) == 3
pkgdest = os.path.join(destination, 'pkg')
files = os.listdir(pkgdest)
pycache_dir = os.path.join(pkgdest, '__pycache__')
assert '__init__.py' in files
assert 'README.txt' in files
if sys.dont_write_bytecode:
    assert not os.path.exists(pycache_dir)
else:
    pyc_files = os.listdir(pycache_dir)
    assert f'__init__.{sys.implementation.cache_tag}.pyc' in pyc_files
```

## Next Steps


---

*Source: test_build_py.py:16 | Complexity: Advanced | Last updated: 2026-06-02*