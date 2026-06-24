# How To: Combine With Uncrawled Resources

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine with uncrawled resources

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
assert combined != expected
```

### Step 2: Assign two = ID_AND_CHILDREN.create_resource(...)

```python
two = ID_AND_CHILDREN.create_resource({'foo': 'bar'})
```

**Verification:**
```python
assert combined.crawl() == expected
```

### Step 3: Assign three = ID_AND_CHILDREN.create_resource(...)

```python
three = ID_AND_CHILDREN.create_resource({'baz': 'quux'})
```

### Step 4: Assign first = Registry.with_resource(...)

```python
first = Registry().with_resource('http://example.com/1', one)
```

### Step 5: Assign second = Registry.with_resource(...)

```python
second = Registry().with_resource('http://example.com/foo/bar', two)
```

### Step 6: Assign third = Registry(...)

```python
third = Registry({'http://example.com/1': one, 'http://example.com/baz': three})
```

### Step 7: Assign expected = Registry(...)

```python
expected = Registry([('http://example.com/1', one), ('http://example.com/foo/bar', two), ('http://example.com/baz', three)])
```

### Step 8: Assign combined = first.combine(...)

```python
combined = first.combine(second, third)
```

**Verification:**
```python
assert combined != expected
```


## Complete Example

```python
# Workflow
one = Resource.opaque(contents={})
two = ID_AND_CHILDREN.create_resource({'foo': 'bar'})
three = ID_AND_CHILDREN.create_resource({'baz': 'quux'})
first = Registry().with_resource('http://example.com/1', one)
second = Registry().with_resource('http://example.com/foo/bar', two)
third = Registry({'http://example.com/1': one, 'http://example.com/baz': three})
expected = Registry([('http://example.com/1', one), ('http://example.com/foo/bar', two), ('http://example.com/baz', three)])
combined = first.combine(second, third)
assert combined != expected
assert combined.crawl() == expected
```

## Next Steps


---

*Source: test_core.py:314 | Complexity: Advanced | Last updated: 2026-06-02*