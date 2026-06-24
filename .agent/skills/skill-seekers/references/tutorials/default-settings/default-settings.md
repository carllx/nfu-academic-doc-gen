# How To: Default Settings

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default settings

## Prerequisites

**Required Modules:**
- `os`
- `distutils.command.install_scripts`
- `distutils.core`
- `distutils.tests`


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert not cmd.force
```

### Step 2: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['build'] = support.DummyCommand(build_scripts='/foo/bar')
```

**Verification:**
```python
assert not cmd.skip_build
```

### Step 3: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['install'] = support.DummyCommand(install_scripts='/splat/funk', force=True, skip_build=True)
```

**Verification:**
```python
assert cmd.build_dir is None
```

### Step 4: Assign cmd = install_scripts(...)

```python
cmd = install_scripts(dist)
```

**Verification:**
```python
assert cmd.install_dir is None
```

### Step 5: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

**Verification:**
```python
assert cmd.force
```


## Complete Example

```python
# Workflow
dist = Distribution()
dist.command_obj['build'] = support.DummyCommand(build_scripts='/foo/bar')
dist.command_obj['install'] = support.DummyCommand(install_scripts='/splat/funk', force=True, skip_build=True)
cmd = install_scripts(dist)
assert not cmd.force
assert not cmd.skip_build
assert cmd.build_dir is None
assert cmd.install_dir is None
cmd.finalize_options()
assert cmd.force
assert cmd.skip_build
assert cmd.build_dir == '/foo/bar'
assert cmd.install_dir == '/splat/funk'
```

## Next Steps


---

*Source: test_install_scripts.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*