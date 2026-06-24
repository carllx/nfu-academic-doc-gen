# How To: Clean

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clean

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `distutils._log`
- `distutils.command.config`
- `distutils.tests`
- `more_itertools`
- `path`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign tmp_dir = self.mkdtemp(...)

```python
tmp_dir = self.mkdtemp()
```

**Verification:**
```python
assert os.path.exists(f)
```

### Step 2: Assign f1 = os.path.join(...)

```python
f1 = os.path.join(tmp_dir, 'one')
```

**Verification:**
```python
assert not os.path.exists(f)
```

### Step 3: Assign f2 = os.path.join(...)

```python
f2 = os.path.join(tmp_dir, 'two')
```

### Step 4: Call self.write_file()

```python
self.write_file(f1, 'xxx')
```

### Step 5: Call self.write_file()

```python
self.write_file(f2, 'xxx')
```

### Step 6: Assign unknown = self.create_dist(...)

```python
pkg_dir, dist = self.create_dist()
```

### Step 7: Assign cmd = config(...)

```python
cmd = config(dist)
```

### Step 8: Call cmd._clean()

```python
cmd._clean(f1, f2)
```

**Verification:**
```python
assert os.path.exists(f)
```


## Complete Example

```python
# Workflow
tmp_dir = self.mkdtemp()
f1 = os.path.join(tmp_dir, 'one')
f2 = os.path.join(tmp_dir, 'two')
self.write_file(f1, 'xxx')
self.write_file(f2, 'xxx')
for f in (f1, f2):
    assert os.path.exists(f)
pkg_dir, dist = self.create_dist()
cmd = config(dist)
cmd._clean(f1, f2)
for f in (f1, f2):
    assert not os.path.exists(f)
```

## Next Steps


---

*Source: test_config_cmd.py:70 | Complexity: Advanced | Last updated: 2026-06-02*