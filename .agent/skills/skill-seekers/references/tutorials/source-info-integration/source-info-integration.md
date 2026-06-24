# How To: Source Info Integration

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Should integrate source info from source_detector.

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

### Step 1: 'Should integrate source info from source_detector.'

```python
'Should integrate source info from source_detector.'
```

**Verification:**
```python
assert ctx.source is not None
```

### Step 2: Assign ctx = ExecutionContext.initialize(...)

```python
ctx = ExecutionContext.initialize(source_info=MockSourceInfo())
```

**Verification:**
```python
assert ctx.source.type == 'web'
```

### Step 3: Assign type = 'web'

```python
type = 'web'
```

**Verification:**
```python
assert ctx.source.raw_source == 'https://react.dev/'
```

### Step 4: Assign raw_source = 'https://react.dev/'

```python
raw_source = 'https://react.dev/'
```

**Verification:**
```python
assert ctx.source.suggested_name == 'react'
```

### Step 5: Assign parsed = value

```python
parsed = {'url': 'https://react.dev/'}
```

### Step 6: Assign suggested_name = 'react'

```python
suggested_name = 'react'
```


## Complete Example

```python
# Workflow
'Should integrate source info from source_detector.'

class MockSourceInfo:
    type = 'web'
    raw_source = 'https://react.dev/'
    parsed = {'url': 'https://react.dev/'}
    suggested_name = 'react'
ctx = ExecutionContext.initialize(source_info=MockSourceInfo())
assert ctx.source is not None
assert ctx.source.type == 'web'
assert ctx.source.raw_source == 'https://react.dev/'
assert ctx.source.suggested_name == 'react'
```

## Next Steps


---

*Source: test_execution_context.py:378 | Complexity: Intermediate | Last updated: 2026-06-02*