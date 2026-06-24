# How To: Variable Too Long

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Test that an error is thrown if the environment variables are too long
to be processed. Current limit is 1024, but this may change later.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `pathlib`
- `platform`
- `re`
- `subprocess`
- `sys`
- `pytest`
- `numpy._core._multiarray_umath`
- `textwrap`
- `subprocess`

**Setup Required:**
```python
# Fixtures: action
```

## Step-by-Step Guide

### Step 1: '\n        Test that an error is thrown if the environment variables are too long\n        to be processed. Current limit is 1024, but this may change later.\n        '

```python
'\n        Test that an error is thrown if the environment variables are too long\n        to be processed. Current limit is 1024, but this may change later.\n        '
```

### Step 2: Assign MAX_VAR_LENGTH = 1024

```python
MAX_VAR_LENGTH = 1024
```

### Step 3: Assign unknown = value

```python
self.env[f'NPY_{action}_CPU_FEATURES'] = 't' * MAX_VAR_LENGTH
```

### Step 4: Assign msg = value

```python
msg = f"Length of environment variable 'NPY_{action}_CPU_FEATURES' is {MAX_VAR_LENGTH + 1}, only {MAX_VAR_LENGTH} accepted"
```

### Step 5: Assign err_type = 'RuntimeError'

```python
err_type = 'RuntimeError'
```

### Step 6: Call self._expect_error()

```python
self._expect_error(msg, err_type)
```


## Complete Example

```python
# Setup
# Fixtures: action

# Workflow
'\n        Test that an error is thrown if the environment variables are too long\n        to be processed. Current limit is 1024, but this may change later.\n        '
MAX_VAR_LENGTH = 1024
self.env[f'NPY_{action}_CPU_FEATURES'] = 't' * MAX_VAR_LENGTH
msg = f"Length of environment variable 'NPY_{action}_CPU_FEATURES' is {MAX_VAR_LENGTH + 1}, only {MAX_VAR_LENGTH} accepted"
err_type = 'RuntimeError'
self._expect_error(msg, err_type)
```

## Next Steps


---

*Source: test_cpu_features.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*