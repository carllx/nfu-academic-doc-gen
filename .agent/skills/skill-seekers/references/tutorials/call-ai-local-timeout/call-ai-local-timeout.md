# How To: Call Ai Local Timeout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Test LOCAL mode timeout handling via AgentClient

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `unittest.mock`
- `pytest`
- `skill_seekers.cli.guide_enhancer`

**Setup Required:**
```python
# Fixtures: mock_call_ai
```

## Step-by-Step Guide

### Step 1: 'Test LOCAL mode timeout handling via AgentClient'

```python
'Test LOCAL mode timeout handling via AgentClient'
```

**Verification:**
```python
assert result is None
```

### Step 2: Assign mock_call_ai.return_value = None

```python
mock_call_ai.return_value = None
```

### Step 3: Assign enhancer = GuideEnhancer(...)

```python
enhancer = GuideEnhancer(mode='local')
```

### Step 4: Assign prompt = 'Test prompt'

```python
prompt = 'Test prompt'
```

### Step 5: Assign result = enhancer._call_ai(...)

```python
result = enhancer._call_ai(prompt)
```

**Verification:**
```python
assert result is None
```


## Complete Example

```python
# Setup
# Fixtures: mock_call_ai

# Workflow
'Test LOCAL mode timeout handling via AgentClient'
mock_call_ai.return_value = None
enhancer = GuideEnhancer(mode='local')
prompt = 'Test prompt'
result = enhancer._call_ai(prompt)
assert result is None
```

## Next Steps


---

*Source: test_guide_enhancer.py:491 | Complexity: Intermediate | Last updated: 2026-06-02*