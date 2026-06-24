# How To: Join Matches Subprocess

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that join produces strings understood by subprocess

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `subprocess`
- `json`
- `sys`
- `numpy.distutils`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: Parser, runner, argv
```

## Step-by-Step Guide

### Step 1: '\n    Test that join produces strings understood by subprocess\n    '

```python
'\n    Test that join produces strings understood by subprocess\n    '
```

**Verification:**
```python
assert json.loads(json_out) == argv
```

### Step 2: Assign cmd = value

```python
cmd = [sys.executable, '-c', 'import json, sys; print(json.dumps(sys.argv[1:]))']
```

### Step 3: Assign joined = Parser.join(...)

```python
joined = Parser.join(cmd + argv)
```

### Step 4: Assign json_out = runner.decode(...)

```python
json_out = runner(joined).decode()
```

**Verification:**
```python
assert json.loads(json_out) == argv
```


## Complete Example

```python
# Setup
# Fixtures: Parser, runner, argv

# Workflow
'\n    Test that join produces strings understood by subprocess\n    '
cmd = [sys.executable, '-c', 'import json, sys; print(json.dumps(sys.argv[1:]))']
joined = Parser.join(cmd + argv)
json_out = runner(joined).decode()
assert json.loads(json_out) == argv
```

## Next Steps


---

*Source: test_shell_utils.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*