# How To: Custom From Contents

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom from contents

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
contents = {}
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

### Step 4: Assign expected = DRAFT202012.create_resource(...)

```python
expected = DRAFT202012.create_resource(contents)
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
contents = {}
stack = [json.dumps(contents)]

@to_cached_resource(from_contents=DRAFT202012.create_resource)
def retrieve(uri):
    return stack.pop()
registry = Registry(retrieve=retrieve)
expected = DRAFT202012.create_resource(contents)
got = registry.get_or_retrieve('urn:example:schema')
assert got.value == expected
again = registry.get_or_retrieve('urn:example:schema')
assert again.value is got.value
```

## Next Steps


---

*Source: test_retrieval.py:50 | Complexity: Advanced | Last updated: 2026-06-02*