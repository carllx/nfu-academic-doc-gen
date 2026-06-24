# How To: Byte Compile

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test byte compile

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

### Step 1: Assign unknown = self.create_dist(...)

```python
project_dir, dist = self.create_dist(py_modules=['boiledeggs'])
```

**Verification:**
```python
assert sorted(found) == ['__pycache__', 'boiledeggs.py']
```

### Step 2: Call os.chdir()

```python
os.chdir(project_dir)
```

**Verification:**
```python
assert found == [f'boiledeggs.{sys.implementation.cache_tag}.pyc']
```

### Step 3: Call self.write_file()

```python
self.write_file('boiledeggs.py', 'import antigravity')
```

### Step 4: Assign cmd = build_py(...)

```python
cmd = build_py(dist)
```

### Step 5: Assign cmd.compile = True

```python
cmd.compile = True
```

### Step 6: Assign cmd.build_lib = 'here'

```python
cmd.build_lib = 'here'
```

### Step 7: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 8: Call cmd.run()

```python
cmd.run()
```

### Step 9: Assign found = os.listdir(...)

```python
found = os.listdir(cmd.build_lib)
```

**Verification:**
```python
assert sorted(found) == ['__pycache__', 'boiledeggs.py']
```

### Step 10: Assign found = os.listdir(...)

```python
found = os.listdir(os.path.join(cmd.build_lib, '__pycache__'))
```

**Verification:**
```python
assert found == [f'boiledeggs.{sys.implementation.cache_tag}.pyc']
```


## Complete Example

```python
# Workflow
project_dir, dist = self.create_dist(py_modules=['boiledeggs'])
os.chdir(project_dir)
self.write_file('boiledeggs.py', 'import antigravity')
cmd = build_py(dist)
cmd.compile = True
cmd.build_lib = 'here'
cmd.finalize_options()
cmd.run()
found = os.listdir(cmd.build_lib)
assert sorted(found) == ['__pycache__', 'boiledeggs.py']
found = os.listdir(os.path.join(cmd.build_lib, '__pycache__'))
assert found == [f'boiledeggs.{sys.implementation.cache_tag}.pyc']
```

## Next Steps


---

*Source: test_build_py.py:82 | Complexity: Advanced | Last updated: 2026-06-02*