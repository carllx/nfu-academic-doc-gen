# How To: Quiet

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test quiet

## Prerequisites

**Required Modules:**
- `os`
- `shutil`
- `sys`
- `distutils.command.bdist_rpm`
- `distutils.core`
- `distutils.tests`
- `pytest`
- `test.support`


## Step-by-Step Guide

### Step 1: Assign tmp_dir = self.mkdtemp(...)

```python
tmp_dir = self.mkdtemp()
```

**Verification:**
```python
assert 'foo-0.1-1.noarch.rpm' in dist_created
```

### Step 2: Assign unknown = tmp_dir

```python
os.environ['HOME'] = tmp_dir
```

**Verification:**
```python
assert ('bdist_rpm', 'any', 'dist/foo-0.1-1.src.rpm') in dist.dist_files
```

### Step 3: Assign pkg_dir = os.path.join(...)

```python
pkg_dir = os.path.join(tmp_dir, 'foo')
```

**Verification:**
```python
assert ('bdist_rpm', 'any', 'dist/foo-0.1-1.noarch.rpm') in dist.dist_files
```

### Step 4: Call os.mkdir()

```python
os.mkdir(pkg_dir)
```

### Step 5: Call self.write_file()

```python
self.write_file((pkg_dir, 'setup.py'), SETUP_PY)
```

### Step 6: Call self.write_file()

```python
self.write_file((pkg_dir, 'foo.py'), '#')
```

### Step 7: Call self.write_file()

```python
self.write_file((pkg_dir, 'MANIFEST.in'), 'include foo.py')
```

### Step 8: Call self.write_file()

```python
self.write_file((pkg_dir, 'README'), '')
```

### Step 9: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'foo', 'version': '0.1', 'py_modules': ['foo'], 'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx'})
```

### Step 10: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 11: Call os.chdir()

```python
os.chdir(pkg_dir)
```

### Step 12: Assign sys.argv = value

```python
sys.argv = ['setup.py']
```

### Step 13: Assign cmd = bdist_rpm(...)

```python
cmd = bdist_rpm(dist)
```

### Step 14: Assign cmd.fix_python = True

```python
cmd.fix_python = True
```

### Step 15: Assign cmd.quiet = True

```python
cmd.quiet = True
```

### Step 16: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 17: Call cmd.run()

```python
cmd.run()
```

### Step 18: Assign dist_created = os.listdir(...)

```python
dist_created = os.listdir(os.path.join(pkg_dir, 'dist'))
```

**Verification:**
```python
assert 'foo-0.1-1.noarch.rpm' in dist_created
```


## Complete Example

```python
# Workflow
tmp_dir = self.mkdtemp()
os.environ['HOME'] = tmp_dir
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
cmd = bdist_rpm(dist)
cmd.fix_python = True
cmd.quiet = True
cmd.ensure_finalized()
cmd.run()
dist_created = os.listdir(os.path.join(pkg_dir, 'dist'))
assert 'foo-0.1-1.noarch.rpm' in dist_created
assert ('bdist_rpm', 'any', 'dist/foo-0.1-1.src.rpm') in dist.dist_files
assert ('bdist_rpm', 'any', 'dist/foo-0.1-1.noarch.rpm') in dist.dist_files
```

## Next Steps


---

*Source: test_bdist_rpm.py:47 | Complexity: Advanced | Last updated: 2026-06-02*