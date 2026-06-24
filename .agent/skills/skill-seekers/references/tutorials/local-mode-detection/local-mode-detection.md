# How To: Local Mode Detection

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Should default to local/auto mode without API key.

## Prerequisites

**Required Modules:**
- `argparse`
- `json`
- `os`
- `tempfile`
- `pytest`
- `skill_seekers.cli.execution_context`
- `pydantic`


## Step-by-Step Guide

### Step 1: 'Should default to local/auto mode without API key.'

```python
'Should default to local/auto mode without API key.'
```

**Verification:**
```python
assert ctx.enhancement.mode in ('local', 'auto')
```

### Step 2: Assign api_keys = value

```python
api_keys = ['ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'MOONSHOT_API_KEY', 'GOOGLE_API_KEY']
```

### Step 3: Assign saved = value

```python
saved = {k: os.environ.pop(k, None) for k in api_keys}
```

### Step 4: Assign args = argparse.Namespace(...)

```python
args = argparse.Namespace(name='test')
```

### Step 5: Assign ctx = ExecutionContext.initialize(...)

```python
ctx = ExecutionContext.initialize(args=args)
```

**Verification:**
```python
assert ctx.enhancement.mode in ('local', 'auto')
```

### Step 6: Assign unknown = v

```python
os.environ[k] = v
```


## Complete Example

```python
# Workflow
'Should default to local/auto mode without API key.'
api_keys = ['ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'MOONSHOT_API_KEY', 'GOOGLE_API_KEY']
saved = {k: os.environ.pop(k, None) for k in api_keys}
try:
    args = argparse.Namespace(name='test')
    ctx = ExecutionContext.initialize(args=args)
    assert ctx.enhancement.mode in ('local', 'auto')
finally:
    for k, v in saved.items():
        if v is not None:
            os.environ[k] = v
```

## Next Steps


---

*Source: test_execution_context.py:186 | Complexity: Advanced | Last updated: 2026-06-02*