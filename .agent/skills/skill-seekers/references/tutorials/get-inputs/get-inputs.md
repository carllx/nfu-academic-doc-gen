# How To: Get Inputs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get inputs

## Prerequisites

**Required Modules:**
- `importlib.util`
- `os`
- `sys`
- `distutils.command.install_lib`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign unknown = self.create_dist(...)

```python
project_dir, dist = self.create_dist()
```

**Verification:**
```python
assert len(inputs) == 2, inputs
```

### Step 2: Call os.chdir()

```python
os.chdir(project_dir)
```

### Step 3: Call os.mkdir()

```python
os.mkdir('spam')
```

### Step 4: Assign cmd = install_lib(...)

```python
cmd = install_lib(dist)
```

### Step 5: Assign cmd.compile, cmd.optimize = 1

```python
cmd.compile = cmd.optimize = 1
```

### Step 6: Assign cmd.install_dir = self.mkdtemp(...)

```python
cmd.install_dir = self.mkdtemp()
```

### Step 7: Assign f = os.path.join(...)

```python
f = os.path.join(project_dir, 'spam', '__init__.py')
```

### Step 8: Call self.write_file()

```python
self.write_file(f, '# python package')
```

### Step 9: Assign cmd.distribution.ext_modules = value

```python
cmd.distribution.ext_modules = [Extension('foo', ['xxx'])]
```

### Step 10: Assign cmd.distribution.packages = value

```python
cmd.distribution.packages = ['spam']
```

### Step 11: Assign cmd.distribution.script_name = 'setup.py'

```python
cmd.distribution.script_name = 'setup.py'
```

### Step 12: Assign inputs = cmd.get_inputs(...)

```python
inputs = cmd.get_inputs()
```

**Verification:**
```python
assert len(inputs) == 2, inputs
```


## Complete Example

```python
# Workflow
project_dir, dist = self.create_dist()
os.chdir(project_dir)
os.mkdir('spam')
cmd = install_lib(dist)
cmd.compile = cmd.optimize = 1
cmd.install_dir = self.mkdtemp()
f = os.path.join(project_dir, 'spam', '__init__.py')
self.write_file(f, '# python package')
cmd.distribution.ext_modules = [Extension('foo', ['xxx'])]
cmd.distribution.packages = ['spam']
cmd.distribution.script_name = 'setup.py'
inputs = cmd.get_inputs()
assert len(inputs) == 2, inputs
```

## Next Steps


---

*Source: test_install_lib.py:76 | Complexity: Advanced | Last updated: 2026-06-02*