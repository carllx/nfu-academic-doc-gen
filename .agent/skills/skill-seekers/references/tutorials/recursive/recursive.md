# How To: Recursive

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test recursive

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

### Step 1: Assign schema = value

```python
schema = {'definitions': {'node': {'anyOf': [{'type': 'object', 'required': ['name', 'children'], 'properties': {'name': {'type': 'string'}, 'children': {'type': 'object', 'patternProperties': {'^.*$': {'$ref': '#/definitions/node'}}}}}]}}, 'type': 'object', 'required': ['root'], 'properties': {'root': {'$ref': '#/definitions/node'}}}
```

### Step 2: Assign instance = value

```python
instance = {'root': {'name': 'root', 'children': {'a': {'name': 'a', 'children': {'ab': {'name': 'ab'}}}}}}
```

### Step 3: Assign validator = validators.Draft4Validator(...)

```python
validator = validators.Draft4Validator(schema)
```

### Step 4: Assign unknown = validator.iter_errors(...)

```python
e, = validator.iter_errors(instance)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(e.absolute_path, deque(['root']))
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(e.absolute_schema_path, deque(['properties', 'root', 'anyOf']))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(e.json_path, '$.root')
```

### Step 8: Assign unknown = value

```python
e1, = e.context
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(e1.absolute_path, deque(['root', 'children', 'a']))
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(e1.absolute_schema_path, deque(['properties', 'root', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf']))
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(e1.json_path, '$.root.children.a')
```

### Step 12: Assign unknown = value

```python
e2, = e1.context
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(e2.absolute_path, deque(['root', 'children', 'a', 'children', 'ab']))
```

### Step 14: Call self.assertEqual()

```python
self.assertEqual(e2.absolute_schema_path, deque(['properties', 'root', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf']))
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(e2.json_path, '$.root.children.a.children.ab')
```


## Complete Example

```python
# Workflow
schema = {'definitions': {'node': {'anyOf': [{'type': 'object', 'required': ['name', 'children'], 'properties': {'name': {'type': 'string'}, 'children': {'type': 'object', 'patternProperties': {'^.*$': {'$ref': '#/definitions/node'}}}}}]}}, 'type': 'object', 'required': ['root'], 'properties': {'root': {'$ref': '#/definitions/node'}}}
instance = {'root': {'name': 'root', 'children': {'a': {'name': 'a', 'children': {'ab': {'name': 'ab'}}}}}}
validator = validators.Draft4Validator(schema)
e, = validator.iter_errors(instance)
self.assertEqual(e.absolute_path, deque(['root']))
self.assertEqual(e.absolute_schema_path, deque(['properties', 'root', 'anyOf']))
self.assertEqual(e.json_path, '$.root')
e1, = e.context
self.assertEqual(e1.absolute_path, deque(['root', 'children', 'a']))
self.assertEqual(e1.absolute_schema_path, deque(['properties', 'root', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf']))
self.assertEqual(e1.json_path, '$.root.children.a')
e2, = e1.context
self.assertEqual(e2.absolute_path, deque(['root', 'children', 'a', 'children', 'ab']))
self.assertEqual(e2.absolute_schema_path, deque(['properties', 'root', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf', 0, 'properties', 'children', 'patternProperties', '^.*$', 'anyOf']))
self.assertEqual(e2.json_path, '$.root.children.a.children.ab')
```

## Next Steps


---

*Source: test_validators.py:1068 | Complexity: Advanced | Last updated: 2026-06-02*