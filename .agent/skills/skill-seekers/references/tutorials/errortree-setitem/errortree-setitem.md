# How To: Errortree Setitem

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: As of v4.20.0, setting items on an ErrorTree is deprecated.

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

### Step 1: '\n        As of v4.20.0, setting items on an ErrorTree is deprecated.\n        '

```python
'\n        As of v4.20.0, setting items on an ErrorTree is deprecated.\n        '
```

### Step 2: Assign e = exceptions.ValidationError(...)

```python
e = exceptions.ValidationError('some error', path=['foo'])
```

### Step 3: Assign tree = exceptions.ErrorTree(...)

```python
tree = exceptions.ErrorTree()
```

### Step 4: Assign subtree = exceptions.ErrorTree(...)

```python
subtree = exceptions.ErrorTree(errors=[e])
```

### Step 5: Assign message = 'ErrorTree.__setitem__ is '

```python
message = 'ErrorTree.__setitem__ is '
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(tree['foo'], subtree)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(w.filename, __file__)
```

### Step 8: Assign unknown = subtree

```python
tree['foo'] = subtree
```


## Complete Example

```python
# Workflow
'\n        As of v4.20.0, setting items on an ErrorTree is deprecated.\n        '
e = exceptions.ValidationError('some error', path=['foo'])
tree = exceptions.ErrorTree()
subtree = exceptions.ErrorTree(errors=[e])
message = 'ErrorTree.__setitem__ is '
with self.assertWarnsRegex(DeprecationWarning, message) as w:
    tree['foo'] = subtree
self.assertEqual(tree['foo'], subtree)
self.assertEqual(w.filename, __file__)
```

## Next Steps


---

*Source: test_deprecations.py:54 | Complexity: Advanced | Last updated: 2026-06-02*