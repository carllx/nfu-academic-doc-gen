# How To: Custom Cache

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom cache

## Prerequisites

**Required Modules:**
- `functools`
- `json`
- `pytest`
- `referencing`
- `referencing.jsonschema`
- `referencing.retrieval`


## Step-by-Step Guide

### Step 1: Assign schema = value

```python
schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
```

**Verification:**
```python
assert got.value == resources['urn:example:1']
```

### Step 2: Assign mapping = value

```python
mapping = {'urn:example:1': dict(schema, foo=1), 'urn:example:2': dict(schema, foo=2), 'urn:example:3': dict(schema, foo=3)}
```

**Verification:**
```python
assert registry.get_or_retrieve('urn:example:1').value is got.value
```

### Step 3: Assign resources = value

```python
resources = {uri: Resource.from_contents(contents) for uri, contents in mapping.items()}
```

**Verification:**
```python
assert registry.get_or_retrieve('urn:example:1').value is got.value
```

### Step 4: Assign registry = Registry(...)

```python
registry = Registry(retrieve=retrieve)
```

**Verification:**
```python
assert got.value == resources['urn:example:2']
```

### Step 5: Assign got = registry.get_or_retrieve(...)

```python
got = registry.get_or_retrieve('urn:example:1')
```

**Verification:**
```python
assert registry.get_or_retrieve('urn:example:2').value is got.value
```

### Step 6: Assign got = registry.get_or_retrieve(...)

```python
got = registry.get_or_retrieve('urn:example:2')
```

**Verification:**
```python
assert registry.get_or_retrieve('urn:example:2').value is got.value
```

### Step 7: Assign got = registry.get_or_retrieve(...)

```python
got = registry.get_or_retrieve('urn:example:3')
```

**Verification:**
```python
assert got.value == resources['urn:example:3']
```

### Step 8: Call registry.get_or_retrieve()

```python
registry.get_or_retrieve('urn:example:1')
```

**Verification:**
```python
assert registry.get_or_retrieve('urn:example:3').value is got.value
```


## Complete Example

```python
# Workflow
schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema'}
mapping = {'urn:example:1': dict(schema, foo=1), 'urn:example:2': dict(schema, foo=2), 'urn:example:3': dict(schema, foo=3)}
resources = {uri: Resource.from_contents(contents) for uri, contents in mapping.items()}

@to_cached_resource(cache=lru_cache(maxsize=2))
def retrieve(uri):
    return json.dumps(mapping.pop(uri))
registry = Registry(retrieve=retrieve)
got = registry.get_or_retrieve('urn:example:1')
assert got.value == resources['urn:example:1']
assert registry.get_or_retrieve('urn:example:1').value is got.value
assert registry.get_or_retrieve('urn:example:1').value is got.value
got = registry.get_or_retrieve('urn:example:2')
assert got.value == resources['urn:example:2']
assert registry.get_or_retrieve('urn:example:2').value is got.value
assert registry.get_or_retrieve('urn:example:2').value is got.value
got = registry.get_or_retrieve('urn:example:3')
assert got.value == resources['urn:example:3']
assert registry.get_or_retrieve('urn:example:3').value is got.value
assert registry.get_or_retrieve('urn:example:3').value is got.value
with pytest.raises(exceptions.Unretrievable):
    registry.get_or_retrieve('urn:example:1')
```

## Next Steps


---

*Source: test_retrieval.py:69 | Complexity: Advanced | Last updated: 2026-06-02*