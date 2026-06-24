# How To: Formats

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test formats

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
assert cmd.formats == ['gztar']
```

### Step 2: Assign cmd = bdist(...)

```python
cmd = bdist(dist)
```

**Verification:**
```python
assert found == formats
```

### Step 3: Assign cmd.formats = value

```python
cmd.formats = ['gztar']
```

### Step 4: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

**Verification:**
```python
assert cmd.formats == ['gztar']
```

### Step 5: Assign formats = value

```python
formats = ['bztar', 'gztar', 'rpm', 'tar', 'xztar', 'zip', 'ztar']
```

### Step 6: Assign found = sorted(...)

```python
found = sorted(cmd.format_commands)
```

**Verification:**
```python
assert found == formats
```


## Complete Example

```python
# Workflow
dist = self.create_dist()[1]
cmd = bdist(dist)
cmd.formats = ['gztar']
cmd.ensure_finalized()
assert cmd.formats == ['gztar']
formats = ['bztar', 'gztar', 'rpm', 'tar', 'xztar', 'zip', 'ztar']
found = sorted(cmd.format_commands)
assert found == formats
```

## Next Steps


---

*Source: test_bdist.py:8 | Complexity: Intermediate | Last updated: 2026-06-02*