# How To: Setup Runs Successfully

**Difficulty**: Intermediate
**Estimated Time**: 5 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: run_setup(interactive=True) should return 0 on success.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `subprocess`
- `sys`
- `tempfile`
- `unittest`
- `unittest.mock`
- `skill_seekers.cli.video_setup`
- `skill_seekers.cli.video_visual`
- `skill_seekers.cli.video_visual`
- `skill_seekers.cli.video_models`
- `skill_seekers.cli.video_visual`
- `skill_seekers.cli.video_models`
- `skill_seekers.cli.arguments.video`
- `argparse`
- `skill_seekers.cli.arguments.video`
- `argparse`
- `skill_seekers.cli.arguments.video`
- `skill_seekers.cli.video_setup`

**Setup Required:**
```python
# Fixtures: mock_setup
```

## Step-by-Step Guide

### Step 1: 'run_setup(interactive=True) should return 0 on success.'

```python
'run_setup(interactive=True) should return 0 on success.'
```

**Verification:**
```python
assert rc == 0
```

### Step 2: Assign rc = run_setup(...)

```python
rc = run_setup(interactive=True)
```

**Verification:**
```python
assert rc == 0
```

### Step 3: Call mock_setup.assert_called_once_with()

```python
mock_setup.assert_called_once_with(interactive=True)
```


## Complete Example

```python
# Setup
# Fixtures: mock_setup

# Workflow
'run_setup(interactive=True) should return 0 on success.'
from skill_seekers.cli.video_setup import run_setup
rc = run_setup(interactive=True)
assert rc == 0
mock_setup.assert_called_once_with(interactive=True)
```

## Next Steps


---

*Source: test_video_setup.py:717 | Complexity: Intermediate | Last updated: 2026-06-02*