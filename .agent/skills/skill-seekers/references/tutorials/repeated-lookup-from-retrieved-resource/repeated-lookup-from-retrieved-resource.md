# How To: Repeated Lookup From Retrieved Resource

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: A (custom-)retrieved resource is added to the registry returned by
looking it up.

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: '\n        A (custom-)retrieved resource is added to the registry returned by\n        looking it up.\n        '

```python
'\n        A (custom-)retrieved resource is added to the registry returned by\n        looking it up.\n        '
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 2: Assign resource = Resource.opaque(...)

```python
resource = Resource.opaque(contents={'foo': 'baz'})
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 3: Assign once = value

```python
once = [resource]
```

### Step 4: Assign resolver = Registry.resolver(...)

```python
resolver = Registry(retrieve=retrieve).resolver()
```

### Step 5: Assign resolved = resolver.lookup(...)

```python
resolved = resolver.lookup('http://example.com/')
```

**Verification:**
```python
assert resolved.contents == resource.contents
```

### Step 6: Assign resolved = resolved.resolver.lookup(...)

```python
resolved = resolved.resolver.lookup('http://example.com/')
```

**Verification:**
```python
assert resolved.contents == resource.contents
```


## Complete Example

```python
# Workflow
'\n        A (custom-)retrieved resource is added to the registry returned by\n        looking it up.\n        '
resource = Resource.opaque(contents={'foo': 'baz'})
once = [resource]

def retrieve(uri):
    return once.pop()
resolver = Registry(retrieve=retrieve).resolver()
resolved = resolver.lookup('http://example.com/')
assert resolved.contents == resource.contents
resolved = resolved.resolver.lookup('http://example.com/')
assert resolved.contents == resource.contents
```

## Next Steps


---

*Source: test_core.py:836 | Complexity: Advanced | Last updated: 2026-06-02*