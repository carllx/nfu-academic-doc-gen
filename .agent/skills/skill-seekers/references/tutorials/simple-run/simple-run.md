# How To: Simple Run

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple run

## Prerequisites

**Required Modules:**
- `os`
- `distutils.command.clean`
- `distutils.tests`


## Step-by-Step Guide

### Step 1: Assign unknown = self.create_dist(...)

```python
pkg_dir, dist = self.create_dist()
```

**Verification:**
```python
assert not os.path.exists(path), f'{path} was not removed'
```

### Step 2: Assign cmd = clean(...)

```python
cmd = clean(dist)
```

### Step 3: Assign dirs = value

```python
dirs = [(d, os.path.join(pkg_dir, d)) for d in ('build_temp', 'build_lib', 'bdist_base', 'build_scripts', 'build_base')]
```

### Step 4: Assign cmd.all = 1

```python
cmd.all = 1
```

### Step 5: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 6: Call cmd.run()

```python
cmd.run()
```

### Step 7: Assign cmd.all = 1

```python
cmd.all = 1
```

### Step 8: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 9: Call cmd.run()

```python
cmd.run()
```

### Step 10: Call os.mkdir()

```python
os.mkdir(path)
```

### Step 11: Call setattr()

```python
setattr(cmd, name, path)
```

**Verification:**
```python
assert not os.path.exists(path), f'{path} was not removed'
```

### Step 12: Call self.write_file()

```python
self.write_file(os.path.join(path, f))
```


## Complete Example

```python
# Workflow
pkg_dir, dist = self.create_dist()
cmd = clean(dist)
dirs = [(d, os.path.join(pkg_dir, d)) for d in ('build_temp', 'build_lib', 'bdist_base', 'build_scripts', 'build_base')]
for name, path in dirs:
    os.mkdir(path)
    setattr(cmd, name, path)
    if name == 'build_base':
        continue
    for f in ('one', 'two', 'three'):
        self.write_file(os.path.join(path, f))
cmd.all = 1
cmd.ensure_finalized()
cmd.run()
for _name, path in dirs:
    assert not os.path.exists(path), f'{path} was not removed'
cmd.all = 1
cmd.ensure_finalized()
cmd.run()
```

## Next Steps


---

*Source: test_clean.py:9 | Complexity: Advanced | Last updated: 2026-06-02*