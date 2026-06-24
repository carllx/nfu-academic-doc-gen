# How To: Lookup Trivial Recursive Ref

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lookup trivial recursive ref

## Prerequisites

**Required Modules:**
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign one = referencing.jsonschema.DRAFT201909.create_resource(...)

```python
one = referencing.jsonschema.DRAFT201909.create_resource({'$recursiveAnchor': True})
```

**Verification:**
```python
assert resolved.contents == one.contents
```

### Step 2: Assign resolver = Registry.with_resource.resolver(...)

```python
resolver = Registry().with_resource('http://example.com', one).resolver()
```

### Step 3: Assign first = resolver.lookup(...)

```python
first = resolver.lookup('http://example.com')
```

### Step 4: Assign resolved = referencing.jsonschema.lookup_recursive_ref(...)

```python
resolved = referencing.jsonschema.lookup_recursive_ref(resolver=first.resolver)
```

**Verification:**
```python
assert resolved.contents == one.contents
```


## Complete Example

```python
# Workflow
one = referencing.jsonschema.DRAFT201909.create_resource({'$recursiveAnchor': True})
resolver = Registry().with_resource('http://example.com', one).resolver()
first = resolver.lookup('http://example.com')
resolved = referencing.jsonschema.lookup_recursive_ref(resolver=first.resolver)
assert resolved.contents == one.contents
```

## Next Steps


---

*Source: test_jsonschema.py:275 | Complexity: Advanced | Last updated: 2026-06-02*