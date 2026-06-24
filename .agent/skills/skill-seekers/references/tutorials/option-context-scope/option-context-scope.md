# How To: Option Context Scope

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test option context scope

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign original_value = 60

```python
original_value = 60
```

**Verification:**
```python
assert cf.get_option(option_name) == original_value
```

### Step 2: Assign context_value = 10

```python
context_value = 10
```

**Verification:**
```python
assert cf.get_option(option_name) == context_value
```

### Step 3: Assign option_name = 'a'

```python
option_name = 'a'
```

**Verification:**
```python
assert cf.get_option(option_name) == original_value
```

### Step 4: Call cf.register_option()

```python
cf.register_option(option_name, original_value)
```

### Step 5: Assign ctx = cf.option_context(...)

```python
ctx = cf.option_context(option_name, context_value)
```

**Verification:**
```python
assert cf.get_option(option_name) == original_value
```


## Complete Example

```python
# Workflow
original_value = 60
context_value = 10
option_name = 'a'
cf.register_option(option_name, original_value)
ctx = cf.option_context(option_name, context_value)
assert cf.get_option(option_name) == original_value
with ctx:
    assert cf.get_option(option_name) == context_value
assert cf.get_option(option_name) == original_value
```

## Next Steps


---

*Source: test_config.py:410 | Complexity: Intermediate | Last updated: 2026-06-02*