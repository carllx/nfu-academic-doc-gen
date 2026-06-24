# How To: Get Source Files

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get source files

## Prerequisites

**Required Modules:**
- `os`
- `distutils.command.build_clib`
- `distutils.errors`
- `distutils.tests`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign unknown = self.create_dist(...)

```python
pkg_dir, dist = self.create_dist()
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b']
```

### Step 2: Assign cmd = build_clib(...)

```python
cmd = build_clib(dist)
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b']
```

### Step 3: Assign cmd.libraries = value

```python
cmd.libraries = [('name', {})]
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b', 'c', 'd']
```

### Step 4: Assign cmd.libraries = value

```python
cmd.libraries = [('name', {'sources': 1})]
```

### Step 5: Assign cmd.libraries = value

```python
cmd.libraries = [('name', {'sources': ['a', 'b']})]
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b']
```

### Step 6: Assign cmd.libraries = value

```python
cmd.libraries = [('name', {'sources': ('a', 'b')})]
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b']
```

### Step 7: Assign cmd.libraries = value

```python
cmd.libraries = [('name', {'sources': ('a', 'b')}), ('name2', {'sources': ['c', 'd']})]
```

**Verification:**
```python
assert cmd.get_source_files() == ['a', 'b', 'c', 'd']
```

### Step 8: Call cmd.get_source_files()

```python
cmd.get_source_files()
```

### Step 9: Call cmd.get_source_files()

```python
cmd.get_source_files()
```


## Complete Example

```python
# Workflow
pkg_dir, dist = self.create_dist()
cmd = build_clib(dist)
cmd.libraries = [('name', {})]
with pytest.raises(DistutilsSetupError):
    cmd.get_source_files()
cmd.libraries = [('name', {'sources': 1})]
with pytest.raises(DistutilsSetupError):
    cmd.get_source_files()
cmd.libraries = [('name', {'sources': ['a', 'b']})]
assert cmd.get_source_files() == ['a', 'b']
cmd.libraries = [('name', {'sources': ('a', 'b')})]
assert cmd.get_source_files() == ['a', 'b']
cmd.libraries = [('name', {'sources': ('a', 'b')}), ('name2', {'sources': ['c', 'd']})]
assert cmd.get_source_files() == ['a', 'b', 'c', 'd']
```

## Next Steps


---

*Source: test_build_clib.py:45 | Complexity: Advanced | Last updated: 2026-06-02*