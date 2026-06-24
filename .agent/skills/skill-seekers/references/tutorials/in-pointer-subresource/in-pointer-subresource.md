# How To: In Pointer Subresource

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test in pointer subresource

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign root = ID_AND_CHILDREN.create_resource(...)

```python
root = ID_AND_CHILDREN.create_resource({'ID': 'http://example.com/', 'children': [{'ID': 'child/', 'children': [{'ID': 'grandchild'}]}]})
```

**Verification:**
```python
assert first.contents == root.contents
```

### Step 2: Assign registry = value

```python
registry = root @ Registry()
```

**Verification:**
```python
assert third.contents == {'ID': 'grandchild'}
```

### Step 3: Assign resolver = registry.resolver(...)

```python
resolver = registry.resolver()
```

### Step 4: Assign first = resolver.lookup(...)

```python
first = resolver.lookup('http://example.com/')
```

**Verification:**
```python
assert first.contents == root.contents
```

### Step 5: Assign second = first.resolver.lookup(...)

```python
second = first.resolver.lookup('#/children/0')
```

### Step 6: Assign third = second.resolver.lookup(...)

```python
third = second.resolver.lookup('grandchild')
```

**Verification:**
```python
assert third.contents == {'ID': 'grandchild'}
```

### Step 7: Call first.resolver.lookup()

```python
first.resolver.lookup('grandchild')
```


## Complete Example

```python
# Workflow
root = ID_AND_CHILDREN.create_resource({'ID': 'http://example.com/', 'children': [{'ID': 'child/', 'children': [{'ID': 'grandchild'}]}]})
registry = root @ Registry()
resolver = registry.resolver()
first = resolver.lookup('http://example.com/')
assert first.contents == root.contents
with pytest.raises(exceptions.Unresolvable):
    first.resolver.lookup('grandchild')
second = first.resolver.lookup('#/children/0')
third = second.resolver.lookup('grandchild')
assert third.contents == {'ID': 'grandchild'}
```

## Next Steps


---

*Source: test_core.py:898 | Complexity: Advanced | Last updated: 2026-06-02*