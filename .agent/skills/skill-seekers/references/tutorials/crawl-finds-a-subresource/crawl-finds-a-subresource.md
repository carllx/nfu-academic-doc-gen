# How To: Crawl Finds A Subresource

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crawl finds a subresource

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign child_id = 'urn:child'

```python
child_id = 'urn:child'
```

**Verification:**
```python
assert registry.crawl()[child_id] == expected
```

### Step 2: Assign root = ID_AND_CHILDREN.create_resource(...)

```python
root = ID_AND_CHILDREN.create_resource({'ID': 'urn:root', 'children': [{'ID': child_id, 'foo': 12}]})
```

### Step 3: Assign registry = value

```python
registry = root @ Registry()
```

### Step 4: Assign expected = ID_AND_CHILDREN.create_resource(...)

```python
expected = ID_AND_CHILDREN.create_resource({'ID': child_id, 'foo': 12})
```

**Verification:**
```python
assert registry.crawl()[child_id] == expected
```

### Step 5: registry[child_id]

```python
registry[child_id]
```


## Complete Example

```python
# Workflow
child_id = 'urn:child'
root = ID_AND_CHILDREN.create_resource({'ID': 'urn:root', 'children': [{'ID': child_id, 'foo': 12}]})
registry = root @ Registry()
with pytest.raises(LookupError):
    registry[child_id]
expected = ID_AND_CHILDREN.create_resource({'ID': child_id, 'foo': 12})
assert registry.crawl()[child_id] == expected
```

## Next Steps


---

*Source: test_core.py:137 | Complexity: Advanced | Last updated: 2026-06-02*