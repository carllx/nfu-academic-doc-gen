# How To: Non List Record Path Errors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test non list record path errors

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`

**Setup Required:**
```python
# Fixtures: value
```

## Step-by-Step Guide

### Step 1: Assign parsed_value = json.loads(...)

```python
parsed_value = json.loads(value)
```

### Step 2: Assign test_input = value

```python
test_input = {'state': 'Texas', 'info': parsed_value}
```

### Step 3: Assign test_path = 'info'

```python
test_path = 'info'
```

### Step 4: Assign msg = value

```python
msg = f'{test_input} has non list value {parsed_value} for path {test_path}. Must be list or null.'
```

### Step 5: Call json_normalize()

```python
json_normalize([test_input], record_path=[test_path])
```


## Complete Example

```python
# Setup
# Fixtures: value

# Workflow
parsed_value = json.loads(value)
test_input = {'state': 'Texas', 'info': parsed_value}
test_path = 'info'
msg = f'{test_input} has non list value {parsed_value} for path {test_path}. Must be list or null.'
with pytest.raises(TypeError, match=msg):
    json_normalize([test_input], record_path=[test_path])
```

## Next Steps


---

*Source: test_normalize.py:544 | Complexity: Intermediate | Last updated: 2026-06-02*