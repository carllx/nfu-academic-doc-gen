# How To: Multiple Nesting

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test multiple nesting

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
instance = [1, {'foo': 2, 'bar': {'baz': [1]}}, 'quux']
```

### Step 2: Assign schema = value

```python
schema = {'type': 'string', 'items': {'type': ['string', 'object'], 'properties': {'foo': {'enum': [1, 3]}, 'bar': {'type': 'array', 'properties': {'bar': {'required': True}, 'baz': {'minItems': 2}}}}}}
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
e1, e2, e3, e4, e5, e6 = sorted_errors(errors)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(e1.path, deque([]))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(e2.path, deque([0]))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(e3.path, deque([1, 'bar']))
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(e4.path, deque([1, 'bar', 'bar']))
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(e5.path, deque([1, 'bar', 'baz']))
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(e6.path, deque([1, 'foo']))
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(e1.json_path, '$')
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(e2.json_path, '$[0]')
```

### Step 14: Call self.assertEqual()

```python
self.assertEqual(e3.json_path, '$[1].bar')
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(e4.json_path, '$[1].bar.bar')
```

### Step 16: Call self.assertEqual()

```python
self.assertEqual(e5.json_path, '$[1].bar.baz')
```

### Step 17: Call self.assertEqual()

```python
self.assertEqual(e6.json_path, '$[1].foo')
```

### Step 18: Call self.assertEqual()

```python
self.assertEqual(e1.schema_path, deque(['type']))
```

### Step 19: Call self.assertEqual()

```python
self.assertEqual(e2.schema_path, deque(['items', 'type']))
```

### Step 20: Call self.assertEqual()

```python
self.assertEqual(list(e3.schema_path), ['items', 'properties', 'bar', 'type'])
```

### Step 21: Call self.assertEqual()

```python
self.assertEqual(list(e4.schema_path), ['items', 'properties', 'bar', 'properties', 'bar', 'required'])
```

### Step 22: Call self.assertEqual()

```python
self.assertEqual(list(e5.schema_path), ['items', 'properties', 'bar', 'properties', 'baz', 'minItems'])
```

### Step 23: Call self.assertEqual()

```python
self.assertEqual(list(e6.schema_path), ['items', 'properties', 'foo', 'enum'])
```

### Step 24: Call self.assertEqual()

```python
self.assertEqual(e1.validator, 'type')
```

### Step 25: Call self.assertEqual()

```python
self.assertEqual(e2.validator, 'type')
```

### Step 26: Call self.assertEqual()

```python
self.assertEqual(e3.validator, 'type')
```

### Step 27: Call self.assertEqual()

```python
self.assertEqual(e4.validator, 'required')
```

### Step 28: Call self.assertEqual()

```python
self.assertEqual(e5.validator, 'minItems')
```

### Step 29: Call self.assertEqual()

```python
self.assertEqual(e6.validator, 'enum')
```


## Complete Example

```python
# Workflow
instance = [1, {'foo': 2, 'bar': {'baz': [1]}}, 'quux']
schema = {'type': 'string', 'items': {'type': ['string', 'object'], 'properties': {'foo': {'enum': [1, 3]}, 'bar': {'type': 'array', 'properties': {'bar': {'required': True}, 'baz': {'minItems': 2}}}}}}
validator = validators.Draft3Validator(schema)
errors = validator.iter_errors(instance)
e1, e2, e3, e4, e5, e6 = sorted_errors(errors)
self.assertEqual(e1.path, deque([]))
self.assertEqual(e2.path, deque([0]))
self.assertEqual(e3.path, deque([1, 'bar']))
self.assertEqual(e4.path, deque([1, 'bar', 'bar']))
self.assertEqual(e5.path, deque([1, 'bar', 'baz']))
self.assertEqual(e6.path, deque([1, 'foo']))
self.assertEqual(e1.json_path, '$')
self.assertEqual(e2.json_path, '$[0]')
self.assertEqual(e3.json_path, '$[1].bar')
self.assertEqual(e4.json_path, '$[1].bar.bar')
self.assertEqual(e5.json_path, '$[1].bar.baz')
self.assertEqual(e6.json_path, '$[1].foo')
self.assertEqual(e1.schema_path, deque(['type']))
self.assertEqual(e2.schema_path, deque(['items', 'type']))
self.assertEqual(list(e3.schema_path), ['items', 'properties', 'bar', 'type'])
self.assertEqual(list(e4.schema_path), ['items', 'properties', 'bar', 'properties', 'bar', 'required'])
self.assertEqual(list(e5.schema_path), ['items', 'properties', 'bar', 'properties', 'baz', 'minItems'])
self.assertEqual(list(e6.schema_path), ['items', 'properties', 'foo', 'enum'])
self.assertEqual(e1.validator, 'type')
self.assertEqual(e2.validator, 'type')
self.assertEqual(e3.validator, 'type')
self.assertEqual(e4.validator, 'required')
self.assertEqual(e5.validator, 'minItems')
self.assertEqual(e6.validator, 'enum')
```

## Next Steps


---

*Source: test_validators.py:1007 | Complexity: Advanced | Last updated: 2026-06-02*