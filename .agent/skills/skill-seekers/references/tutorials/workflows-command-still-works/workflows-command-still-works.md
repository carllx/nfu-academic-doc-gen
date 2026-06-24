# How To: Workflows Command Still Works

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: The workflows subcommand is accessible via the main CLI.

## Prerequisites

**Required Modules:**
- `pytest`
- `subprocess`
- `skill_seekers.cli.source_detector`
- `subprocess`
- `subprocess`
- `subprocess`
- `subprocess`
- `json`
- `skill_seekers.cli.skill_converter`
- `skill_seekers.cli.skill_converter`
- `skill_seekers.cli.skill_converter`
- `skill_seekers.cli.skill_converter`
- `skill_seekers.cli.execution_context`
- `skill_seekers.cli.execution_context`
- `argparse`
- `subprocess`
- `subprocess`
- `subprocess`
- `subprocess`


## Step-by-Step Guide

### Step 1: 'The workflows subcommand is accessible via the main CLI.'

```python
'The workflows subcommand is accessible via the main CLI.'
```

**Verification:**
```python
assert result.returncode == 0
```

### Step 2: Assign result = subprocess.run(...)

```python
result = subprocess.run(['skill-seekers', 'workflows', '--help'], capture_output=True, text=True, timeout=10)
```

**Verification:**
```python
assert result.returncode == 0
```


## Complete Example

```python
# Workflow
'The workflows subcommand is accessible via the main CLI.'
import subprocess
result = subprocess.run(['skill-seekers', 'workflows', '--help'], capture_output=True, text=True, timeout=10)
assert result.returncode == 0
```

## Next Steps


---

*Source: test_create_integration_basic.py:205 | Complexity: Beginner | Last updated: 2026-06-02*