# How To: With Contents From Json Schema

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with contents from json schema

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign uri = 'urn:example'

```python
uri = 'urn:example'
```

**Verification:**
```python
assert registry[uri] == expected
```

### Step 2: Assign schema = value

```python
schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
```

### Step 3: Assign registry = Registry.with_contents(...)

```python
registry = Registry().with_contents([(uri, schema)])
```

### Step 4: Assign expected = Resource(...)

```python
expected = Resource(contents=schema, specification=DRAFT202012)
```

**Verification:**
```python
assert registry[uri] == expected
```


## Complete Example

```python
# Workflow
uri = 'urn:example'
schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
registry = Registry().with_contents([(uri, schema)])
expected = Resource(contents=schema, specification=DRAFT202012)
assert registry[uri] == expected
```

## Next Steps


---

*Source: test_core.py:90 | Complexity: Advanced | Last updated: 2026-06-02*