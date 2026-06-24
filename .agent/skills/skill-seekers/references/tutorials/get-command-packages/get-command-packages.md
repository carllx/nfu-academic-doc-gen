# How To: Get Command Packages

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get command packages

## Prerequisites

**Required Modules:**
- `email`
- `email.generator`
- `email.policy`
- `functools`
- `io`
- `os`
- `sys`
- `textwrap`
- `unittest.mock`
- `warnings`
- `distutils.cmd`
- `distutils.dist`
- `distutils.tests`
- `typing`
- `jaraco.path`
- `pytest`
- `distutils.tests.test_dist`


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert dist.command_packages is None
```

### Step 2: Assign cmds = dist.get_command_packages(...)

```python
cmds = dist.get_command_packages()
```

**Verification:**
```python
assert cmds == ['distutils.command']
```

### Step 3: Assign dist.command_packages = 'one,two'

```python
dist.command_packages = 'one,two'
```

**Verification:**
```python
assert dist.command_packages == ['distutils.command']
```

### Step 4: Assign cmds = dist.get_command_packages(...)

```python
cmds = dist.get_command_packages()
```

**Verification:**
```python
assert cmds == ['distutils.command', 'one', 'two']
```


## Complete Example

```python
# Workflow
dist = Distribution()
assert dist.command_packages is None
cmds = dist.get_command_packages()
assert cmds == ['distutils.command']
assert dist.command_packages == ['distutils.command']
dist.command_packages = 'one,two'
cmds = dist.get_command_packages()
assert cmds == ['distutils.command', 'one', 'two']
```

## Next Steps


---

*Source: test_dist.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*