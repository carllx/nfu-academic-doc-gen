# How To: Propertynames

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test propertyNames

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
instance = {'foo': 12}
```

### Step 2: Assign schema = value

```python
schema = {'propertyNames': {'not': {'const': 'foo'}}}
```

### Step 3: Assign validator = validators.Draft7Validator(...)

```python
validator = validators.Draft7Validator(schema)
```

### Step 4: Assign unknown = validator.iter_errors(...)

```python
error, = validator.iter_errors(instance)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(error.validator, 'not')
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(error.message, "'foo' should not be valid under {'const': 'foo'}")
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(error.path, deque([]))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(error.json_path, '$')
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(error.schema_path, deque(['propertyNames', 'not']))
```


## Complete Example

```python
# Workflow
instance = {'foo': 12}
schema = {'propertyNames': {'not': {'const': 'foo'}}}
validator = validators.Draft7Validator(schema)
error, = validator.iter_errors(instance)
self.assertEqual(error.validator, 'not')
self.assertEqual(error.message, "'foo' should not be valid under {'const': 'foo'}")
self.assertEqual(error.path, deque([]))
self.assertEqual(error.json_path, '$')
self.assertEqual(error.schema_path, deque(['propertyNames', 'not']))
```

## Next Steps


---

*Source: test_validators.py:1248 | Complexity: Advanced | Last updated: 2026-06-02*