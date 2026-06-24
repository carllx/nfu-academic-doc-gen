# How To: Unset Error

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test unset error

## Prerequisites

**Required Modules:**
- `unittest`
- `textwrap`
- `jsonpath_ng`
- `jsonschema`
- `jsonschema.validators`


## Step-by-Step Guide

### Step 1: Assign error = exceptions.ValidationError(...)

```python
error = exceptions.ValidationError('message')
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(str(error), 'message')
```

### Step 3: Assign kwargs = value

```python
kwargs = {'validator': 'type', 'validator_value': 'string', 'instance': 5, 'schema': {'type': 'string'}}
```

### Step 4: Assign k = dict(...)

```python
k = dict(kwargs)
```

### Step 5: Assign error = exceptions.ValidationError(...)

```python
error = exceptions.ValidationError('message', **k)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(str(error), 'message')
```


## Complete Example

```python
# Workflow
error = exceptions.ValidationError('message')
self.assertEqual(str(error), 'message')
kwargs = {'validator': 'type', 'validator_value': 'string', 'instance': 5, 'schema': {'type': 'string'}}
for attr in kwargs:
    k = dict(kwargs)
    del k[attr]
    error = exceptions.ValidationError('message', **k)
    self.assertEqual(str(error), 'message')
```

## Next Steps


---

*Source: test_exceptions.py:540 | Complexity: Advanced | Last updated: 2026-06-02*