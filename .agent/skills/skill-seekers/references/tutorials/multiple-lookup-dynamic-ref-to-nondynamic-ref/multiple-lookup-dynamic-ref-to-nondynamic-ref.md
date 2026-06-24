# How To: Multiple Lookup Dynamic Ref To Nondynamic Ref

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple lookup dynamic ref to nondynamic ref

## Prerequisites

**Required Modules:**
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign one = referencing.jsonschema.DRAFT202012.create_resource(...)

```python
one = referencing.jsonschema.DRAFT202012.create_resource({'$anchor': 'fooAnchor'})
```

**Verification:**
```python
assert fourth.contents == two.contents
```

### Step 2: Assign two = referencing.jsonschema.DRAFT202012.create_resource(...)

```python
two = referencing.jsonschema.DRAFT202012.create_resource({'$id': 'http://example.com', '$dynamicAnchor': 'fooAnchor', '$defs': {'foo': {'$id': 'foo', '$dynamicAnchor': 'fooAnchor', '$defs': {'bar': True, 'baz': {'$dynamicAnchor': 'fooAnchor'}}}}})
```

### Step 3: Assign resolver = Registry.with_resources.resolver(...)

```python
resolver = Registry().with_resources([('http://example.com', two), ('http://example.com/foo/', one), ('http://example.com/foo/bar', two)]).resolver()
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

### Step 7: Assign fourth = resolver.lookup(...)

```python
fourth = resolver.lookup('#fooAnchor')
```

**Verification:**
```python
assert fourth.contents == two.contents
```


## Complete Example

```python
# Workflow
one = referencing.jsonschema.DRAFT202012.create_resource({'$anchor': 'fooAnchor'})
two = referencing.jsonschema.DRAFT202012.create_resource({'$id': 'http://example.com', '$dynamicAnchor': 'fooAnchor', '$defs': {'foo': {'$id': 'foo', '$dynamicAnchor': 'fooAnchor', '$defs': {'bar': True, 'baz': {'$dynamicAnchor': 'fooAnchor'}}}}})
resolver = Registry().with_resources([('http://example.com', two), ('http://example.com/foo/', one), ('http://example.com/foo/bar', two)]).resolver()
first = resolver.lookup('http://example.com')
second = first.resolver.lookup('foo/')
resolver = second.resolver.lookup('bar').resolver
fourth = resolver.lookup('#fooAnchor')
assert fourth.contents == two.contents
```

## Next Steps


---

*Source: test_jsonschema.py:234 | Complexity: Advanced | Last updated: 2026-06-02*