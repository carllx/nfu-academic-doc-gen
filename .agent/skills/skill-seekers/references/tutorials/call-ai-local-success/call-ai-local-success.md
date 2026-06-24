# How To: Call Ai Local Success

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Test successful LOCAL mode call via AgentClient

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

### Step 1: 'Test successful LOCAL mode call via AgentClient'

```python
'Test successful LOCAL mode call via AgentClient'
```

**Verification:**
```python
assert result is not None
```

### Step 2: Assign mock_call_ai.return_value = json.dumps(...)

```python
mock_call_ai.return_value = json.dumps({'step_descriptions': [], 'troubleshooting': [], 'prerequisites_detailed': [], 'next_steps': [], 'use_cases': []})
```

**Verification:**
```python
assert mock_call_ai.called
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
assert result is not None
```


## Complete Example

```python
# Setup
# Fixtures: mock_call_ai

# Workflow
'Test successful LOCAL mode call via AgentClient'
mock_call_ai.return_value = json.dumps({'step_descriptions': [], 'troubleshooting': [], 'prerequisites_detailed': [], 'next_steps': [], 'use_cases': []})
enhancer = GuideEnhancer(mode='local')
prompt = 'Test prompt'
result = enhancer._call_ai(prompt)
assert result is not None
assert mock_call_ai.called
```

## Next Steps


---

*Source: test_guide_enhancer.py:471 | Complexity: Intermediate | Last updated: 2026-06-02*