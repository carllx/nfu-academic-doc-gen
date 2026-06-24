# How To: Combine

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine

## Prerequisites

**Required Modules:**
- `rpds`
- `pytest`
- `referencing`
- `referencing.jsonschema`


## Step-by-Step Guide

### Step 1: Assign one = Resource.opaque(...)

```python
one = Resource.opaque(contents={})
```

**Verification:**
```python
assert first.combine(second, third, fourth) == Registry([('http://example.com/1', one), ('http://example.com/baz', three), ('http://example.com/foo/quux', four)], anchors=HashTrieMap({('http://example.com/foo/quux', 'foo'): Anchor(name='foo', resource=ID_AND_CHILDREN.create_resource(12))})).with_resource('http://example.com/foo/bar', two)
```

### Step 2: Assign two = ID_AND_CHILDREN.create_resource(...)

```python
two = ID_AND_CHILDREN.create_resource({'foo': 'bar'})
```

### Step 3: Assign three = ID_AND_CHILDREN.create_resource(...)

```python
three = ID_AND_CHILDREN.create_resource({'baz': 'quux'})
```

### Step 4: Assign four = ID_AND_CHILDREN.create_resource(...)

```python
four = ID_AND_CHILDREN.create_resource({'anchors': {'foo': 12}})
```

### Step 5: Assign first = Registry(...)

```python
first = Registry({'http://example.com/1': one})
```

### Step 6: Assign second = Registry.with_resource(...)

```python
second = Registry().with_resource('http://example.com/foo/bar', two)
```

### Step 7: Assign third = Registry(...)

```python
third = Registry({'http://example.com/1': one, 'http://example.com/baz': three})
```

### Step 8: Assign fourth = Registry.with_resource.crawl(...)

```python
fourth = Registry().with_resource('http://example.com/foo/quux', four).crawl()
```

**Verification:**
```python
assert first.combine(second, third, fourth) == Registry([('http://example.com/1', one), ('http://example.com/baz', three), ('http://example.com/foo/quux', four)], anchors=HashTrieMap({('http://example.com/foo/quux', 'foo'): Anchor(name='foo', resource=ID_AND_CHILDREN.create_resource(12))})).with_resource('http://example.com/foo/bar', two)
```


## Complete Example

```python
# Workflow
one = Resource.opaque(contents={})
two = ID_AND_CHILDREN.create_resource({'foo': 'bar'})
three = ID_AND_CHILDREN.create_resource({'baz': 'quux'})
four = ID_AND_CHILDREN.create_resource({'anchors': {'foo': 12}})
first = Registry({'http://example.com/1': one})
second = Registry().with_resource('http://example.com/foo/bar', two)
third = Registry({'http://example.com/1': one, 'http://example.com/baz': three})
fourth = Registry().with_resource('http://example.com/foo/quux', four).crawl()
assert first.combine(second, third, fourth) == Registry([('http://example.com/1', one), ('http://example.com/baz', three), ('http://example.com/foo/quux', four)], anchors=HashTrieMap({('http://example.com/foo/quux', 'foo'): Anchor(name='foo', resource=ID_AND_CHILDREN.create_resource(12))})).with_resource('http://example.com/foo/bar', two)
```

## Next Steps


---

*Source: test_core.py:264 | Complexity: Advanced | Last updated: 2026-06-02*