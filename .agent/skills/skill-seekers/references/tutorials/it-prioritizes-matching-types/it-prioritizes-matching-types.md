# How To: It Prioritizes Matching Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test it prioritizes matching types

## Prerequisites

**Required Modules:**
- `unittest`
- `textwrap`
- `jsonpath_ng`
- `jsonschema`
- `jsonschema.validators`


## Step-by-Step Guide

### Step 1: Assign schema = value

```python
schema = {'properties': {'foo': {'anyOf': [{'type': 'array', 'minItems': 2}, {'type': 'string', 'minLength': 10}]}}}
```

### Step 2: Assign best = self.best_match_of(...)

```python
best = self.best_match_of(instance={'foo': 'bar'}, schema=schema)
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(best.validator, 'minLength')
```

### Step 4: Assign reordered = value

```python
reordered = {'properties': {'foo': {'anyOf': [{'type': 'string', 'minLength': 10}, {'type': 'array', 'minItems': 2}]}}}
```

### Step 5: Assign best = self.best_match_of(...)

```python
best = self.best_match_of(instance={'foo': 'bar'}, schema=reordered)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(best.validator, 'minLength')
```


## Complete Example

```python
# Workflow
schema = {'properties': {'foo': {'anyOf': [{'type': 'array', 'minItems': 2}, {'type': 'string', 'minLength': 10}]}}}
best = self.best_match_of(instance={'foo': 'bar'}, schema=schema)
self.assertEqual(best.validator, 'minLength')
reordered = {'properties': {'foo': {'anyOf': [{'type': 'string', 'minLength': 10}, {'type': 'array', 'minItems': 2}]}}}
best = self.best_match_of(instance={'foo': 'bar'}, schema=reordered)
self.assertEqual(best.validator, 'minLength')
```

## Next Steps


---

*Source: test_exceptions.py:263 | Complexity: Intermediate | Last updated: 2026-06-02*