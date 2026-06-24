# How To: Cli Overrides Config

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: CLI args should override config file values.

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

### Step 1: 'CLI args should override config file values.'

```python
'CLI args should override config file values.'
```

**Verification:**
```python
assert ctx.output.name == 'cli-name'
```

### Step 2: Assign config = value

```python
config = {'name': 'config-name', 'sources': []}
```

### Step 3: Call json.dump()

```python
json.dump(config, f)
```

### Step 4: Assign config_path = value

```python
config_path = f.name
```

### Step 5: Assign args = argparse.Namespace(...)

```python
args = argparse.Namespace(name='cli-name')
```

### Step 6: Assign ctx = ExecutionContext.initialize(...)

```python
ctx = ExecutionContext.initialize(args=args, config_path=config_path)
```

**Verification:**
```python
assert ctx.output.name == 'cli-name'
```

### Step 7: Call os.unlink()

```python
os.unlink(config_path)
```


## Complete Example

```python
# Workflow
'CLI args should override config file values.'
config = {'name': 'config-name', 'sources': []}
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump(config, f)
    config_path = f.name
try:
    args = argparse.Namespace(name='cli-name')
    ctx = ExecutionContext.initialize(args=args, config_path=config_path)
    assert ctx.output.name == 'cli-name'
finally:
    os.unlink(config_path)
```

## Next Steps


---

*Source: test_execution_context.py:321 | Complexity: Advanced | Last updated: 2026-06-02*