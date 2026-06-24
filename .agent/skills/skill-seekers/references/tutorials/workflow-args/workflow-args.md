# How To: Workflow Args

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Should extract workflow args correctly.

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

### Step 1: 'Should extract workflow args correctly.'

```python
'Should extract workflow args correctly.'
```

**Verification:**
```python
assert ctx.enhancement.workflows == ['security-focus', 'api-docs']
```

### Step 2: Assign args = argparse.Namespace(...)

```python
args = argparse.Namespace(name='test', enhance_workflow=['security-focus', 'api-docs'], enhance_stage=['stage1:prompt1'], var=['key1=value1', 'key2=value2'])
```

**Verification:**
```python
assert ctx.enhancement.stages == ['stage1:prompt1']
```

### Step 3: Assign ctx = ExecutionContext.initialize(...)

```python
ctx = ExecutionContext.initialize(args=args)
```

**Verification:**
```python
assert ctx.enhancement.workflow_vars == {'key1': 'value1', 'key2': 'value2'}
```


## Complete Example

```python
# Workflow
'Should extract workflow args correctly.'
args = argparse.Namespace(name='test', enhance_workflow=['security-focus', 'api-docs'], enhance_stage=['stage1:prompt1'], var=['key1=value1', 'key2=value2'])
ctx = ExecutionContext.initialize(args=args)
assert ctx.enhancement.workflows == ['security-focus', 'api-docs']
assert ctx.enhancement.stages == ['stage1:prompt1']
assert ctx.enhancement.workflow_vars == {'key1': 'value1', 'key2': 'value2'}
```

## Next Steps


---

*Source: test_execution_context.py:147 | Complexity: Beginner | Last updated: 2026-06-02*