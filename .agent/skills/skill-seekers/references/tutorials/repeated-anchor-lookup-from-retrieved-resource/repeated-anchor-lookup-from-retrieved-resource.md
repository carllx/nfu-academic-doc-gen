# How To: Repeated Anchor Lookup From Retrieved Resource

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeated anchor lookup from retrieved resource

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign resource = Resource.opaque(...)

```python
resource = Resource.opaque(contents={'foo': 'baz'})
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 2: Assign once = value

```python
once = [resource]
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 3: Assign resolver = Registry.resolver(...)

```python
resolver = Registry(retrieve=retrieve).resolver()
```

### Step 4: Assign resolved = resolver.lookup(...)

```python
resolved = resolver.lookup('http://example.com/')
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 5: Assign resolved = resolved.resolver.lookup(...)

```python
resolved = resolved.resolver.lookup('#')
```

**Verification:**
```python
assert resolved.contents == resource.contents
```


## Complete Example

```python
# Workflow
resource = Resource.opaque(contents={'foo': 'baz'})
once = [resource]

def retrieve(uri):
    return once.pop()
resolver = Registry(retrieve=retrieve).resolver()
resolved = resolver.lookup('http://example.com/')
assert resolved.contents == resource.contents
resolved = resolved.resolver.lookup('#')
assert resolved.contents == resource.contents
```

## Next Steps


---

*Source: test_core.py:854 | Complexity: Advanced | Last updated: 2026-06-02*