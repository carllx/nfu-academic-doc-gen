# How To: Simple Built

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test simple built

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `zipfile`
- `distutils.command.bdist_dumb`
- `distutils.core`
- `distutils.tests`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign tmp_dir = self.mkdtemp(...)

```python
tmp_dir = self.mkdtemp()
```

**Verification:**
```python
assert dist_created == [base]
```

### Step 2: Assign pkg_dir = os.path.join(...)

```python
pkg_dir = os.path.join(tmp_dir, 'foo')
```

**Verification:**
```python
assert contents == sorted(wanted)
```

### Step 3: Call os.mkdir()

```python
os.mkdir(pkg_dir)
```

### Step 4: Call self.write_file()

```python
self.write_file((pkg_dir, 'setup.py'), SETUP_PY)
```

### Step 5: Call self.write_file()

```python
self.write_file((pkg_dir, 'foo.py'), '#')
```

### Step 6: Call self.write_file()

```python
self.write_file((pkg_dir, 'MANIFEST.in'), 'include foo.py')
```

### Step 7: Call self.write_file()

```python
self.write_file((pkg_dir, 'README'), '')
```

### Step 8: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'foo', 'version': '0.1', 'py_modules': ['foo'], 'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx'})
```

### Step 9: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 10: Call os.chdir()

```python
os.chdir(pkg_dir)
```

### Step 11: Assign sys.argv = value

```python
sys.argv = ['setup.py']
```

### Step 12: Assign cmd = bdist_dumb(...)

```python
cmd = bdist_dumb(dist)
```

### Step 13: Assign cmd.format = 'zip'

```python
cmd.format = 'zip'
```

### Step 14: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 15: Call cmd.run()

```python
cmd.run()
```

### Step 16: Assign dist_created = os.listdir(...)

```python
dist_created = os.listdir(os.path.join(pkg_dir, 'dist'))
```

### Step 17: Assign base = value

```python
base = f'{dist.get_fullname()}.{cmd.plat_name}.zip'
```

**Verification:**
```python
assert dist_created == [base]
```

### Step 18: Assign fp = zipfile.ZipFile(...)

```python
fp = zipfile.ZipFile(os.path.join('dist', base))
```

### Step 19: Assign contents = sorted(...)

```python
contents = sorted(filter(None, map(os.path.basename, contents)))
```

### Step 20: Assign wanted = value

```python
wanted = ['foo-0.1-py{}.{}.egg-info'.format(*sys.version_info[:2]), 'foo.py']
```

**Verification:**
```python
assert contents == sorted(wanted)
```

### Step 21: Assign contents = fp.namelist(...)

```python
contents = fp.namelist()
```

### Step 22: Call fp.close()

```python
fp.close()
```

### Step 23: Call wanted.append()

```python
wanted.append(f'foo.{sys.implementation.cache_tag}.pyc')
```


## Complete Example

```python
# Workflow
tmp_dir = self.mkdtemp()
pkg_dir = os.path.join(tmp_dir, 'foo')
os.mkdir(pkg_dir)
self.write_file((pkg_dir, 'setup.py'), SETUP_PY)
self.write_file((pkg_dir, 'foo.py'), '#')
self.write_file((pkg_dir, 'MANIFEST.in'), 'include foo.py')
self.write_file((pkg_dir, 'README'), '')
dist = Distribution({'name': 'foo', 'version': '0.1', 'py_modules': ['foo'], 'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx'})
dist.script_name = 'setup.py'
os.chdir(pkg_dir)
sys.argv = ['setup.py']
cmd = bdist_dumb(dist)
cmd.format = 'zip'
cmd.ensure_finalized()
cmd.run()
dist_created = os.listdir(os.path.join(pkg_dir, 'dist'))
base = f'{dist.get_fullname()}.{cmd.plat_name}.zip'
assert dist_created == [base]
fp = zipfile.ZipFile(os.path.join('dist', base))
try:
    contents = fp.namelist()
finally:
    fp.close()
contents = sorted(filter(None, map(os.path.basename, contents)))
wanted = ['foo-0.1-py{}.{}.egg-info'.format(*sys.version_info[:2]), 'foo.py']
if not sys.dont_write_bytecode:
    wanted.append(f'foo.{sys.implementation.cache_tag}.pyc')
assert contents == sorted(wanted)
```

## Next Steps


---

*Source: test_bdist_dumb.py:30 | Complexity: Advanced | Last updated: 2026-06-02*