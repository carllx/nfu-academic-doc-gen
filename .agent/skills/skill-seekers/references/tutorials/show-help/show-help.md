# How To: Show Help

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test show help

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: request, capsys
```

## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert output
```

### Step 2: Assign sys.argv = value

```python
sys.argv = []
```

### Step 3: Assign dist.help = True

```python
dist.help = True
```

### Step 4: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 5: Call dist.parse_command_line()

```python
dist.parse_command_line()
```

### Step 6: Assign output = value

```python
output = [line for line in capsys.readouterr().out.split('\n') if line.strip() != '']
```

**Verification:**
```python
assert output
```


## Complete Example

```python
# Setup
# Fixtures: request, capsys

# Workflow
dist = Distribution()
sys.argv = []
dist.help = True
dist.script_name = 'setup.py'
dist.parse_command_line()
output = [line for line in capsys.readouterr().out.split('\n') if line.strip() != '']
assert output
```

## Next Steps


---

*Source: test_dist.py:474 | Complexity: Intermediate | Last updated: 2026-06-02*