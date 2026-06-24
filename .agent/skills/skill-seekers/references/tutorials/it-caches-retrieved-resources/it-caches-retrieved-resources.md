# How To: It Caches Retrieved Resources

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test it caches retrieved resources

## Prerequisites

**Required Modules:**
- `functools`
- `json`
- `pytest`
- `referencing`
- `referencing.jsonschema`
- `referencing.retrieval`


## Step-by-Step Guide

### Step 1: Assign contents = value

```python
contents = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
```

**Verification:**
```python
assert got.value == expected
```

### Step 2: Assign stack = value

```python
stack = [json.dumps(contents)]
```

**Verification:**
```python
assert again.value is got.value
```

### Step 3: Assign registry = Registry(...)

```python
registry = Registry(retrieve=retrieve)
```

### Step 4: Assign expected = Resource.from_contents(...)

```python
expected = Resource.from_contents(contents)
```

### Step 5: Assign got = registry.get_or_retrieve(...)

```python
got = registry.get_or_retrieve('urn:example:schema')
```

**Verification:**
```python
assert got.value == expected
```

### Step 6: Assign again = registry.get_or_retrieve(...)

```python
again = registry.get_or_retrieve('urn:example:schema')
```

**Verification:**
```python
assert again.value is got.value
```


## Complete Example

```python
# Workflow
contents = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
stack = [json.dumps(contents)]

@to_cached_resource()
def retrieve(uri):
    return stack.pop()
registry = Registry(retrieve=retrieve)
expected = Resource.from_contents(contents)
got = registry.get_or_retrieve('urn:example:schema')
assert got.value == expected
again = registry.get_or_retrieve('urn:example:schema')
assert again.value is got.value
```

## Next Steps


---

*Source: test_retrieval.py:12 | Complexity: Advanced | Last updated: 2026-06-02*