# How To: Default Values

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Should have sensible defaults.

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

### Step 1: 'Should have sensible defaults.'

```python
'Should have sensible defaults.'
```

**Verification:**
```python
assert ctx.enhancement.enabled is True
```

### Step 2: Assign api_keys = value

```python
api_keys = ('ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'MOONSHOT_API_KEY', 'GOOGLE_API_KEY')
```

**Verification:**
```python
assert ctx.enhancement.level == 2
```

### Step 3: Assign saved = value

```python
saved = {k: os.environ.pop(k, None) for k in api_keys}
```

**Verification:**
```python
assert ctx.enhancement.mode == 'auto'
```

### Step 4: Assign ctx = ExecutionContext.initialize(...)

```python
ctx = ExecutionContext.initialize()
```

**Verification:**
```python
assert ctx.enhancement.timeout == 2700
```

### Step 5: Assign unknown = v

```python
os.environ[k] = v
```

**Verification:**
```python
assert ctx.output.name is None
```


## Complete Example

```python
# Workflow
'Should have sensible defaults.'
api_keys = ('ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'MOONSHOT_API_KEY', 'GOOGLE_API_KEY')
saved = {k: os.environ.pop(k, None) for k in api_keys}
try:
    ctx = ExecutionContext.initialize()
    assert ctx.enhancement.enabled is True
    assert ctx.enhancement.level == 2
    assert ctx.enhancement.mode == 'auto'
    assert ctx.enhancement.timeout == 2700
finally:
    for k, v in saved.items():
        if v is not None:
            os.environ[k] = v
assert ctx.output.name is None
assert ctx.output.dry_run is False
assert ctx.scraping.browser is False
assert ctx.scraping.workers == 1
assert ctx.scraping.languages == ['en']
assert ctx.analysis.depth == 'surface'
assert ctx.analysis.skip_patterns is False
assert ctx.rag.chunk_for_rag is False
assert ctx.rag.chunk_tokens == 512
```

## Next Steps


---

*Source: test_execution_context.py:478 | Complexity: Advanced | Last updated: 2026-06-02*