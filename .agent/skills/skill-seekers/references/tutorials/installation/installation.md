# How To: Installation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test installation

## Prerequisites

**Required Modules:**
- `os`
- `distutils.command.install_scripts`
- `distutils.core`
- `distutils.tests`


## Step-by-Step Guide

### Step 1: Assign source = self.mkdtemp(...)

```python
source = self.mkdtemp()
```

**Verification:**
```python
assert name in installed
```

### Step 2: Assign expected = test_build_scripts.TestBuildScripts.write_sample_scripts(...)

```python
expected = test_build_scripts.TestBuildScripts.write_sample_scripts(source)
```

### Step 3: Assign target = self.mkdtemp(...)

```python
target = self.mkdtemp()
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 5: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['build'] = support.DummyCommand(build_scripts=source)
```

### Step 6: Assign unknown = support.DummyCommand(...)

```python
dist.command_obj['install'] = support.DummyCommand(install_scripts=target, force=True, skip_build=True)
```

### Step 7: Assign cmd = install_scripts(...)

```python
cmd = install_scripts(dist)
```

### Step 8: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 9: Call cmd.run()

```python
cmd.run()
```

### Step 10: Assign installed = os.listdir(...)

```python
installed = os.listdir(target)
```

**Verification:**
```python
assert name in installed
```


## Complete Example

```python
# Workflow
source = self.mkdtemp()
expected = test_build_scripts.TestBuildScripts.write_sample_scripts(source)
target = self.mkdtemp()
dist = Distribution()
dist.command_obj['build'] = support.DummyCommand(build_scripts=source)
dist.command_obj['install'] = support.DummyCommand(install_scripts=target, force=True, skip_build=True)
cmd = install_scripts(dist)
cmd.finalize_options()
cmd.run()
installed = os.listdir(target)
for name in expected:
    assert name in installed
```

## Next Steps


---

*Source: test_install_scripts.py:33 | Complexity: Advanced | Last updated: 2026-06-02*