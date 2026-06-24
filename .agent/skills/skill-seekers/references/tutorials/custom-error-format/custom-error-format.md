# How To: Custom Error Format

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test custom error format

## Prerequisites

**Required Modules:**
- `contextlib`
- `importlib`
- `io`
- `json`
- `pathlib`
- `textwrap`
- `unittest`
- `json`
- `os`
- `subprocess`
- `sys`
- `tempfile`
- `warnings`
- `jsonschema`
- `jsonschema.exceptions`
- `jsonschema.validators`
- `jsonschema`


## Step-by-Step Guide

### Step 1: Assign first_instance = 12

```python
first_instance = 12
```

### Step 2: Assign first_errors = value

```python
first_errors = [ValidationError('An error', instance=first_instance), ValidationError('Another error', instance=first_instance)]
```

### Step 3: Assign second_instance = 'foo'

```python
second_instance = 'foo'
```

### Step 4: Assign second_errors = value

```python
second_errors = [ValidationError('BOOM', instance=second_instance)]
```

### Step 5: Call self.assertOutputs()

```python
self.assertOutputs(files=dict(some_schema='{"does not": "matter since it is stubbed"}', some_first_instance=json.dumps(first_instance), some_second_instance=json.dumps(second_instance)), validator=fake_validator(first_errors, second_errors), argv=['--error-format', ':{error.message}._-_.{error.instance}:', '-i', 'some_first_instance', '-i', 'some_second_instance', 'some_schema'], exit_code=1, stderr=':An error._-_.12::Another error._-_.12::BOOM._-_.foo:')
```


## Complete Example

```python
# Workflow
first_instance = 12
first_errors = [ValidationError('An error', instance=first_instance), ValidationError('Another error', instance=first_instance)]
second_instance = 'foo'
second_errors = [ValidationError('BOOM', instance=second_instance)]
self.assertOutputs(files=dict(some_schema='{"does not": "matter since it is stubbed"}', some_first_instance=json.dumps(first_instance), some_second_instance=json.dumps(second_instance)), validator=fake_validator(first_errors, second_errors), argv=['--error-format', ':{error.message}._-_.{error.instance}:', '-i', 'some_first_instance', '-i', 'some_second_instance', 'some_schema'], exit_code=1, stderr=':An error._-_.12::Another error._-_.12::BOOM._-_.foo:')
```

## Next Steps


---

*Source: test_cli.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*