# How To: Multiple Lookup Recursive Ref To Bool

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple lookup recursive ref to bool

## Prerequisites

**Required Modules:**
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign TRUE = referencing.jsonschema.DRAFT201909.create_resource(...)

```python
TRUE = referencing.jsonschema.DRAFT201909.create_resource(True)
```

**Verification:**
```python
assert fourth.contents == root.contents
```

### Step 2: Assign root = referencing.jsonschema.DRAFT201909.create_resource(...)

```python
root = referencing.jsonschema.DRAFT201909.create_resource({'$id': 'http://example.com', '$recursiveAnchor': True, '$defs': {'foo': {'$id': 'foo', '$recursiveAnchor': True, '$defs': {'bar': True, 'baz': {'$recursiveAnchor': True, '$anchor': 'fooAnchor'}}}}})
```

### Step 3: Assign resolver = Registry.with_resources.resolver(...)

```python
resolver = Registry().with_resources([('http://example.com', root), ('http://example.com/foo/', TRUE), ('http://example.com/foo/bar', root)]).resolver()
```

### Step 4: Assign first = resolver.lookup(...)

```python
first = resolver.lookup('http://example.com')
```

### Step 5: Assign second = first.resolver.lookup(...)

```python
second = first.resolver.lookup('foo/')
```

### Step 6: Assign resolver = value

```python
resolver = second.resolver.lookup('bar').resolver
```

### Step 7: Assign fourth = referencing.jsonschema.lookup_recursive_ref(...)

```python
fourth = referencing.jsonschema.lookup_recursive_ref(resolver=resolver)
```

**Verification:**
```python
assert fourth.contents == root.contents
```


## Complete Example

```python
# Workflow
TRUE = referencing.jsonschema.DRAFT201909.create_resource(True)
root = referencing.jsonschema.DRAFT201909.create_resource({'$id': 'http://example.com', '$recursiveAnchor': True, '$defs': {'foo': {'$id': 'foo', '$recursiveAnchor': True, '$defs': {'bar': True, 'baz': {'$recursiveAnchor': True, '$anchor': 'fooAnchor'}}}}})
resolver = Registry().with_resources([('http://example.com', root), ('http://example.com/foo/', TRUE), ('http://example.com/foo/bar', root)]).resolver()
first = resolver.lookup('http://example.com')
second = first.resolver.lookup('foo/')
resolver = second.resolver.lookup('bar').resolver
fourth = referencing.jsonschema.lookup_recursive_ref(resolver=resolver)
assert fourth.contents == root.contents
```

## Next Steps


---

*Source: test_jsonschema.py:296 | Complexity: Advanced | Last updated: 2026-06-02*