# How To: Multiple Lookup Recursive Ref With Nonrecursive Ref

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple lookup recursive ref with nonrecursive ref

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
assert fourth.contents == two.contents
```

### Step 2: Assign two = referencing.jsonschema.DRAFT201909.create_resource(...)

```python
two = referencing.jsonschema.DRAFT201909.create_resource({'$id': 'http://example.com', '$recursiveAnchor': True, '$defs': {'foo': {'$id': 'foo', '$recursiveAnchor': True, '$defs': {'bar': True, 'baz': {'$recursiveAnchor': True, '$anchor': 'fooAnchor'}}}}})
```

### Step 3: Assign three = referencing.jsonschema.DRAFT201909.create_resource(...)

```python
three = referencing.jsonschema.DRAFT201909.create_resource({'$recursiveAnchor': False})
```

### Step 4: Assign resolver = Registry.with_resources.resolver(...)

```python
resolver = Registry().with_resources([('http://example.com', three), ('http://example.com/foo/', two), ('http://example.com/foo/bar', one)]).resolver()
```

### Step 5: Assign first = resolver.lookup(...)

```python
first = resolver.lookup('http://example.com')
```

### Step 6: Assign second = first.resolver.lookup(...)

```python
second = first.resolver.lookup('foo/')
```

### Step 7: Assign resolver = value

```python
resolver = second.resolver.lookup('bar').resolver
```

### Step 8: Assign fourth = referencing.jsonschema.lookup_recursive_ref(...)

```python
fourth = referencing.jsonschema.lookup_recursive_ref(resolver=resolver)
```

**Verification:**
```python
assert fourth.contents == two.contents
```


## Complete Example

```python
# Workflow
one = referencing.jsonschema.DRAFT201909.create_resource({'$recursiveAnchor': True})
two = referencing.jsonschema.DRAFT201909.create_resource({'$id': 'http://example.com', '$recursiveAnchor': True, '$defs': {'foo': {'$id': 'foo', '$recursiveAnchor': True, '$defs': {'bar': True, 'baz': {'$recursiveAnchor': True, '$anchor': 'fooAnchor'}}}}})
three = referencing.jsonschema.DRAFT201909.create_resource({'$recursiveAnchor': False})
resolver = Registry().with_resources([('http://example.com', three), ('http://example.com/foo/', two), ('http://example.com/foo/bar', one)]).resolver()
first = resolver.lookup('http://example.com')
second = first.resolver.lookup('foo/')
resolver = second.resolver.lookup('bar').resolver
fourth = referencing.jsonschema.lookup_recursive_ref(resolver=resolver)
assert fourth.contents == two.contents
```

## Next Steps


---

*Source: test_jsonschema.py:336 | Complexity: Advanced | Last updated: 2026-06-02*