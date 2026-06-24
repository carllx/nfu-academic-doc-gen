# How To: Skip Build

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip build

## Prerequisites

**Required Modules:**
- `distutils.command.bdist`
- `distutils.tests`


## Step-by-Step Guide

### Step 1: Assign dist = value

```python
dist = self.create_dist()[1]
```

**Verification:**
```python
assert subcmd.skip_build, f'{name} should take --skip-build from bdist'
```

### Step 2: Assign cmd = bdist(...)

```python
cmd = bdist(dist)
```

### Step 3: Assign cmd.skip_build = True

```python
cmd.skip_build = True
```

### Step 4: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 5: Assign unknown = cmd

```python
dist.command_obj['bdist'] = cmd
```

### Step 6: Assign names = value

```python
names = ['bdist_dumb']
```

### Step 7: Assign subcmd = cmd.get_finalized_command(...)

```python
subcmd = cmd.get_finalized_command(name)
```

**Verification:**
```python
assert subcmd.skip_build, f'{name} should take --skip-build from bdist'
```


## Complete Example

```python
# Workflow
dist = self.create_dist()[1]
cmd = bdist(dist)
cmd.skip_build = True
cmd.ensure_finalized()
dist.command_obj['bdist'] = cmd
names = ['bdist_dumb']
for name in names:
    subcmd = cmd.get_finalized_command(name)
    if getattr(subcmd, '_unsupported', False):
        continue
    assert subcmd.skip_build, f'{name} should take --skip-build from bdist'
```

## Next Steps


---

*Source: test_bdist.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*