# How To: Additionalitems With Items

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test additionalItems with items

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
instance = ['foo', 'bar', 1]
```

### Step 2: Assign schema = value

```python
schema = {'items': [{}], 'additionalItems': {'type': 'integer', 'minimum': 5}}
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
self.assertEqual(e1.path, deque([1]))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(e2.path, deque([2]))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(e1.json_path, '$[1]')
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(e2.json_path, '$[2]')
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
instance = ['foo', 'bar', 1]
schema = {'items': [{}], 'additionalItems': {'type': 'integer', 'minimum': 5}}
validator = validators.Draft3Validator(schema)
errors = validator.iter_errors(instance)
e1, e2 = sorted_errors(errors)
self.assertEqual(e1.path, deque([1]))
self.assertEqual(e2.path, deque([2]))
self.assertEqual(e1.json_path, '$[1]')
self.assertEqual(e2.json_path, '$[2]')
self.assertEqual(e1.validator, 'type')
self.assertEqual(e2.validator, 'minimum')
```

## Next Steps


---

*Source: test_validators.py:1228 | Complexity: Advanced | Last updated: 2026-06-02*