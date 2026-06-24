# How To: Lookup Non Existent Anchor

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lookup non existent anchor

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign root = ID_AND_CHILDREN.create_resource(...)

```python
root = ID_AND_CHILDREN.create_resource({'anchors': {}})
```

**Verification:**
```python
assert resolved.contents == root.contents
```

### Step 2: Assign resolver = Registry.with_resource.resolver(...)

```python
resolver = Registry().with_resource('urn:example', root).resolver()
```

**Verification:**
```python
assert "'noSuchAnchor' does not exist" in str(e.value)
```

### Step 3: Assign resolved = resolver.lookup(...)

```python
resolved = resolver.lookup('urn:example')
```

**Verification:**
```python
assert e.value == exceptions.NoSuchAnchor(ref='urn:example', resource=root, anchor='noSuchAnchor')
```

### Step 4: Assign ref = 'urn:example#noSuchAnchor'

```python
ref = 'urn:example#noSuchAnchor'
```

**Verification:**
```python
assert "'noSuchAnchor' does not exist" in str(e.value)
```

### Step 5: Call resolver.lookup()

```python
resolver.lookup(ref)
```


## Complete Example

```python
# Workflow
root = ID_AND_CHILDREN.create_resource({'anchors': {}})
resolver = Registry().with_resource('urn:example', root).resolver()
resolved = resolver.lookup('urn:example')
assert resolved.contents == root.contents
ref = 'urn:example#noSuchAnchor'
with pytest.raises(exceptions.Unresolvable) as e:
    resolver.lookup(ref)
assert "'noSuchAnchor' does not exist" in str(e.value)
assert e.value == exceptions.NoSuchAnchor(ref='urn:example', resource=root, anchor='noSuchAnchor')
```

## Next Steps


---

*Source: test_core.py:782 | Complexity: Advanced | Last updated: 2026-06-02*