# How To: Single Nesting

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test single nesting

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
instance = {'foo': 2, 'bar': [1], 'baz': 15, 'quux': 'spam'}
```

### Step 2: Assign schema = value

```python
schema = {'properties': {'foo': {'type': 'string'}, 'bar': {'minItems': 2}, 'baz': {'maximum': 10, 'enum': [2, 4, 6, 8]}}}
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
e1, e2, e3, e4 = sorted_errors(errors)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(e1.path, deque(['bar']))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(e2.path, deque(['baz']))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(e3.path, deque(['baz']))
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(e4.path, deque(['foo']))
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(e1.relative_path, deque(['bar']))
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(e2.relative_path, deque(['baz']))
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(e3.relative_path, deque(['baz']))
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(e4.relative_path, deque(['foo']))
```

### Step 14: Call self.assertEqual()

```python
self.assertEqual(e1.absolute_path, deque(['bar']))
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(e2.absolute_path, deque(['baz']))
```

### Step 16: Call self.assertEqual()

```python
self.assertEqual(e3.absolute_path, deque(['baz']))
```

### Step 17: Call self.assertEqual()

```python
self.assertEqual(e4.absolute_path, deque(['foo']))
```

### Step 18: Call self.assertEqual()

```python
self.assertEqual(e1.json_path, '$.bar')
```

### Step 19: Call self.assertEqual()

```python
self.assertEqual(e2.json_path, '$.baz')
```

### Step 20: Call self.assertEqual()

```python
self.assertEqual(e3.json_path, '$.baz')
```

### Step 21: Call self.assertEqual()

```python
self.assertEqual(e4.json_path, '$.foo')
```

### Step 22: Call self.assertEqual()

```python
self.assertEqual(e1.validator, 'minItems')
```

### Step 23: Call self.assertEqual()

```python
self.assertEqual(e2.validator, 'enum')
```

### Step 24: Call self.assertEqual()

```python
self.assertEqual(e3.validator, 'maximum')
```

### Step 25: Call self.assertEqual()

```python
self.assertEqual(e4.validator, 'type')
```


## Complete Example

```python
# Workflow
instance = {'foo': 2, 'bar': [1], 'baz': 15, 'quux': 'spam'}
schema = {'properties': {'foo': {'type': 'string'}, 'bar': {'minItems': 2}, 'baz': {'maximum': 10, 'enum': [2, 4, 6, 8]}}}
validator = validators.Draft3Validator(schema)
errors = validator.iter_errors(instance)
e1, e2, e3, e4 = sorted_errors(errors)
self.assertEqual(e1.path, deque(['bar']))
self.assertEqual(e2.path, deque(['baz']))
self.assertEqual(e3.path, deque(['baz']))
self.assertEqual(e4.path, deque(['foo']))
self.assertEqual(e1.relative_path, deque(['bar']))
self.assertEqual(e2.relative_path, deque(['baz']))
self.assertEqual(e3.relative_path, deque(['baz']))
self.assertEqual(e4.relative_path, deque(['foo']))
self.assertEqual(e1.absolute_path, deque(['bar']))
self.assertEqual(e2.absolute_path, deque(['baz']))
self.assertEqual(e3.absolute_path, deque(['baz']))
self.assertEqual(e4.absolute_path, deque(['foo']))
self.assertEqual(e1.json_path, '$.bar')
self.assertEqual(e2.json_path, '$.baz')
self.assertEqual(e3.json_path, '$.baz')
self.assertEqual(e4.json_path, '$.foo')
self.assertEqual(e1.validator, 'minItems')
self.assertEqual(e2.validator, 'enum')
self.assertEqual(e3.validator, 'maximum')
self.assertEqual(e4.validator, 'type')
```

## Next Steps


---

*Source: test_validators.py:968 | Complexity: Advanced | Last updated: 2026-06-02*