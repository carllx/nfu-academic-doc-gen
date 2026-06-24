# How To: Patternproperties

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test patternProperties

## Prerequisites

**Required Modules:**
- `__future__`
- `collections`
- `contextlib`
- `decimal`
- `io`
- `typing`
- `unittest`
- `urllib.request`
- `json`
- `os`
- `sys`
- `tempfile`
- `warnings`
- `attrs`
- `referencing.jsonschema`
- `referencing.exceptions`
- `jsonschema`
- `threading`


## Step-by-Step Guide

### Step 1: Assign instance = value

```python
instance = {'bar': 1, 'foo': 2}
```

### Step 2: Assign schema = value

```python
schema = {'patternProperties': {'bar': {'type': 'string'}, 'foo': {'minimum': 5}}}
```

### Step 3: Assign validator = validators.Draft3Validator(...)

```python
validator = validators.Draft3Validator(schema)
```

### Step 4: Assign errors = validator.iter_errors(...)

```python
errors = validator.iter_errors(instance)
```

### Step 5: Assign unknown = sorted_errors(...)

```python
e1, e2 = sorted_errors(errors)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(e1.path, deque(['bar']))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(e2.path, deque(['foo']))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(e1.json_path, '$.bar')
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(e2.json_path, '$.foo')
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(e1.validator, 'type')
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(e2.validator, 'minimum')
```


## Complete Example

```python
# Workflow
instance = {'bar': 1, 'foo': 2}
schema = {'patternProperties': {'bar': {'type': 'string'}, 'foo': {'minimum': 5}}}
validator = validators.Draft3Validator(schema)
errors = validator.iter_errors(instance)
e1, e2 = sorted_errors(errors)
self.assertEqual(e1.path, deque(['bar']))
self.assertEqual(e2.path, deque(['foo']))
self.assertEqual(e1.json_path, '$.bar')
self.assertEqual(e2.json_path, '$.foo')
self.assertEqual(e1.validator, 'type')
self.assertEqual(e2.validator, 'minimum')
```

## Next Steps


---

*Source: test_validators.py:1186 | Complexity: Advanced | Last updated: 2026-06-02*