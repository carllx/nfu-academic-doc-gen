# How To: Matmul Many Resources

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matmul many resources

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign one_uri = 'urn:example:one'

```python
one_uri = 'urn:example:one'
```

**Verification:**
```python
assert registry == Registry().with_resources([(one_uri, one), (two_uri, two)])
```

### Step 2: Assign one = ID_AND_CHILDREN.create_resource(...)

```python
one = ID_AND_CHILDREN.create_resource({'ID': one_uri, 'foo': 12})
```

### Step 3: Assign two_uri = 'urn:example:two'

```python
two_uri = 'urn:example:two'
```

### Step 4: Assign two = ID_AND_CHILDREN.create_resource(...)

```python
two = ID_AND_CHILDREN.create_resource({'ID': two_uri, 'foo': 12})
```

### Step 5: Assign registry = value

```python
registry = [one, two] @ Registry()
```

**Verification:**
```python
assert registry == Registry().with_resources([(one_uri, one), (two_uri, two)])
```


## Complete Example

```python
# Workflow
one_uri = 'urn:example:one'
one = ID_AND_CHILDREN.create_resource({'ID': one_uri, 'foo': 12})
two_uri = 'urn:example:two'
two = ID_AND_CHILDREN.create_resource({'ID': two_uri, 'foo': 12})
registry = [one, two] @ Registry()
assert registry == Registry().with_resources([(one_uri, one), (two_uri, two)])
```

## Next Steps


---

*Source: test_core.py:72 | Complexity: Advanced | Last updated: 2026-06-02*