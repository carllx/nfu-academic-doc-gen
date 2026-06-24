# How To: Automatic Remote Retrieval

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: Automatic retrieval of remote references is deprecated as of v4.18.0.

## Prerequisites

**Required Modules:**
- `contextlib`
- `io`
- `unittest`
- `importlib.metadata`
- `json`
- `subprocess`
- `sys`
- `urllib.request`
- `referencing.exceptions`
- `jsonschema`
- `jsonschema`
- `jsonschema.validators`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema.validators`
- `jsonschema`
- `jsonschema.exceptions`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema`
- `jsonschema.cli`


## Step-by-Step Guide

### Step 1: '\n        Automatic retrieval of remote references is deprecated as of v4.18.0.\n        '

```python
'\n        Automatic retrieval of remote references is deprecated as of v4.18.0.\n        '
```

### Step 2: Assign ref = 'http://bar#/$defs/baz'

```python
ref = 'http://bar#/$defs/baz'
```

### Step 3: Assign schema = value

```python
schema = {'$defs': {'baz': {'type': 'integer'}}}
```

### Step 4: Assign unknown = None

```python
sys.modules['requests'] = None
```

### Step 5: Assign validator = validators.Draft202012Validator(...)

```python
validator = validators.Draft202012Validator({'$ref': ref})
```

### Step 6: Assign message = 'Automatically retrieving remote references '

```python
message = 'Automatically retrieving remote references '
```

### Step 7: Assign patch = mock.patch.object(...)

```python
patch = mock.patch.object(urllib.request, 'urlopen', new=fake_urlopen)
```

### Step 8: Call self.addCleanup()

```python
self.addCleanup(sys.modules.__setitem__, 'requests', sys.modules['requests'])
```

### Step 9: Call self.assertIsInstance()

```python
self.assertIsInstance(request, urllib.request.Request)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(request.full_url, 'http://bar')
```

### Step 11: Assign unknown = request.header_items(...)

```python
(header, value), = request.header_items()
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(header.lower(), 'user-agent')
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(value, 'python-jsonschema (deprecated $ref resolution)')
```

### Step 14: yield BytesIO(json.dumps(schema).encode('utf8'))

```python
yield BytesIO(json.dumps(schema).encode('utf8'))
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual((validator.is_valid({}), validator.is_valid(37)), (False, True))
```


## Complete Example

```python
# Workflow
'\n        Automatic retrieval of remote references is deprecated as of v4.18.0.\n        '
ref = 'http://bar#/$defs/baz'
schema = {'$defs': {'baz': {'type': 'integer'}}}
if 'requests' in sys.modules:
    self.addCleanup(sys.modules.__setitem__, 'requests', sys.modules['requests'])
sys.modules['requests'] = None

@contextmanager
def fake_urlopen(request):
    self.assertIsInstance(request, urllib.request.Request)
    self.assertEqual(request.full_url, 'http://bar')
    (header, value), = request.header_items()
    self.assertEqual(header.lower(), 'user-agent')
    self.assertEqual(value, 'python-jsonschema (deprecated $ref resolution)')
    yield BytesIO(json.dumps(schema).encode('utf8'))
validator = validators.Draft202012Validator({'$ref': ref})
message = 'Automatically retrieving remote references '
patch = mock.patch.object(urllib.request, 'urlopen', new=fake_urlopen)
with patch, self.assertWarnsRegex(DeprecationWarning, message):
    self.assertEqual((validator.is_valid({}), validator.is_valid(37)), (False, True))
```

## Next Steps


---

*Source: test_deprecations.py:396 | Complexity: Advanced | Last updated: 2026-06-02*