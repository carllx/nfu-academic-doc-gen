# How To: Pbr Integration

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Ensure pbr packages install.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `subprocess`
- `pytest`

**Setup Required:**
```python
# Fixtures: pbr_package, venv
```

## Step-by-Step Guide

### Step 1: 'Ensure pbr packages install.'

```python
'Ensure pbr packages install.'
```

**Verification:**
```python
assert 'Hello world!' in out
```

### Step 2: Assign cmd = value

```python
cmd = ['python', '-m', 'pip', '-v', 'install', '--no-build-isolation', pbr_package]
```

### Step 3: Call venv.run()

```python
venv.run(cmd, stderr=subprocess.STDOUT)
```

### Step 4: Assign out = venv.run(...)

```python
out = venv.run(['python', '-c', 'import mypkg.hello'])
```

**Verification:**
```python
assert 'Hello world!' in out
```


## Complete Example

```python
# Setup
# Fixtures: pbr_package, venv

# Workflow
'Ensure pbr packages install.'
cmd = ['python', '-m', 'pip', '-v', 'install', '--no-build-isolation', pbr_package]
venv.run(cmd, stderr=subprocess.STDOUT)
out = venv.run(['python', '-c', 'import mypkg.hello'])
assert 'Hello world!' in out
```

## Next Steps


---

*Source: test_pbr.py:7 | Complexity: Intermediate | Last updated: 2026-06-02*