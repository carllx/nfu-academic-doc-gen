# How To: Byte Compile Optimized

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test byte compile optimized

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
assert sorted(found) == [expect]
```

### Step 3: Call self.write_file()

```python
self.write_file('boiledeggs.py', 'import antigravity')
```

### Step 4: Assign cmd = build_py(...)

```python
cmd = build_py(dist)
```

### Step 5: Assign cmd.compile = False

```python
cmd.compile = False
```

### Step 6: Assign cmd.optimize = 1

```python
cmd.optimize = 1
```

### Step 7: Assign cmd.build_lib = 'here'

```python
cmd.build_lib = 'here'
```

### Step 8: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 9: Call cmd.run()

```python
cmd.run()
```

### Step 10: Assign found = os.listdir(...)

```python
found = os.listdir(cmd.build_lib)
```

**Verification:**
```python
assert sorted(found) == ['__pycache__', 'boiledeggs.py']
```

### Step 11: Assign found = os.listdir(...)

```python
found = os.listdir(os.path.join(cmd.build_lib, '__pycache__'))
```

### Step 12: Assign expect = value

```python
expect = f'boiledeggs.{sys.implementation.cache_tag}.opt-1.pyc'
```

**Verification:**
```python
assert sorted(found) == [expect]
```


## Complete Example

```python
# Workflow
project_dir, dist = self.create_dist(py_modules=['boiledeggs'])
os.chdir(project_dir)
self.write_file('boiledeggs.py', 'import antigravity')
cmd = build_py(dist)
cmd.compile = False
cmd.optimize = 1
cmd.build_lib = 'here'
cmd.finalize_options()
cmd.run()
found = os.listdir(cmd.build_lib)
assert sorted(found) == ['__pycache__', 'boiledeggs.py']
found = os.listdir(os.path.join(cmd.build_lib, '__pycache__'))
expect = f'boiledeggs.{sys.implementation.cache_tag}.opt-1.pyc'
assert sorted(found) == [expect]
```

## Next Steps


---

*Source: test_build_py.py:98 | Complexity: Advanced | Last updated: 2026-06-02*